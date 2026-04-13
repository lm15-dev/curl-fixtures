#!/usr/bin/env python3
"""
Run pi subagents to generate missing curl fixture cases, one session per feature.

Pipeline stages per task:
1. generate fixture with pi
2. validate that single case live (or skip if API key missing)
3. persist pipeline state after every step

Examples:
  python3 curl-fixtures/run_pi_fixture_pipeline.py
  python3 curl-fixtures/run_pi_fixture_pipeline.py --provider openai --concurrency 3
  python3 curl-fixtures/run_pi_fixture_pipeline.py --task openai.multi_turn
  python3 curl-fixtures/run_pi_fixture_pipeline.py --retry-failed
  python3 curl-fixtures/run_pi_fixture_pipeline.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("pip install pyyaml", file=sys.stderr)
    raise

ROOT = Path(__file__).parent
FEATURES = ROOT / "features.yaml"
PIPELINE_DIR = ROOT / "pipeline"
RUNS_DIR = PIPELINE_DIR / "runs"
SESSIONS_DIR = PIPELINE_DIR / "sessions"
LOGS_DIR = PIPELINE_DIR / "logs"
LATEST_RUN = PIPELINE_DIR / "latest-run.json"
DOTENV_PATH = ROOT.parent / ".env"
LOCK = threading.Lock()

KEY_MAP = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "gemini": "GEMINI_API_KEY",
}


def load_dotenv(path: Path = DOTENV_PATH) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value and ((value[0] == value[-1]) and value[0] in {'"', "'"}):
            value = value[1:-1]
        os.environ.setdefault(key, value)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_features() -> dict[str, Any]:
    with open(FEATURES) as f:
        return yaml.safe_load(f)


def build_tasks(data: dict[str, Any], provider_filter: str | None, task_filter: str | None, retry_failed: bool) -> list[dict[str, Any]]:
    latest = None
    if LATEST_RUN.exists():
        latest = json.loads(LATEST_RUN.read_text())
        if latest:
            latest = json.loads(Path(latest["run_file"]).read_text())

    prev_tasks = {}
    if latest:
        for t in latest.get("tasks", []):
            prev_tasks[t["id"]] = t

    tasks = []
    for provider, pdata in data.items():
        if provider_filter and provider != provider_filter:
            continue
        for feature, finfo in pdata.get("features", {}).items():
            task_id = f"{provider}.{feature}"
            if task_filter and task_id != task_filter:
                continue
            prev = prev_tasks.get(task_id)
            if not retry_failed and prev and prev.get("status") in {"validated", "skipped_validation"}:
                continue
            if not retry_failed and prev and prev.get("status") in {"running", "generated", "validating"}:
                continue
            if finfo.get("status") != "todo":
                continue
            tasks.append({
                "id": task_id,
                "provider": provider,
                "feature": feature,
                "description": finfo.get("description", ""),
                "status": "pending",
                "attempts": (prev or {}).get("attempts", 0),
                "case_file": f"cases/{provider}/{feature}.json",
                "session_file": str((SESSIONS_DIR / provider / f"{feature}.jsonl").relative_to(ROOT)),
                "log_file": str((LOGS_DIR / provider / f"{feature}.log").relative_to(ROOT)),
                "validation": None,
                "last_error": None,
                "started_at": None,
                "ended_at": None,
            })
    return tasks


def make_run(tasks: list[dict[str, Any]]) -> dict[str, Any]:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run = {
        "run_id": run_id,
        "created_at": now_iso(),
        "cwd": str(ROOT),
        "tasks": tasks,
    }
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    run_file = RUNS_DIR / f"{run_id}.json"
    run["run_file"] = str(run_file)
    save_run(run)
    LATEST_RUN.parent.mkdir(parents=True, exist_ok=True)
    LATEST_RUN.write_text(json.dumps({"run_id": run_id, "run_file": str(run_file)}, indent=2))
    return run


def save_run(run: dict[str, Any]) -> None:
    Path(run["run_file"]).write_text(json.dumps(run, indent=2, sort_keys=True))


def update_task(run: dict[str, Any], task_id: str, **updates: Any) -> None:
    with LOCK:
        for task in run["tasks"]:
            if task["id"] == task_id:
                task.update(updates)
                break
        save_run(run)


def build_prompt(task: dict[str, Any]) -> str:
    provider = task["provider"]
    feature = task["feature"]
    case_file = task["case_file"]

    return f"""You are working in the curl-fixtures project.

Task: implement exactly one missing fixture case.

Target:
- provider: {provider}
- feature: {feature}
- case file: {case_file}

Requirements:
1. Read these files first:
   - README.md
   - features.yaml
   - api-references/README.md
   - the provider docs relevant to this feature under api-references/{provider}/pages/
   - 2-4 nearby examples in cases/{provider}/
2. Create or update exactly this file: {case_file}
3. Match the existing case style exactly.
4. Use the feature description from features.yaml as the source of truth for intent.
5. Pick a minimal, robust request that tests the feature.
6. Keep expect.status to the correct live HTTP status.
7. Do not edit unrelated files.
8. At the end, output a short summary with:
   - FILE: <path>
   - CHANGED: yes/no
   - NOTES: <one line>

If the feature appears unsupported or blocked by docs ambiguity, still create the best reasonable todo fixture and explain in NOTES.
"""


def ensure_dirs_for(task: dict[str, Any]) -> None:
    (ROOT / task["session_file"]).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / task["log_file"]).parent.mkdir(parents=True, exist_ok=True)


def run_pi(task: dict[str, Any], model: str | None, dry_run: bool) -> tuple[int, str, str, list[str]]:
    ensure_dirs_for(task)
    cmd = [
        "pi",
        "-p",
        "--model", model or "openai/gpt-5.4:medium",
        "--session", str(ROOT / task["session_file"]),
        "--tools", "read,bash,write,edit",
        "--no-extensions",
        "--append-system-prompt", "Be precise. Change only the requested file.",
        build_prompt(task),
    ]
    if dry_run:
        return 0, "", "", cmd

    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    log_text = "\n".join([
        "$ " + " ".join(cmd),
        "\n--- STDOUT ---\n",
        proc.stdout,
        "\n--- STDERR ---\n",
        proc.stderr,
    ])
    (ROOT / task["log_file"]).write_text(log_text)
    return proc.returncode, proc.stdout, proc.stderr, cmd


def run_validation(task: dict[str, Any], dry_run: bool) -> dict[str, Any]:
    key_var = KEY_MAP[task["provider"]]
    if not os.environ.get(key_var):
        return {
            "status": "skipped_validation",
            "reason": f"{key_var} not set",
            "validated_at": now_iso(),
        }

    cmd = [
        sys.executable,
        str(ROOT / "validate_live.py"),
        "--task",
        task["id"],
    ]
    if dry_run:
        return {
            "status": "dry_run",
            "command": cmd,
            "validated_at": now_iso(),
        }

    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    latest = json.loads((ROOT / "results/latest.json").read_text()) if (ROOT / "results/latest.json").exists() else {"cases": {}}
    case_result = latest.get("cases", {}).get(task["id"])
    return {
        "status": "validated" if proc.returncode == 0 else "validation_failed",
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "case_result": case_result,
        "validated_at": now_iso(),
    }


def worker(run: dict[str, Any], task: dict[str, Any], model: str | None, dry_run: bool) -> dict[str, Any]:
    start = now_iso()
    update_task(run, task["id"], status="running", started_at=start, attempts=task["attempts"] + 1)

    rc, stdout, stderr, cmd = run_pi(task, model, dry_run)
    if dry_run:
        update_task(run, task["id"], status="dry_run", ended_at=now_iso())
        return {"task_id": task["id"], "status": "dry_run", "command": cmd}

    if rc != 0:
        update_task(run, task["id"], status="pi_failed", ended_at=now_iso(), last_error=stderr or stdout)
        return {"task_id": task["id"], "status": "pi_failed", "returncode": rc}

    update_task(run, task["id"], status="generated")
    validation = run_validation(task, dry_run=dry_run)
    update_task(run, task["id"], status=validation["status"], validation=validation, ended_at=now_iso())
    return {"task_id": task["id"], "status": validation["status"], "validation": validation}


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["openai", "anthropic", "gemini"])
    parser.add_argument("--task", help="Exact task id, e.g. openai.multi_turn")
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--model", help="pi model, default openai/gpt-5.4:medium")
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = load_features()
    tasks = build_tasks(data, args.provider, args.task, args.retry_failed)
    if not tasks:
        print("No todo tasks selected.")
        return 0

    run = make_run(tasks)
    print(f"Run: {run['run_id']}")
    print(f"Tasks: {len(tasks)}")

    if args.dry_run:
        for task in tasks:
            result = worker(run, task, args.model, dry_run=True)
            print(f"\n--- {task['id']} ---")
            print(" ".join(result["command"]))
        return 0

    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as ex:
        futures = [ex.submit(worker, run, task, args.model, False) for task in tasks]
        for fut in as_completed(futures):
            result = fut.result()
            results.append(result)
            print(f"[{result['status']}] {result['task_id']}")

    validated = sum(1 for r in results if r["status"] == "validated")
    skipped = sum(1 for r in results if r["status"] == "skipped_validation")
    failed = len(results) - validated - skipped
    print(f"Done. validated={validated} skipped_validation={skipped} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
