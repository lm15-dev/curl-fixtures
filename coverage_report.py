#!/usr/bin/env python3
"""
Generate the lm15 SDK coverage report.

Reads from:
  - features.yaml          (all provider features + scope)
  - cases/*/               (fixture JSON files)
  - results/latest.json    (last live-test run)
  - cross-sdk output dir   (SDK dump_request results)

Writes:
  - COVERAGE_REPORT.md

Usage:
    python3 curl-fixtures/coverage_report.py
    python3 curl-fixtures/coverage_report.py --json   # also write machine-readable summary
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).parent
REPO_ROOT = ROOT.parent
CROSS_SDK_DIR = REPO_ROOT / "cross-sdk-curl-tests"
SDKS = ["py", "ts", "go", "rs", "jl"]
SDK_LABELS = {"py": "Python", "ts": "TypeScript", "go": "Go", "rs": "Rust", "jl": "Julia"}
PROVIDERS = ["openai", "anthropic", "gemini"]
WRITE_JSON = "--json" in sys.argv


# ── Load data sources ────────────────────────────────────────────────────────

def load_features():
    with open(ROOT / "features.yaml") as f:
        return yaml.safe_load(f)


def load_fixtures():
    fixtures = {}
    for f in sorted((ROOT / "cases").rglob("*.json")):
        data = json.loads(f.read_text())
        fixtures[data["id"]] = data
    return fixtures


def load_live_results():
    path = ROOT / "results" / "latest.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text())
    return data.get("cases", {})


def load_sdk_results(fixtures):
    """
    Find SDK test results. Checks two places:
    1. Fixture files with logical_input — look for matching SDK output
    2. Legacy cross-sdk-curl-tests output directory
    """
    # Build reverse map: fixture_id → cross-sdk case IDs
    # The cross-sdk tests use different IDs (e.g. "openai.with_system" vs "openai.system_prompt")
    cross_sdk_outputs = {}

    # Scan all cross-sdk output files
    output_dir = CROSS_SDK_DIR / "output"
    if output_dir.exists():
        for f in output_dir.glob("*.json"):
            # filename like: openai.basic_text.py.json
            parts = f.stem.rsplit(".", 1)  # ["openai.basic_text", "py"]
            if len(parts) == 2:
                case_id, sdk = parts
                if sdk in SDKS:
                    cross_sdk_outputs.setdefault(case_id, {})[sdk] = f

    # Map cross-sdk case IDs to fixture IDs by comparing request bodies
    fixture_sdk_match = {}  # fixture_id → {sdk: bool}

    for fixture_id, fixture in fixtures.items():
        fixture_body = fixture["request"]["body"]
        fixture_sdk_match[fixture_id] = {}

        for case_id, sdk_files in cross_sdk_outputs.items():
            for sdk, path in sdk_files.items():
                if fixture_id in fixture_sdk_match and sdk in fixture_sdk_match[fixture_id]:
                    continue  # already matched
                try:
                    sdk_output = json.loads(path.read_text())
                    sdk_body = sdk_output.get("body", {})
                    # Deep compare with sorted keys
                    if json.dumps(fixture_body, sort_keys=True) == json.dumps(sdk_body, sort_keys=True):
                        fixture_sdk_match[fixture_id][sdk] = True
                except (json.JSONDecodeError, KeyError):
                    pass

    return fixture_sdk_match


# ── Report generation ────────────────────────────────────────────────────────

def generate_report():
    features = load_features()
    fixtures = load_fixtures()
    live_results = load_live_results()
    sdk_results = load_sdk_results(fixtures)

    lines = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines.append("# lm15 Coverage Report")
    lines.append("")
    lines.append(f"_Generated at {now} by `coverage_report.py`._")
    lines.append("")
    lines.append("## Legend")
    lines.append("")
    lines.append("| Column | Meaning |")
    lines.append("|---|---|")
    lines.append("| Fixture | Curl fixture case file exists |")
    lines.append("| Live | Last live test against real API passed |")
    lines.append("| Scope | `lm15` = SDK should abstract; `provider` = provider-only feature |")
    lines.append("| py/ts/go/rs/jl | SDK produces request body matching the fixture |")
    lines.append("| ✅ | Present / passing |")
    lines.append("| · | Missing (lm15 scope — gap to close) |")
    lines.append("| — | Not applicable (provider-only) |")
    lines.append("")

    # Per-provider tables
    totals = {
        "features": 0, "fixtures": 0, "live": 0,
        "lm15_scope": 0, "sdk_tested": 0,
    }
    totals.update({s: 0 for s in SDKS})
    provider_stats = {}
    all_gaps = {}

    for provider in PROVIDERS:
        pconfig = features[provider]
        pfeatures = pconfig["features"]
        pstats = {
            "features": 0, "fixtures": 0, "live": 0,
            "lm15_scope": 0, "sdk_tested": 0,
        }
        pstats.update({s: 0 for s in SDKS})
        gaps = []

        lines.append(f"## {provider.upper()} ({len(pfeatures)} features)")
        lines.append("")
        lines.append("| Feature | Fixture | Live | Scope | py | ts | go | rs | jl |")
        lines.append("|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")

        for fname, finfo in pfeatures.items():
            fid = f"{provider}.{fname}"
            pstats["features"] += 1
            totals["features"] += 1

            scope = finfo.get("scope", "provider")
            is_lm15 = scope == "lm15"
            if is_lm15:
                pstats["lm15_scope"] += 1
                totals["lm15_scope"] += 1

            has_fixture = fid in fixtures
            if has_fixture:
                pstats["fixtures"] += 1
                totals["fixtures"] += 1

            lr = live_results.get(fid, {})
            live_pass = lr.get("result") == "pass"
            live_fail = lr.get("result") == "fail"
            if live_pass:
                pstats["live"] += 1
                totals["live"] += 1
            live_str = "✅" if live_pass else ("❌" if live_fail else "·")

            sdk_match = sdk_results.get(fid, {})
            any_sdk = any(sdk_match.get(s) for s in SDKS)
            if any_sdk:
                pstats["sdk_tested"] += 1
                totals["sdk_tested"] += 1

            sdk_strs = {}
            for s in SDKS:
                if sdk_match.get(s):
                    sdk_strs[s] = "✅"
                    pstats[s] += 1
                    totals[s] += 1
                elif not is_lm15:
                    sdk_strs[s] = "—"
                else:
                    sdk_strs[s] = "·"

            if is_lm15 and any_sdk:
                scope_str = "✅"
            elif is_lm15:
                scope_str = "**gap**"
                gaps.append((fname, finfo, fid, live_pass))
            else:
                scope_str = "provider"

            lines.append(
                f"| {fname} | {'✅' if has_fixture else '·'} | {live_str} "
                f"| {scope_str} | {sdk_strs['py']} | {sdk_strs['ts']} "
                f"| {sdk_strs['go']} | {sdk_strs['rs']} | {sdk_strs['jl']} |"
            )

        lines.append("")
        provider_stats[provider] = pstats
        if gaps:
            all_gaps[provider] = gaps

    # ── Summary table ────────────────────────────────────────────────────

    lines.append("## Summary")
    lines.append("")
    lines.append("| | Features | Fixtures | Live ✅ | lm15 scope | SDK tested | py | ts | go | rs | jl |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for provider in PROVIDERS:
        p = provider_stats[provider]
        lines.append(
            f"| {provider} | {p['features']} | {p['fixtures']} | {p['live']} "
            f"| {p['lm15_scope']} | {p['sdk_tested']} "
            f"| {p['py']} | {p['ts']} | {p['go']} | {p['rs']} | {p['jl']} |"
        )
    lines.append(
        f"| **Total** | **{totals['features']}** | **{totals['fixtures']}** "
        f"| **{totals['live']}** | **{totals['lm15_scope']}** "
        f"| **{totals['sdk_tested']}** "
        f"| **{totals['py']}** | **{totals['ts']}** | **{totals['go']}** "
        f"| **{totals['rs']}** | **{totals['jl']}** |"
    )
    lines.append("")

    # Coverage percentages
    lines.append("### Coverage rates")
    lines.append("")
    if totals["lm15_scope"] > 0:
        pct = totals["sdk_tested"] / totals["lm15_scope"] * 100
        lines.append(f"- **SDK vs lm15 scope:** {totals['sdk_tested']}/{totals['lm15_scope']} ({pct:.0f}%)")
    if totals["features"] > 0:
        pct = totals["fixtures"] / totals["features"] * 100
        lines.append(f"- **Fixture coverage:** {totals['fixtures']}/{totals['features']} ({pct:.0f}%)")
        pct = totals["live"] / totals["features"] * 100
        lines.append(f"- **Live-tested:** {totals['live']}/{totals['features']} ({pct:.0f}%)")
    lines.append("")

    # ── Gaps detail ──────────────────────────────────────────────────────

    if all_gaps:
        total_gaps = sum(len(g) for g in all_gaps.values())
        lines.append(f"## Gaps ({total_gaps} lm15-scope features without SDK tests)")
        lines.append("")

        for provider, gaps in all_gaps.items():
            lines.append(f"### {provider}")
            lines.append("")
            for fname, finfo, fid, live_pass in gaps:
                desc = finfo.get("description", "")
                fixture = fixtures.get(fid)
                body_keys = sorted(fixture["request"]["body"].keys()) if fixture else []
                lines.append(f"- **{fname}** — {desc}")
                lines.append(f"  - Live: {'✅' if live_pass else '·'} | Body fields: `{body_keys}`")
            lines.append("")

    # ── Action plan ──────────────────────────────────────────────────────

    lines.append("## How to close gaps")
    lines.append("")
    lines.append("For each gap above:")
    lines.append("")
    lines.append("1. Check if the SDK already supports the feature")
    lines.append("2. Add `logical_input` to the fixture in `curl-fixtures/cases/`")
    lines.append("3. Run `dump_request` for each SDK with that logical input")
    lines.append("4. Verify output body matches fixture body (subset check)")
    lines.append("5. If SDK doesn't support it yet, implement it, then repeat")
    lines.append("")
    lines.append("To regenerate this report:")
    lines.append("```bash")
    lines.append("python3 curl-fixtures/coverage_report.py")
    lines.append("```")

    report = "\n".join(lines)

    # Write markdown
    out_path = ROOT / "COVERAGE_REPORT.md"
    out_path.write_text(report + "\n")
    print(f"Written to {out_path}")

    # Optionally write machine-readable JSON
    if WRITE_JSON:
        summary = {
            "generated_at": now,
            "totals": totals,
            "providers": provider_stats,
            "gaps": {
                p: [{"feature": f, "id": fid, "live": lp}
                    for f, _, fid, lp in gs]
                for p, gs in all_gaps.items()
            },
        }
        json_path = ROOT / "COVERAGE_REPORT.json"
        json_path.write_text(json.dumps(summary, indent=2) + "\n")
        print(f"Written to {json_path}")

    # Print summary to stdout
    print()
    print(f"Features: {totals['features']}  |  "
          f"lm15 scope: {totals['lm15_scope']}  |  "
          f"SDK tested: {totals['sdk_tested']}  |  "
          f"Gaps: {totals['lm15_scope'] - totals['sdk_tested']}")

    return totals["lm15_scope"] - totals["sdk_tested"]


if __name__ == "__main__":
    gaps = generate_report()
    # Exit 0 always — this is a report, not a test
    # Use --strict if you want CI to fail on gaps
    if "--strict" in sys.argv and gaps > 0:
        sys.exit(1)
