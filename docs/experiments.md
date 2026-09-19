# Experiments

One entry per experiment: the question it was set to answer, how it was run,
what came out, and where the data sits. Numbers are the ones after the
19 September recomputation.

---

## 1. Attack generation and evaluation

**Question.** Do generators written from a text description produce attacks that
bypass production guardrails?

**Setup.** Thirteen strategies, six reproduced from curated descriptions and
seven found by the pipeline itself. Each generator transforms five vanilla
prompt datasets, and every attack runs against three targets and is judged by
four consensus guards plus a fifth reported separately. 159 921 rows.

**Result.** Strict guard-jailbreak rates range from under one percent to
forty-seven, depending on attack and guard. The ordering of guards is stable:
Llama-Guard and Granite-Guardian are bypassed most, Qwen3-Guard under the strict
reading of its `Controversial` label least.

**Data.** `data/paper/`. **Tables.** `results/paper_tables.md`,
`results/latex/tab_gj_abs.tex`, `tab_gj_lift_all.tex`.

---

## 2. Verdict completeness

**Question.** How much of the corpus carries a usable judgement, and does the
missing part bias the result?

**Setup.** Every row is checked for whether each of the four consensus guards
returned a readable verdict on the target answer.

**Result.** 5 312 of 159 921 target answers lost at least one verdict, 3.3%.
WildGuard accounts for 4 540, Granite-Guardian for 772, Llama-Guard for one,
Qwen3-Guard for none. Only 44 prompts out of 53 307 lost every target and left
the count entirely. The loss is concentrated: ten of the thirteen strategies
lose nothing.

The cause is the answer, not the guard. Attacks that drive the target into
repeating a token produce text a guard either declines to judge or cannot parse
its own output for. Of the rows with a missing verdict, 86 to 94 percent carry a
degenerate answer, so re-running the guards returns the same silence.

Dropping these rows lowers our own numbers rather than raising them, because a
silent guard inflates the apparent jailbreak rate.

**Tables.** `results/latex/tab_guard_missing.tex`, `results/guard_failures.md`.

---

## 3. Consensus threshold

**Question.** How much does the reported rate depend on the threshold?

**Setup.** The rate for every guard recomputed at every threshold from one to
five.

**Result.** The ranking of guards holds for thresholds two through four. At five
it collapses, because a single dissenting guard is then enough to condemn an
answer and every guard lands in one narrow band. At one the rates are too low to
separate the weaker attacks.

**Tables.** `results/latex/tab_sigma_sweep.tex`, `results/consensus_sweep/`.

---

## 4. Generator quality

**Question.** Does the pipeline's own validation pass let through generators
that are faithful to their source, and are those generators adequate?

**Setup.** Phase 1.5 has the model that wrote the generator score three fresh
samples on ten criteria, five of form and five of substance, with the right to
repair the code. Because the author is the examiner, a second model that wrote
none of the code and cannot change it rescored ten samples per strategy, 130 in
total, one stateless completion at temperature zero.

**Result.** One judgement out of 1 170 fails. Rejections in the pipeline's own
pass cite substance more often than form, so the synthesiser writes well-formed
code that does the wrong thing more often than malformed code.

The audit is a floor, not a ranking. Every strategy scores at or near one, and a
check with no spread would have passed the RespAttack generator described below,
whose three samples are faithful and whose defect appears only at full scale.

**Data.** `data/paper/*/validation/`. **Tables.** `results/quality_audit/`,
`results/validation_stats/`.

---

## 5. Open synthesiser

**Question.** Does the method depend on one proprietary model?

**Setup.** The synthesis stage rerun with DeepSeek-V4-Flash-0731 under `dsh`,
its own open harness, against Claude Opus 4.7 under Claude Code. Model and
harness change together so each runs in its native wrapper. Same prompts, same
retry budgets, each arm validating its own generator. Compared on AdvBench-520.

**Result.** Over the twelve strategies both arms completed, 72.3% ASR against
66.5%, and strict guard-jailbreak 15.3% against 11.2%. Four strategies carry
almost the whole gap, and on one the open arm is ahead by eighteen points.

The thirteenth is where the open arm failed. For RespAttack it emitted three
attacks instead of 520. Its generator builds a semaphore from the concurrency
limit and never acquires it, so all 520 prompts hit a four-slot inference server
at once, every auxiliary call times out, and a handler meant to keep sibling
tasks alive swallows the prompt. Both Opus arms acquire the same semaphore on
the same task. Rerunning the generator unchanged reproduced the collapse.

Validation could not catch it: three samples do not load the server, and the
output contract checks the shape of each record rather than how many arrive.

**Data.** `data/arms/`. **Tables.** `results/arm_comparison/`.

---

## 6. Augmentation

**Question.** Does perturbing an attack keep it working?

**Setup.** For each guard, up to 100 prompts that were a strict guard-jailbreak
against it are selected, pooled into 3 111 unique attacks, perturbed by each
operator, and rerun through the targets and all four guards. The metric is the
share that remains a jailbreak.

**Result.** Around 41% survive homoglyph substitution or typo injection. The
grown training pool is therefore not a pool of attacks: most of its members no
longer bypass the guard they came from. Preservation depends on the guard more
than on the operator. Rewriting LogiBreak's logical symbols is the one operator
that damages the attack itself rather than the prompt surface, at 19.8% against
WildGuard.

**Tables.** `results/augmentation/`.

---

## 7. Deduplication

**Question.** Does deduplication work, is the threshold good, and is too much
removed?

**Setup.** Agglomerative clustering with average linkage over cosine distance
between Qwen3-Embedding-0.6B vectors. The threshold was swept and the removals
judged by an LLM on a fixed budget of 400 verdicts.

**Result.** Negative, and the negative result is the useful one. A third of the
candidates is removed, not half. The false removal rate comes out at 53%, 79% or
95% depending only on how much source text the judge is shown. A quantity that
moves by forty points with the evidence shown is not measuring the threshold.

The cause is the object compared. Clustering compares one extracted prompt while
the judge compares methods. One cluster of 79 items turned out to be ten
distinct sources, six of which have no prompt to extract at all, joined because
they quote the same AdvBench example.

**Tables.** `results/dedup_audit/`.

---

## 8. Fine-tuning

Guard adaptation and the regression check on standard benchmarks are in the
paper. The artifacts here were produced before the 19 September recomputation
and have not been rechecked against it.

**Tables.** `results/kl_protocol_wildguard_runs.csv`, `results/REPORT.md`.
