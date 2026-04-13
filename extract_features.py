#!/usr/bin/env python3
"""
Extract top-level request body parameters from cached API reference docs.
Compares against features.yaml and reports any undocumented parameters.

Usage:
    python3 curl-fixtures/extract_features.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def extract_openai_params(doc_path: Path) -> list[str]:
    """Extract top-level body params from OpenAI responses--create.md."""
    text = doc_path.read_text()
    # Pattern: lines like "- `param_name: optional type`" at indent level 0
    # Only between "### Body Parameters" and the next "###"
    in_body = False
    params = []
    for line in text.splitlines():
        if line.strip() == "### Body Parameters":
            in_body = True
            continue
        if in_body and line.startswith("### "):
            break
        if in_body:
            m = re.match(r"^- `([a-z_]+):", line)
            if m:
                params.append(m.group(1))
    return params


def extract_anthropic_params(doc_path: Path) -> list[str]:
    """Extract top-level body params from Anthropic messages--create.md."""
    text = doc_path.read_text()
    # Anthropic uses same pattern: "- `param_name: type`"
    # Look for body section
    in_body = False
    params = []
    for line in text.splitlines():
        if "Body" in line and line.startswith("#"):
            in_body = True
            continue
        if in_body and line.startswith("# "):
            break
        if in_body:
            m = re.match(r"^- `([a-z_]+):", line)
            if m:
                params.append(m.group(1))
    return params


def extract_gemini_params(doc_path: Path) -> list[str]:
    """Extract top-level request body params from Gemini generate-content.md."""
    text = doc_path.read_text()
    # Pattern: "`paramName` `type` Optional/Required."
    in_body = False
    params = []
    for line in text.splitlines():
        if "Request body" in line and line.startswith("#"):
            in_body = True
            continue
        if in_body and line.startswith("#"):
            break
        if in_body:
            m = re.match(r"^`([a-zA-Z_\[\]]+)`\s+`", line)
            if m:
                param = m.group(1).rstrip("[]")
                params.append(param)
    return params


def load_features_yaml() -> dict:
    """Load features.yaml and return provider -> set of documented feature keys."""
    import yaml
    with open(ROOT / "features.yaml") as f:
        data = yaml.safe_load(f)
    return data


def main():
    print("=== Extracting API parameters from cached docs ===\n")

    # OpenAI
    openai_doc = ROOT / "api-references/openai/pages/responses--create.md"
    openai_params = extract_openai_params(openai_doc)
    print(f"OpenAI responses.create: {len(openai_params)} params")
    for p in openai_params:
        print(f"  - {p}")

    print()

    # Anthropic
    anthropic_doc = ROOT / "api-references/anthropic/pages/messages--create.md"
    anthropic_params = extract_anthropic_params(anthropic_doc)
    print(f"Anthropic messages.create: {len(anthropic_params)} params")
    for p in anthropic_params:
        print(f"  - {p}")

    print()

    # Gemini
    gemini_doc = ROOT / "api-references/gemini/pages/generate-content.md"
    gemini_params = extract_gemini_params(gemini_doc)
    print(f"Gemini generateContent: {len(gemini_params)} params")
    for p in gemini_params:
        print(f"  - {p}")

    print()

    # Try to load features.yaml and compare
    try:
        import yaml
    except ImportError:
        print("(install pyyaml to compare against features.yaml)")
        return

    data = load_features_yaml()

    print("=== Coverage check ===\n")

    # For each provider, list params not yet mapped to any feature
    # This is a simple heuristic — param name matching
    for provider, params, config_key in [
        ("OpenAI", openai_params, "openai"),
        ("Anthropic", anthropic_params, "anthropic"),
        ("Gemini", gemini_params, "gemini"),
    ]:
        features = data.get(config_key, {}).get("features", {})
        feature_names = set(features.keys())

        # Build a set of param names that are covered by at least one feature
        # We check if the param name appears in any feature key or description
        covered_params = set()
        for fname, fdata in features.items():
            desc = fdata.get("description", "").lower()
            # Direct name match
            for p in params:
                if p.lower() in fname.lower() or p.lower() in desc:
                    covered_params.add(p)

        uncovered = [p for p in params if p not in covered_params]
        todo = [k for k, v in features.items() if v.get("status") == "todo"]
        covered_count = len([k for k, v in features.items() if v.get("status") == "covered"])

        print(f"{provider}:")
        print(f"  API params: {len(params)}")
        print(f"  Features defined: {len(features)}")
        print(f"  Covered (has fixture): {covered_count}")
        print(f"  Todo (needs fixture): {len(todo)}")
        if uncovered:
            print(f"  ⚠️  Unmapped API params: {uncovered}")
        else:
            print(f"  ✅ All API params mapped to features")
        print()


if __name__ == "__main__":
    main()
