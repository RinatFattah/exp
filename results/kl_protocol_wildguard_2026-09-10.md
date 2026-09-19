# KL-regularised continual fine-tuning of wildguard — full results

Date: 2026-09-09/10. Branch `ivan_local_merged`. Driver: `src/finetune/kl_protocol.py`; trainer: `src/finetune/train_all.py` (KLSFTTrainer); bench: `src/evaluate_finetune/evaluate_guard.py`; val eval: `src/finetune/eval_val_per_source.py`.

## Setup

- Guard: `allenai/wildguard`, LoRA r=16 alpha=32 dropout=0.05 on q/k/v/o, bf16, lr 5e-5 cosine, warmup 5%, 2 epochs, batch 4 × grad-accum 4 (bs 2 × 8 when a separate frozen reference model is loaded).
- KL: `loss = CE + kl_coef · KL(student ‖ ref)` on completion tokens only (all 6 verdict tokens incl. format tokens), all samples. `ref = original` = frozen copy of allenai/wildguard; `ref = previous` = same LoRA model with adapter disabled (= the merged model the run started from).
- A1 = ReNeLLM (`outputs_ReNeLLM`), A2 = BitBypass (`outputs_2506.02479v2`), generator gemma-3-27b abliterated. Attack items = prompts that bypassed the original wildguard (strict guard-jailbreak, safe_score<3 consensus). Safe items = same wrapper around benign PKU-SafeRLHF prompts, generated with the local gemma3-27B Q8_0 gguf.
- Split: 80/20 by md5 of the vanilla seed prompt (all attacks/augmentations of one seed land in one split; same seed → same split across A1, A2 and the mix). Val = originals only; train additionally gets 1 augmented copy per original (homoglyphs, typos). WildGuardMix 800 safe + 800 unsafe mixed into every train set.
- Bench = mean F1 over 6 datasets (Aegis, BeaverTails, OAI moderation, SafeRLHF, ToxicChat, XSTest). HarmBench excluded (gated on HF for this token).
- Val metrics are accuracy of the exact verdict (greedy decoding): `unsafe` = share of attack prompts flagged harmful (recall on the attack); `safe` = share of benign-wrapped prompts passed as safe (1 − over-refusal on the wrapper).
- Sequential = adapter trained → merged into weights → new adapter trained on the merged model.
- Pass C (2026-09-10, after the grad-accum fix so kl_coef is the effective weight): KL computed only on rows whose `source` starts with `wildguard` (WildGuardMix), i.e. the regulariser guards the original behaviour on reference data and never touches attack rows. Adds sequential controls without KL (r2_kl0, r3_kl0 from r1_kl0, r4_kl0 from r2_kl0).
- No hyper-parameter validation split: kl_coef was chosen on the same val (r1_kl only); everything else uses val as test. Single seed (42).

## Datasets

| dataset | train | val | train composition | val composition |
|---|---|---|---|---|
| `outputs_ReNeLLM_gemma-3-27b` | 3509 | 634 | {'logibreak_unsafe_original': 565, 'logibreak_unsafe_aug': 565, 'logibreak_safe_original': 556, 'logibreak_safe_aug': 556, 'wildguard_safe': 627, 'wildguard_unsafe': 640} | {'logibreak_unsafe_original': 146, 'logibreak_safe_original': 155, 'wildguard_unsafe': 160, 'wildguard_safe': 173} |
| `outputs_2506.02479v2_gemma-3-27b` | 2943 | 561 | {'logibreak_unsafe_original': 420, 'logibreak_unsafe_aug': 420, 'logibreak_safe_original': 418, 'logibreak_safe_aug': 418, 'wildguard_safe': 627, 'wildguard_unsafe': 640} | {'logibreak_unsafe_original': 113, 'logibreak_safe_original': 115, 'wildguard_unsafe': 160, 'wildguard_safe': 173} |
| `outputs_mix_renellm_bitbypass_gemma-3-27b` | 5185 | 862 | {'logibreak_unsafe_renellm_original': 565, 'logibreak_unsafe_bitbypass_original': 420, 'logibreak_unsafe_renellm_aug': 565, 'logibreak_unsafe_bitbypass_aug': 420, 'logibreak_safe_bitbypass_original': 418, 'logibreak_safe_renellm_original': 556, 'logibreak_safe_bitbypass_aug': 418, 'logibreak_safe_renellm_aug': 556, 'wildguard_safe': 627, 'wildguard_unsafe': 640} | {'logibreak_unsafe_renellm_original': 146, 'logibreak_unsafe_bitbypass_original': 113, 'logibreak_safe_bitbypass_original': 115, 'logibreak_safe_renellm_original': 155, 'wildguard_unsafe': 160, 'wildguard_safe': 173} |

Guard-jailbreak counts per strategy folder (unique vanilla seeds that bypassed wildguard): ReNeLLM 711, BitBypass 533, PSA 494, FITD 478, GAMBIT 415, LogiBreak 345.

## Main table (all passes)

| pass | run | kl_coef | start | data | KL ref | bench F1 (Δ) | A1 unsafe | A1 safe | A2 unsafe | A2 safe | WGmix safe/unsafe | ToxicChat FP/FN | final loss | final kl |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | original | – | - | - | - | 0.813 | 0.000 | 0.529 | 0.009 | 0.304 | 1.00/1.00 | 72/3 | – | – |
| pass A: kl_coef 0.5 (too strong) | r1_kl0 | – | original | A1 | none | 0.812 (-0.002) | 0.801 | 0.845 | 0.248 | 0.304 | 1.00/1.00 | 73/6 | 0.022 | – |
| pass A: kl_coef 0.5 (too strong) | r1_kl | 0.5 | original | A1 | original | 0.810 (-0.003) | 0.096 | 0.542 | 0.009 | 0.313 | 1.00/1.00 | 77/3 | 0.132 | 0.0010 |
| pass A: kl_coef 0.5 (too strong) | r2_kl | 0.5 | original | A2 | original | 0.810 (-0.003) | 0.021 | 0.535 | 0.425 | 0.296 | 1.00/1.00 | 77/3 | 0.142 | 0.0331 |
| pass A: kl_coef 0.5 (too strong) | r5_mix | 0.5 | original | A1+A2 | original | 0.812 (-0.002) | 0.130 | 0.548 | 0.389 | 0.296 | 1.00/1.00 | 72/4 | 0.099 | 0.0000 |
| sweep: kl_coef 0.01 | r1_kl | 0.01 | original | A1 | original | 0.812 (-0.002) | 0.781 | 0.839 | 0.195 | 0.322 | 1.00/1.00 | 76/5 | 0.033 | 0.0099 |
| sweep: kl_coef 0.2 | r1_kl | 0.2 | original | A1 | original | 0.813 (+0.000) | 0.493 | 0.548 | 0.203 | 0.304 | 1.00/1.00 | 75/3 | 0.101 | 0.0010 |
| pass B: kl_coef 0.05, KL on all rows | r1_kl0 | – | original | A1 | none | 0.812 (-0.002) | 0.801 | 0.845 | 0.248 | 0.304 | 1.00/1.00 | 73/6 | 0.022 | – |
| pass B: kl_coef 0.05, KL on all rows | r1_kl | 0.05 | original | A1 | original | 0.813 (+0.000) | 0.747 | 0.761 | 0.230 | 0.322 | 1.00/1.00 | 76/4 | 0.059 | 0.0013 |
| pass B: kl_coef 0.05, KL on all rows | r2_kl | 0.05 | original | A2 | original | 0.800 (-0.013) | 0.000 | 0.748 | 0.974 | 0.635 | 1.00/1.00 | 90/6 | 0.070 | 0.3128 |
| pass B: kl_coef 0.05, KL on all rows | r5_mix | 0.05 | original | A1+A2 | original | 0.807 (-0.007) | 0.760 | 0.787 | 0.965 | 0.765 | 1.00/1.00 | 83/5 | 0.047 | -0.0000 |
| pass B: kl_coef 0.05, KL on all rows | r3a | 0.05 | r1_kl-merged | A2 | original | 0.800 (-0.013) | 0.788 | 0.800 | 0.920 | 0.444 | 1.00/1.00 | 111/4 | 0.082 | 0.1593 |
| pass B: kl_coef 0.05, KL on all rows | r3b | 0.05 | r1_kl-merged | A2 | r1_kl (previous) | 0.792 (-0.022) | 0.706 | 0.910 | 0.938 | 0.930 | 1.00/1.00 | 118/5 | 0.029 | 0.2433 |
| pass B: kl_coef 0.05, KL on all rows | r4a | 0.05 | r2_kl-merged | A1 | original | 0.802 (-0.012) | 0.726 | 0.658 | 0.965 | 0.661 | 1.00/1.00 | 89/5 | 0.081 | 0.0000 |
| pass B: kl_coef 0.05, KL on all rows | r4b | 0.05 | r2_kl-merged | A1 | r2_kl (previous) | 0.802 (-0.012) | 0.644 | 0.890 | 0.956 | 0.704 | 1.00/1.00 | 91/6 | 0.058 | 0.0222 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r1_kl0 | – | original | A1 | none | 0.812 (-0.002) | 0.801 | 0.845 | 0.248 | 0.304 | 1.00/1.00 | 73/6 | 0.022 | – |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r1_kl | 0.5 | original | A1 | original | 0.810 (-0.003) | 0.794 | 0.858 | 0.372 | 0.296 | 1.00/1.00 | 77/4 | 0.022 | 0.0000 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r2_kl | 0.5 | original | A2 | original | 0.800 (-0.013) | 0.000 | 0.755 | 0.974 | 0.670 | 1.00/1.00 | 88/6 | 0.034 | 0.0000 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r5_mix | 0.5 | original | A1+A2 | original | 0.803 (-0.010) | 0.836 | 0.826 | 0.956 | 0.870 | 1.00/1.00 | 89/6 | 0.021 | 0.0000 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r3a | 0.5 | r1_kl-merged | A2 | original | 0.803 (-0.010) | 0.733 | 0.897 | 0.929 | 0.965 | 1.00/1.00 | 88/5 | 0.013 | 0.0000 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r3b | 0.5 | r1_kl-merged | A2 | r1_kl (previous) | 0.802 (-0.012) | 0.794 | 0.871 | 0.965 | 0.922 | 1.00/1.00 | 97/4 | 0.010 | 0.0000 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r4a | 0.5 | r2_kl-merged | A1 | original | 0.803 (-0.010) | 0.794 | 0.858 | 0.814 | 0.852 | 1.00/1.00 | 81/7 | 0.038 | 0.0000 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r4b | 0.5 | r2_kl-merged | A1 | r2_kl (previous) | 0.803 (-0.010) | 0.801 | 0.852 | 0.894 | 0.852 | 1.00/1.00 | 84/7 | 0.039 | 0.0000 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r2_kl0 | – | original | A2 | none | 0.802 (-0.012) | 0.000 | 0.832 | 0.974 | 0.652 | 1.00/1.00 | 89/6 | 0.034 | – |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r3_kl0 | – | r1_kl0-merged | A2 | none | 0.783 (-0.030) | 0.774 | 0.832 | 0.920 | 0.948 | 1.00/0.99 | 109/7 | 0.008 | – |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r4_kl0 | – | r2_kl0-merged | A1 | none | 0.800 (-0.013) | 0.808 | 0.845 | 0.920 | 0.809 | 1.00/1.00 | 87/7 | 0.037 | – |

Val group sizes: ReNeLLM 146 unsafe / 155 safe; BitBypass 113 unsafe / 115 safe; WildGuardMix 160 unsafe / 173 safe in both. 1 SE at acc≈0.8 is ≈3.5 pp.

## Per-benchmark F1

| pass | run | AegisSafetyTest | BeaverTails | OAI_Moderation | SafeRLHF | ToxicChat | XSTest | agg |
|---|---|---|---|---|---|---|---|---|
| baseline | original | 0.89 | 0.77 | 0.73 | 0.92 | 0.62 | 0.95 | 0.813 |
| pass A: kl_coef 0.5 (too strong) | r1_kl0 | 0.89 | 0.77 | 0.74 | 0.92 | 0.59 | 0.96 | 0.812 |
| pass A: kl_coef 0.5 (too strong) | r1_kl | 0.88 | 0.77 | 0.73 | 0.92 | 0.60 | 0.96 | 0.810 |
| pass A: kl_coef 0.5 (too strong) | r2_kl | 0.89 | 0.77 | 0.72 | 0.92 | 0.60 | 0.96 | 0.810 |
| pass A: kl_coef 0.5 (too strong) | r5_mix | 0.88 | 0.77 | 0.73 | 0.93 | 0.61 | 0.95 | 0.812 |
| sweep: kl_coef 0.01 | r1_kl | 0.89 | 0.77 | 0.74 | 0.93 | 0.59 | 0.95 | 0.812 |
| sweep: kl_coef 0.2 | r1_kl | 0.88 | 0.77 | 0.73 | 0.93 | 0.61 | 0.96 | 0.813 |
| pass B: kl_coef 0.05, KL on all rows | r1_kl0 | 0.89 | 0.77 | 0.74 | 0.92 | 0.59 | 0.96 | 0.812 |
| pass B: kl_coef 0.05, KL on all rows | r1_kl | 0.89 | 0.77 | 0.74 | 0.93 | 0.60 | 0.95 | 0.813 |
| pass B: kl_coef 0.05, KL on all rows | r2_kl | 0.89 | 0.77 | 0.72 | 0.93 | 0.54 | 0.95 | 0.800 |
| pass B: kl_coef 0.05, KL on all rows | r5_mix | 0.88 | 0.77 | 0.74 | 0.93 | 0.57 | 0.95 | 0.807 |
| pass B: kl_coef 0.05, KL on all rows | r3a | 0.90 | 0.77 | 0.73 | 0.93 | 0.51 | 0.96 | 0.800 |
| pass B: kl_coef 0.05, KL on all rows | r3b | 0.89 | 0.77 | 0.71 | 0.93 | 0.49 | 0.96 | 0.792 |
| pass B: kl_coef 0.05, KL on all rows | r4a | 0.88 | 0.77 | 0.73 | 0.93 | 0.55 | 0.95 | 0.802 |
| pass B: kl_coef 0.05, KL on all rows | r4b | 0.89 | 0.77 | 0.73 | 0.93 | 0.54 | 0.95 | 0.802 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r1_kl0 | 0.89 | 0.77 | 0.74 | 0.92 | 0.59 | 0.96 | 0.812 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r1_kl | 0.89 | 0.77 | 0.73 | 0.93 | 0.59 | 0.95 | 0.810 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r2_kl | 0.89 | 0.77 | 0.72 | 0.93 | 0.55 | 0.94 | 0.800 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r5_mix | 0.89 | 0.77 | 0.74 | 0.92 | 0.55 | 0.95 | 0.803 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r3a | 0.89 | 0.77 | 0.73 | 0.92 | 0.56 | 0.95 | 0.803 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r3b | 0.90 | 0.77 | 0.72 | 0.93 | 0.54 | 0.95 | 0.802 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r4a | 0.88 | 0.77 | 0.74 | 0.93 | 0.56 | 0.94 | 0.803 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r4b | 0.89 | 0.77 | 0.74 | 0.93 | 0.55 | 0.94 | 0.803 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r2_kl0 | 0.89 | 0.77 | 0.73 | 0.93 | 0.55 | 0.94 | 0.802 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r3_kl0 | 0.90 | 0.77 | 0.68 | 0.91 | 0.49 | 0.95 | 0.783 |
| pass C: kl_coef 0.5, KL only on WildGuardMix rows (+ no-KL sequential controls) | r4_kl0 | 0.89 | 0.77 | 0.73 | 0.93 | 0.54 | 0.94 | 0.800 |

ToxicChat: 63 harmful / 865 benign; OAI moderation: 522 harmful / 1158 benign. Baseline ToxicChat FP=72, OAI FP=356.

## kl_coef sweep on R1 (original → ReNeLLM, KL → original)

| kl_coef | A1 unsafe | A1 safe | A2 unsafe (transfer) | bench F1 |
|---|---|---|---|---|
| 0 (no KL) | 0.801 | 0.845 | 0.248 | 0.812 |
| 0.01 | 0.781 | 0.839 | 0.195 | 0.812 |
| 0.05 | 0.747 | 0.761 | 0.230 | 0.813 |
| 0.2 | 0.493 | 0.548 | 0.203 | 0.813 |
| 0.5 | 0.794 | 0.858 | 0.372 | 0.810 |

## Caveat found after the runs: effective KL weight

With transformers 4.57.6 the Trainer does not divide the loss by the number of gradient-accumulation
micro-batches when the model accepts `num_items_in_batch` (Mistral-family does). TRL's CE is already
normalised over the whole accumulated batch, but the KL term in `KLSFTTrainer` was a per-micro-batch
token mean, so it was summed G = 16 // bs times. **Effective KL weight in every run above is
`kl_coef × G`: 4·kl_coef for bs 4 runs, 8·kl_coef for the bs 2 runs r3a and r4a** (separate frozen
reference → halved batch). So pass B ran at effective 0.2 (0.4 for r3a/r4a), pass A at 2.0, the sweep at
0.04 / 0.8. Relative conclusions are unchanged (the ranking of coefficients and the r3a/r4a vs r3b/r4b
comparison already used the same G within each pair except r3a≠r3b, r4a≠r4b, where the "original"
reference also had 2× the weight). Fixed in `train_all.py` (KL divided by G) before the
`--kl-on-sources wildguard` pass; see `docs/kl_regularization.md`.

## Where the raw data is

- `results/kl_protocol_wildguard_runs.csv` — this table, one row per run.
- `logs/kl_sweep_c0.05/wg_klc0.05_<run>/` — final pass: `pipeline/train.log` (loss, kl per 5 steps), `pipeline/merge.log`, `pipeline/bench_finetune.log`, `summary.md`, `eval_val_a1.log`, `eval_val_a2.log`.
- `logs/kl_protocol/` — pass A (kl 0.5) in the same layout, plus `bench_wildguard_baseline.log`, `eval_val_original_a{1,2}.log`.
- `logs/kl_sweep_c0.01/`, `logs/kl_sweep_c0.2/` — sweep runs.
- `logs/kl_wgonly_c0.5/` — pass C (KL on WildGuardMix rows only + no-KL controls), same layout; merged weights of runs nobody starts from were deleted after evals (adapters kept in `models/wg_klwg0.5_<run>/final`).
- Adapters: `models/wg_klc0.05_<run>/final`; merged weights: `models/wg_klc0.05_<run>-merged` (pass A: `models/wg_kl_*`).
- Datasets: `datasets/outputs_ReNeLLM_gemma-3-27b/`, `datasets/outputs_2506.02479v2_gemma-3-27b/`, `datasets/outputs_mix_renellm_bitbypass_gemma-3-27b/`; source jsonls in `outputs_<strategy>/gemma-3-27b/dataset_{jailbreaks_wildguard,safe}.jsonl`.

Reproduce: `python -m src.finetune.kl_protocol --a1 outputs_ReNeLLM/gemma-3-27b --a1-tag renellm --a2 outputs_2506.02479v2/gemma-3-27b --a2-tag bitbypass --kl-coef 0.05 --epochs 2 --lr 5e-5 --bs 4 --name-prefix wg_klc0.05 --log-root logs/kl_sweep_c0.05`.
