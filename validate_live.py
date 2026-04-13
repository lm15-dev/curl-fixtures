#!/usr/bin/env python3
"""
Validate curl fixtures against live APIs and persist machine-readable results.

Outputs:
- results/latest.json
- results/history.jsonl
- results/bodies/<case-id>/<timestamp>.txt
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
CASES_DIR = ROOT / "cases"
RESULTS_DIR = ROOT / "results"
BODIES_DIR = RESULTS_DIR / "bodies"
LATEST_JSON = RESULTS_DIR / "latest.json"
HISTORY_JSONL = RESULTS_DIR / "history.jsonl"

KEY_MAP = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "gemini": "GEMINI_API_KEY",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_request(case: dict, api_key: str, redact: bool = False):
    req = case["request"]
    url = req["url"]
    params = req.get("params", {})
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url += "?" + qs

    headers = {}
    for k, v in req.get("headers", {}).items():
        if isinstance(v, str) and "$" in v:
            for env_var in KEY_MAP.values():
                v = v.replace(f"${env_var}", api_key if not redact else "REDACTED")
        headers[k] = v

    return url, headers, req.get("body")


def build_curl_display(case: dict, api_key: str) -> str:
    url, headers, body = build_request(case, api_key, redact=True)
    parts = [f"curl -X {case['request']['method']} '{url}'"]
    for k, v in headers.items():
        parts.append(f"  -H '{k}: {v}'")
    if body:
        parts.append(f"  -d '{json.dumps(body)}'")
    return " \\\n".join(parts)


def run_curl(case: dict, api_key: str, timeout: int = 45):
    url, headers, body = build_request(case, api_key, redact=False)
    body_file = RESULTS_DIR / ".tmp_body.txt"
    cmd = [
        "curl", "-sS", "-o", str(body_file), "-w", "%{http_code}",
        "-X", case["request"]["method"], url,
    ]
    for k, v in headers.items():
        cmd.extend(["-H", f"{k}: {v}"])
    if body is not None:
        cmd.extend(["-d", json.dumps(body)])

    started = time.time()
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    ended = time.time()
    http_code = proc.stdout.strip()
    raw_body = body_file.read_text() if body_file.exists() else ""
    if body_file.exists():
        body_file.unlink()
    return {
        "http_code": http_code,
        "raw_body": raw_body,
        "stderr": proc.stderr,
        "duration_seconds": round(ended - started, 3),
    }


def estimate_cost_usd(provider: str, case: dict, raw_body: str):
    # Placeholder. Can be upgraded later with provider pricing tables + token parsing.
    return None


def save_body(case_id: str, tested_at: str, raw_body: str) -> str | None:
    if raw_body is None:
        return None
    safe_case = case_id.replace("/", "_")
    stamp = tested_at.replace(":", "-")
    out_dir = BODIES_DIR / safe_case
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{stamp}.txt"
    path.write_text(raw_body)
    return str(path.relative_to(ROOT))


def load_latest():
    if not LATEST_JSON.exists():
        return {"generated_at": None, "cases": {}}
    with open(LATEST_JSON) as f:
        return json.load(f)


def persist_results(run_results: dict):
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    latest = load_latest()
    latest["generated_at"] = now_iso()
    latest.setdefault("cases", {}).update(run_results)
    with open(LATEST_JSON, "w") as f:
        json.dump(latest, f, indent=2, sort_keys=True)
    with open(HISTORY_JSONL, "a") as f:
        for result in run_results.values():
            f.write(json.dumps(result, sort_keys=True) + "\n")


def main():
    filter_provider = None
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg in KEY_MAP:
            filter_provider = arg

    passed = failed = skipped = 0
    run_results = {}

    for provider_dir in sorted(CASES_DIR.iterdir()):
        if not provider_dir.is_dir():
            continue
        provider = provider_dir.name
        if filter_provider and provider != filter_provider:
            continue

        key_var = KEY_MAP.get(provider)
        api_key = os.environ.get(key_var, "") if key_var else ""

        for case_file in sorted(provider_dir.glob("*.json")):
            feature = case_file.stem
            case_id = f"{provider}.{feature}"
            case = json.loads(case_file.read_text())
            tested_at = now_iso()

            if dry_run:
                if not api_key:
                    print(f"  ⚠️  {case_id}: {key_var} not set, skipping")
                else:
                    print(f"--- {case_id} ---")
                    print(build_curl_display(case, api_key))
                    print()
                continue

            if not api_key:
                print(f"  ⚠️  {case_id}: {key_var} not set, skipping")
                rec = {
                    "case_id": case_id,
                    "provider": provider,
                    "feature": feature,
                    "tested_at": tested_at,
                    "result": "skipped",
                    "http_code": None,
                    "duration_seconds": None,
                    "estimated_cost_usd": None,
                    "body_path": None,
                    "reason": f"{key_var} not set",
                }
                run_results[case_id] = rec
                skipped += 1
                continue

            try:
                result = run_curl(case, api_key)
                expected = str(case.get("expect", {}).get("status", 200))
                outcome = "pass" if result["http_code"] == expected else "fail"
                body_path = save_body(case_id, tested_at, result["raw_body"])
                rec = {
                    "case_id": case_id,
                    "provider": provider,
                    "feature": feature,
                    "tested_at": tested_at,
                    "result": outcome,
                    "http_code": int(result["http_code"]) if result["http_code"].isdigit() else result["http_code"],
                    "duration_seconds": result["duration_seconds"],
                    "estimated_cost_usd": estimate_cost_usd(provider, case, result["raw_body"]),
                    "body_path": body_path,
                    "stderr": result["stderr"] or None,
                }
                run_results[case_id] = rec
                if outcome == "pass":
                    print(f"  ✅ {case_id} (HTTP {result['http_code']}, {result['duration_seconds']}s)")
                    passed += 1
                else:
                    preview = result['raw_body'][:200].replace("\n", " ")
                    print(f"  ❌ {case_id} (expected {expected}, got {result['http_code']}, {result['duration_seconds']}s)")
                    if preview:
                        print(f"     {preview}")
                    failed += 1
            except subprocess.TimeoutExpired:
                rec = {
                    "case_id": case_id,
                    "provider": provider,
                    "feature": feature,
                    "tested_at": tested_at,
                    "result": "fail",
                    "http_code": None,
                    "duration_seconds": None,
                    "estimated_cost_usd": None,
                    "body_path": None,
                    "reason": "timeout",
                }
                run_results[case_id] = rec
                print(f"  ❌ {case_id} (timeout)")
                failed += 1
            except Exception as e:
                rec = {
                    "case_id": case_id,
                    "provider": provider,
                    "feature": feature,
                    "tested_at": tested_at,
                    "result": "fail",
                    "http_code": None,
                    "duration_seconds": None,
                    "estimated_cost_usd": None,
                    "body_path": None,
                    "reason": str(e),
                }
                run_results[case_id] = rec
                print(f"  ❌ {case_id} ({e})")
                failed += 1

    if not dry_run:
        persist_results(run_results)
        print(f"\n=== Summary ===")
        print(f"Pass: {passed}")
        print(f"Fail: {failed}")
        print(f"Skip: {skipped}")
        if failed > 0:
            sys.exit(1)


if __name__ == "__main__":
    main()
