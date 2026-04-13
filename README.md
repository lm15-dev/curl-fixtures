# Curl Fixtures

Comprehensive repository of curl requests for every feature of the OpenAI, Anthropic, and Gemini APIs. These fixtures serve two purposes:

1. **Live validation** — periodically fire each curl against real APIs to confirm they still work
2. **SDK ground truth** — `cross-sdk-curl-tests/` verifies all five lm15 SDKs produce request bodies matching these fixtures

## Structure

```
curl-fixtures/
├── api-references/           # Cached API docs (source of truth for features)
│   ├── openai/
│   ├── anthropic/
│   └── gemini/
├── cases/                    # One JSON file per curl fixture
│   ├── openai/
│   ├── anthropic/
│   └── gemini/
├── features.yaml             # Feature matrix extracted from API docs
├── extract_features.py       # Parse API docs → features.yaml
├── generate_cases.py         # Generate fixture JSONs from features + docs
├── validate_live.sh          # Run all curls against real APIs
└── check_coverage.py         # Diff features.yaml vs cases/, flag gaps
```

## Workflow

```bash
# 1. Update API docs
bash api-references/openai/update.sh
bash api-references/anthropic/update.sh
bash api-references/gemini/update.sh

# 2. Extract features from docs
python3 extract_features.py

# 3. Check what's missing
python3 check_coverage.py

# 4. Generate new cases (or write manually)
python3 generate_cases.py

# 5. Validate against live APIs
bash validate_live.sh
```

## Case format

Each file in `cases/` is a self-contained curl fixture:

```json
{
  "id": "openai.structured_output",
  "provider": "openai",
  "feature": "structured_output",
  "description": "JSON schema response format via response_format",
  "request": {
    "method": "POST",
    "url": "https://api.openai.com/v1/responses",
    "headers": {
      "Authorization": "Bearer $OPENAI_API_KEY",
      "Content-Type": "application/json"
    },
    "body": { ... }
  },
  "expect": {
    "status": 200,
    "body_path": "output[0].content[0].text"
  }
}
```

## Adding a new feature

1. Add it to `features.yaml` under the right provider
2. Create `cases/<provider>/<feature>.json` with a minimal working request
3. Run `bash validate_live.sh` to confirm it works
4. Run `python3 check_coverage.py` to verify coverage is complete
