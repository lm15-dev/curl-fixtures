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
| openai | 41 | 41 | 0 | 41 | 0 | 41 | 0 | 0.00000000 |
| anthropic | 28 | 28 | 0 | 28 | 28 | 0 | 0 | 0.09136625 |
| gemini | 27 | 27 | 0 | 27 | 27 | 0 | 0 | 0.00259270 |

## Fixture matrix

| Provider | Feature | Done | Todo | Tested | Last result | Last tested at | HTTP | Duration s | Cost USD | Response body | Description |
|---|---|---|---|---|---|---|---:|---:|---:|---|---|
| openai | basic_text | yes | no | yes | fail | 2026-08-24T13:56:34Z | 429 | 7.024 | 0.0 | [2026-08-24T13-56-34Z.txt](results/bodies/openai.basic_text/2026-08-24T13-56-34Z.txt) | Simple text prompt → text response |
| openai | streaming | yes | no | yes | fail | 2026-08-24T13:58:38Z | 200 | 4.858 | 0.0 | [2026-08-24T13-58-38Z.txt](results/bodies/openai.streaming/2026-08-24T13-58-38Z.txt) | stream: true |
| openai | system_prompt | yes | no | yes | fail | 2026-08-24T13:58:52Z | 429 | 4.982 | 0.0 | [2026-08-24T13-58-52Z.txt](results/bodies/openai.system_prompt/2026-08-24T13-58-52Z.txt) | instructions field (system prompt) |
| openai | temperature | yes | no | yes | fail | 2026-08-24T13:58:57Z | 429 | 5.955 | 0.0 | [2026-08-24T13-58-57Z.txt](results/bodies/openai.temperature/2026-08-24T13-58-57Z.txt) | temperature + max_output_tokens |
| openai | tools | yes | no | yes | fail | 2026-08-24T13:59:24Z | 429 | 4.957 | 0.0 | [2026-08-24T13-59-24Z.txt](results/bodies/openai.tools/2026-08-24T13-59-24Z.txt) | Function calling with tools array |
| openai | image_url | yes | no | yes | fail | 2026-08-24T13:57:12Z | 429 | 6.78 | 0.0 | [2026-08-24T13-57-12Z.txt](results/bodies/openai.image_url/2026-08-24T13-57-12Z.txt) | Image input via URL (input_image with image_url) |
| openai | image_file | yes | no | yes | fail | 2026-08-24T13:57:04Z | 429 | 7.575 | 0.0 | [2026-08-24T13-57-04Z.txt](results/bodies/openai.image_file/2026-08-24T13-57-04Z.txt) | Image input via file_id |
| openai | file_input | yes | no | yes | fail | 2026-08-24T14:02:09Z | 429 | 7.117 | 0.0 | [2026-08-24T14-02-09Z.txt](results/bodies/openai.file_input/2026-08-24T14-02-09Z.txt) | File/PDF input via file object |
| openai | multi_turn | yes | no | yes | fail | 2026-08-24T13:57:36Z | 429 | 4.914 | 0.0 | [2026-08-24T13-57-36Z.txt](results/bodies/openai.multi_turn/2026-08-24T13-57-36Z.txt) | Multiple user/assistant messages |
| openai | multi_turn_tool_result | yes | no | yes | fail | 2026-08-24T13:57:41Z | 429 | 6.159 | 0.0 | [2026-08-24T13-57-41Z.txt](results/bodies/openai.multi_turn_tool_result/2026-08-24T13-57-41Z.txt) | Conversation with tool call + tool result |
| openai | tool_choice_auto | yes | no | yes | fail | 2026-08-24T13:59:03Z | 429 | 5.296 | 0.0 | [2026-08-24T13-59-03Z.txt](results/bodies/openai.tool_choice_auto/2026-08-24T13-59-03Z.txt) | tool_choice: 'auto' |
| openai | tool_choice_required | yes | no | yes | fail | 2026-08-24T13:59:13Z | 429 | 5.166 | 0.0 | [2026-08-24T13-59-13Z.txt](results/bodies/openai.tool_choice_required/2026-08-24T13-59-13Z.txt) | tool_choice: 'required' |
| openai | tool_choice_none | yes | no | yes | fail | 2026-08-24T13:59:09Z | 429 | 4.568 | 0.0 | [2026-08-24T13-59-09Z.txt](results/bodies/openai.tool_choice_none/2026-08-24T13-59-09Z.txt) | tool_choice: 'none' |
| openai | tool_choice_specific | yes | no | yes | fail | 2026-08-24T13:59:18Z | 429 | 6.041 | 0.0 | [2026-08-24T13-59-18Z.txt](results/bodies/openai.tool_choice_specific/2026-08-24T13-59-18Z.txt) | tool_choice: {type: 'function', name: 'fn'} |
| openai | parallel_tool_calls | yes | no | yes | fail | 2026-08-24T13:57:47Z | 429 | 5.819 | 0.0 | [2026-08-24T13-57-47Z.txt](results/bodies/openai.parallel_tool_calls/2026-08-24T13-57-47Z.txt) | parallel_tool_calls: true/false |
| openai | max_tool_calls | yes | no | yes | fail | 2026-08-24T13:57:24Z | 429 | 6.361 | 0.0 | [2026-08-24T13-57-24Z.txt](results/bodies/openai.max_tool_calls/2026-08-24T13-57-24Z.txt) | max_tool_calls limit |
| openai | structured_output | yes | no | yes | fail | 2026-08-24T13:58:43Z | 429 | 5.0 | 0.0 | [2026-08-24T13-58-43Z.txt](results/bodies/openai.structured_output/2026-08-24T13-58-43Z.txt) | text.format with json_schema response format |
| openai | structured_output_json_object | yes | no | yes | fail | 2026-08-24T13:58:48Z | 429 | 4.429 | 0.0 | [2026-08-24T13-58-48Z.txt](results/bodies/openai.structured_output_json_object/2026-08-24T13-58-48Z.txt) | text.format with json_object type |
| openai | top_p | yes | no | yes | fail | 2026-08-24T13:59:35Z | 429 | 5.792 | 0.0 | [2026-08-24T13-59-35Z.txt](results/bodies/openai.top_p/2026-08-24T13-59-35Z.txt) | top_p sampling parameter |
| openai | top_logprobs | yes | no | yes | fail | 2026-08-24T13:59:29Z | 429 | 5.716 | 0.0 | [2026-08-24T13-59-29Z.txt](results/bodies/openai.top_logprobs/2026-08-24T13-59-29Z.txt) | top_logprobs for token probabilities |
| openai | reasoning | yes | no | yes | fail | 2026-08-24T13:58:14Z | 429 | 0.941 | 0.0 | [2026-08-24T13-58-14Z.txt](results/bodies/openai.reasoning/2026-08-24T13-58-14Z.txt) | reasoning.effort parameter |
| openai | reasoning_encrypted | yes | no | yes | fail | 2026-08-24T13:58:15Z | 429 | 0.547 | 0.0 | [2026-08-24T13-58-15Z.txt](results/bodies/openai.reasoning_encrypted/2026-08-24T13-58-15Z.txt) | reasoning with encrypted_content include |
| openai | web_search | yes | no | yes | fail | 2026-08-24T13:59:51Z | 429 | 0.587 | 0.0 | [2026-08-24T13-59-51Z.txt](results/bodies/openai.web_search/2026-08-24T13-59-51Z.txt) | Web search tool |
| openai | file_search | yes | no | yes | fail | 2026-08-24T13:56:58Z | 429 | 4.889 | 0.0 | [2026-08-24T13-56-58Z.txt](results/bodies/openai.file_search/2026-08-24T13-56-58Z.txt) | File search / retrieval tool |
| openai | code_interpreter | yes | no | yes | fail | 2026-08-24T13:56:41Z | 429 | 1.89 | 0.0 | [2026-08-24T13-56-41Z.txt](results/bodies/openai.code_interpreter/2026-08-24T13-56-41Z.txt) | Code interpreter tool |
| openai | computer_use | yes | no | yes | fail | 2026-08-24T13:56:43Z | 404 | 1.162 | — | [2026-08-24T13-56-43Z.txt](results/bodies/openai.computer_use/2026-08-24T13-56-43Z.txt) | Computer use tool |
| openai | previous_response_id | yes | no | yes | fail | 2026-08-24T13:57:53Z | — | — | — | — | Chain responses via previous_response_id |
| openai | conversation | yes | no | yes | fail | 2026-08-24T13:56:50Z | 429 | 6.963 | 0.0 | [2026-08-24T13-56-50Z.txt](results/bodies/openai.conversation/2026-08-24T13-56-50Z.txt) | Conversation object for multi-turn |
| openai | store | yes | no | yes | fail | 2026-08-24T13:58:28Z | 429 | 4.911 | 0.0 | [2026-08-24T13-58-28Z.txt](results/bodies/openai.store/2026-08-24T13-58-28Z.txt) | store: true/false for response storage |
| openai | background | yes | no | yes | fail | 2026-08-24T13:56:21Z | 200 | 12.942 | 0.0 | [2026-08-24T13-56-21Z.txt](results/bodies/openai.background/2026-08-24T13-56-21Z.txt) | background: true for async processing |
| openai | truncation | yes | no | yes | fail | 2026-08-24T13:59:41Z | 429 | 5.285 | 0.0 | [2026-08-24T13-59-41Z.txt](results/bodies/openai.truncation/2026-08-24T13-59-41Z.txt) | truncation: 'auto' or 'disabled' |
| openai | service_tier | yes | no | yes | fail | 2026-08-24T13:58:22Z | 429 | 5.785 | 0.0 | [2026-08-24T13-58-22Z.txt](results/bodies/openai.service_tier/2026-08-24T13-58-22Z.txt) | service_tier selection |
| openai | metadata | yes | no | yes | fail | 2026-08-24T13:57:31Z | 429 | 5.31 | 0.0 | [2026-08-24T13-57-31Z.txt](results/bodies/openai.metadata/2026-08-24T13-57-31Z.txt) | Request metadata |
| openai | prompt | yes | no | yes | fail | 2026-08-24T13:57:58Z | 429 | 5.118 | 0.0 | [2026-08-24T13-57-58Z.txt](results/bodies/openai.prompt/2026-08-24T13-57-58Z.txt) | Stored prompt reference |
| openai | include | yes | no | yes | fail | 2026-08-24T13:57:19Z | 429 | 5.813 | 0.0 | [2026-08-24T13-57-19Z.txt](results/bodies/openai.include/2026-08-24T13-57-19Z.txt) | include array for additional output data |
| openai | context_management | yes | no | yes | fail | 2026-08-24T13:56:44Z | 429 | 5.856 | 0.0 | [2026-08-24T13-56-44Z.txt](results/bodies/openai.context_management/2026-08-24T13-56-44Z.txt) | Context management / compaction configuration |
| openai | prompt_cache_key | yes | no | yes | fail | 2026-08-24T13:58:03Z | 429 | 6.14 | 0.0 | [2026-08-24T13-58-03Z.txt](results/bodies/openai.prompt_cache_key/2026-08-24T13-58-03Z.txt) | prompt_cache_key for caching |
| openai | prompt_cache_retention | yes | no | yes | fail | 2026-08-24T13:58:09Z | 429 | 4.835 | 0.0 | [2026-08-24T13-58-09Z.txt](results/bodies/openai.prompt_cache_retention/2026-08-24T13-58-09Z.txt) | prompt_cache_retention duration |
| openai | safety_identifier | yes | no | yes | fail | 2026-08-24T13:58:16Z | 429 | 6.247 | 0.0 | [2026-08-24T13-58-16Z.txt](results/bodies/openai.safety_identifier/2026-08-24T13-58-16Z.txt) | safety_identifier for content filtering |
| openai | stream_options | yes | no | yes | fail | 2026-08-24T13:58:33Z | 200 | 5.256 | 0.0 | [2026-08-24T13-58-33Z.txt](results/bodies/openai.stream_options/2026-08-24T13-58-33Z.txt) | stream_options (include_obfuscation) |
| openai | user | yes | no | yes | fail | 2026-08-24T13:59:46Z | 429 | 4.441 | 0.0 | [2026-08-24T13-59-46Z.txt](results/bodies/openai.user/2026-08-24T13-59-46Z.txt) | user identifier for abuse tracking |
| anthropic | basic_text | yes | no | yes | pass | 2026-08-24T13:52:47Z | 200 | 7.171 | 0.0002625 | [2026-08-24T13-52-47Z.txt](results/bodies/anthropic.basic_text/2026-08-24T13-52-47Z.txt) | Simple text prompt → text response |
| anthropic | streaming | yes | no | yes | pass | 2026-08-24T13:54:02Z | 200 | 1.013 | 0.00025875 | [2026-08-24T13-54-02Z.txt](results/bodies/anthropic.streaming/2026-08-24T13-54-02Z.txt) | stream: true (SSE) |
| anthropic | system_prompt | yes | no | yes | pass | 2026-08-24T13:54:05Z | 200 | 2.481 | 0.00145125 | [2026-08-24T13-54-05Z.txt](results/bodies/anthropic.system_prompt/2026-08-24T13-54-05Z.txt) | system field (string or content blocks) |
| anthropic | temperature | yes | no | yes | pass | 2026-08-24T13:54:07Z | 200 | 9.773 | 0.00024375 | [2026-08-24T13-54-07Z.txt](results/bodies/anthropic.temperature/2026-08-24T13-54-07Z.txt) | temperature parameter |
| anthropic | max_tokens | yes | no | yes | pass | 2026-08-24T13:53:48Z | 200 | 1.051 | 0.0002625 | [2026-08-24T13-53-48Z.txt](results/bodies/anthropic.max_tokens/2026-08-24T13-53-48Z.txt) | max_tokens (required field) |
| anthropic | tools | yes | no | yes | pass | 2026-08-24T13:54:31Z | 200 | 1.551 | 0.0031125 | [2026-08-24T13-54-31Z.txt](results/bodies/anthropic.tools/2026-08-24T13-54-31Z.txt) | Function calling with tools array |
| anthropic | image_base64 | yes | no | yes | pass | 2026-08-24T13:53:42Z | 200 | 1.328 | 0.00033375 | [2026-08-24T13-53-42Z.txt](results/bodies/anthropic.image_base64/2026-08-24T13-53-42Z.txt) | Image input via base64 source |
| anthropic | image_url | yes | no | yes | pass | 2026-08-24T13:53:43Z | 200 | 2.456 | 0.00064875 | [2026-08-24T13-53-43Z.txt](results/bodies/anthropic.image_url/2026-08-24T13-53-43Z.txt) | Image input via URL source |
| anthropic | pdf_base64 | yes | no | yes | pass | 2026-08-24T13:53:57Z | 200 | 1.578 | 0.0060525 | [2026-08-24T13-53-57Z.txt](results/bodies/anthropic.pdf_base64/2026-08-24T13-53-57Z.txt) | PDF input via base64 document source |
| anthropic | multi_turn | yes | no | yes | pass | 2026-08-24T13:53:51Z | 200 | 0.927 | 0.00022875 | [2026-08-24T13-53-51Z.txt](results/bodies/anthropic.multi_turn/2026-08-24T13-53-51Z.txt) | Multiple user/assistant messages |
| anthropic | multi_turn_tool_result | yes | no | yes | pass | 2026-08-24T13:53:52Z | 200 | 1.165 | 0.00249 | [2026-08-24T13-53-52Z.txt](results/bodies/anthropic.multi_turn_tool_result/2026-08-24T13-53-52Z.txt) | Conversation with tool_use + tool_result blocks |
| anthropic | system_content_blocks | yes | no | yes | pass | 2026-08-24T13:54:03Z | 200 | 2.167 | 0.0002025 | [2026-08-24T13-54-03Z.txt](results/bodies/anthropic.system_content_blocks/2026-08-24T13-54-03Z.txt) | System as array of TextBlockParam (with cache_control) |
| anthropic | tool_choice_auto | yes | no | yes | pass | 2026-08-24T13:54:27Z | 200 | 1.51 | 0.0031125 | [2026-08-24T13-54-27Z.txt](results/bodies/anthropic.tool_choice_auto/2026-08-24T13-54-27Z.txt) | tool_choice: {type: 'auto'} |
| anthropic | tool_choice_any | yes | no | yes | pass | 2026-08-24T13:54:26Z | 200 | 1.122 | 0.00302625 | [2026-08-24T13-54-26Z.txt](results/bodies/anthropic.tool_choice_any/2026-08-24T13-54-26Z.txt) | tool_choice: {type: 'any'} |
| anthropic | tool_choice_specific | yes | no | yes | pass | 2026-08-24T13:54:30Z | 200 | 1.327 | 0.0029325 | [2026-08-24T13-54-30Z.txt](results/bodies/anthropic.tool_choice_specific/2026-08-24T13-54-30Z.txt) | tool_choice: {type: 'tool', name: 'fn'} |
| anthropic | tool_choice_none | yes | no | yes | pass | 2026-08-24T13:54:29Z | 200 | 1.35 | 0.00241875 | [2026-08-24T13-54-29Z.txt](results/bodies/anthropic.tool_choice_none/2026-08-24T13-54-29Z.txt) | tool_choice: {type: 'none'} |
| anthropic | stop_sequences | yes | no | yes | pass | 2026-08-24T13:54:01Z | 200 | 0.986 | 0.00024 | [2026-08-24T13-54-01Z.txt](results/bodies/anthropic.stop_sequences/2026-08-24T13-54-01Z.txt) | Custom stop sequences |
| anthropic | top_p | yes | no | yes | pass | 2026-08-24T13:54:34Z | 200 | 1.228 | 0.00024375 | [2026-08-24T13-54-34Z.txt](results/bodies/anthropic.top_p/2026-08-24T13-54-34Z.txt) | top_p (nucleus sampling) |
| anthropic | top_k | yes | no | yes | pass | 2026-08-24T13:54:33Z | 200 | 1.724 | 0.00013875 | [2026-08-24T13-54-33Z.txt](results/bodies/anthropic.top_k/2026-08-24T13-54-33Z.txt) | top_k sampling |
| anthropic | thinking | yes | no | yes | pass | 2026-08-24T13:54:17Z | 200 | 5.119 | 0.00648 | [2026-08-24T13-54-17Z.txt](results/bodies/anthropic.thinking/2026-08-24T13-54-17Z.txt) | Extended thinking with thinking.type='enabled' |
| anthropic | thinking_budget | yes | no | yes | pass | 2026-08-24T13:54:22Z | 200 | 3.686 | 0.00428625 | [2026-08-24T13-54-22Z.txt](results/bodies/anthropic.thinking_budget/2026-08-24T13-54-22Z.txt) | Thinking with budget_tokens |
| anthropic | cache_control | yes | no | yes | pass | 2026-08-24T13:52:55Z | 200 | 1.412 | 0.0001425 | [2026-08-24T13-52-55Z.txt](results/bodies/anthropic.cache_control/2026-08-24T13-52-55Z.txt) | Prompt caching via cache_control on messages/system |
| anthropic | metadata | yes | no | yes | pass | 2026-08-24T13:53:49Z | 200 | 2.298 | 0.00012 | [2026-08-24T13-53-49Z.txt](results/bodies/anthropic.metadata/2026-08-24T13-53-49Z.txt) | Request metadata (user_id) |
| anthropic | service_tier | yes | no | yes | pass | 2026-08-24T13:53:59Z | 200 | 1.712 | 0.0001425 | [2026-08-24T13-53-59Z.txt](results/bodies/anthropic.service_tier/2026-08-24T13-53-59Z.txt) | service_tier selection |
| anthropic | output_config | yes | no | yes | pass | 2026-08-24T13:53:53Z | 200 | 4.033 | 0.00075 | [2026-08-24T13-53-53Z.txt](results/bodies/anthropic.output_config/2026-08-24T13-53-53Z.txt) | Output configuration (JSON mode etc) |
| anthropic | web_search | yes | no | yes | pass | 2026-08-24T13:54:36Z | 200 | 7.761 | 0.04209375 | [2026-08-24T13-54-36Z.txt](results/bodies/anthropic.web_search/2026-08-24T13-54-36Z.txt) | Web search via server-side tool |
| anthropic | container | yes | no | yes | pass | 2026-08-24T14:00:34Z | 200 | 15.381 | 0.00904125 | [2026-08-24T14-00-34Z.txt](results/bodies/anthropic.container/2026-08-24T14-00-34Z.txt) | Container for sandboxed execution |
| anthropic | inference_geo | yes | no | yes | pass | 2026-08-24T13:53:46Z | 200 | 2.317 | 0.00065 | [2026-08-24T13-53-46Z.txt](results/bodies/anthropic.inference_geo/2026-08-24T13-53-46Z.txt) | inference_geo region preference |
| gemini | basic_text | yes | no | yes | pass | 2026-08-24T13:54:48Z | 200 | 0.716 | 6.2e-06 | [2026-08-24T13-54-48Z.txt](results/bodies/gemini.basic_text/2026-08-24T13-54-48Z.txt) | Simple text prompt → text response |
| gemini | streaming | yes | no | yes | pass | 2026-08-24T13:55:30Z | 200 | 0.614 | 2.34e-05 | [2026-08-24T13-55-30Z.txt](results/bodies/gemini.streaming/2026-08-24T13-55-30Z.txt) | streamGenerateContent endpoint |
| gemini | system_prompt | yes | no | yes | pass | 2026-08-24T13:55:31Z | 200 | 0.92 | 2.77e-05 | [2026-08-24T13-55-31Z.txt](results/bodies/gemini.system_prompt/2026-08-24T13-55-31Z.txt) | systemInstruction field |
| gemini | tools | yes | no | yes | pass | 2026-08-24T13:55:46Z | 200 | 1.025 | 5.16e-05 | [2026-08-24T13-55-46Z.txt](results/bodies/gemini.tools/2026-08-24T13-55-46Z.txt) | Function calling with tools/functionDeclarations |
| gemini | image_inline | yes | no | yes | pass | 2026-08-24T13:55:11Z | 200 | 3.286 | 9.44e-05 | [2026-08-24T13-55-11Z.txt](results/bodies/gemini.image_inline/2026-08-24T13-55-11Z.txt) | Image via inlineData (base64) |
| gemini | image_file_uri | yes | no | yes | pass | 2026-08-24T13:54:55Z | 200 | 15.421 | 0.0001041 | [2026-08-24T13-54-55Z.txt](results/bodies/gemini.image_file_uri/2026-08-24T13-54-55Z.txt) | Image via fileData (Google file URI) |
| gemini | audio_inline | yes | no | yes | pass | 2026-08-24T13:54:43Z | 200 | 4.932 | 2.55e-05 | [2026-08-24T13-54-43Z.txt](results/bodies/gemini.audio_inline/2026-08-24T13-54-43Z.txt) | Audio via inlineData |
| gemini | video_file | yes | no | yes | pass | 2026-08-24T13:56:04Z | 200 | 16.64 | 5.17e-05 | [2026-08-24T13-56-04Z.txt](results/bodies/gemini.video_file/2026-08-24T13-56-04Z.txt) | Video via fileData |
| gemini | pdf_inline | yes | no | yes | pass | 2026-08-24T13:55:16Z | 200 | 1.703 | 8.75e-05 | [2026-08-24T13-55-16Z.txt](results/bodies/gemini.pdf_inline/2026-08-24T13-55-16Z.txt) | PDF via inlineData |
| gemini | multi_turn | yes | no | yes | pass | 2026-08-24T13:55:15Z | 200 | 0.908 | 1.12e-05 | [2026-08-24T13-55-15Z.txt](results/bodies/gemini.multi_turn/2026-08-24T13-55-15Z.txt) | Multi-turn conversation (multiple contents) |
| gemini | multi_turn_function_response | yes | no | yes | pass | 2026-08-24T13:55:16Z | 200 | 0.437 | 2.77e-05 | [2026-08-24T13-55-16Z.txt](results/bodies/gemini.multi_turn_function_response/2026-08-24T13-55-16Z.txt) | Conversation with functionCall + functionResponse |
| gemini | temperature | yes | no | yes | pass | 2026-08-24T13:55:32Z | 200 | 5.629 | 1.99e-05 | [2026-08-24T13-55-32Z.txt](results/bodies/gemini.temperature/2026-08-24T13-55-32Z.txt) | generationConfig.temperature |
| gemini | max_output_tokens | yes | no | yes | pass | 2026-08-24T13:55:14Z | 200 | 0.621 | 4.2e-06 | [2026-08-24T13-55-14Z.txt](results/bodies/gemini.max_output_tokens/2026-08-24T13-55-14Z.txt) | generationConfig.maxOutputTokens |
| gemini | top_p | yes | no | yes | pass | 2026-08-24T13:55:57Z | 200 | 7.56 | 2.49e-05 | [2026-08-24T13-55-57Z.txt](results/bodies/gemini.top_p/2026-08-24T13-55-57Z.txt) | generationConfig.topP |
| gemini | top_k | yes | no | yes | pass | 2026-08-24T13:55:47Z | 200 | 10.095 | 2.74e-05 | [2026-08-24T13-55-47Z.txt](results/bodies/gemini.top_k/2026-08-24T13-55-47Z.txt) | generationConfig.topK |
| gemini | stop_sequences | yes | no | yes | pass | 2026-08-24T13:55:29Z | 200 | 0.724 | 4.6e-06 | [2026-08-24T13-55-29Z.txt](results/bodies/gemini.stop_sequences/2026-08-24T13-55-29Z.txt) | generationConfig.stopSequences |
| gemini | response_mime_type | yes | no | yes | pass | 2026-08-24T13:55:18Z | 200 | 1.64 | 0.0002992 | [2026-08-24T13-55-18Z.txt](results/bodies/gemini.response_mime_type/2026-08-24T13-55-18Z.txt) | generationConfig.responseMimeType (JSON mode) |
| gemini | response_schema | yes | no | yes | pass | 2026-08-24T13:55:19Z | 200 | 2.659 | 0.0003374 | [2026-08-24T13-55-19Z.txt](results/bodies/gemini.response_schema/2026-08-24T13-55-19Z.txt) | generationConfig.responseSchema (structured output) |
| gemini | thinking | yes | no | yes | pass | 2026-08-24T13:55:37Z | 200 | 3.174 | 0.0001895 | [2026-08-24T13-55-37Z.txt](results/bodies/gemini.thinking/2026-08-24T13-55-37Z.txt) | generationConfig.thinkingConfig |
| gemini | tool_config_auto | yes | no | yes | pass | 2026-08-24T13:55:42Z | 200 | 1.124 | 7.29e-05 | [2026-08-24T13-55-42Z.txt](results/bodies/gemini.tool_config_auto/2026-08-24T13-55-42Z.txt) | toolConfig.functionCallingConfig.mode: AUTO |
| gemini | tool_config_any | yes | no | yes | pass | 2026-08-24T13:55:41Z | 200 | 1.022 | 7.29e-05 | [2026-08-24T13-55-41Z.txt](results/bodies/gemini.tool_config_any/2026-08-24T13-55-41Z.txt) | toolConfig.functionCallingConfig.mode: ANY |
| gemini | tool_config_none | yes | no | yes | pass | 2026-08-24T13:55:43Z | 200 | 2.865 | 0.0001954 | [2026-08-24T13-55-43Z.txt](results/bodies/gemini.tool_config_none/2026-08-24T13-55-43Z.txt) | toolConfig.functionCallingConfig.mode: NONE |
| gemini | safety_settings | yes | no | yes | pass | 2026-08-24T13:55:22Z | 200 | 6.644 | 0.0003077 | [2026-08-24T13-55-22Z.txt](results/bodies/gemini.safety_settings/2026-08-24T13-55-22Z.txt) | Safety settings (harm categories + thresholds) |
| gemini | google_search | yes | no | yes | pass | 2026-08-24T13:54:52Z | 200 | 3.514 | 0.0002045 | [2026-08-24T13-54-52Z.txt](results/bodies/gemini.google_search/2026-08-24T13-54-52Z.txt) | Google Search grounding tool |
| gemini | code_execution | yes | no | yes | pass | 2026-08-24T13:54:50Z | 200 | 2.047 | 0.0003169 | [2026-08-24T13-54-50Z.txt](results/bodies/gemini.code_execution/2026-08-24T13-54-50Z.txt) | Code execution tool |
| gemini | cached_content | yes | no | yes | pass | 2026-08-24T13:54:49Z | 200 | 0.613 | — | [2026-08-24T13-54-49Z.txt](results/bodies/gemini.cached_content/2026-08-24T13-54-49Z.txt) | Use cachedContent for context caching |
| gemini | store | yes | no | yes | pass | 2026-08-24T13:55:29Z | 200 | 0.817 | 4.3e-06 | [2026-08-24T13-55-29Z.txt](results/bodies/gemini.store/2026-08-24T13-55-29Z.txt) | Logging/storage configuration |

## Results format

- Latest run summary: `results/latest.json`
- Run history: `results/history.jsonl`
- Response bodies: `results/bodies/<case-id>/<timestamp>.txt`

_README generated at 2026-08-24T14:04:02.142119Z by `generate_readme.py`._
