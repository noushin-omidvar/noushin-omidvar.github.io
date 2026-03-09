# ============================================================
# Figure 1: Chemical space visualization using UMAP
#
# Purpose:
#   Project molecular fingerprints into 2D space to visualize
#   how different split strategies distribute molecules.
#
# Output:
#   fig1_chemical_space.png  — 3-panel plot comparing
#   random, scaffold, and cluster splits.
#
# Requirements:
#   rdkit, umap-learn, numpy, pandas, matplotlib
#
# Usage:
#   Supply a DataFrame `df` with columns:
#       smiles        — SMILES strings
#       random_split  — "train" / "test"
#       scaffold_split — "train" / "test"
#       cluster_split  — "train" / "test"
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs

import umap


# ---- Fingerprint conversion ----

def smiles_to_fp(smiles):
    mol = Chem.MolFromSmiles(smiles)
    fp = AllChem.GetMorganFingerprintAsBitVect(
        mol,
        radius=2,
        nBits=2048
    )
    arr = np.zeros((2048,))
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr


X = np.vstack(df.smiles.apply(smiles_to_fp))


# ---- UMAP projection ----

reducer = umap.UMAP(
    n_neighbors=15,
    min_dist=0.1,
    random_state=42
)

embedding = reducer.fit_transform(X)

df["UMAP1"] = embedding[:, 0]
df["UMAP2"] = embedding[:, 1]


# ---- Plotting helper ----

def plot_split(ax, split_col):
    for label, color in zip(
        ["train", "test"],
        ["#1f77b4", "#d62728"]
    ):
        subset = df[df[split_col] == label]
        ax.scatter(
            subset.UMAP1,
            subset.UMAP2,
            label=label,
            s=20,
            alpha=0.7,
            color=color
        )
    ax.set_title(split_col.replace("_", " ").title())
    ax.set_xlabel("UMAP1")
    ax.set_ylabel("UMAP2")


# ---- 3-panel figure ----

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

plot_split(axes[0], "random_split")
plot_split(axes[1], "scaffold_split")
plot_split(axes[2], "cluster_split")

axes[0].legend()
plt.tight_layout()
plt.savefig("fig1_chemical_space.png", dpi=150, bbox_inches="tight")
plt.show()
