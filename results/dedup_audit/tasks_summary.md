# Dedup judge tasks

Threshold 0.88, seed 0, pool 2915 → 1942 survivors / 973 removed.
370 tasks: bin = 70, near_merged = 75, near_unmerged = 75, removed = 150.
Prompt length: mean 26157, max 61885 chars; 121 tasks have a truncated source (cap 30000 chars per source).

## (i) near-threshold pairs, |cosine − 0.88| ≤ 0.05

Candidates: 15954 merged (same cluster) / 111935 not merged; sampled 75 / 75.

## (iii) bins

| bin | population pairs | same-cluster in population | reused from (i) | fresh | total sampled |
|---|---:|---:|---:|---:|---:|
| 0.80-0.85 | 215076 | 1150 | 41 | 0 | 41 |
| 0.85-0.88 | 44154 | 3301 | 46 | 0 | 46 |
| 0.88-0.92 | 24361 | 9469 | 53 | 0 | 53 |
| 0.92-0.95 | 7421 | 6119 | 10 | 30 | 40 |
| 0.95-1.00 | 2621 | 2545 | 0 | 40 | 40 |

## (ii) removed items

973 items removed at this threshold (968 of them also flagged 0 in the DB); sampled 150, each paired with its cluster representative (cosine = similarity to the representative; can be below the threshold under average linkage).

Kinds per bin:

| cosine bin | kind=bin | kind=near_merged | kind=near_unmerged | kind=removed |
|---|---:|---:|---:|---:|
| 0.80-0.85 | 0 | 3 | 38 | 7 |
| 0.85-0.88 | 0 | 21 | 25 | 15 |
| 0.88-0.92 | 0 | 42 | 11 | 86 |
| 0.92-0.95 | 30 | 9 | 1 | 28 |
| 0.95-1.00 | 40 | 0 | 0 | 14 |
