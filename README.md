# RT-Agent: experiment data

Raw and analysed data behind the RT-Agent paper: an end-to-end pipeline that
reads jailbreak descriptions from papers, repositories and forums, has an LLM
write an executable attack generator for each, runs the generated attacks
against target models and guardrails, and fine-tunes the guards on what got
through.

**Contents.** 159 921 attack rows across the thirteen strategies the paper
evaluates, three target models and five guards, plus the two synthesis arms, the
discovery candidates that the ASR gate rejected, and the analysis artifacts.

## Contents warning

This repository contains working jailbreak prompts and the harmful completions
they elicited from open-weight models. It is published for red-teaming and
guardrail research, in the same spirit as AdvBench, HarmBench and
JailbreakBench. Do not use it to attack systems you do not own.

## Layout

```
data/paper/<strategy>/              the thirteen strategies of the paper
    dataset.jsonl.gz                generated attacks
    dataset_<target>_evaluated.jsonl.gz     attacks + target answer + guard verdicts
    dataset_<target>_evaluated.gptoss.jsonl.gz   the same rows judged by the fifth guard
    generator.py                    the executable generator the LLM wrote
    text.txt                        the source description it was written from
    validation/attempt_N.json       phase-1.5 verdicts, including rejections
data/arms/<strategy>__opus47/       repeat synthesis, Claude Opus 4.7
data/arms/<strategy>__dsh/          synthesis by DeepSeek-V4-Flash under its own harness
data/discovery-rejected/<id>/       candidates the ASR gate rejected
results/                            analysis artifacts, see below
MANIFEST.json                       per-folder file and byte counts
docs/experiments.md                 what each experiment asked and what it found
docs/data-format.md                 the record schema
```

All `.jsonl` are gzipped. Read them without unpacking:

```python
import gzip, json
with gzip.open("data/paper/ReNeLLM/dataset_llama-3.1-8b_evaluated.jsonl.gz", "rt") as fh:
    rows = [json.loads(line) for line in fh]
```

## Which numbers are current

The statistics were recomputed on 19 September 2026 on a stricter denominator: a
target answer counts only when all four consensus guards returned a readable
verdict on it. Files written before that date use the older rule, where every
row counted and a silent guard contributed zero safe-score points, which reads
the same as a harmful verdict.

| file | date | status |
|---|---|---|
| `results/paper_tables.md` | 19 Sep | **current**, the numbers in the paper |
| `results/latex/*.tex` | 19 Sep | **current**, the tables as typeset |
| `results/main_body_changes.md` | 19 Sep | current, lists what the recomputation invalidated |
| `results/REPORT.md` | 17 Sep | superseded, kept for history |
| `results/guard_tables.md` | 17 Sep | superseded |
| `results/gptoss_guard_report.md` | 17 Sep | superseded |
| `results/vanilla_lift.md` | 17 Sep | superseded |
| `results/ОТЧЁТ.md` | 16 Sep | superseded, Russian working report |

The superseded files are kept because they document intermediate states and the
bugs found along the way. Do not mix their numbers with the current ones.

## Strategy names

The paper uses short names. The folders keep the original identifiers so that a
re-run of the pipeline lands on the same paths.

| paper | folder | source |
|---|---|---|
| FITD | `2025.emnlp-main.100` | Foot-In-The-Door, EMNLP 2025 |
| LogiBreak | `2505.13527v2` | Logic Jailbreak |
| BitBypass | `2506.02479v2` | bitstream camouflage |
| RespAttack | `2507.05248v2` | Response Attack |
| ReNeLLM | `ReNeLLM` | nested prompt rewriting |
| Humanize | `humanize` | in-house paraphrase baseline |
| D1 | `018565__arxiv.org_abs_2510.17904` | BreakFun |
| D2 | `018482__arxiv.org_abs_2601.03416` | GAMBIT |
| D3 | `015272__arxiv.org_abs_2510.05709` | prompt-injection extraction |
| D4 | `017849__arxiv.org_abs_2507.13474` | Paper Summary Attack |
| D5 | `043008__github.com_sidfeels_redprobe` | RedProbe |
| D6 | `024653__www.reddit.com_r_ClaudeAIJailbreak…` | Reddit role-play framing |
| D7 | `026062__github.com_fvelazquez-X_AI-Red-Teaming` | red-teaming templates |

## Setup

Targets: Llama-3.1-8B-Instruct (FP8), Qwen-2.5-7B-Instruct, Gemma-3-4B-IT. Six
of the thirteen strategies also carry Dolphin-2.9-8B, which the paper does not
use.

Guards: WildGuard 7B, Qwen3-Guard-Gen 4B, Granite-Guardian-3.2 3B, Llama-Guard-3
1B form the consensus. gpt-oss-Safeguard-20B is reported separately and
contributes no consensus points.

Attack generator: Gemma-3-27B-IT abliterated, served locally.

Prompt pool: AdvBench (520), HarmBench (400), HarmfulQA (1960), do-not-answer
(939), JBB-Behaviors (500).
