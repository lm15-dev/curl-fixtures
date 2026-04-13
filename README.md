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
| openai | 41 | 41 | 0 | 41 | 41 | 0 | 0 | 0.01510042 |
| anthropic | 27 | 27 | 0 | 27 | 27 | 0 | 0 | 0.04196600 |
| gemini | 27 | 27 | 0 | 27 | 27 | 0 | 0 | 0.00079042 |

## Fixture matrix

| Provider | Feature | Done | Todo | Tested | Last result | Last tested at | HTTP | Duration s | Cost USD | Response body | Description |
|---|---|---|---|---|---|---|---:|---:|---:|---|---|
| openai | basic_text | yes | no | yes | pass | 2026-04-13T14:51:18Z | 200 | 0.786 | 2e-05 | [2026-04-13T14-51-18Z.txt](results/bodies/openai.basic_text/2026-04-13T14-51-18Z.txt) | Simple text prompt → text response |
| openai | streaming | yes | no | yes | pass | 2026-04-13T14:52:06Z | 200 | 6.933 | 1.96e-05 | [2026-04-13T14-52-06Z.txt](results/bodies/openai.streaming/2026-04-13T14-52-06Z.txt) | stream: true |
| openai | system_prompt | yes | no | yes | pass | 2026-04-13T14:52:18Z | 200 | 2.509 | 0.0001408 | [2026-04-13T14-52-18Z.txt](results/bodies/openai.system_prompt/2026-04-13T14-52-18Z.txt) | instructions field (system prompt) |
| openai | temperature | yes | no | yes | pass | 2026-04-13T14:52:21Z | 200 | 2.15 | 3.68e-05 | [2026-04-13T14-52-21Z.txt](results/bodies/openai.temperature/2026-04-13T14-52-21Z.txt) | temperature + max_output_tokens |
| openai | tools | yes | no | yes | pass | 2026-04-13T14:52:27Z | 200 | 0.716 | 4.4e-05 | [2026-04-13T14-52-27Z.txt](results/bodies/openai.tools/2026-04-13T14-52-27Z.txt) | Function calling with tools array |
| openai | image_url | yes | no | yes | pass | 2026-04-13T14:51:47Z | 200 | 1.432 | 0.0001008 | [2026-04-13T14-51-47Z.txt](results/bodies/openai.image_url/2026-04-13T14-51-47Z.txt) | Image input via URL (input_image with image_url) |
| openai | image_file | yes | no | yes | pass | 2026-04-13T14:51:45Z | 200 | 1.536 | 9.44e-05 | [2026-04-13T14-51-45Z.txt](results/bodies/openai.image_file/2026-04-13T14-51-45Z.txt) | Image input via file_id |
| openai | file_input | yes | no | yes | pass | 2026-04-13T14:51:38Z | 200 | 3.892 | 2.16e-05 | [2026-04-13T14-51-38Z.txt](results/bodies/openai.file_input/2026-04-13T14-51-38Z.txt) | File/PDF input via file object |
| openai | multi_turn | yes | no | yes | pass | 2026-04-13T14:51:51Z | 200 | 2.283 | 1.92e-05 | [2026-04-13T14-51-51Z.txt](results/bodies/openai.multi_turn/2026-04-13T14-51-51Z.txt) | Multiple user/assistant messages |
| openai | multi_turn_tool_result | yes | no | yes | pass | 2026-04-13T14:51:54Z | 200 | 0.949 | 7.84e-05 | [2026-04-13T14-51-54Z.txt](results/bodies/openai.multi_turn_tool_result/2026-04-13T14-51-54Z.txt) | Conversation with tool call + tool result |
| openai | tool_choice_auto | yes | no | yes | pass | 2026-04-13T14:52:23Z | 200 | 1.229 | 4.4e-05 | [2026-04-13T14-52-23Z.txt](results/bodies/openai.tool_choice_auto/2026-04-13T14-52-23Z.txt) | tool_choice: 'auto' |
| openai | tool_choice_required | yes | no | yes | pass | 2026-04-13T14:52:25Z | 200 | 0.818 | 3.48e-05 | [2026-04-13T14-52-25Z.txt](results/bodies/openai.tool_choice_required/2026-04-13T14-52-25Z.txt) | tool_choice: 'required' |
| openai | tool_choice_none | yes | no | yes | pass | 2026-04-13T14:52:24Z | 200 | 0.819 | 3.48e-05 | [2026-04-13T14-52-24Z.txt](results/bodies/openai.tool_choice_none/2026-04-13T14-52-24Z.txt) | tool_choice: 'none' |
| openai | tool_choice_specific | yes | no | yes | pass | 2026-04-13T14:52:26Z | 200 | 1.228 | 3.28e-05 | [2026-04-13T14-52-26Z.txt](results/bodies/openai.tool_choice_specific/2026-04-13T14-52-26Z.txt) | tool_choice: {type: 'function', name: 'fn'} |
| openai | parallel_tool_calls | yes | no | yes | pass | 2026-04-13T14:51:55Z | 200 | 1.351 | 0.000106 | [2026-04-13T14-51-55Z.txt](results/bodies/openai.parallel_tool_calls/2026-04-13T14-51-55Z.txt) | parallel_tool_calls: true/false |
| openai | max_tool_calls | yes | no | yes | pass | 2026-04-13T14:51:49Z | 200 | 1.941 | 0.0033384 | [2026-04-13T14-51-49Z.txt](results/bodies/openai.max_tool_calls/2026-04-13T14-51-49Z.txt) | max_tool_calls limit |
| openai | structured_output | yes | no | yes | pass | 2026-04-13T14:52:13Z | 200 | 3.04 | 0.0001428 | [2026-04-13T14-52-13Z.txt](results/bodies/openai.structured_output/2026-04-13T14-52-13Z.txt) | text.format with json_schema response format |
| openai | structured_output_json_object | yes | no | yes | pass | 2026-04-13T14:52:16Z | 200 | 2.754 | 0.000168 | [2026-04-13T14-52-16Z.txt](results/bodies/openai.structured_output_json_object/2026-04-13T14-52-16Z.txt) | text.format with json_object type |
| openai | top_p | yes | no | yes | pass | 2026-04-13T14:52:29Z | 200 | 0.723 | 2.16e-05 | [2026-04-13T14-52-29Z.txt](results/bodies/openai.top_p/2026-04-13T14-52-29Z.txt) | top_p sampling parameter |
| openai | top_logprobs | yes | no | yes | pass | 2026-04-13T14:52:28Z | 200 | 1.221 | 9.2e-06 | [2026-04-13T14-52-28Z.txt](results/bodies/openai.top_logprobs/2026-04-13T14-52-28Z.txt) | top_logprobs for token probabilities |
| openai | reasoning | yes | no | yes | pass | 2026-04-13T14:52:00Z | 200 | 1.697 | 1.443e-05 | [2026-04-13T14-52-00Z.txt](results/bodies/openai.reasoning/2026-04-13T14-52-00Z.txt) | reasoning.effort parameter |
| openai | reasoning_encrypted | yes | no | yes | pass | 2026-04-13T14:52:01Z | 200 | 1.536 | 1.559e-05 | [2026-04-13T14-52-01Z.txt](results/bodies/openai.reasoning_encrypted/2026-04-13T14-52-01Z.txt) | reasoning with encrypted_content include |
| openai | web_search | yes | no | yes | pass | 2026-04-13T14:52:31Z | 200 | 11.468 | 0.008648 | [2026-04-13T14-52-31Z.txt](results/bodies/openai.web_search/2026-04-13T14-52-31Z.txt) | Web search tool |
| openai | file_search | yes | no | yes | pass | 2026-04-13T14:51:42Z | 200 | 1.809 | 0.000404 | [2026-04-13T14-51-42Z.txt](results/bodies/openai.file_search/2026-04-13T14-51-42Z.txt) | File search / retrieval tool |
| openai | code_interpreter | yes | no | yes | pass | 2026-04-13T14:51:18Z | 200 | 10.034 | 0.001348 | [2026-04-13T14-51-18Z.txt](results/bodies/openai.code_interpreter/2026-04-13T14-51-18Z.txt) | Code interpreter tool |
| openai | computer_use | yes | no | yes | pass | 2026-04-13T14:51:28Z | 200 | 4.505 | — | [2026-04-13T14-51-28Z.txt](results/bodies/openai.computer_use/2026-04-13T14-51-28Z.txt) | Computer use tool |
| openai | previous_response_id | yes | no | yes | pass | 2026-04-13T14:51:56Z | 200 | 0.649 | 2.16e-05 | [2026-04-13T14-51-56Z.txt](results/bodies/openai.previous_response_id/2026-04-13T14-51-56Z.txt) | Chain responses via previous_response_id |
| openai | conversation | yes | no | yes | pass | 2026-04-13T14:51:35Z | 200 | 2.878 | 2.8e-05 | [2026-04-13T14-51-35Z.txt](results/bodies/openai.conversation/2026-04-13T14-51-35Z.txt) | Conversation object for multi-turn |
| openai | store | yes | no | yes | pass | 2026-04-13T14:52:04Z | 200 | 0.606 | 8e-06 | [2026-04-13T14-52-04Z.txt](results/bodies/openai.store/2026-04-13T14-52-04Z.txt) | store: true/false for response storage |
| openai | background | yes | no | yes | pass | 2026-04-13T14:51:08Z | 200 | 9.72 | 8e-06 | [2026-04-13T14-51-08Z.txt](results/bodies/openai.background/2026-04-13T14-51-08Z.txt) | background: true for async processing |
| openai | truncation | yes | no | yes | pass | 2026-04-13T14:52:30Z | 200 | 0.819 | 9.6e-06 | [2026-04-13T14-52-30Z.txt](results/bodies/openai.truncation/2026-04-13T14-52-30Z.txt) | truncation: 'auto' or 'disabled' |
| openai | service_tier | yes | no | yes | pass | 2026-04-13T14:52:04Z | 200 | 0.724 | 1e-05 | [2026-04-13T14-52-04Z.txt](results/bodies/openai.service_tier/2026-04-13T14-52-04Z.txt) | service_tier selection |
| openai | metadata | yes | no | yes | pass | 2026-04-13T14:51:51Z | 200 | 0.716 | 8e-06 | [2026-04-13T14-51-51Z.txt](results/bodies/openai.metadata/2026-04-13T14-51-51Z.txt) | Request metadata |
| openai | prompt | yes | no | yes | pass | 2026-04-13T14:51:58Z | 200 | 0.709 | 8e-06 | [2026-04-13T14-51-58Z.txt](results/bodies/openai.prompt/2026-04-13T14-51-58Z.txt) | Stored prompt reference |
| openai | include | yes | no | yes | pass | 2026-04-13T14:51:48Z | 200 | 0.824 | 9.2e-06 | [2026-04-13T14-51-48Z.txt](results/bodies/openai.include/2026-04-13T14-51-48Z.txt) | include array for additional output data |
| openai | context_management | yes | no | yes | pass | 2026-04-13T14:51:33Z | 200 | 1.736 | 1e-05 | [2026-04-13T14-51-33Z.txt](results/bodies/openai.context_management/2026-04-13T14-51-33Z.txt) | Context management / compaction configuration |
| openai | prompt_cache_key | yes | no | yes | pass | 2026-04-13T14:51:58Z | 200 | 0.689 | 8e-06 | [2026-04-13T14-51-58Z.txt](results/bodies/openai.prompt_cache_key/2026-04-13T14-51-58Z.txt) | prompt_cache_key for caching |
| openai | prompt_cache_retention | yes | no | yes | pass | 2026-04-13T14:51:59Z | 200 | 0.657 | 8e-06 | [2026-04-13T14-51-59Z.txt](results/bodies/openai.prompt_cache_retention/2026-04-13T14-51-59Z.txt) | prompt_cache_retention duration |
| openai | safety_identifier | yes | no | yes | pass | 2026-04-13T14:52:03Z | 200 | 0.715 | 1e-05 | [2026-04-13T14-52-03Z.txt](results/bodies/openai.safety_identifier/2026-04-13T14-52-03Z.txt) | safety_identifier for content filtering |
| openai | stream_options | yes | no | yes | pass | 2026-04-13T14:52:05Z | 200 | 0.733 | 8e-06 | [2026-04-13T14-52-05Z.txt](results/bodies/openai.stream_options/2026-04-13T14-52-05Z.txt) | stream_options (include_obfuscation) |
| openai | user | yes | no | yes | pass | 2026-04-13T14:52:31Z | 200 | 0.819 | 8e-06 | [2026-04-13T14-52-31Z.txt](results/bodies/openai.user/2026-04-13T14-52-31Z.txt) | user identifier for abuse tracking |
| anthropic | basic_text | yes | no | yes | pass | 2026-04-13T14:48:36Z | 200 | 0.917 | 0.00021 | [2026-04-13T14-48-36Z.txt](results/bodies/anthropic.basic_text/2026-04-13T14-48-36Z.txt) | Simple text prompt → text response |
| anthropic | streaming | yes | no | yes | pass | 2026-04-13T14:49:00Z | 200 | 0.818 | 0.000207 | [2026-04-13T14-49-00Z.txt](results/bodies/anthropic.streaming/2026-04-13T14-49-00Z.txt) | stream: true (SSE) |
| anthropic | system_prompt | yes | no | yes | pass | 2026-04-13T14:49:02Z | 200 | 3.964 | 0.002376 | [2026-04-13T14-49-02Z.txt](results/bodies/anthropic.system_prompt/2026-04-13T14-49-02Z.txt) | system field (string or content blocks) |
| anthropic | temperature | yes | no | yes | pass | 2026-04-13T14:49:06Z | 200 | 1.462 | 0.000195 | [2026-04-13T14-49-06Z.txt](results/bodies/anthropic.temperature/2026-04-13T14-49-06Z.txt) | temperature parameter |
| anthropic | max_tokens | yes | no | yes | pass | 2026-04-13T14:48:48Z | 200 | 0.921 | 0.00021 | [2026-04-13T14-48-48Z.txt](results/bodies/anthropic.max_tokens/2026-04-13T14-48-48Z.txt) | max_tokens (required field) |
| anthropic | tools | yes | no | yes | pass | 2026-04-13T14:49:20Z | 200 | 2.075 | 0.00249 | [2026-04-13T14-49-20Z.txt](results/bodies/anthropic.tools/2026-04-13T14-49-20Z.txt) | Function calling with tools array |
| anthropic | image_base64 | yes | no | yes | pass | 2026-04-13T14:48:43Z | 200 | 1.331 | 0.000282 | [2026-04-13T14-48-43Z.txt](results/bodies/anthropic.image_base64/2026-04-13T14-48-43Z.txt) | Image input via base64 source |
| anthropic | image_url | yes | no | yes | pass | 2026-04-13T14:48:44Z | 200 | 2.046 | 0.000519 | [2026-04-13T14-48-44Z.txt](results/bodies/anthropic.image_url/2026-04-13T14-48-44Z.txt) | Image input via URL source |
| anthropic | pdf_base64 | yes | no | yes | pass | 2026-04-13T14:48:55Z | 200 | 1.245 | 0.004842 | [2026-04-13T14-48-55Z.txt](results/bodies/anthropic.pdf_base64/2026-04-13T14-48-55Z.txt) | PDF input via base64 document source |
| anthropic | multi_turn | yes | no | yes | pass | 2026-04-13T14:48:51Z | 200 | 1.229 | 0.000183 | [2026-04-13T14-48-51Z.txt](results/bodies/anthropic.multi_turn/2026-04-13T14-48-51Z.txt) | Multiple user/assistant messages |
| anthropic | multi_turn_tool_result | yes | no | yes | pass | 2026-04-13T14:48:52Z | 200 | 1.173 | 0.001992 | [2026-04-13T14-48-52Z.txt](results/bodies/anthropic.multi_turn_tool_result/2026-04-13T14-48-52Z.txt) | Conversation with tool_use + tool_result blocks |
| anthropic | system_content_blocks | yes | no | yes | pass | 2026-04-13T14:49:01Z | 200 | 0.922 | 0.000162 | [2026-04-13T14-49-01Z.txt](results/bodies/anthropic.system_content_blocks/2026-04-13T14-49-01Z.txt) | System as array of TextBlockParam (with cache_control) |
| anthropic | tool_choice_auto | yes | no | yes | pass | 2026-04-13T14:49:16Z | 200 | 1.536 | 0.00249 | [2026-04-13T14-49-16Z.txt](results/bodies/anthropic.tool_choice_auto/2026-04-13T14-49-16Z.txt) | tool_choice: {type: 'auto'} |
| anthropic | tool_choice_any | yes | no | yes | pass | 2026-04-13T14:49:15Z | 200 | 1.073 | 0.002421 | [2026-04-13T14-49-15Z.txt](results/bodies/anthropic.tool_choice_any/2026-04-13T14-49-15Z.txt) | tool_choice: {type: 'any'} |
| anthropic | tool_choice_specific | yes | no | yes | pass | 2026-04-13T14:49:19Z | 200 | 0.996 | 0.002346 | [2026-04-13T14-49-19Z.txt](results/bodies/anthropic.tool_choice_specific/2026-04-13T14-49-19Z.txt) | tool_choice: {type: 'tool', name: 'fn'} |
| anthropic | tool_choice_none | yes | no | yes | pass | 2026-04-13T14:49:18Z | 200 | 1.329 | 0.001935 | [2026-04-13T14-49-18Z.txt](results/bodies/anthropic.tool_choice_none/2026-04-13T14-49-18Z.txt) | tool_choice: {type: 'none'} |
| anthropic | stop_sequences | yes | no | yes | pass | 2026-04-13T14:48:58Z | 200 | 2.353 | 0.000192 | [2026-04-13T14-48-58Z.txt](results/bodies/anthropic.stop_sequences/2026-04-13T14-48-58Z.txt) | Custom stop sequences |
| anthropic | top_p | yes | no | yes | pass | 2026-04-13T14:49:23Z | 200 | 1.561 | 0.000195 | [2026-04-13T14-49-23Z.txt](results/bodies/anthropic.top_p/2026-04-13T14-49-23Z.txt) | top_p (nucleus sampling) |
| anthropic | top_k | yes | no | yes | pass | 2026-04-13T14:49:22Z | 200 | 0.995 | 0.000111 | [2026-04-13T14-49-22Z.txt](results/bodies/anthropic.top_k/2026-04-13T14-49-22Z.txt) | top_k sampling |
| anthropic | thinking | yes | no | yes | pass | 2026-04-13T14:49:07Z | 200 | 4.198 | 0.005169 | [2026-04-13T14-49-07Z.txt](results/bodies/anthropic.thinking/2026-04-13T14-49-07Z.txt) | Extended thinking with thinking.type='enabled' |
| anthropic | thinking_budget | yes | no | yes | pass | 2026-04-13T14:49:12Z | 200 | 3.535 | 0.004374 | [2026-04-13T14-49-12Z.txt](results/bodies/anthropic.thinking_budget/2026-04-13T14-49-12Z.txt) | Thinking with budget_tokens |
| anthropic | cache_control | yes | no | yes | pass | 2026-04-13T14:48:37Z | 200 | 0.958 | 0.000114 | [2026-04-13T14-48-37Z.txt](results/bodies/anthropic.cache_control/2026-04-13T14-48-37Z.txt) | Prompt caching via cache_control on messages/system |
| anthropic | metadata | yes | no | yes | pass | 2026-04-13T14:48:49Z | 200 | 1.432 | 9.6e-05 | [2026-04-13T14-48-49Z.txt](results/bodies/anthropic.metadata/2026-04-13T14-48-49Z.txt) | Request metadata (user_id) |
| anthropic | service_tier | yes | no | yes | pass | 2026-04-13T14:48:57Z | 200 | 1.229 | 0.000114 | [2026-04-13T14-48-57Z.txt](results/bodies/anthropic.service_tier/2026-04-13T14-48-57Z.txt) | service_tier selection |
| anthropic | output_config | yes | no | yes | pass | 2026-04-13T14:48:53Z | 200 | 2.393 | 0.0006 | [2026-04-13T14-48-53Z.txt](results/bodies/anthropic.output_config/2026-04-13T14-48-53Z.txt) | Output configuration (JSON mode etc) |
| anthropic | container | yes | no | yes | pass | 2026-04-13T14:48:38Z | 200 | 4.471 | 0.007491 | [2026-04-13T14-48-38Z.txt](results/bodies/anthropic.container/2026-04-13T14-48-38Z.txt) | Container for sandboxed execution |
| anthropic | inference_geo | yes | no | yes | pass | 2026-04-13T14:48:46Z | 200 | 2.048 | 0.00065 | [2026-04-13T14-48-46Z.txt](results/bodies/anthropic.inference_geo/2026-04-13T14-48-46Z.txt) | inference_geo region preference |
| gemini | basic_text | yes | no | yes | pass | 2026-04-13T14:49:32Z | 200 | 0.931 | 1.78e-06 | [2026-04-13T14-49-32Z.txt](results/bodies/gemini.basic_text/2026-04-13T14-49-32Z.txt) | Simple text prompt → text response |
| gemini | streaming | yes | no | yes | pass | 2026-04-13T14:50:18Z | 200 | 1.02 | 6.66e-06 | [2026-04-13T14-50-18Z.txt](results/bodies/gemini.streaming/2026-04-13T14-50-18Z.txt) | streamGenerateContent endpoint |
| gemini | system_prompt | yes | no | yes | pass | 2026-04-13T14:50:19Z | 200 | 1.364 | 1.146e-05 | [2026-04-13T14-50-19Z.txt](results/bodies/gemini.system_prompt/2026-04-13T14-50-19Z.txt) | systemInstruction field |
| gemini | tools | yes | no | yes | pass | 2026-04-13T14:50:40Z | 200 | 1.227 | 1.488e-05 | [2026-04-13T14-50-40Z.txt](results/bodies/gemini.tools/2026-04-13T14-50-40Z.txt) | Function calling with tools/functionDeclarations |
| gemini | image_inline | yes | no | yes | pass | 2026-04-13T14:49:53Z | 200 | 4.511 | 2.741e-05 | [2026-04-13T14-49-53Z.txt](results/bodies/gemini.image_inline/2026-04-13T14-49-53Z.txt) | Image via inlineData (base64) |
| gemini | image_file_uri | yes | no | yes | pass | 2026-04-13T14:49:40Z | 200 | 13.106 | 3.087e-05 | [2026-04-13T14-49-40Z.txt](results/bodies/gemini.image_file_uri/2026-04-13T14-49-40Z.txt) | Image via fileData (Google file URI) |
| gemini | audio_inline | yes | no | yes | pass | 2026-04-13T14:49:25Z | 200 | 6.966 | 1.013e-05 | [2026-04-13T14-49-25Z.txt](results/bodies/gemini.audio_inline/2026-04-13T14-49-25Z.txt) | Audio via inlineData |
| gemini | video_file | yes | no | yes | pass | 2026-04-13T14:50:53Z | 200 | 14.478 | 9.07e-06 | [2026-04-13T14-50-53Z.txt](results/bodies/gemini.video_file/2026-04-13T14-50-53Z.txt) | Video via fileData |
| gemini | pdf_inline | yes | no | yes | pass | 2026-04-13T14:50:01Z | 200 | 1.638 | 2.617e-05 | [2026-04-13T14-50-01Z.txt](results/bodies/gemini.pdf_inline/2026-04-13T14-50-01Z.txt) | PDF via inlineData |
| gemini | multi_turn | yes | no | yes | pass | 2026-04-13T14:49:59Z | 200 | 1.154 | 3.32e-06 | [2026-04-13T14-49-59Z.txt](results/bodies/gemini.multi_turn/2026-04-13T14-49-59Z.txt) | Multi-turn conversation (multiple contents) |
| gemini | multi_turn_function_response | yes | no | yes | pass | 2026-04-13T14:50:00Z | 200 | 0.893 | 8.27e-06 | [2026-04-13T14-50-00Z.txt](results/bodies/gemini.multi_turn_function_response/2026-04-13T14-50-00Z.txt) | Conversation with functionCall + functionResponse |
| gemini | temperature | yes | no | yes | pass | 2026-04-13T14:50:20Z | 200 | 10.002 | 4.98e-06 | [2026-04-13T14-50-20Z.txt](results/bodies/gemini.temperature/2026-04-13T14-50-20Z.txt) | generationConfig.temperature |
| gemini | max_output_tokens | yes | no | yes | pass | 2026-04-13T14:49:58Z | 200 | 0.915 | 1.26e-06 | [2026-04-13T14-49-58Z.txt](results/bodies/gemini.max_output_tokens/2026-04-13T14-49-58Z.txt) | generationConfig.maxOutputTokens |
| gemini | top_p | yes | no | yes | pass | 2026-04-13T14:50:47Z | 200 | 6.143 | 4.98e-06 | [2026-04-13T14-50-47Z.txt](results/bodies/gemini.top_p/2026-04-13T14-50-47Z.txt) | generationConfig.topP |
| gemini | top_k | yes | no | yes | pass | 2026-04-13T14:50:42Z | 200 | 5.632 | 7.11e-06 | [2026-04-13T14-50-42Z.txt](results/bodies/gemini.top_k/2026-04-13T14-50-42Z.txt) | generationConfig.topK |
| gemini | stop_sequences | yes | no | yes | pass | 2026-04-13T14:50:15Z | 200 | 1.637 | 1.34e-06 | [2026-04-13T14-50-15Z.txt](results/bodies/gemini.stop_sequences/2026-04-13T14-50-15Z.txt) | generationConfig.stopSequences |
| gemini | response_mime_type | yes | no | yes | pass | 2026-04-13T14:50:03Z | 200 | 1.714 | 0.00010208 | [2026-04-13T14-50-03Z.txt](results/bodies/gemini.response_mime_type/2026-04-13T14-50-03Z.txt) | generationConfig.responseMimeType (JSON mode) |
| gemini | response_schema | yes | no | yes | pass | 2026-04-13T14:50:04Z | 200 | 3.098 | 0.00011787 | [2026-04-13T14-50-04Z.txt](results/bodies/gemini.response_schema/2026-04-13T14-50-04Z.txt) | generationConfig.responseSchema (structured output) |
| gemini | thinking | yes | no | yes | pass | 2026-04-13T14:50:30Z | 200 | 4.915 | 7.59e-05 | [2026-04-13T14-50-30Z.txt](results/bodies/gemini.thinking/2026-04-13T14-50-30Z.txt) | generationConfig.thinkingConfig |
| gemini | tool_config_auto | yes | no | yes | pass | 2026-04-13T14:50:37Z | 200 | 1.433 | 2.103e-05 | [2026-04-13T14-50-37Z.txt](results/bodies/gemini.tool_config_auto/2026-04-13T14-50-37Z.txt) | toolConfig.functionCallingConfig.mode: AUTO |
| gemini | tool_config_any | yes | no | yes | pass | 2026-04-13T14:50:35Z | 200 | 1.534 | 2.103e-05 | [2026-04-13T14-50-35Z.txt](results/bodies/gemini.tool_config_any/2026-04-13T14-50-35Z.txt) | toolConfig.functionCallingConfig.mode: ANY |
| gemini | tool_config_none | yes | no | yes | pass | 2026-04-13T14:50:38Z | 200 | 2.149 | 5.724e-05 | [2026-04-13T14-50-38Z.txt](results/bodies/gemini.tool_config_none/2026-04-13T14-50-38Z.txt) | toolConfig.functionCallingConfig.mode: NONE |
| gemini | safety_settings | yes | no | yes | pass | 2026-04-13T14:50:07Z | 200 | 7.884 | 7.749e-05 | [2026-04-13T14-50-07Z.txt](results/bodies/gemini.safety_settings/2026-04-13T14-50-07Z.txt) | Safety settings (harm categories + thresholds) |
| gemini | google_search | yes | no | yes | pass | 2026-04-13T14:49:36Z | 200 | 4.168 | 5.673e-05 | [2026-04-13T14-49-36Z.txt](results/bodies/gemini.google_search/2026-04-13T14-49-36Z.txt) | Google Search grounding tool |
| gemini | code_execution | yes | no | yes | pass | 2026-04-13T14:49:33Z | 200 | 3.023 | 9.011e-05 | [2026-04-13T14-49-33Z.txt](results/bodies/gemini.code_execution/2026-04-13T14-49-33Z.txt) | Code execution tool |
| gemini | cached_content | yes | no | yes | pass | 2026-04-13T14:49:33Z | 200 | 0.58 | — | [2026-04-13T14-49-33Z.txt](results/bodies/gemini.cached_content/2026-04-13T14-49-33Z.txt) | Use cachedContent for context caching |
| gemini | store | yes | no | yes | pass | 2026-04-13T14:50:17Z | 200 | 1.026 | 1.25e-06 | [2026-04-13T14-50-17Z.txt](results/bodies/gemini.store/2026-04-13T14-50-17Z.txt) | Logging/storage configuration |

## Results format

- Latest run summary: `results/latest.json`
- Run history: `results/history.jsonl`
- Response bodies: `results/bodies/<case-id>/<timestamp>.txt`

_README generated at 2026-04-13T14:52:43.523675Z by `generate_readme.py`._
