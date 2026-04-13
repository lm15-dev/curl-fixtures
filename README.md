# Curl Fixtures

Comprehensive repository of curl requests for the OpenAI, Anthropic, and Gemini APIs.

## What this repo tracks

- fixture coverage from provider docs
- live test status for each covered case
- last test timestamp
- last test duration
- estimated test cost when available
- link to the last saved response body

## Workflow

```bash
# update provider docs
bash api-references/openai/update.sh
bash api-references/anthropic/update.sh
bash api-references/gemini/update.sh

# check feature coverage
python3 extract_features.py
python3 check_coverage.py

# run live tests and persist results
bash validate_live.sh

# regenerate this README matrix
python3 generate_readme.py
```

## Provider summary

| Provider | Total features | Done | Todo | Last tested cases | Pass | Fail | Skipped | Cost to run covered tests USD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| openai | 41 | 13 | 28 | 13 | 13 | 0 | 0 | 0.00080240 |
| anthropic | 27 | 12 | 15 | 12 | 12 | 0 | 0 | 0.01771800 |
| gemini | 27 | 12 | 15 | 12 | 12 | 0 | 0 | 0.00042719 |

## Fixture matrix

| Provider | Feature | Done | Todo | Tested | Last result | Last tested at | HTTP | Duration s | Cost USD | Response body | Description |
|---|---|---|---|---|---|---|---:|---:|---:|---|---|
| openai | basic_text | yes | no | yes | pass | 2026-04-13T13:30:26Z | 200 | 2.252 | 2e-05 | [2026-04-13T13-30-26Z.txt](results/bodies/openai.basic_text/2026-04-13T13-30-26Z.txt) | Simple text prompt → text response |
| openai | streaming | yes | no | yes | pass | 2026-04-13T13:30:31Z | 200 | 1.815 | 1.96e-05 | [2026-04-13T13-30-31Z.txt](results/bodies/openai.streaming/2026-04-13T13-30-31Z.txt) | stream: true |
| openai | system_prompt | yes | no | yes | pass | 2026-04-13T13:30:39Z | 200 | 1.637 | 0.0001104 | [2026-04-13T13-30-39Z.txt](results/bodies/openai.system_prompt/2026-04-13T13-30-39Z.txt) | instructions field (system prompt) |
| openai | temperature | yes | no | yes | pass | 2026-04-13T13:30:40Z | 200 | 1.741 | 3.84e-05 | [2026-04-13T13-30-40Z.txt](results/bodies/openai.temperature/2026-04-13T13-30-40Z.txt) | temperature + max_output_tokens |
| openai | tools | yes | no | yes | pass | 2026-04-13T13:30:45Z | 200 | 2.354 | 4.4e-05 | [2026-04-13T13-30-45Z.txt](results/bodies/openai.tools/2026-04-13T13-30-45Z.txt) | Function calling with tools array |
| openai | image_url | yes | no | yes | pass | 2026-04-13T13:30:28Z | 200 | 3.377 | 0.000104 | [2026-04-13T13-30-28Z.txt](results/bodies/openai.image_url/2026-04-13T13-30-28Z.txt) | Image input via URL (input_image with image_url) |
| openai | image_file | no | yes | no | not_tested | — | — | — | — | — | Image input via file_id |
| openai | file_input | no | yes | no | not_tested | — | — | — | — | — | File/PDF input via file object |
| openai | multi_turn | no | yes | no | not_tested | — | — | — | — | — | Multiple user/assistant messages |
| openai | multi_turn_tool_result | no | yes | no | not_tested | — | — | — | — | — | Conversation with tool call + tool result |
| openai | tool_choice_auto | yes | no | yes | pass | 2026-04-13T13:42:43Z | 200 | 5.108 | 4.4e-05 | [2026-04-13T13-42-43Z.txt](results/bodies/openai.tool_choice_auto/2026-04-13T13-42-43Z.txt) | tool_choice: 'auto' |
| openai | tool_choice_required | yes | no | yes | pass | 2026-04-13T13:30:44Z | 200 | 0.716 | 3.48e-05 | [2026-04-13T13-30-44Z.txt](results/bodies/openai.tool_choice_required/2026-04-13T13-30-44Z.txt) | tool_choice: 'required' |
| openai | tool_choice_none | yes | no | yes | pass | 2026-04-13T13:30:42Z | 200 | 1.535 | 3.48e-05 | [2026-04-13T13-30-42Z.txt](results/bodies/openai.tool_choice_none/2026-04-13T13-30-42Z.txt) | tool_choice: 'none' |
| openai | tool_choice_specific | yes | no | yes | pass | 2026-04-13T13:30:44Z | 200 | 0.717 | 3.28e-05 | [2026-04-13T13-30-44Z.txt](results/bodies/openai.tool_choice_specific/2026-04-13T13-30-44Z.txt) | tool_choice: {type: 'function', name: 'fn'} |
| openai | parallel_tool_calls | no | yes | no | not_tested | — | — | — | — | — | parallel_tool_calls: true/false |
| openai | max_tool_calls | no | yes | no | not_tested | — | — | — | — | — | max_tool_calls limit |
| openai | structured_output | yes | no | yes | pass | 2026-04-13T13:30:33Z | 200 | 2.484 | 0.0001444 | [2026-04-13T13-30-33Z.txt](results/bodies/openai.structured_output/2026-04-13T13-30-33Z.txt) | text.format with json_schema response format |
| openai | structured_output_json_object | yes | no | yes | pass | 2026-04-13T13:30:36Z | 200 | 2.868 | 0.0001552 | [2026-04-13T13-30-36Z.txt](results/bodies/openai.structured_output_json_object/2026-04-13T13-30-36Z.txt) | text.format with json_object type |
| openai | top_p | yes | no | yes | pass | 2026-04-13T13:30:47Z | 200 | 1.536 | 2e-05 | [2026-04-13T13-30-47Z.txt](results/bodies/openai.top_p/2026-04-13T13-30-47Z.txt) | top_p sampling parameter |
| openai | top_logprobs | no | yes | no | not_tested | — | — | — | — | — | top_logprobs for token probabilities |
| openai | reasoning | no | yes | no | not_tested | — | — | — | — | — | reasoning.effort parameter |
| openai | reasoning_encrypted | no | yes | no | not_tested | — | — | — | — | — | reasoning with encrypted_content include |
| openai | web_search | no | yes | no | not_tested | — | — | — | — | — | Web search tool |
| openai | file_search | no | yes | no | not_tested | — | — | — | — | — | File search / retrieval tool |
| openai | code_interpreter | no | yes | no | not_tested | — | — | — | — | — | Code interpreter tool |
| openai | computer_use | no | yes | no | not_tested | — | — | — | — | — | Computer use tool |
| openai | previous_response_id | no | yes | no | not_tested | — | — | — | — | — | Chain responses via previous_response_id |
| openai | conversation | no | yes | no | not_tested | — | — | — | — | — | Conversation object for multi-turn |
| openai | store | no | yes | no | not_tested | — | — | — | — | — | store: true/false for response storage |
| openai | background | no | yes | no | not_tested | — | — | — | — | — | background: true for async processing |
| openai | truncation | no | yes | no | not_tested | — | — | — | — | — | truncation: 'auto' or 'disabled' |
| openai | service_tier | no | yes | no | not_tested | — | — | — | — | — | service_tier selection |
| openai | metadata | no | yes | no | not_tested | — | — | — | — | — | Request metadata |
| openai | prompt | no | yes | no | not_tested | — | — | — | — | — | Stored prompt reference |
| openai | include | no | yes | no | not_tested | — | — | — | — | — | include array for additional output data |
| openai | context_management | no | yes | no | not_tested | — | — | — | — | — | Context management / compaction configuration |
| openai | prompt_cache_key | no | yes | no | not_tested | — | — | — | — | — | prompt_cache_key for caching |
| openai | prompt_cache_retention | no | yes | no | not_tested | — | — | — | — | — | prompt_cache_retention duration |
| openai | safety_identifier | no | yes | no | not_tested | — | — | — | — | — | safety_identifier for content filtering |
| openai | stream_options | no | yes | no | not_tested | — | — | — | — | — | stream_options (include_obfuscation) |
| openai | user | no | yes | no | not_tested | — | — | — | — | — | user identifier for abuse tracking |
| anthropic | basic_text | yes | no | yes | pass | 2026-04-13T13:29:34Z | 200 | 0.987 | 0.00027 | [2026-04-13T13-29-34Z.txt](results/bodies/anthropic.basic_text/2026-04-13T13-29-34Z.txt) | Simple text prompt → text response |
| anthropic | streaming | yes | no | yes | pass | 2026-04-13T13:29:38Z | 200 | 1.636 | 0.000207 | [2026-04-13T13-29-38Z.txt](results/bodies/anthropic.streaming/2026-04-13T13-29-38Z.txt) | stream: true (SSE) |
| anthropic | system_prompt | yes | no | yes | pass | 2026-04-13T13:29:40Z | 200 | 2.662 | 0.001236 | [2026-04-13T13-29-40Z.txt](results/bodies/anthropic.system_prompt/2026-04-13T13-29-40Z.txt) | system field (string or content blocks) |
| anthropic | temperature | yes | no | yes | pass | 2026-04-13T13:29:43Z | 200 | 1.214 | 0.000195 | [2026-04-13T13-29-43Z.txt](results/bodies/anthropic.temperature/2026-04-13T13-29-43Z.txt) | temperature parameter |
| anthropic | max_tokens | yes | no | yes | pass | 2026-04-13T13:29:37Z | 200 | 1.229 | 0.00021 | [2026-04-13T13-29-37Z.txt](results/bodies/anthropic.max_tokens/2026-04-13T13-29-37Z.txt) | max_tokens (required field) |
| anthropic | tools | yes | no | yes | pass | 2026-04-13T13:29:52Z | 200 | 1.329 | 0.00249 | [2026-04-13T13-29-52Z.txt](results/bodies/anthropic.tools/2026-04-13T13-29-52Z.txt) | Function calling with tools array |
| anthropic | image_base64 | no | yes | no | not_tested | — | — | — | — | — | Image input via base64 source |
| anthropic | image_url | yes | no | yes | pass | 2026-04-13T13:29:35Z | 200 | 1.995 | 0.000519 | [2026-04-13T13-29-35Z.txt](results/bodies/anthropic.image_url/2026-04-13T13-29-35Z.txt) | Image input via URL source |
| anthropic | pdf_base64 | no | yes | no | not_tested | — | — | — | — | — | PDF input via base64 document source |
| anthropic | multi_turn | no | yes | no | not_tested | — | — | — | — | — | Multiple user/assistant messages |
| anthropic | multi_turn_tool_result | no | yes | no | not_tested | — | — | — | — | — | Conversation with tool_use + tool_result blocks |
| anthropic | system_content_blocks | no | yes | no | not_tested | — | — | — | — | — | System as array of TextBlockParam (with cache_control) |
| anthropic | tool_choice_auto | yes | no | yes | pass | 2026-04-13T13:29:48Z | 200 | 1.725 | 0.00249 | [2026-04-13T13-29-48Z.txt](results/bodies/anthropic.tool_choice_auto/2026-04-13T13-29-48Z.txt) | tool_choice: {type: 'auto'} |
| anthropic | tool_choice_any | yes | no | yes | pass | 2026-04-13T13:29:47Z | 200 | 1.125 | 0.002421 | [2026-04-13T13-29-47Z.txt](results/bodies/anthropic.tool_choice_any/2026-04-13T13-29-47Z.txt) | tool_choice: {type: 'any'} |
| anthropic | tool_choice_specific | yes | no | yes | pass | 2026-04-13T13:29:51Z | 200 | 1.016 | 0.002346 | [2026-04-13T13-29-51Z.txt](results/bodies/anthropic.tool_choice_specific/2026-04-13T13-29-51Z.txt) | tool_choice: {type: 'tool', name: 'fn'} |
| anthropic | tool_choice_none | yes | no | yes | pass | 2026-04-13T13:29:50Z | 200 | 1.032 | 0.00195 | [2026-04-13T13-29-50Z.txt](results/bodies/anthropic.tool_choice_none/2026-04-13T13-29-50Z.txt) | tool_choice: {type: 'none'} |
| anthropic | stop_sequences | no | yes | no | not_tested | — | — | — | — | — | Custom stop sequences |
| anthropic | top_p | no | yes | no | not_tested | — | — | — | — | — | top_p (nucleus sampling) |
| anthropic | top_k | no | yes | no | not_tested | — | — | — | — | — | top_k sampling |
| anthropic | thinking | yes | no | yes | pass | 2026-04-13T13:29:44Z | 200 | 2.881 | 0.003384 | [2026-04-13T13-29-44Z.txt](results/bodies/anthropic.thinking/2026-04-13T13-29-44Z.txt) | Extended thinking with thinking.type='enabled' |
| anthropic | thinking_budget | no | yes | no | not_tested | — | — | — | — | — | Thinking with budget_tokens |
| anthropic | cache_control | no | yes | no | not_tested | — | — | — | — | — | Prompt caching via cache_control on messages/system |
| anthropic | metadata | no | yes | no | not_tested | — | — | — | — | — | Request metadata (user_id) |
| anthropic | service_tier | no | yes | no | not_tested | — | — | — | — | — | service_tier selection |
| anthropic | output_config | no | yes | no | not_tested | — | — | — | — | — | Output configuration (JSON mode etc) |
| anthropic | container | no | yes | no | not_tested | — | — | — | — | — | Container for sandboxed execution |
| anthropic | inference_geo | no | yes | no | not_tested | — | — | — | — | — | inference_geo region preference |
| gemini | basic_text | yes | no | yes | pass | 2026-04-13T13:29:53Z | 200 | 0.702 | 1.78e-06 | [2026-04-13T13-29-53Z.txt](results/bodies/gemini.basic_text/2026-04-13T13-29-53Z.txt) | Simple text prompt → text response |
| gemini | streaming | yes | no | yes | pass | 2026-04-13T13:30:07Z | 200 | 2.148 | 6.66e-06 | [2026-04-13T13-30-07Z.txt](results/bodies/gemini.streaming/2026-04-13T13-30-07Z.txt) | streamGenerateContent endpoint |
| gemini | system_prompt | yes | no | yes | pass | 2026-04-13T13:30:09Z | 200 | 1.127 | 2.94e-06 | [2026-04-13T13-30-09Z.txt](results/bodies/gemini.system_prompt/2026-04-13T13-30-09Z.txt) | systemInstruction field |
| gemini | tools | yes | no | yes | pass | 2026-04-13T13:30:25Z | 200 | 1.126 | 1.488e-05 | [2026-04-13T13-30-25Z.txt](results/bodies/gemini.tools/2026-04-13T13-30-25Z.txt) | Function calling with tools/functionDeclarations |
| gemini | image_inline | yes | no | yes | pass | 2026-04-13T13:29:54Z | 200 | 3.635 | 2.812e-05 | [2026-04-13T13-29-54Z.txt](results/bodies/gemini.image_inline/2026-04-13T13-29-54Z.txt) | Image via inlineData (base64) |
| gemini | image_file_uri | no | yes | no | not_tested | — | — | — | — | — | Image via fileData (Google file URI) |
| gemini | audio_inline | no | yes | no | not_tested | — | — | — | — | — | Audio via inlineData |
| gemini | video_file | no | yes | no | not_tested | — | — | — | — | — | Video via fileData |
| gemini | pdf_inline | no | yes | no | not_tested | — | — | — | — | — | PDF via inlineData |
| gemini | multi_turn | no | yes | no | not_tested | — | — | — | — | — | Multi-turn conversation (multiple contents) |
| gemini | multi_turn_function_response | no | yes | no | not_tested | — | — | — | — | — | Conversation with functionCall + functionResponse |
| gemini | temperature | yes | no | yes | pass | 2026-04-13T13:30:10Z | 200 | 9.033 | 5.69e-06 | [2026-04-13T13-30-10Z.txt](results/bodies/gemini.temperature/2026-04-13T13-30-10Z.txt) | generationConfig.temperature |
| gemini | max_output_tokens | no | yes | no | not_tested | — | — | — | — | — | generationConfig.maxOutputTokens |
| gemini | top_p | no | yes | no | not_tested | — | — | — | — | — | generationConfig.topP |
| gemini | top_k | no | yes | no | not_tested | — | — | — | — | — | generationConfig.topK |
| gemini | stop_sequences | no | yes | no | not_tested | — | — | — | — | — | generationConfig.stopSequences |
| gemini | response_mime_type | yes | no | yes | pass | 2026-04-13T13:29:57Z | 200 | 1.498 | 8.859e-05 | [2026-04-13T13-29-57Z.txt](results/bodies/gemini.response_mime_type/2026-04-13T13-29-57Z.txt) | generationConfig.responseMimeType (JSON mode) |
| gemini | response_schema | yes | no | yes | pass | 2026-04-13T13:29:59Z | 200 | 2.492 | 8.947e-05 | [2026-04-13T13-29-59Z.txt](results/bodies/gemini.response_schema/2026-04-13T13-29-59Z.txt) | generationConfig.responseSchema (structured output) |
| gemini | thinking | yes | no | yes | pass | 2026-04-13T13:30:19Z | 200 | 4.317 | 6.312e-05 | [2026-04-13T13-30-19Z.txt](results/bodies/gemini.thinking/2026-04-13T13-30-19Z.txt) | generationConfig.thinkingConfig |
| gemini | tool_config_auto | yes | no | yes | pass | 2026-04-13T13:43:36Z | 200 | 1.417 | 2.103e-05 | [2026-04-13T13-43-36Z.txt](results/bodies/gemini.tool_config_auto/2026-04-13T13-43-36Z.txt) | toolConfig.functionCallingConfig.mode: AUTO |
| gemini | tool_config_any | yes | no | yes | pass | 2026-04-13T13:30:24Z | 200 | 1.188 | 2.103e-05 | [2026-04-13T13-30-24Z.txt](results/bodies/gemini.tool_config_any/2026-04-13T13-30-24Z.txt) | toolConfig.functionCallingConfig.mode: ANY |
| gemini | tool_config_none | no | yes | no | not_tested | — | — | — | — | — | toolConfig.functionCallingConfig.mode: NONE |
| gemini | safety_settings | yes | no | yes | pass | 2026-04-13T13:30:01Z | 200 | 5.598 | 8.388e-05 | [2026-04-13T13-30-01Z.txt](results/bodies/gemini.safety_settings/2026-04-13T13-30-01Z.txt) | Safety settings (harm categories + thresholds) |
| gemini | google_search | no | yes | no | not_tested | — | — | — | — | — | Google Search grounding tool |
| gemini | code_execution | no | yes | no | not_tested | — | — | — | — | — | Code execution tool |
| gemini | cached_content | no | yes | no | not_tested | — | — | — | — | — | Use cachedContent for context caching |
| gemini | store | no | yes | no | not_tested | — | — | — | — | — | Logging/storage configuration |

## Results format

- Latest run summary: `results/latest.json`
- Run history: `results/history.jsonl`
- Response bodies: `results/bodies/<case-id>/<timestamp>.txt`

_README generated at 2026-04-13T13:44:27.783444Z by `generate_readme.py`._
