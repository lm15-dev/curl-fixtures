#!/usr/bin/env python3
"""
Validate curl fixtures against live APIs.

Usage:
    python3 curl-fixtures/validate_live.py
    python3 curl-fixtures/validate_live.py openai
    python3 curl-fixtures/validate_live.py --dry-run
"""

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CASES_DIR = ROOT / "cases"

KEY_MAP = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "gemini": "GEMINI_API_KEY",
}


def build_curl(case: dict, api_key: str, redact: bool = False) -> list[str]:
    """Build a curl command from a case dict."""
    req = case["request"]
    url = req["url"]

    # Query params
    params = req.get("params", {})
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url += "?" + qs

    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", req["method"], url]

    for k, v in req.get("headers", {}).items():
        # Substitute $ENV_VAR references
        if isinstance(v, str) and "$" in v:
            for env_var in KEY_MAP.values():
                v = v.replace(f"${env_var}", api_key if not redact else "REDACTED")
        cmd.extend(["-H", f"{k}: {v}"])

    body = req.get("body")
    if body:
        cmd.extend(["-d", json.dumps(body)])

    return cmd


def build_curl_display(case: dict, api_key: str, redact: bool = True) -> str:
    """Build a displayable curl command string."""
    req = case["request"]
    url = req["url"]

    params = req.get("params", {})
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url += "?" + qs

    parts = [f"curl -X {req['method']} '{url}'"]

    for k, v in req.get("headers", {}).items():
        if isinstance(v, str) and "$" in v:
            for env_var in KEY_MAP.values():
                v = v.replace(f"${env_var}", "REDACTED" if redact else api_key)
        parts.append(f"  -H '{k}: {v}'")

    body = req.get("body")
    if body:
        parts.append(f"  -d '{json.dumps(body)}'")

    return " \\\n".join(parts)


def main():
    filter_provider = None
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg in KEY_MAP:
            filter_provider = arg

    passed = 0
    failed = 0
    skipped = 0

    for provider_dir in sorted(CASES_DIR.iterdir()):
        if not provider_dir.is_dir():
            continue
        provider = provider_dir.name
        if filter_provider and provider != filter_provider:
            continue

        key_var = KEY_MAP.get(provider)
        if not key_var:
            continue

        api_key = os.environ.get(key_var, "")
        if not api_key:
            for case_file in sorted(provider_dir.glob("*.json")):
                feature = case_file.stem
                print(f"  ⚠️  {provider}.{feature}: {key_var} not set, skipping")
                skipped += 1
            continue

        for case_file in sorted(provider_dir.glob("*.json")):
            feature = case_file.stem
            case_id = f"{provider}.{feature}"

            with open(case_file) as f:
                case = json.load(f)

            if dry_run:
                print(f"--- {case_id} ---")
                print(build_curl_display(case, api_key, redact=True))
                print()
                continue

            cmd = build_curl(case, api_key)
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                http_code = result.stdout.strip()
                expected = str(case.get("expect", {}).get("status", 200))

                if http_code == expected:
                    print(f"  ✅ {case_id} (HTTP {http_code})")
                    passed += 1
                else:
                    print(f"  ❌ {case_id} (expected {expected}, got {http_code})")
                    # Re-run to capture body for debugging
                    debug_cmd = build_curl(case, api_key)
                    debug_cmd[debug_cmd.index("-o")] = "-o"  # already there
                    # Actually just re-run without -o /dev/null
                    debug_cmd2 = [c for c in debug_cmd if c != "/dev/null" and c != "-o" and c != "-w" and c != "%{http_code}"]
                    debug_result = subprocess.run(debug_cmd2, capture_output=True, text=True, timeout=30)
                    body_preview = debug_result.stdout[:200]
                    print(f"     {body_preview}")
                    failed += 1
            except subprocess.TimeoutExpired:
                print(f"  ❌ {case_id} (timeout)")
                failed += 1
            except Exception as e:
                print(f"  ❌ {case_id} ({e})")
                failed += 1

    if not dry_run:
        print(f"\n=== Summary ===")
        print(f"Pass: {passed}")
        print(f"Fail: {failed}")
        print(f"Skip: {skipped}")

        if failed > 0:
            sys.exit(1)


if __name__ == "__main__":
    main()
