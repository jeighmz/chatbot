Ollama has advantages for prompting a knowledge base offline but at times can get very slow. It takes too long for it to be useful in a chatbot app.

Response time average per model:

- llama-3-405b: 30 seconds
- mistral-nemo: > 4 minutes

Using cloud deployment offloads all the computation. 

- llama-3-405b-instruct: 3 seconds

Other available models:
| Model                         | Path                                   |
|-------------------------------|----------------------------------------|
| MT0_XXL                       | bigscience/mt0-xxl                     |
| CODELLAMA_34B_INSTRUCT_HF     | codellama/codellama-34b-instruct-hf    |
| FLAN_T5_XL                    | google/flan-t5-xl                      |
| FLAN_T5_XXL                   | google/flan-t5-xxl                     |
| FLAN_UL2                      | google/flan-ul2                        |
| MERLINITE_7B                  | ibm-mistralai/merlinite-7b             |
| GRANITE_13B_CHAT_V2           | ibm/granite-13b-chat-v2                |
| GRANITE_13B_INSTRUCT_V2       | ibm/granite-13b-instruct-v2            |
| GRANITE_20B_CODE_INSTRUCT     | ibm/granite-20b-code-instruct          |
| GRANITE_20B_MULTILINGUAL      | ibm/granite-20b-multilingual           |
| GRANITE_34B_CODE_INSTRUCT     | ibm/granite-34b-code-instruct          |
| GRANITE_3B_CODE_INSTRUCT      | ibm/granite-3b-code-instruct           |
| GRANITE_7B_LAB                | ibm/granite-7b-lab                     |
| GRANITE_8B_CODE_INSTRUCT      | ibm/granite-8b-code-instruct           |
| LLAMA_2_13B_CHAT              | meta-llama/llama-2-13b-chat            |
| LLAMA_2_70B_CHAT              | meta-llama/llama-2-70b-chat            |
| LLAMA_3_405B_INSTRUCT         | meta-llama/llama-3-405b-instruct       |
| LLAMA_3_70B_INSTRUCT          | meta-llama/llama-3-70b-instruct        |
| LLAMA_3_8B_INSTRUCT           | meta-llama/llama-3-8b-instruct         |
| MISTRAL_LARGE                 | mistralai/mistral-large                |
| MIXTRAL_8X7B_INSTRUCT_V01     | mistralai/mixtral-8x7b-instruct-v01    |