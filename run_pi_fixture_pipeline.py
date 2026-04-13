#!/usr/bin/env python3
"""
Generate missing curl fixture cases with pi, validate them live, repair failures,
and mark successful features as covered.

Pipeline per task:
1. ask pi to create/update exactly one case file
2. lint the produced case
3. validate exactly that case live
4. if validation fails, feed the failure back to pi and retry
5. on success, mark the feature covered in features.yaml
6. regenerate README at the end

Examples:
  python3 curl-fixtures/run_pi_fixture_pipeline.py --provider openai --concurrency 2
  python3 curl-fixtures/run_pi_fixture_pipeline.py --task openai.tool_choice_auto
  python3 curl-fixtures/run_pi_fixture_pipeline.py --task gemini.tool_config_auto --max-attempts 3
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
README = ROOT / "README.md"
PIPELINE_DIR = ROOT / "pipeline"
RUNS_DIR = PIPELINE_DIR / "runs"
SESSIONS_DIR = PIPELINE_DIR / "sessions"
LOGS_DIR = PIPELINE_DIR / "logs"
LATEST_RUN = PIPELINE_DIR / "latest-run.json"
DOTENV_PATH = ROOT.parent / ".env"
KEY_MAP = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "gemini": "GEMINI_API_KEY",
}

STATE_LOCK = threading.Lock()
VALIDATION_LOCK = threading.Lock()
FEATURES_LOCK = threading.Lock()


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


def save_features(data: dict[str, Any]) -> None:
    FEATURES.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))


def load_previous_run() -> dict[str, Any] | None:
    if not LATEST_RUN.exists():
        return None
    latest = json.loads(LATEST_RUN.read_text())
    run_file = Path(latest["run_file"])
    if not run_file.exists():
        return None
    return json.loads(run_file.read_text())


def build_tasks(data: dict[str, Any], provider_filter: str | None, task_filter: str | None, retry_failed: bool) -> list[dict[str, Any]]:
    previous = load_previous_run()
    prev_tasks = {t["id"]: t for t in (previous or {}).get("tasks", [])}

    tasks = []
    for provider, pdata in data.items():
        if provider_filter and provider != provider_filter:
            continue
        for feature, finfo in pdata.get("features", {}).items():
            task_id = f"{provider}.{feature}"
            if task_filter and task_filter != task_id:
                continue
            prev = prev_tasks.get(task_id)
            if finfo.get("status") != "todo":
                continue
            if not retry_failed and prev and prev.get("status") in {"validated", "skipped_validation"}:
                continue
            tasks.append({
                "id": task_id,
                "provider": provider,
                "feature": feature,
                "description": finfo.get("description", ""),
                "status": "pending",
                "attempts": 0,
                "case_file": f"cases/{provider}/{feature}.json",
                "session_file": str((SESSIONS_DIR / provider / f"{feature}.jsonl").relative_to(ROOT)),
                "log_file": str((LOGS_DIR / provider / f"{feature}.log").relative_to(ROOT)),
                "attempt_log_files": [],
                "validation": None,
                "lint": None,
                "last_error": None,
                "started_at": None,
                "ended_at": None,
            })
    return tasks


def make_run(tasks: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run = {
        "run_id": run_id,
        "created_at": now_iso(),
        "cwd": str(ROOT),
        "args": vars(args),
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
    with STATE_LOCK:
        for task in run["tasks"]:
            if task["id"] == task_id:
                task.update(updates)
                break
        save_run(run)


def ensure_dirs_for(task: dict[str, Any]) -> None:
    (ROOT / task["session_file"]).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / task["log_file"]).parent.mkdir(parents=True, exist_ok=True)


def nearby_examples(provider: str, limit: int = 4) -> list[str]:
    case_dir = ROOT / "cases" / provider
    if not case_dir.exists():
        return []
    return sorted(p.name for p in case_dir.glob("*.json"))[:limit]


def provider_doc_hints(provider: str, feature: str) -> list[str]:
    pages_dir = ROOT / "api-references" / provider / "pages"
    names = []
    if provider == "openai":
        names = ["responses--create.md", "guide--function-calling.md", "guide--structured-output.md", "guide--reasoning.md"]
    elif provider == "anthropic":
        names = ["messages--create.md", "messages--streaming.md", "beta-headers.md"]
    elif provider == "gemini":
        names = ["generate-content.md", "caching.md", "models-gemini.md"]
    out = [str((pages_dir / n).relative_to(ROOT)) for n in names if (pages_dir / n).exists()]
    if feature in {"image_url", "image_inline", "image_base64", "pdf_base64", "pdf_inline"}:
        extra = [p for p in pages_dir.glob("*.md") if "generate-content" in p.name or "messages--create" in p.name or "responses--create" in p.name]
        out.extend(str(p.relative_to(ROOT)) for p in extra[:1])
    return out


def build_generation_prompt(task: dict[str, Any]) -> str:
    provider = task["provider"]
    feature = task["feature"]
    case_file = task["case_file"]
    docs = "\n".join(f"   - {p}" for p in provider_doc_hints(provider, feature))
    examples = "\n".join(f"   - cases/{provider}/{name}" for name in nearby_examples(provider))
    return f"""You are working in the curl-fixtures repository.

Implement exactly one missing fixture case.

Target:
- provider: {provider}
- feature: {feature}
- case file: {case_file}

You must read first:
- README.md
- features.yaml
- api-references/README.md
{docs if docs else ''}
{examples if examples else ''}

Requirements:
1. Create or update exactly this file: {case_file}
2. Do not edit unrelated files.
3. Match the existing case JSON style exactly.
4. Use the feature description in features.yaml as the source of truth.
5. Prefer the smallest robust request that really exercises the feature.
6. Prefer stable public assets and low-cost prompts.
7. Keep expect.status correct for a successful live request.
8. The file must contain:
   - id = {provider}.{feature}
   - provider = {provider}
   - feature = {feature}
9. Make the fixture likely to pass the live validator:
   - valid JSON response or valid SSE completion
   - usage should be present when the provider returns it
   - use provider-supported field names exactly
10. At the end, print exactly:
   FILE: {case_file}
   CHANGED: yes|no
   NOTES: <one line>
"""


def build_repair_prompt(task: dict[str, Any], validation: dict[str, Any] | None, lint_errors: list[str] | None) -> str:
    provider = task["provider"]
    feature = task["feature"]
    case_file = task["case_file"]
    current = (ROOT / case_file).read_text() if (ROOT / case_file).exists() else "<missing>"
    errors = []
    if lint_errors:
        errors.extend(f"- lint: {e}" for e in lint_errors)
    if validation:
        if validation.get("stderr"):
            errors.append(f"- validator stderr: {validation['stderr'][:1200]}")
        if validation.get("stdout"):
            errors.append(f"- validator stdout: {validation['stdout'][:1600]}")
        case_result = validation.get("case_result") or {}
        sem = case_result.get("semantic_errors") or []
        for e in sem:
            errors.append(f"- semantic: {e}")
    error_text = "\n".join(errors) if errors else "- unknown validation failure"

    return f"""You are repairing one curl fixture in the curl-fixtures repository.

Target:
- provider: {provider}
- feature: {feature}
- file: {case_file}

Only edit this file.
Do not edit unrelated files.

Current file:
```json
{current}
```

Failure details:
{error_text}

Your job:
1. Read the relevant provider docs under api-references/{provider}/pages/
2. Fix the fixture so it passes live validation
3. Keep it minimal and robust
4. Preserve id/provider/feature fields
5. At the end, print exactly:
   FILE: {case_file}
   CHANGED: yes|no
   NOTES: <one line>
"""


def run_pi_prompt(task: dict[str, Any], prompt: str, model: str | None, attempt: int, dry_run: bool) -> tuple[int, str, str, list[str], str]:
    ensure_dirs_for(task)
    attempt_log = ROOT / task["log_file"].replace(".log", f".attempt{attempt}.log")
    cmd = [
        "pi",
        "-p",
        "--session", str(ROOT / task["session_file"]),
        "--tools", "read,bash,write,edit",
        "--no-extensions",
        "--append-system-prompt", "Be precise. Change only the requested file. Prefer robust low-cost fixtures.",
    ]
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt)

    if dry_run:
        return 0, "", "", cmd, str(attempt_log.relative_to(ROOT))

    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    log_text = "\n".join([
        "$ " + " ".join(cmd),
        "\n--- STDOUT ---\n",
        proc.stdout,
        "\n--- STDERR ---\n",
        proc.stderr,
    ])
    attempt_log.write_text(log_text)
    return proc.returncode, proc.stdout, proc.stderr, cmd, str(attempt_log.relative_to(ROOT))


def lint_case(task: dict[str, Any]) -> tuple[bool, list[str]]:
    path = ROOT / task["case_file"]
    errors: list[str] = []
    if not path.exists():
        return False, ["case file was not created"]
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        return False, [f"invalid JSON: {e}"]

    if data.get("id") != task["id"]:
        errors.append(f"id must be {task['id']}")
    if data.get("provider") != task["provider"]:
        errors.append(f"provider must be {task['provider']}")
    if data.get("feature") != task["feature"]:
        errors.append(f"feature must be {task['feature']}")
    req = data.get("request")
    if not isinstance(req, dict):
        errors.append("missing request object")
    else:
        if req.get("method") != "POST":
            errors.append("request.method should usually be POST")
        if not req.get("url"):
            errors.append("missing request.url")
        if "headers" not in req:
            errors.append("missing request.headers")
        if "body" not in req:
            errors.append("missing request.body")
    expect = data.get("expect")
    if not isinstance(expect, dict) or not isinstance(expect.get("status"), int):
        errors.append("expect.status must be an integer")
    return len(errors) == 0, errors


def run_validation(task: dict[str, Any], dry_run: bool) -> dict[str, Any]:
    key_var = KEY_MAP[task["provider"]]
    if not os.environ.get(key_var):
        return {
            "status": "skipped_validation",
            "reason": f"{key_var} not set",
            "validated_at": now_iso(),
        }

    cmd = [sys.executable, str(ROOT / "validate_live.py"), "--task", task["id"]]
    if dry_run:
        return {"status": "dry_run", "command": cmd, "validated_at": now_iso()}

    with VALIDATION_LOCK:
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


def mark_feature_covered(provider: str, feature: str) -> bool:
    with FEATURES_LOCK:
        data = load_features()
        if data[provider]["features"][feature]["status"] == "covered":
            return False
        data[provider]["features"][feature]["status"] = "covered"
        save_features(data)
        return True


def regenerate_readme() -> None:
    subprocess.run([sys.executable, str(ROOT / "generate_readme.py")], cwd=ROOT, check=False, capture_output=True, text=True)


def worker(run: dict[str, Any], task: dict[str, Any], model: str | None, max_attempts: int, dry_run: bool) -> dict[str, Any]:
    update_task(run, task["id"], status="running", started_at=now_iso())
    validation = None
    lint_errors: list[str] | None = None

    for attempt in range(1, max_attempts + 1):
        prompt = build_generation_prompt(task) if attempt == 1 else build_repair_prompt(task, validation, lint_errors)
        update_task(run, task["id"], status="generating", attempts=attempt)
        rc, stdout, stderr, cmd, attempt_log = run_pi_prompt(task, prompt, model, attempt, dry_run)

        with STATE_LOCK:
            for t in run["tasks"]:
                if t["id"] == task["id"]:
                    t.setdefault("attempt_log_files", []).append(attempt_log)
                    break
            save_run(run)

        if dry_run:
            update_task(run, task["id"], status="dry_run", ended_at=now_iso(), last_error=None)
            return {"task_id": task["id"], "status": "dry_run", "command": cmd}

        if rc != 0:
            update_task(run, task["id"], status="pi_failed", last_error=stderr or stdout, ended_at=now_iso())
            return {"task_id": task["id"], "status": "pi_failed", "returncode": rc}

        ok, lint_errors = lint_case(task)
        update_task(run, task["id"], status="generated", lint={"ok": ok, "errors": lint_errors})
        if not ok:
            validation = {"status": "lint_failed", "stdout": "", "stderr": "\n".join(lint_errors), "case_result": None}
            if attempt < max_attempts:
                continue
            update_task(run, task["id"], status="lint_failed", last_error="; ".join(lint_errors), ended_at=now_iso())
            return {"task_id": task["id"], "status": "lint_failed", "errors": lint_errors}

        update_task(run, task["id"], status="validating")
        validation = run_validation(task, dry_run=False)
        update_task(run, task["id"], status=validation["status"], validation=validation)

        if validation["status"] == "validated":
            changed = mark_feature_covered(task["provider"], task["feature"])
            regenerate_readme()
            update_task(run, task["id"], status="validated", ended_at=now_iso(), last_error=None, covered_marked=changed)
            return {"task_id": task["id"], "status": "validated", "validation": validation}

        if validation["status"] == "skipped_validation":
            update_task(run, task["id"], status="skipped_validation", ended_at=now_iso())
            return {"task_id": task["id"], "status": "skipped_validation", "validation": validation}

    update_task(run, task["id"], status="validation_failed", ended_at=now_iso(), last_error=(validation or {}).get("stderr") or (validation or {}).get("stdout"))
    return {"task_id": task["id"], "status": "validation_failed", "validation": validation}


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["openai", "anthropic", "gemini"])
    parser.add_argument("--task", help="Exact task id, e.g. openai.tool_choice_auto")
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--model", help="pi model; default is pi's own default model")
    parser.add_argument("--max-attempts", type=int, default=3)
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = load_features()
    tasks = build_tasks(data, args.provider, args.task, args.retry_failed)
    if not tasks:
        print("No todo tasks selected.")
        return 0

    run = make_run(tasks, args)
    print(f"Run: {run['run_id']}")
    print(f"Tasks: {len(tasks)}")

    if args.dry_run:
        for task in tasks:
            result = worker(run, task, args.model, args.max_attempts, dry_run=True)
            print(f"\n--- {task['id']} ---")
            print(" ".join(result["command"]))
        return 0

    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as ex:
        futs = [ex.submit(worker, run, task, args.model, args.max_attempts, False) for task in tasks]
        for fut in as_completed(futs):
            result = fut.result()
            results.append(result)
            print(f"[{result['status']}] {result['task_id']}")

    regenerate_readme()
    validated = sum(1 for r in results if r["status"] == "validated")
    skipped = sum(1 for r in results if r["status"] == "skipped_validation")
    failed = len(results) - validated - skipped
    print(f"Done. validated={validated} skipped_validation={skipped} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
