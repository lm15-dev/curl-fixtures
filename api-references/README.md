# API References (local cache)

Locally cached API reference docs for OpenAI, Anthropic, and Gemini. These serve as the source of truth for:

1. **Generating curl fixtures** — `extract_features.py` parses these to find every parameter/feature
2. **Building provider adapters** — read the relevant `pages/` file when implementing or debugging
3. **Tracking new features** — re-run `update.sh`, diff against existing cases, flag gaps

## Providers

| Provider | Pages | Key endpoint doc | Update |
|----------|-------|-----------------|--------|
| OpenAI | `openai/pages/` (39 files) | `responses--create.md` | `bash openai/update.sh` |
| Anthropic | `anthropic/pages/` (26 files) | `messages--create.md` | `bash anthropic/update.sh` |
| Gemini | `gemini/pages/` (14 files) | `generate-content.md` | `bash gemini/update.sh` |

## Updating all

```bash
cd curl-fixtures/api-references
bash openai/update.sh
bash anthropic/update.sh
bash gemini/update.sh
```

## Sources

- OpenAI: https://developers.openai.com (native `.md` + Stainless `/index.md`)
- Anthropic: https://platform.claude.com/docs/en/api (native `.md`)
- Gemini: https://ai.google.dev/api (native `.md.txt`)
