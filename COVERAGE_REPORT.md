# lm15 Coverage Report

_Generated at 2026-04-13T15:04:43Z by `coverage_report.py`._

## Legend

| Column | Meaning |
|---|---|
| Fixture | Curl fixture case file exists |
| Live | Last live test against real API passed |
| Scope | `lm15` = SDK should abstract; `provider` = provider-only feature |
| py/ts/go/rs/jl | SDK produces request body matching the fixture |
| ✅ | Present / passing |
| · | Missing (lm15 scope — gap to close) |
| — | Not applicable (provider-only) |

## OPENAI (41 features)

| Feature | Fixture | Live | Scope | py | ts | go | rs | jl |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| basic_text | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| streaming | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| system_prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| temperature | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| tools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| image_url | ✅ | ✅ | **gap** | · | · | · | · | · |
| image_file | ✅ | ✅ | provider | — | — | — | — | — |
| file_input | ✅ | ✅ | provider | — | — | — | — | — |
| multi_turn | ✅ | ✅ | **gap** | · | · | · | · | · |
| multi_turn_tool_result | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_choice_auto | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_choice_required | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_choice_none | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_choice_specific | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| parallel_tool_calls | ✅ | ✅ | provider | — | — | — | — | — |
| max_tool_calls | ✅ | ✅ | provider | — | — | — | — | — |
| structured_output | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| structured_output_json_object | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| top_p | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| top_logprobs | ✅ | ✅ | provider | — | — | — | — | — |
| reasoning | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| reasoning_encrypted | ✅ | ✅ | provider | — | — | — | — | — |
| web_search | ✅ | ✅ | provider | — | — | — | — | — |
| file_search | ✅ | ✅ | provider | — | — | — | — | — |
| code_interpreter | ✅ | ✅ | provider | — | — | — | — | — |
| computer_use | ✅ | ✅ | provider | — | — | — | — | — |
| previous_response_id | ✅ | ✅ | provider | — | — | — | — | — |
| conversation | ✅ | ✅ | provider | — | — | — | — | — |
| store | ✅ | ✅ | provider | — | — | — | — | — |
| background | ✅ | ✅ | provider | — | — | — | — | — |
| truncation | ✅ | ✅ | provider | — | — | — | — | — |
| service_tier | ✅ | ✅ | provider | — | — | — | — | — |
| metadata | ✅ | ✅ | provider | — | — | — | — | — |
| prompt | ✅ | ✅ | provider | — | — | — | — | — |
| include | ✅ | ✅ | provider | — | — | — | — | — |
| context_management | ✅ | ✅ | provider | — | — | — | — | — |
| prompt_cache_key | ✅ | ✅ | provider | — | — | — | — | — |
| prompt_cache_retention | ✅ | ✅ | provider | — | — | — | — | — |
| safety_identifier | ✅ | ✅ | provider | — | — | — | — | — |
| stream_options | ✅ | ✅ | provider | — | — | — | — | — |
| user | ✅ | ✅ | provider | — | — | — | — | — |

## ANTHROPIC (27 features)

| Feature | Fixture | Live | Scope | py | ts | go | rs | jl |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| basic_text | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| streaming | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| system_prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| temperature | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| max_tokens | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| image_base64 | ✅ | ✅ | provider | — | — | — | — | — |
| image_url | ✅ | ✅ | **gap** | · | · | · | · | · |
| pdf_base64 | ✅ | ✅ | provider | — | — | — | — | — |
| multi_turn | ✅ | ✅ | **gap** | · | · | · | · | · |
| multi_turn_tool_result | ✅ | ✅ | **gap** | · | · | · | · | · |
| system_content_blocks | ✅ | ✅ | provider | — | — | — | — | — |
| tool_choice_auto | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_choice_any | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_choice_specific | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_choice_none | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| stop_sequences | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| top_p | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| top_k | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| thinking | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| thinking_budget | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| cache_control | ✅ | ✅ | provider | — | — | — | — | — |
| metadata | ✅ | ✅ | provider | — | — | — | — | — |
| service_tier | ✅ | ✅ | provider | — | — | — | — | — |
| output_config | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| container | ✅ | ✅ | provider | — | — | — | — | — |
| inference_geo | ✅ | ✅ | provider | — | — | — | — | — |

## GEMINI (27 features)

| Feature | Fixture | Live | Scope | py | ts | go | rs | jl |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| basic_text | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| streaming | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| system_prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| tools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| image_inline | ✅ | ✅ | **gap** | · | · | · | · | · |
| image_file_uri | ✅ | ✅ | provider | — | — | — | — | — |
| audio_inline | ✅ | ✅ | provider | — | — | — | — | — |
| video_file | ✅ | ✅ | provider | — | — | — | — | — |
| pdf_inline | ✅ | ✅ | provider | — | — | — | — | — |
| multi_turn | ✅ | ✅ | **gap** | · | · | · | · | · |
| multi_turn_function_response | ✅ | ✅ | **gap** | · | · | · | · | · |
| temperature | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| max_output_tokens | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| top_p | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| top_k | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| stop_sequences | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| response_mime_type | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| response_schema | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| thinking | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_config_auto | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_config_any | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| tool_config_none | ✅ | ✅ | ✅ | ✅ | · | · | · | · |
| safety_settings | ✅ | ✅ | provider | — | — | — | — | — |
| google_search | ✅ | ✅ | provider | — | — | — | — | — |
| code_execution | ✅ | ✅ | provider | — | — | — | — | — |
| cached_content | ✅ | ✅ | provider | — | — | — | — | — |
| store | ✅ | ✅ | provider | — | — | — | — | — |

## Summary

| | Features | Fixtures | Live ✅ | lm15 scope | SDK tested | py | ts | go | rs | jl |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| openai | 41 | 41 | 41 | 16 | 13 | 13 | 5 | 5 | 5 | 5 |
| anthropic | 27 | 27 | 27 | 19 | 16 | 16 | 3 | 3 | 3 | 3 |
| gemini | 27 | 27 | 27 | 18 | 15 | 15 | 4 | 4 | 4 | 4 |
| **Total** | **95** | **95** | **95** | **53** | **44** | **44** | **12** | **12** | **12** | **12** |

### Coverage rates

- **SDK vs lm15 scope:** 44/53 (83%)
- **Fixture coverage:** 95/95 (100%)
- **Live-tested:** 95/95 (100%)

## Gaps (9 lm15-scope features without SDK tests)

### openai

- **image_url** — Image input via URL (input_image with image_url)
  - Live: ✅ | Body fields: `['input', 'model', 'stream']`
- **multi_turn** — Multiple user/assistant messages
  - Live: ✅ | Body fields: `['input', 'model', 'stream']`
- **multi_turn_tool_result** — Conversation with tool call + tool result
  - Live: ✅ | Body fields: `['input', 'model', 'stream', 'tools']`

### anthropic

- **image_url** — Image input via URL source
  - Live: ✅ | Body fields: `['max_tokens', 'messages', 'model', 'stream']`
- **multi_turn** — Multiple user/assistant messages
  - Live: ✅ | Body fields: `['max_tokens', 'messages', 'model', 'stream']`
- **multi_turn_tool_result** — Conversation with tool_use + tool_result blocks
  - Live: ✅ | Body fields: `['max_tokens', 'messages', 'model', 'stream', 'tools']`

### gemini

- **image_inline** — Image via inlineData (base64)
  - Live: ✅ | Body fields: `['contents']`
- **multi_turn** — Multi-turn conversation (multiple contents)
  - Live: ✅ | Body fields: `['contents']`
- **multi_turn_function_response** — Conversation with functionCall + functionResponse
  - Live: ✅ | Body fields: `['contents', 'tools']`

## How to close gaps

For each gap above:

1. Check if the SDK already supports the feature
2. Add `logical_input` to the fixture in `curl-fixtures/cases/`
3. Run `dump_request` for each SDK with that logical input
4. Verify output body matches fixture body (subset check)
5. If SDK doesn't support it yet, implement it, then repeat

To regenerate this report:
```bash
python3 curl-fixtures/coverage_report.py
```
