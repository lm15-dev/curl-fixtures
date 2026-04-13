#!/usr/bin/env bash
# Validate curl fixtures against live APIs.
#
# Usage:
#   bash curl-fixtures/validate_live.sh                    # all providers
#   bash curl-fixtures/validate_live.sh openai             # one provider
#   bash curl-fixtures/validate_live.sh --dry-run          # show curls without running
#
# Required env vars (or .env file):
#   OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Load .env if present
if [ -f "$SCRIPT_DIR/../.env" ]; then
    set -a
    source "$SCRIPT_DIR/../.env"
    set +a
fi

exec python3 "$SCRIPT_DIR/validate_live.py" "$@"
