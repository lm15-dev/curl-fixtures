# API References (local cache)

Locally cached API reference docs for OpenAI, Anthropic, and Gemini. These serve as the source of truth for:

1. **Generating curl fixtures** — `extract_features.py` parses these to find every parameter/feature
2. **Building provider adapters** — read the relevant `pages/` file when implementing or debugging
3. **Tracking new features** — re-run `update.sh`, diff against existing cases, flag gaps

## Providers

| Provider | Pages | Key endpoint doc | Update |
|----------|-------|-----------------|--------|
| OpenAI | `openai/pages/` (39 files) | `responses--create.md` | `bash openai/update.sh` |
| Anthropic | `anthropic/pages/` (25 files) | `messages--create.md` | `bash anthropic/update.sh` |
| Gemini | `gemini/pages/` (14 files) | `generate-content.md` | `bash gemini/update.sh` |

## Updating all

Each `update.sh` sources `fetch.sh`: a page is written only when the server
answers 200 with a body. A dead URL keeps the cached copy, is printed, and
makes the script exit 1. Never commit a page whose body is "Not Found";
fix the URL in the script instead (17 pages rotted that way before the
guard existed, 2026-09-02).

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
