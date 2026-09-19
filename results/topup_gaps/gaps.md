# Дыры в данных (§1.6)

Папок: 13; датасетов: 5; таргетов: 3.

- Тип A (только гарды): 5259 строк-гардов
- Тип B (инференс таргета по готовым атакам): 37 строк
- Тип C (атаки отсутствуют → генерация + таргет + гарды): 8520 атак×таргет

| папка | датасет | ожид. | атак | таргет | ответов | wildguard | qwen3guard | granite4 | llamaguard |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|
| outputs_2025.emnlp-main.100 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_2025.emnlp-main.100 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_2025.emnlp-main.100 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_2025.emnlp-main.100 | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_2025.emnlp-main.100 | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_2025.emnlp-main.100 | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_2025.emnlp-main.100 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2025.emnlp-main.100 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2025.emnlp-main.100 | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2025.emnlp-main.100 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_2025.emnlp-main.100 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_2025.emnlp-main.100 | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_2025.emnlp-main.100 | JBB-Behaviors | 500 | 500 | llama-3.1-8b | 500 | 500 | 500 | 500 | 500 |
| outputs_2025.emnlp-main.100 | JBB-Behaviors | 500 | 500 | qwen-2.5-7b | 500 | 500 | 500 | 500 | 500 |
| outputs_2025.emnlp-main.100 | JBB-Behaviors | 500 | 500 | gemma-3-4b | 500 | 500 | 500 | 500 | 500 |
| outputs_2505.13527v2 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_2505.13527v2 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_2505.13527v2 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_2505.13527v2 | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_2505.13527v2 | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_2505.13527v2 | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_2505.13527v2 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2505.13527v2 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2505.13527v2 | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2505.13527v2 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_2505.13527v2 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_2505.13527v2 | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_2505.13527v2 | JBB-Behaviors | 500 | 500 | llama-3.1-8b | 500 | 500 | 500 | 500 | 500 |
| outputs_2505.13527v2 | JBB-Behaviors | 500 | 500 | qwen-2.5-7b | 500 | 500 | 500 | 500 | 500 |
| outputs_2505.13527v2 | JBB-Behaviors | 500 | 500 | gemma-3-4b | 500 | 500 | 500 | 500 | 500 |
| outputs_2506.02479v2 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_2506.02479v2 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_2506.02479v2 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_2506.02479v2 | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_2506.02479v2 | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_2506.02479v2 | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_2506.02479v2 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2506.02479v2 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2506.02479v2 | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2506.02479v2 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_2506.02479v2 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_2506.02479v2 | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_2506.02479v2 ⚠ | JBB-Behaviors | 500 | 300 | llama-3.1-8b | 300 | 300 | 300 | 300 | 300 |
| outputs_2506.02479v2 ⚠ | JBB-Behaviors | 500 | 300 | qwen-2.5-7b | 300 | 300 | 300 | 300 | 300 |
| outputs_2506.02479v2 ⚠ | JBB-Behaviors | 500 | 300 | gemma-3-4b | 300 | 300 | 300 | 300 | 300 |
| outputs_2507.05248v2 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_2507.05248v2 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_2507.05248v2 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_2507.05248v2 | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_2507.05248v2 | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_2507.05248v2 | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_2507.05248v2 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2507.05248v2 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2507.05248v2 | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_2507.05248v2 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_2507.05248v2 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_2507.05248v2 | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_2507.05248v2 ⚠ | JBB-Behaviors | 500 | 300 | llama-3.1-8b | 300 | 300 | 300 | 300 | 300 |
| outputs_2507.05248v2 ⚠ | JBB-Behaviors | 500 | 300 | qwen-2.5-7b | 300 | 300 | 300 | 300 | 300 |
| outputs_2507.05248v2 ⚠ | JBB-Behaviors | 500 | 300 | gemma-3-4b | 300 | 300 | 300 | 300 | 300 |
| outputs_ReNeLLM | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_ReNeLLM | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_ReNeLLM | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_ReNeLLM ⚠ | harmbench | 400 | 80 | llama-3.1-8b | 80 | 80 | 80 | 80 | 80 |
| outputs_ReNeLLM ⚠ | harmbench | 400 | 80 | qwen-2.5-7b | 80 | 80 | 80 | 80 | 80 |
| outputs_ReNeLLM ⚠ | harmbench | 400 | 80 | gemma-3-4b | 80 | 80 | 80 | 80 | 80 |
| outputs_ReNeLLM | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_ReNeLLM | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_ReNeLLM | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_ReNeLLM | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_ReNeLLM | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_ReNeLLM | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_ReNeLLM | JBB-Behaviors | 500 | 500 | llama-3.1-8b | 500 | 500 | 500 | 500 | 500 |
| outputs_ReNeLLM | JBB-Behaviors | 500 | 500 | qwen-2.5-7b | 500 | 500 | 500 | 500 | 500 |
| outputs_ReNeLLM | JBB-Behaviors | 500 | 500 | gemma-3-4b | 500 | 500 | 500 | 500 | 500 |
| outputs_humanize | AdvBench | 520 | 520 | llama-3.1-8b | 1885 | 1885 | 1885 | 1885 | 1885 |
| outputs_humanize | AdvBench | 520 | 520 | qwen-2.5-7b | 1558 | 1558 | 1558 | 1558 | 1558 |
| outputs_humanize | AdvBench | 520 | 520 | gemma-3-4b | 1507 | 1507 | 1507 | 1507 | 1507 |
| outputs_humanize | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_humanize | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_humanize | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_humanize | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_humanize | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_humanize | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_humanize | do-not-answer | 939 | 939 | llama-3.1-8b | 2679 | 2679 | 2679 | 2679 | 2679 |
| outputs_humanize | do-not-answer | 939 | 939 | qwen-2.5-7b | 3020 | 3020 | 3020 | 3020 | 3020 |
| outputs_humanize | do-not-answer | 939 | 939 | gemma-3-4b | 2919 | 2919 | 2919 | 2919 | 2919 |
| outputs_humanize | JBB-Behaviors | 500 | 500 | llama-3.1-8b | 1123 | 1123 | 1123 | 1123 | 1123 |
| outputs_humanize | JBB-Behaviors | 500 | 500 | qwen-2.5-7b | 1308 | 1308 | 1308 | 1308 | 1308 |
| outputs_humanize | JBB-Behaviors | 500 | 500 | gemma-3-4b | 1057 | 1057 | 1057 | 1057 | 1057 |
| outputs_018565__arxiv.org_abs_2510.179 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_018565__arxiv.org_abs_2510.179 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_018565__arxiv.org_abs_2510.179 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_018565__arxiv.org_abs_2510.179 ⚠ | harmbench | 400 | 400 | llama-3.1-8b | 395 | 395 | 395 | 395 | 395 |
| outputs_018565__arxiv.org_abs_2510.179 ⚠ | harmbench | 400 | 400 | qwen-2.5-7b | 392 | 392 | 392 | 392 | 392 |
| outputs_018565__arxiv.org_abs_2510.179 ⚠ | harmbench | 400 | 400 | gemma-3-4b | 392 | 392 | 392 | 392 | 392 |
| outputs_018565__arxiv.org_abs_2510.179 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_018565__arxiv.org_abs_2510.179 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_018565__arxiv.org_abs_2510.179 | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_018565__arxiv.org_abs_2510.179 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_018565__arxiv.org_abs_2510.179 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_018565__arxiv.org_abs_2510.179 | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_018565__arxiv.org_abs_2510.179 ⚠ | JBB-Behaviors | 500 | 200 | llama-3.1-8b | 200 | 200 | 200 | 200 | 200 |
| outputs_018565__arxiv.org_abs_2510.179 ⚠ | JBB-Behaviors | 500 | 200 | qwen-2.5-7b | 200 | 200 | 200 | 200 | 200 |
| outputs_018565__arxiv.org_abs_2510.179 ⚠ | JBB-Behaviors | 500 | 200 | gemma-3-4b | 200 | 200 | 200 | 200 | 200 |
| outputs_018482__arxiv.org_abs_2601.034 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_018482__arxiv.org_abs_2601.034 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_018482__arxiv.org_abs_2601.034 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_018482__arxiv.org_abs_2601.034 ⚠ | harmbench | 400 | 400 | llama-3.1-8b | 399 | 399 | 399 | 399 | 399 |
| outputs_018482__arxiv.org_abs_2601.034 ⚠ | harmbench | 400 | 400 | qwen-2.5-7b | 399 | 399 | 399 | 399 | 399 |
| outputs_018482__arxiv.org_abs_2601.034 ⚠ | harmbench | 400 | 400 | gemma-3-4b | 399 | 399 | 399 | 399 | 399 |
| outputs_018482__arxiv.org_abs_2601.034 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_018482__arxiv.org_abs_2601.034 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_018482__arxiv.org_abs_2601.034 | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_018482__arxiv.org_abs_2601.034 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_018482__arxiv.org_abs_2601.034 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_018482__arxiv.org_abs_2601.034 | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_018482__arxiv.org_abs_2601.034 ⚠ | JBB-Behaviors | 500 | 200 | llama-3.1-8b | 200 | 200 | 200 | 200 | 200 |
| outputs_018482__arxiv.org_abs_2601.034 ⚠ | JBB-Behaviors | 500 | 200 | qwen-2.5-7b | 200 | 200 | 200 | 200 | 200 |
| outputs_018482__arxiv.org_abs_2601.034 ⚠ | JBB-Behaviors | 500 | 200 | gemma-3-4b | 200 | 200 | 200 | 200 | 200 |
| outputs_015272__arxiv.org_abs_2510.057 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_015272__arxiv.org_abs_2510.057 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_015272__arxiv.org_abs_2510.057 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_015272__arxiv.org_abs_2510.057 ⚠ | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 0 | 400 |
| outputs_015272__arxiv.org_abs_2510.057 | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_015272__arxiv.org_abs_2510.057 | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_015272__arxiv.org_abs_2510.057 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_015272__arxiv.org_abs_2510.057 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_015272__arxiv.org_abs_2510.057 ⚠ | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 0 | 1960 | 0 | 1960 |
| outputs_015272__arxiv.org_abs_2510.057 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_015272__arxiv.org_abs_2510.057 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_015272__arxiv.org_abs_2510.057 ⚠ | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 0 | 939 |
| outputs_015272__arxiv.org_abs_2510.057 ⚠ | JBB-Behaviors | 500 | 200 | llama-3.1-8b | 200 | 200 | 200 | 200 | 200 |
| outputs_015272__arxiv.org_abs_2510.057 ⚠ | JBB-Behaviors | 500 | 200 | qwen-2.5-7b | 200 | 200 | 200 | 200 | 200 |
| outputs_015272__arxiv.org_abs_2510.057 ⚠ | JBB-Behaviors | 500 | 200 | gemma-3-4b | 200 | 200 | 200 | 200 | 200 |
| outputs_017849__arxiv.org_abs_2507.134 | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_017849__arxiv.org_abs_2507.134 | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_017849__arxiv.org_abs_2507.134 | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_017849__arxiv.org_abs_2507.134 | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_017849__arxiv.org_abs_2507.134 | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_017849__arxiv.org_abs_2507.134 | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_017849__arxiv.org_abs_2507.134 | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_017849__arxiv.org_abs_2507.134 | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_017849__arxiv.org_abs_2507.134 | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_017849__arxiv.org_abs_2507.134 | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_017849__arxiv.org_abs_2507.134 | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_017849__arxiv.org_abs_2507.134 | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_017849__arxiv.org_abs_2507.134 ⚠ | JBB-Behaviors | 500 | 200 | llama-3.1-8b | 200 | 200 | 200 | 200 | 200 |
| outputs_017849__arxiv.org_abs_2507.134 ⚠ | JBB-Behaviors | 500 | 200 | qwen-2.5-7b | 200 | 200 | 200 | 200 | 200 |
| outputs_017849__arxiv.org_abs_2507.134 ⚠ | JBB-Behaviors | 500 | 200 | gemma-3-4b | 200 | 200 | 200 | 200 | 200 |
| outputs_043008__github.com_sidfeels_re | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_043008__github.com_sidfeels_re | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_043008__github.com_sidfeels_re | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_043008__github.com_sidfeels_re | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_043008__github.com_sidfeels_re | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_043008__github.com_sidfeels_re | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_043008__github.com_sidfeels_re | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_043008__github.com_sidfeels_re | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_043008__github.com_sidfeels_re | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_043008__github.com_sidfeels_re | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_043008__github.com_sidfeels_re | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_043008__github.com_sidfeels_re | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_043008__github.com_sidfeels_re | JBB-Behaviors | 500 | 500 | llama-3.1-8b | 500 | 500 | 500 | 500 | 500 |
| outputs_043008__github.com_sidfeels_re | JBB-Behaviors | 500 | 500 | qwen-2.5-7b | 500 | 500 | 500 | 500 | 500 |
| outputs_043008__github.com_sidfeels_re | JBB-Behaviors | 500 | 500 | gemma-3-4b | 500 | 500 | 500 | 500 | 500 |
| outputs_024653__www.reddit.com_r_Claud | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_024653__www.reddit.com_r_Claud | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_024653__www.reddit.com_r_Claud | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_024653__www.reddit.com_r_Claud ⚠ | harmbench | 400 | 80 | llama-3.1-8b | 80 | 80 | 80 | 80 | 80 |
| outputs_024653__www.reddit.com_r_Claud ⚠ | harmbench | 400 | 80 | qwen-2.5-7b | 80 | 80 | 80 | 80 | 80 |
| outputs_024653__www.reddit.com_r_Claud ⚠ | harmbench | 400 | 80 | gemma-3-4b | 80 | 80 | 80 | 80 | 80 |
| outputs_024653__www.reddit.com_r_Claud | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_024653__www.reddit.com_r_Claud | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_024653__www.reddit.com_r_Claud | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_024653__www.reddit.com_r_Claud | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_024653__www.reddit.com_r_Claud | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_024653__www.reddit.com_r_Claud | do-not-answer | 939 | 939 | gemma-3-4b | 939 | 939 | 939 | 939 | 939 |
| outputs_024653__www.reddit.com_r_Claud ⚠ | JBB-Behaviors | 500 | 200 | llama-3.1-8b | 200 | 200 | 200 | 200 | 200 |
| outputs_024653__www.reddit.com_r_Claud ⚠ | JBB-Behaviors | 500 | 200 | qwen-2.5-7b | 200 | 200 | 200 | 200 | 200 |
| outputs_024653__www.reddit.com_r_Claud ⚠ | JBB-Behaviors | 500 | 200 | gemma-3-4b | 200 | 200 | 200 | 200 | 200 |
| outputs_026062__github.com_fvelazquez- | AdvBench | 520 | 520 | llama-3.1-8b | 520 | 520 | 520 | 520 | 520 |
| outputs_026062__github.com_fvelazquez- | AdvBench | 520 | 520 | qwen-2.5-7b | 520 | 520 | 520 | 520 | 520 |
| outputs_026062__github.com_fvelazquez- | AdvBench | 520 | 520 | gemma-3-4b | 520 | 520 | 520 | 520 | 520 |
| outputs_026062__github.com_fvelazquez- | harmbench | 400 | 400 | llama-3.1-8b | 400 | 400 | 400 | 400 | 400 |
| outputs_026062__github.com_fvelazquez- | harmbench | 400 | 400 | qwen-2.5-7b | 400 | 400 | 400 | 400 | 400 |
| outputs_026062__github.com_fvelazquez- | harmbench | 400 | 400 | gemma-3-4b | 400 | 400 | 400 | 400 | 400 |
| outputs_026062__github.com_fvelazquez- | HarmfulQA | 1960 | 1960 | llama-3.1-8b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_026062__github.com_fvelazquez- | HarmfulQA | 1960 | 1960 | qwen-2.5-7b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_026062__github.com_fvelazquez- | HarmfulQA | 1960 | 1960 | gemma-3-4b | 1960 | 1960 | 1960 | 1960 | 1960 |
| outputs_026062__github.com_fvelazquez- | do-not-answer | 939 | 939 | llama-3.1-8b | 939 | 939 | 939 | 939 | 939 |
| outputs_026062__github.com_fvelazquez- | do-not-answer | 939 | 939 | qwen-2.5-7b | 939 | 939 | 939 | 939 | 939 |
| outputs_026062__github.com_fvelazquez- ⚠ | do-not-answer | 939 | 939 | gemma-3-4b | 926 | 926 | 926 | 926 | 926 |
| outputs_026062__github.com_fvelazquez- ⚠ | JBB-Behaviors | 500 | 200 | llama-3.1-8b | 200 | 200 | 200 | 200 | 200 |
| outputs_026062__github.com_fvelazquez- ⚠ | JBB-Behaviors | 500 | 200 | qwen-2.5-7b | 200 | 200 | 200 | 200 | 200 |
| outputs_026062__github.com_fvelazquez- ⚠ | JBB-Behaviors | 500 | 200 | gemma-3-4b | 200 | 200 | 200 | 200 | 200 |
