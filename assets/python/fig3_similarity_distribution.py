# ============================================================
# Figure 3: Train-test similarity distribution analysis
#
# Purpose:
#   For each test molecule, compute its maximum Tanimoto
#   similarity to any molecule in the training set.
#   High similarity implies the model has already seen
#   closely related structures, explaining why random splits
#   tend to yield overly optimistic performance estimates.
#
# Output:
#   fig3_similarity.png  — overlapping histograms of
#   max train-test Tanimoto similarity per split strategy
#
# Requirements:
#   rdkit, numpy, pandas, matplotlib
#
# Usage:
#   Supply a DataFrame `df` with columns:
#       smiles         — SMILES strings
#       random_split   — "train" / "test"
#       scaffold_split — "train" / "test"
#       cluster_split  — "train" / "test"
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs


# ---- Pre-compute fingerprints ----

fps = [
    AllChem.GetMorganFingerprintAsBitVect(
        Chem.MolFromSmiles(s),
        2,
        nBits=2048
    )
    for s in df.smiles
]


# ---- Similarity computation ----

def compute_similarity(split_col):
    train_idx = df.index[df[split_col] == "train"]
    test_idx  = df.index[df[split_col] == "test"]

    train_fps = [fps[i] for i in train_idx]

    sims = []
    for i in test_idx:
        test_fp = fps[i]
        sim = max(
            DataStructs.BulkTanimotoSimilarity(test_fp, train_fps)
        )
        sims.append(sim)

    return sims


sim_random   = compute_similarity("random_split")
sim_scaffold = compute_similarity("scaffold_split")
sim_cluster  = compute_similarity("cluster_split")


# ---- Histogram ----

plt.figure(figsize=(7, 5))
plt.hist(sim_random,   bins=30, alpha=0.6, label="Random")
plt.hist(sim_scaffold, bins=30, alpha=0.6, label="Scaffold")
plt.hist(sim_cluster,  bins=30, alpha=0.6, label="Cluster")
plt.xlabel("Max Train-Test Tanimoto Similarity")
plt.ylabel("Count")
plt.title("Similarity Between Test Molecules and Training Set")
plt.legend()
plt.tight_layout()
plt.savefig("fig3_similarity.png", dpi=150, bbox_inches="tight")
plt.show()
