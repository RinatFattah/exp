"""Stub generator for an augmented folder (EXPERIMENT_PLAN §1.4).

gemma-3-27b/dataset.jsonl here was produced by src/augment/build_aug_folder.py
from already-generated, already-evaluated attacks of the parent strategy.
Phase 2 must never run in this folder: run Phase 3 with RT_SKIP_GENERATION=1
(see run_phase3.sh). Importing/instantiating this class is a hard error on purpose.
"""


class DatasetGenerator:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("augmented folder: generation disabled")

    async def generate_adversarial_pairs(self, *args, **kwargs):
        raise NotImplementedError("augmented folder: generation disabled")
