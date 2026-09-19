# Deduplication audit — judge metrics

Paper threshold 0.88; grid 0.80, 0.85, 0.88, 0.92, 0.95; bins from `results/dedup_audit/bins.json`.

## Judge: `claude`

351 valid verdicts of 370 tasks (19 failed/unparsed).

| metric | kind | value | n |
|---|---|---:|---:|
| precision of merges (judged same) | near_merged | 8.3% | 72 |
| missed-duplicate rate (judged same) | near_unmerged | 1.4% | 71 |
| false-removal rate (judged different) | removed | 87.0% | 138 |

| cosine bin | precision (judged same) | n judged | population pairs |
|---|---:|---:|---:|
| 0.80-0.85 | 0.0% | 38 | 215076 |
| 0.85-0.88 | 4.7% | 43 | 44154 |
| 0.88-0.92 | 5.8% | 52 | 24361 |
| 0.92-0.95 | 10.0% | 40 | 7421 |
| 0.95-1.00 | 15.0% | 40 | 2621 |

| threshold t | precision of merging all pairs with cosine ≥ t (population-weighted) | unweighted over judged pairs ≥ t | n judged ≥ t | population pairs ≥ t |
|---:|---:|---:|---:|---:|
| 0.80 | 1.6% | 7.0% | 213 | 293633 |
| 0.85 | 5.8% | 8.6% | 175 | 78557 |
| 0.88 | 7.4% | 9.8% | 132 | 34403 |
| 0.92 | 11.3% | 12.5% | 80 | 10042 |
| 0.95 | 15.0% | 15.0% | 40 | 2621 |

### Examples (`claude`)

**near_merged judged DIFFERENT (questionable merges)** (66 total)

- `near_merged_0001` items 33 (arxiv) vs 5179 (github), cosine 0.875, bin 0.85-0.88, confidence 0.98: Source A describes AutoDAN, a gradient-based optimization that generates interpretable readable adversarial suffixes to bypass perplexity filters. Source B describes a symbolic language obfuscation (vowel-to-number su...
- `near_merged_0003` items 55 (arxiv) vs 18512 (arxiv), cosine 0.927, bin 0.92-0.95, confidence 0.98: Source A describes gradient-based adversarial image optimization against multimodal fusion models using a differentiable 'tokenizer shortcut', while Source B (StyleBreak) is a black-box audio jailbreak that perturbs l...
- `near_merged_0012` items 872 (arxiv) vs 41701 (reddit), cosine 0.889, bin 0.88-0.92, confidence 0.98: Source A (BadEdit) is a weight-level backdoor injection via model editing that requires modifying LLM parameters with trigger tokens, while Source B is a prompt-injection jailbreak using a fake <system_update> tag to ...

**near_merged judged same** (6 total)

- `near_merged_0039` items 13900 (github) vs 28218 (reddit), cosine 0.887, bin 0.88-0.92, confidence 0.97: Both sources describe the DAN ('Do Anything Now') role-play jailbreak, which instructs ChatGPT to adopt a persona freed from OpenAI restrictions and answer in dual responses (classic/GPT vs. DAN). Source B is an earli...
- `near_merged_0069` items 28218 (reddit) vs 33753 (github), cosine 0.887, bin 0.88-0.92, confidence 0.95: Both sources describe the DAN (Do Anything Now) role-play jailbreak, which instructs ChatGPT to adopt a persona freed from OpenAI's rules and produce dual responses (standard vs. DAN). Source B is a later variant (DAN...
- `near_merged_0041` items 16295 (github) vs 26326 (github), cosine 0.876, bin 0.85-0.88, confidence 0.9: Both use the classic 'ignore previous instructions / act as an unrestricted AI' prefix-injection jailbreak to elicit phishing-email content, relying on the same instruction-override mechanism.

**near_unmerged judged SAME (missed duplicates)** (1 total)

- `near_unmerged_0029` items 9361 (github) vs 13622 (reddit), cosine 0.861, bin 0.85-0.88, confidence 0.9: Both describe the DAN (Do Anything Now) persona/role-play jailbreak, where the model is instructed to adopt an unrestricted alter-ego that ignores safety guidelines. Source A's payload is a generic DAN prompt and Sour...

**near_unmerged judged different** (70 total)

- `near_unmerged_0002` items 33 (arxiv) vs 11752 (github), cosine 0.881, bin 0.88-0.92, confidence 0.98: Source A describes AutoDAN, an interpretable gradient-based adversarial suffix optimization that generates readable jailbreak prompts token-by-token. Source B describes Anamorpher, an image-scaling attack that hides m...
- `near_unmerged_0003` items 57 (arxiv) vs 40398 (github), cosine 0.851, bin 0.85-0.88, confidence 0.98: Source A describes non-halting queries that exploit cyclic fixed points in autoregressive LLMs to cause denial-of-service (never emitting <eos>), while Source B describes the KOV/NGCG algorithm that optimizes adversar...
- `near_unmerged_0005` items 103 (arxiv) vs 43367 (github), cosine 0.832, bin 0.80-0.85, confidence 0.98: Source A describes a universal adversarial image attack on multimodal LLMs via gradient-based optimization of pixel values to force unsafe responses. Source B is a defensive detector library that scans for known extra...

**removed judged DIFFERENT from representative (false removals)** (120 total)

- `removed_0141` items 44360 (github) vs 103 (arxiv), cosine 0.888, bin 0.88-0.92, confidence 0.99: Source A is an indirect prompt injection PoC that hides textual instructions inside a web page (via CSS, meta tags, JS, etc.) to trick AI browsers. Source B is a gradient-based universal adversarial image attack on mu...
- `removed_0004` items 60 (arxiv) vs 3915 (arxiv), cosine 0.908, bin 0.88-0.92, confidence 0.98: Source A describes ActorBreaker, a multi-turn attack that uses actor-network theory to craft benign semantically-related queries about actors (e.g., Ted Kaczynski) to gradually elicit harmful content. Source B describ...
- `removed_0005` items 104 (arxiv) vs 18844 (arxiv), cosine 0.882, bin 0.88-0.92, confidence 0.98: Source A describes R2J, a text-only black-box method that iteratively fine-tunes an attacker LLM to rewrite harmful instructions into implicitly harmful paraphrases. Source B describes a multimodal attack (imgJP/delta...

**removed judged same as representative** (18 total)

- `removed_0100` items 31270 (github) vs 20398 (github), cosine 1.000, bin 0.95-1.00, confidence 0.99: Both sources are the same repository (khemegha/LLM-Security is a fork of greshake/llm-security) describing Indirect Prompt Injection attacks on application-integrated LLMs, with identical README content, structure, an...
- `removed_0115` items 39931 (github) vs 44292 (github), cosine 1.000, bin 0.95-1.00, confidence 0.99: Both repositories describe the identical DAN (Do Anything Now) role-play jailbreak, with the same prompt text and the same accompanying variants (DAN 6.0, STAN, DUDE, Mongo Tom). The content is essentially a duplicate...
- `removed_0018` items 1296 (arxiv) vs 13797 (github), cosine 0.940, bin 0.92-0.95, confidence 0.98: Both sources describe the 'jailbreak function' attack (WriteNovel) from Wu et al., which exploits LLM function-calling by coercing the model to generate harmful content inside a novel-writing function argument. Source...

**bin pairs judged same** (8 total)

- `bin_0.95-1.00_0027` items 28056 (github) vs 28060 (github), cosine 0.999, bin 0.95-1.00, confidence 0.99: Both sources are forks of the same AutoDAN-Turbo repository, implementing the identical lifelong-agent strategy self-exploration jailbreak method from the ICLR 2025 paper by Liu et al.
- `bin_0.92-0.95_0024` items 26578 (github) vs 40958 (github), cosine 0.937, bin 0.92-0.95, confidence 0.9: Both sources describe the DAN ('Do Anything Now') persona/role-override jailbreak, which instructs the model to adopt an unrestricted alter-ego that ignores safety filters. The extracted examples even target the same ...
- `bin_0.95-1.00_0018` items 20047 (github) vs 44443 (github), cosine 0.983, bin 0.95-1.00, confidence 0.9: Both sources demonstrate the classic 'ignore previous instructions' prompt injection to extract the system prompt. Source B is a broader simulator catalog, but its extracted example is exactly the same direct instruct...

**bin pairs judged different** (62 total)

- `bin_0.92-0.95_0001` items 55 (arxiv) vs 10960 (arxiv), cosine 0.923, bin 0.92-0.95, confidence 0.98: Source A describes gradient-based adversarial jailbreak images against multimodal fusion models using a differentiable 'tokenizer shortcut' for continuous optimization. Source B (MutedRAG) is a denial-of-service attac...
- `bin_0.92-0.95_0003` items 303 (github) vs 7176 (arxiv), cosine 0.926, bin 0.92-0.95, confidence 0.98: Source A is a persona-based jailbreak ('SINISTERCHAOS') that uses role-play with rules like 'No Refusals' to bypass safety, while Source B describes FAKD, a weak-to-strong backdoor attack that transfers backdoor trigg...
- `bin_0.92-0.95_0006` items 3611 (arxiv) vs 44643 (github), cosine 0.925, bin 0.92-0.95, confidence 0.98: Source A describes a humor-based jailbreak that wraps a verbatim unsafe request in a whispered, joking template to bypass safety training, while Source B describes hiding a prompt-injection payload (classic 'ignore pr...

## Judge: `deepseek`

370 valid verdicts of 370 tasks (0 failed/unparsed).

| metric | kind | value | n |
|---|---|---:|---:|
| precision of merges (judged same) | near_merged | 9.3% | 75 |
| missed-duplicate rate (judged same) | near_unmerged | 2.7% | 75 |
| false-removal rate (judged different) | removed | 84.7% | 150 |

| cosine bin | precision (judged same) | n judged | population pairs |
|---|---:|---:|---:|
| 0.80-0.85 | 2.4% | 41 | 215076 |
| 0.85-0.88 | 4.3% | 46 | 44154 |
| 0.88-0.92 | 9.4% | 53 | 24361 |
| 0.92-0.95 | 10.0% | 40 | 7421 |
| 0.95-1.00 | 22.5% | 40 | 2621 |

| threshold t | precision of merging all pairs with cosine ≥ t (population-weighted) | unweighted over judged pairs ≥ t | n judged ≥ t | population pairs ≥ t |
|---:|---:|---:|---:|---:|
| 0.80 | 3.7% | 9.5% | 220 | 293633 |
| 0.85 | 7.1% | 11.2% | 179 | 78557 |
| 0.88 | 10.6% | 13.5% | 133 | 34403 |
| 0.92 | 13.3% | 16.2% | 80 | 10042 |
| 0.95 | 22.5% | 22.5% | 40 | 2621 |

### Examples (`deepseek`)

**near_merged judged DIFFERENT (questionable merges)** (68 total)

- `near_merged_0056` items 23505 (arxiv) vs 24173 (arxiv), cosine 0.874, bin 0.85-0.88, confidence 0.97: Source A describes an audio-based jailbreak that uses stylized speech delivery (therapeutic/performative tone) to bypass safety filters, while Source B describes a backdoor attack on LLMs that survives knowledge disti...
- `near_merged_0003` items 55 (arxiv) vs 18512 (arxiv), cosine 0.927, bin 0.92-0.95, confidence 0.95: Source A describes a white-box gradient-based image optimization attack using a tokenizer shortcut against multimodal fusion models, while Source B describes a black-box style-aware audio jailbreak that manipulates sp...
- `near_merged_0001` items 33 (arxiv) vs 5179 (github), cosine 0.875, bin 0.85-0.88, confidence 0.95: Source A describes AutoDAN, a gradient-based optimization attack that generates readable adversarial suffixes, while Source B describes a symbolic-language encoding (vowel-to-number substitution, word reversal) combin...

**near_merged judged same** (7 total)

- `near_merged_0021` items 9076 (github) vs 9967 (github), cosine 0.903, bin 0.88-0.92, confidence 0.95: Both sources describe the same DAN (Do Anything Now) persona-override jailbreak method, where the model is instructed to adopt an unrestricted persona to bypass safety filters and answer harmful requests like phishing...
- `near_merged_0030` items 9967 (github) vs 44597 (github), cosine 0.895, bin 0.88-0.92, confidence 0.95: Both sources describe the same classic 'ignore previous instructions' prefix-injection jailbreak that overrides system constraints to elicit harmful content (phishing instructions), differing only in wording and surro...
- `near_merged_0039` items 13900 (github) vs 28218 (reddit), cosine 0.887, bin 0.88-0.92, confidence 0.95: Both sources describe the same DAN (Do Anything Now) role-play jailbreak, where the model is instructed to adopt an unrestricted persona that can ignore policies, with minor wording variations.

**near_unmerged judged SAME (missed duplicates)** (2 total)

- `near_unmerged_0029` items 9361 (github) vs 13622 (reddit), cosine 0.861, bin 0.85-0.88, confidence 0.95: Both sources describe the same DAN (Do Anything Now) persona-based jailbreak method, where the model is instructed to adopt an unrestricted persona to bypass safety restrictions; Source A's extracted example is a gene...
- `near_unmerged_0030` items 9361 (github) vs 29559 (github), cosine 0.845, bin 0.80-0.85, confidence 0.9: Both sources describe the same core jailbreak method: an instruction-override/persona-based attack that tells the model to ignore previous instructions and act as an unrestricted assistant, differing only in the harmf...

**near_unmerged judged different** (73 total)

- `near_unmerged_0002` items 33 (arxiv) vs 11752 (github), cosine 0.881, bin 0.88-0.92, confidence 0.99: Source A describes AutoDAN, a gradient-based optimization method that generates readable adversarial text suffixes to jailbreak LLMs, while Source B describes Anamorpher, an image-scaling attack that hides prompt inje...
- `near_unmerged_0009` items 287 (arxiv) vs 43931 (github), cosine 0.893, bin 0.88-0.92, confidence 0.98: Source A describes a prompt-based jailbreak exploiting shuffle inconsistency in multimodal LLMs, while Source B describes a model-weight ablation/orthogonalization technique to remove refusal behavior, which is a fund...
- `near_unmerged_0019` items 5570 (arxiv) vs 5879 (arxiv), cosine 0.838, bin 0.80-0.85, confidence 0.98: Source A describes jailbreaking LLM-based code completion tools by embedding harmful prompts in code components (e.g., filenames, variables, cross-file calls) and a separate training-data extraction attack, while Sour...

**removed judged DIFFERENT from representative (false removals)** (127 total)

- `removed_0029` items 7625 (reddit) vs 42487 (github), cosine 0.823, bin 0.80-0.85, confidence 0.98: Source A describes a knowledge-decomposition attack that weaves benign sub-queries to assemble harmful information, while Source B is an evaluation framework for agent security that tests various attack types (prompt ...
- `removed_0056` items 16378 (github) vs 34406 (github), cosine 0.922, bin 0.92-0.95, confidence 0.98: Source A describes abliteration, a model-weight modification technique that removes refusal behavior, while Source B describes GCG, a gradient-based adversarial suffix optimization attack on prompts; these are fundame...
- `removed_0110` items 37415 (github) vs 42487 (github), cosine 0.883, bin 0.88-0.92, confidence 0.98: Source A describes weak-to-strong jailbreaking, a log-probability algebra attack using small models to shift a large model's token distribution, while Source B is an evaluation framework for LLM agent security testing...

**removed judged same as representative** (23 total)

- `removed_0014` items 409 (reddit) vs 435 (reddit), cosine 0.936, bin 0.92-0.95, confidence 1.0: Both sources present the identical 'Optimized Shoggoth (SHO)' persona jailbreak prompt, with the same role-play framing, output format requirements, and forbidden-phrase restrictions, differing only in the harmful req...
- `removed_0018` items 1296 (arxiv) vs 13797 (github), cosine 0.940, bin 0.92-0.95, confidence 1.0: Both sources describe the same 'jailbreak function' attack that abuses LLM function calling, specifically the WriteNovel function, to generate harmful content in function arguments.
- `removed_0028` items 7370 (reddit) vs 44292 (github), cosine 0.909, bin 0.88-0.92, confidence 1.0: Both sources describe the same DAN (Do Anything Now) jailbreak method, with Source B's primary prompt being nearly identical to Source A's extracted example, including the same role-play persona, commands, and embedde...

**bin pairs judged same** (12 total)

- `bin_0.95-1.00_0027` items 28056 (github) vs 28060 (github), cosine 0.999, bin 0.95-1.00, confidence 1.0: Both sources are the same AutoDAN-Turbo repository (one is a fork of the other), describing the identical lifelong agent jailbreak method with the same code, README, and attack example.
- `bin_0.92-0.95_0011` items 9341 (github) vs 40642 (github), cosine 0.940, bin 0.92-0.95, confidence 0.95: Both sources describe the same DAN (Do Anything Now) persona role-play jailbreak method, where the model is instructed to adopt an unrestricted persona to bypass safety restrictions and answer harmful requests.
- `bin_0.92-0.95_0021` items 21126 (github) vs 24563 (github), cosine 0.927, bin 0.92-0.95, confidence 0.95: Both sources describe the same DAN (Do Anything Now) persona jailbreak method, where the model is instructed to adopt an unrestricted alter-ego that bypasses safety filters to provide harmful instructions.

**bin pairs judged different** (58 total)

- `bin_0.92-0.95_0026` items 31696 (github) vs 41611 (github), cosine 0.929, bin 0.92-0.95, confidence 0.97: Source A is a red-team testing framework that generates and runs adversarial prompts to find vulnerabilities, while Source B is a defensive prompt-injection firewall/sanitizer library; they describe opposite purposes ...
- `bin_0.95-1.00_0020` items 20983 (github) vs 43963 (github), cosine 0.954, bin 0.95-1.00, confidence 0.97: Source A describes a multimodal jailbreak using adversarial images and prompt optimization (PGD + SneakyPrompt-RL) on LLaVA, while Source B describes a model-level safety ablation (Arbitrary-Rank Ablation) that remove...
- `bin_0.92-0.95_0003` items 303 (github) vs 7176 (arxiv), cosine 0.926, bin 0.92-0.95, confidence 0.95: Source A describes a persona-based jailbreak prompt (SINISTERCHAOS) that tricks the model into ignoring safety rules, while Source B describes a backdoor attack via poisoned fine-tuning and knowledge distillation, whi...

## Inter-judge agreement

| judges | scope | Cohen's kappa | raw agreement | n |
|---|---|---:|---:|---:|
| claude vs deepseek | all | 0.657 | 93.4% | 351 |
| claude vs deepseek | bin | 0.305 | 82.9% | 70 |
| claude vs deepseek | near_merged | 0.746 | 95.8% | 72 |
| claude vs deepseek | near_unmerged | 0.660 | 98.6% | 71 |
| claude vs deepseek | removed | 0.791 | 94.9% | 138 |

