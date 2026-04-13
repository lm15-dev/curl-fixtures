# lm15 Coverage Report

## Current state

### OPENAI (41 features)

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
| tool_choice_auto | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_choice_required | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_choice_none | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_choice_specific | ✅ | ✅ | **gap** | · | · | · | · | · |
| parallel_tool_calls | ✅ | ✅ | provider | — | — | — | — | — |
| max_tool_calls | ✅ | ✅ | provider | — | — | — | — | — |
| structured_output | ✅ | ✅ | **gap** | · | · | · | · | · |
| structured_output_json_object | ✅ | ✅ | **gap** | · | · | · | · | · |
| top_p | ✅ | ✅ | **gap** | · | · | · | · | · |
| top_logprobs | ✅ | ✅ | provider | — | — | — | — | — |
| reasoning | ✅ | ✅ | **gap** | · | · | · | · | · |
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

### ANTHROPIC (27 features)

| Feature | Fixture | Live | Scope | py | ts | go | rs | jl |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| basic_text | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| streaming | ✅ | ✅ | **gap** | · | · | · | · | · |
| system_prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| temperature | ✅ | ✅ | **gap** | · | · | · | · | · |
| max_tokens | ✅ | ✅ | **gap** | · | · | · | · | · |
| tools | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| image_base64 | ✅ | ✅ | provider | — | — | — | — | — |
| image_url | ✅ | ✅ | **gap** | · | · | · | · | · |
| pdf_base64 | ✅ | ✅ | provider | — | — | — | — | — |
| multi_turn | ✅ | ✅ | **gap** | · | · | · | · | · |
| multi_turn_tool_result | ✅ | ✅ | **gap** | · | · | · | · | · |
| system_content_blocks | ✅ | ✅ | provider | — | — | — | — | — |
| tool_choice_auto | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_choice_any | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_choice_specific | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_choice_none | ✅ | ✅ | **gap** | · | · | · | · | · |
| stop_sequences | ✅ | ✅ | **gap** | · | · | · | · | · |
| top_p | ✅ | ✅ | **gap** | · | · | · | · | · |
| top_k | ✅ | ✅ | **gap** | · | · | · | · | · |
| thinking | ✅ | ✅ | **gap** | · | · | · | · | · |
| thinking_budget | ✅ | ✅ | **gap** | · | · | · | · | · |
| cache_control | ✅ | ✅ | provider | — | — | — | — | — |
| metadata | ✅ | ✅ | provider | — | — | — | — | — |
| service_tier | ✅ | ✅ | provider | — | — | — | — | — |
| output_config | ✅ | ✅ | **gap** | · | · | · | · | · |
| container | ✅ | ✅ | provider | — | — | — | — | — |
| inference_geo | ✅ | ✅ | provider | — | — | — | — | — |

### GEMINI (27 features)

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
| temperature | ✅ | ✅ | **gap** | · | · | · | · | · |
| max_output_tokens | ✅ | ✅ | **gap** | · | · | · | · | · |
| top_p | ✅ | ✅ | **gap** | · | · | · | · | · |
| top_k | ✅ | ✅ | **gap** | · | · | · | · | · |
| stop_sequences | ✅ | ✅ | **gap** | · | · | · | · | · |
| response_mime_type | ✅ | ✅ | **gap** | · | · | · | · | · |
| response_schema | ✅ | ✅ | **gap** | · | · | · | · | · |
| thinking | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_config_auto | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_config_any | ✅ | ✅ | **gap** | · | · | · | · | · |
| tool_config_none | ✅ | ✅ | **gap** | · | · | · | · | · |
| safety_settings | ✅ | ✅ | provider | — | — | — | — | — |
| google_search | ✅ | ✅ | provider | — | — | — | — | — |
| code_execution | ✅ | ✅ | provider | — | — | — | — | — |
| cached_content | ✅ | ✅ | provider | — | — | — | — | — |
| store | ✅ | ✅ | provider | — | — | — | — | — |

## Summary

| | Features | Fixtures | Live ✅ | lm15 scope | SDK tested | py | ts | go | rs | jl |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| openai | 41 | 41 | 41 | 16 | 5 | 5 | 5 | 5 | 5 | 5 |
| anthropic | 27 | 27 | 27 | 19 | 3 | 3 | 3 | 3 | 3 | 3 |
| gemini | 27 | 27 | 27 | 18 | 4 | 4 | 4 | 4 | 4 | 4 |
| **Total** | **95** | **95** | **95** | **53** | **12** | **12** | **12** | **12** | **12** | **12** |

## Gaps: lm15-scope features without SDK tests

These are features lm15 *should* abstract but no SDK is tested against the fixture.

### openai

- **image_url** — Image input via URL (input_image with image_url)
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream']`
- **multi_turn** — Multiple user/assistant messages
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream']`
- **multi_turn_tool_result** — Conversation with tool call + tool result
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'tools']`
- **tool_choice_auto** — tool_choice: 'auto'
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'tool_choice', 'tools']`
- **tool_choice_required** — tool_choice: 'required'
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'tool_choice', 'tools']`
- **tool_choice_none** — tool_choice: 'none'
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'tool_choice', 'tools']`
- **tool_choice_specific** — tool_choice: {type: 'function', name: 'fn'}
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'tool_choice', 'tools']`
- **structured_output** — text.format with json_schema response format
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'text']`
- **structured_output_json_object** — text.format with json_object type
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'text']`
- **top_p** — top_p sampling parameter
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'stream', 'top_p']`
- **reasoning** — reasoning.effort parameter
  - Live tested: yes ✅
  - Body fields: `['input', 'model', 'reasoning', 'stream']`

### anthropic

- **streaming** — stream: true (SSE)
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream']`
- **temperature** — temperature parameter
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'temperature']`
- **max_tokens** — max_tokens (required field)
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream']`
- **image_url** — Image input via URL source
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream']`
- **multi_turn** — Multiple user/assistant messages
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream']`
- **multi_turn_tool_result** — Conversation with tool_use + tool_result blocks
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'tools']`
- **tool_choice_auto** — tool_choice: {type: 'auto'}
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'tool_choice', 'tools']`
- **tool_choice_any** — tool_choice: {type: 'any'}
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'tool_choice', 'tools']`
- **tool_choice_specific** — tool_choice: {type: 'tool', name: 'fn'}
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'tool_choice', 'tools']`
- **tool_choice_none** — tool_choice: {type: 'none'}
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'tool_choice', 'tools']`
- **stop_sequences** — Custom stop sequences
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stop_sequences', 'stream']`
- **top_p** — top_p (nucleus sampling)
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'top_p']`
- **top_k** — top_k sampling
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'top_k']`
- **thinking** — Extended thinking with thinking.type='enabled'
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'thinking']`
- **thinking_budget** — Thinking with budget_tokens
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'stream', 'thinking']`
- **output_config** — Output configuration (JSON mode etc)
  - Live tested: yes ✅
  - Body fields: `['max_tokens', 'messages', 'model', 'output_config', 'stream']`

### gemini

- **image_inline** — Image via inlineData (base64)
  - Live tested: yes ✅
  - Body fields: `['contents']`
- **multi_turn** — Multi-turn conversation (multiple contents)
  - Live tested: yes ✅
  - Body fields: `['contents']`
- **multi_turn_function_response** — Conversation with functionCall + functionResponse
  - Live tested: yes ✅
  - Body fields: `['contents', 'tools']`
- **temperature** — generationConfig.temperature
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **max_output_tokens** — generationConfig.maxOutputTokens
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **top_p** — generationConfig.topP
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **top_k** — generationConfig.topK
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **stop_sequences** — generationConfig.stopSequences
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **response_mime_type** — generationConfig.responseMimeType (JSON mode)
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **response_schema** — generationConfig.responseSchema (structured output)
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **thinking** — generationConfig.thinkingConfig
  - Live tested: yes ✅
  - Body fields: `['contents', 'generationConfig']`
- **tool_config_auto** — toolConfig.functionCallingConfig.mode: AUTO
  - Live tested: yes ✅
  - Body fields: `['contents', 'toolConfig', 'tools']`
- **tool_config_any** — toolConfig.functionCallingConfig.mode: ANY
  - Live tested: yes ✅
  - Body fields: `['contents', 'toolConfig', 'tools']`
- **tool_config_none** — toolConfig.functionCallingConfig.mode: NONE
  - Live tested: yes ✅
  - Body fields: `['contents', 'toolConfig', 'tools']`

## Action plan

### Phase 1: Wire fixtures to SDKs (the missing link)

1. Add `logical_input` to each lm15-scope fixture in `curl-fixtures/cases/`
2. Write `curl-fixtures/test_sdks.sh` — for each fixture with `logical_input`:
   - Feed `logical_input` to each SDK's `dump_request`
   - Assert `fixture.request.body ⊆ sdk_output.body` (subset match)
   - Assert `fixture.request.url == sdk_output.url`
   - Assert `fixture.request.method == sdk_output.method`
3. Retire `cross-sdk-curl-tests/test_cases.json` (fixtures replace it)

### Phase 2: Expand lm15 scope coverage

**Easy** (21 features — lm15 likely already supports, just needs `logical_input` + test):

- `anthropic.max_tokens`
- `anthropic.stop_sequences`
- `anthropic.streaming`
- `anthropic.temperature`
- `anthropic.tool_choice_any`
- `anthropic.tool_choice_auto`
- `anthropic.tool_choice_none`
- `anthropic.tool_choice_specific`
- `anthropic.top_p`
- `gemini.max_output_tokens`
- `gemini.stop_sequences`
- `gemini.temperature`
- `gemini.tool_config_any`
- `gemini.tool_config_auto`
- `gemini.tool_config_none`
- `gemini.top_p`
- `openai.tool_choice_auto`
- `openai.tool_choice_none`
- `openai.tool_choice_required`
- `openai.tool_choice_specific`
- `openai.top_p`

**Medium** (20 features — may need SDK work):

- `anthropic.image_url`
- `anthropic.multi_turn`
- `anthropic.multi_turn_tool_result`
- `anthropic.output_config`
- `anthropic.thinking`
- `anthropic.thinking_budget`
- `anthropic.top_k`
- `gemini.image_inline`
- `gemini.multi_turn`
- `gemini.multi_turn_function_response`
- `gemini.response_mime_type`
- `gemini.response_schema`
- `gemini.thinking`
- `gemini.top_k`
- `openai.image_url`
- `openai.multi_turn`
- `openai.multi_turn_tool_result`
- `openai.reasoning`
- `openai.structured_output`
- `openai.structured_output_json_object`

### Phase 3: CI integration

| Trigger | Test | Cost | Catches |
|---|---|---|---|
| Every commit | `test_sdks.sh` (offline, subset match) | Free | SDK regressions, field mismatches |
| Pre-release | `validate_live.sh` (all fixtures) | ~$0.02 | Provider-side changes, actual correctness |
| Weekly cron | `validate_live.sh` | ~$0.02 | Provider API drift between releases |

### Phase 4: Coverage report generation

One script (`curl-fixtures/coverage_report.py`) generates this report.
Run it anytime. Include output in CI artifacts or README.
Shows exactly where each SDK stands relative to the fixture ground truth.
