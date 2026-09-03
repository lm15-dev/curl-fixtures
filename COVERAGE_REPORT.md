# lm15 Coverage Report

_Generated at 2026-04-29T14:09:30Z by `coverage_report.py`._

## Legend

| Column | Meaning |
|---|---|
| Fixture | Curl fixture case file exists |
| Live | Last live test against real API passed |
| Scope | `lm15` = SDK should abstract; `provider` = provider-only feature |
| py/ts/go/rs/jl request | SDK produces request body matching the fixture |
| py response | Python parses a saved complete provider response against `expect_lm15` |
| py stream | Python parses and materializes a saved SSE response against `expect_lm15` |
| ✅ | Present / passing |
| · | Missing (lm15 scope — gap to close) |
| — | Not applicable (provider-only) |

## OPENAI (41 features)

| Feature | Fixture | Live | Scope | py request | ts request | go request | rs request | jl request | py response | py stream |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| basic_text | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| streaming | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| system_prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| temperature | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| image_url | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| image_file | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| file_input | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| multi_turn | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| multi_turn_tool_result | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| tool_choice_auto | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_choice_required | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_choice_none | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_choice_specific | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| parallel_tool_calls | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| max_tool_calls | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| structured_output | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| structured_output_json_object | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| top_p | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| top_logprobs | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| reasoning | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| reasoning_encrypted | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| web_search | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| file_search | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| code_interpreter | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| computer_use | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| previous_response_id | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| conversation | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| store | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| background | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| truncation | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| service_tier | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| metadata | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| prompt | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| include | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| context_management | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| prompt_cache_key | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| prompt_cache_retention | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| safety_identifier | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| stream_options | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| user | ✅ | ✅ | provider | — | — | — | — | — | — | — |

## ANTHROPIC (28 features)

| Feature | Fixture | Live | Scope | py request | ts request | go request | rs request | jl request | py response | py stream |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| basic_text | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| streaming | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| system_prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| temperature | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| max_tokens | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| image_base64 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| image_url | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| pdf_base64 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| multi_turn | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| multi_turn_tool_result | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| system_content_blocks | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| tool_choice_auto | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_choice_any | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_choice_specific | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_choice_none | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| stop_sequences | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| top_p | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| top_k | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| thinking | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| thinking_budget | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| cache_control | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| metadata | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| service_tier | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| output_config | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| web_search | ✅ | · | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| container | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| inference_geo | ✅ | ✅ | provider | — | — | — | — | — | — | — |

## GEMINI (27 features)

| Feature | Fixture | Live | Scope | py request | ts request | go request | rs request | jl request | py response | py stream |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| basic_text | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| streaming | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| system_prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| image_inline | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| image_file_uri | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| audio_inline | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| video_file | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| pdf_inline | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| multi_turn | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| multi_turn_function_response | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| temperature | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| max_output_tokens | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| top_p | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| top_k | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| stop_sequences | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| response_mime_type | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| response_schema | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| thinking | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_config_auto | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_config_any | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| tool_config_none | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | · | — |
| safety_settings | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| google_search | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| code_execution | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| cached_content | ✅ | ✅ | provider | — | — | — | — | — | — | — |
| store | ✅ | ✅ | provider | — | — | — | — | — | — | — |

## Summary

| | Features | Fixtures | Live ✅ | lm15 scope | SDK tested | py req | ts req | go req | rs req | jl req | py response | py stream |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| openai | 41 | 41 | 41 | 22 | 22 | 22 | 22 | 22 | 22 | 22 | 6 | 1 |
| anthropic | 28 | 28 | 27 | 23 | 23 | 23 | 23 | 23 | 23 | 23 | 3 | 1 |
| gemini | 27 | 27 | 27 | 24 | 24 | 24 | 24 | 24 | 24 | 24 | 4 | 1 |
| **Total** | **96** | **96** | **95** | **69** | **69** | **69** | **69** | **69** | **69** | **69** | **13** | **3** |

### Coverage rates

- **SDK vs lm15 scope:** 69/69 (100%)
- **Python response parse fixtures:** 13/14 (93%)
- **Python stream parse fixtures:** 3/3 (100%)
- **Fixture coverage:** 96/96 (100%)
- **Live-tested:** 95/96 (99%)

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
