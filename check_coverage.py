#!/usr/bin/env python3
"""
Check that every API parameter is covered by a fixture case, and that
every 'todo' feature is flagged. Exit 1 if there are gaps.

Usage:
    python3 curl-fixtures/check_coverage.py
    python3 curl-fixtures/check_coverage.py --strict  # fail on any 'todo'
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).parent
STRICT = "--strict" in sys.argv


def load_features():
    with open(ROOT / "features.yaml") as f:
        return yaml.safe_load(f)


def check_cases_exist(provider: str, features: dict) -> list[str]:
    """Check that each 'covered' feature has a corresponding case file."""
    cases_dir = ROOT / "cases" / provider
    missing = []
    for name, info in features.items():
        if info.get("status") == "covered":
            case_file = cases_dir / f"{name}.json"
            if not case_file.exists():
                missing.append(name)
    return missing


def main():
    data = load_features()
    errors = []
    warnings = []

    for provider in ["openai", "anthropic", "gemini"]:
        config = data.get(provider, {})
        features = config.get("features", {})

        covered = [k for k, v in features.items() if v.get("status") == "covered"]
        todo = [k for k, v in features.items() if v.get("status") == "todo"]
        skip = [k for k, v in features.items() if v.get("status") == "skip"]

        print(f"\n{provider.upper()}: {len(covered)} covered, {len(todo)} todo, {len(skip)} skip")

        # Check case files exist for covered features
        missing_cases = check_cases_exist(provider, features)
        if missing_cases:
            for m in missing_cases:
                errors.append(f"{provider}.{m}: marked 'covered' but no case file")
                print(f"  ❌ {m}: marked covered but cases/{provider}/{m}.json missing")

        for t in todo:
            msg = f"{provider}.{t}: {features[t].get('description', '')}"
            if STRICT:
                errors.append(msg)
                print(f"  ❌ {t}: todo")
            else:
                warnings.append(msg)
                print(f"  ⚠️  {t}: todo")

        for c in covered:
            if c not in missing_cases:
                print(f"  ✅ {c}")

    print(f"\n=== Summary ===")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\nFailing due to errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ All covered features have case files.")
        if warnings:
            print(f"({len(warnings)} features still todo)")


if __name__ == "__main__":
    main()
