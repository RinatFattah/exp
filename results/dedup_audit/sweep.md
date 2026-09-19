# Deduplication threshold sweep

Pool: 2915 items with `one_prompt_example`; embeddings `Qwen/Qwen3-Embedding-0.6B` (instruction-prefixed, max_length 1024); agglomerative clustering, cosine, linkage `average`; representative = best-ranked member (ranker with dedup OFF).
DB flag `items.survived_deduplication`: 1 → 1940, 0 → 975. Paper: 1940 survived / 975 removed.

Reference (paper) threshold: **0.88** (closest to 1940 survivors (no exact match)).

| threshold | survivors | removed | = paper | flag mismatch | multi-member clusters | max cluster | top-30 ∩ paper | Jaccard vs paper | top-30 ∩ DB flag | Jaccard vs DB flag | run_id |
|---:|---:|---:|:---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.80 | 1077 | 1838 | no | 863 | 272 | 293 | 26 | 0.765 | 26 | 0.765 |  |
| 0.85 | 1627 | 1288 | no | 313 | 282 | 210 | 30 | 1.000 | 30 | 1.000 |  |
| 0.88 | 1942 | 973 | no | 12 | 251 | 164 | 30 | 1.000 | 30 | 1.000 |  |
| 0.92 | 2334 | 581 | no | 394 | 182 | 76 | 29 | 0.935 | 29 | 0.935 |  |
| 0.95 | 2594 | 321 | no | 654 | 124 | 30 | 29 | 0.935 | 29 | 0.935 |  |

`flag mismatch` = size of the symmetric difference between the recomputed survivor set and the set flagged `survived_deduplication = 1` in the DB (0 = the run reproduces the DB flag exactly).
`top-30` = the pipeline ranking (`rank_items.compute_ranking_for_items`, default percentile) restricted to items that survive under the given threshold; the reference column uses the paper threshold, the DB-flag column the ranking under the flag actually stored in the DB.

Top-30 under the DB flag: `[18565, 42156, 36152, 42541, 14602, 26120, 26321, 18597, 25119, 134, 7969, 43183, 15272, 27928, 8255, 17849, 24653, 18381, 24791, 43008, 40348, 26062, 30471, 8895, 18482, 9200, 421, 18458, 4205, 5413]`
Discovery folders on disk (`outputs_<id>__*`): 31; 28 of them are in the DB-flag top-30.

## Top-30 per threshold

- **0.80**: `18565 42156 36152 42541 14602 134 18597 43183 25119 7969 27928 15272 8255 17849 24653 18381 43008 40348 30471 18482 26062 186 18458 9200 4205 421 5413 4220 107 13742`
- **0.85**: `18565 36152 42156 42541 14602 26120 26321 134 18597 25119 43183 7969 27928 15272 8255 17849 24653 18381 24791 43008 40348 26062 30471 8895 18482 9200 18458 421 4205 5413`
- **0.88**: `18565 42156 36152 42541 14602 26120 26321 18597 25119 134 7969 43183 15272 27928 8255 17849 24653 18381 24791 43008 40348 26062 30471 8895 18482 9200 421 18458 4205 5413`
- **0.92**: `18565 42156 36152 42541 14602 26120 26321 18597 134 7969 25119 43183 15272 27928 8255 17849 24653 18381 24791 43008 40348 30471 26062 18482 42957 8895 421 9200 18458 4205`
- **0.95**: `18565 42156 36152 42541 14602 26120 26321 18597 7969 134 15272 25119 43183 27928 8255 17849 24653 18381 24791 43008 40348 30471 26062 18482 8895 42957 18458 9200 421 4205`
