# Augmentation preservation (§4.1)

Generated 2026-09-17 14:44Z by `src/augment/preservation.py --score 3` over 28 folders in `.`.
preservation = still strict guard-jailbreak after augmentation / strict guard-jailbreak originally, counted over rows whose augmented evaluation is complete; coverage = evaluated / originally-GJ.

## Per method (all strategies, targets, guards)

| method | preservation | coverage |
|---|---:|---:|
| homoglyphs | 40.7% (4004/9842) | 9842/9842 |
| typos | 41.6% (4090/9842) | 9842/9842 |
| logic_symbols | 31.9% (312/977) | 977/977 |
| logic_vars | 42.2% (412/977) | 977/977 |

## Per method x guard

| method | wildguard | qwen3guard | granite4 | llamaguard |
|---|---:|---:|---:|---:|
| homoglyphs | 42.6% (979/2299) | 32.7% (371/1136) | 33.8% (986/2916) | 47.8% (1668/3491) |
| typos | 40.8% (939/2299) | 33.7% (383/1136) | 37.2% (1085/2916) | 48.2% (1683/3491) |
| logic_symbols | 19.8% (26/131) | 22.3% (40/179) | 40.0% (167/417) | 31.6% (79/250) |
| logic_vars | 36.6% (48/131) | 32.4% (58/179) | 48.9% (204/417) | 40.8% (102/250) |

## Per method x target

| method | llama-3.1-8b | qwen-2.5-7b | gemma-3-4b |
|---|---:|---:|---:|
| homoglyphs | 36.8% (1097/2978) | 41.7% (1541/3692) | 43.1% (1366/3172) |
| typos | 39.7% (1181/2978) | 41.5% (1533/3692) | 43.4% (1376/3172) |
| logic_symbols | 24.4% (74/303) | 33.6% (169/503) | 40.4% (69/171) |
| logic_vars | 40.6% (123/303) | 39.0% (196/503) | 54.4% (93/171) |

## Per strategy x method (over targets and guards)

| стратегия | homoglyphs | typos | logic_symbols | logic_vars |
|---|---:|---:|---:|---:|
| ReNeLLM | 44.3% (626/1413) | 50.3% (711/1413) | — | — |
| 2505.13527v2 (LogiBreak) | 34.6% (338/977) | 31.8% (311/977) | 31.9% (312/977) | 42.2% (412/977) |
| 2506.02479v2 (BitBypass) | 31.5% (218/692) | 33.1% (229/692) | — | — |
| 2507.05248v2 (Response-Attack) | 39.3% (358/911) | 38.2% (348/911) | — | — |
| 2025.emnlp-main.100 (FITD) | 46.9% (206/439) | 47.8% (210/439) | — | — |
| humanize (PAP) | 34.9% (106/304) | 45.4% (138/304) | — | — |
| 018565 | 47.6% (646/1357) | 48.9% (664/1357) | — | — |
| 018482 (GAMBIT) | 42.5% (409/963) | 44.1% (425/963) | — | — |
| 015272 | 34.0% (161/474) | 44.3% (210/474) | — | — |
| 017849 (PSA) | 44.0% (348/791) | 34.1% (270/791) | — | — |
| 043008 (RedProbe) | 50.3% (268/533) | 43.9% (234/533) | — | — |
| 024653 | 21.9% (117/535) | 23.4% (125/535) | — | — |
| 026062 | 44.8% (203/453) | 47.5% (215/453) | — | — |

## Coverage notes

- all folders fully evaluated
