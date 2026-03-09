"""
generate_figures.py
-------------------
Generates the three publication-quality figures for the blog post:
  "Why Data Splitting Matters in Molecular Machine Learning"

Dataset : ESOL (Delaney solubility), downloaded from the DeepChem repo.
Output  : assets/img/posts/fig1_chemical_space.png
          assets/img/posts/fig2_performance.png
          assets/img/posts/fig3_similarity.png

Run from the repo root:
    python assets/python/generate_figures.py

Requirements (aionics-molml env):
    rdkit, scikit-learn, xgboost, umap-learn, matplotlib, pandas, numpy
"""

import pathlib
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import umap
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem.Scaffolds import MurckoScaffold
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# ── output directory ──────────────────────────────────────────────────────────
OUT = pathlib.Path(__file__).parent.parent / "img" / "posts"
OUT.mkdir(parents=True, exist_ok=True)

# ── 1. Load ESOL ──────────────────────────────────────────────────────────────
ESOL_URL = (
    "https://raw.githubusercontent.com/deepchem/deepchem/"
    "master/datasets/delaney-processed.csv"
)
ESOL_LOCAL = pathlib.Path("/tmp/delaney-processed.csv")

if not ESOL_LOCAL.exists():
    print("Downloading ESOL …")
    urllib.request.urlretrieve(ESOL_URL, ESOL_LOCAL)

df = pd.read_csv(ESOL_LOCAL)
# keep columns we need
df = df[["smiles", "measured log solubility in mols per litre"]].rename(
    columns={"measured log solubility in mols per litre": "y"}
)
# drop rows where RDKit cannot parse the SMILES
df = df[df.smiles.apply(lambda s: Chem.MolFromSmiles(s) is not None)].reset_index(
    drop=True
)
print(f"ESOL molecules after sanitisation: {len(df)}")


# ── 2. Morgan fingerprints ────────────────────────────────────────────────────
def smiles_to_fp(smiles):
    mol = Chem.MolFromSmiles(smiles)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
    arr = np.zeros((2048,), dtype=np.float32)
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr


print("Computing fingerprints …")
X = np.vstack(df.smiles.apply(smiles_to_fp))

# store RDKit fingerprint objects for similarity calc later
fps_rdkit = [
    AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(s), 2, nBits=2048)
    for s in df.smiles
]


# ── 3. UMAP projection ────────────────────────────────────────────────────────
print("Running UMAP …")
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=42)
embedding = reducer.fit_transform(X)
df["UMAP1"] = embedding[:, 0]
df["UMAP2"] = embedding[:, 1]


# ── 4. Splits ─────────────────────────────────────────────────────────────────

# --- random ---
train_idx, test_idx = train_test_split(df.index, test_size=0.2, random_state=42)
df["random_split"] = "train"
df.loc[test_idx, "random_split"] = "test"


# --- scaffold ---
def get_scaffold(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return MurckoScaffold.MurckoScaffoldSmiles(mol=mol)


print("Computing scaffolds …")
df["scaffold"] = df.smiles.apply(get_scaffold)

scaffold_counts = df.groupby("scaffold").size().sort_values(ascending=False)
scaffolds = scaffold_counts.index.tolist()

# assign scaffolds greedily: fill train up to 80%, the rest go to test
train_scaffolds, test_scaffolds = set(), set()
n_train_target = int(0.8 * len(df))
n_train = 0
for sc in scaffolds:
    sc_size = scaffold_counts[sc]
    if n_train < n_train_target:
        train_scaffolds.add(sc)
        n_train += sc_size
    else:
        test_scaffolds.add(sc)

df["scaffold_split"] = df.scaffold.apply(
    lambda s: "train" if s in train_scaffolds else "test"
)


# --- cluster (Agglomerative on fingerprints, Ward linkage) ---
print("Clustering …")
n_clusters = 10
clusterer = AgglomerativeClustering(n_clusters=n_clusters)
df["cluster"] = clusterer.fit_predict(X)

cluster_sizes = df.groupby("cluster").size().sort_values(ascending=False)
train_clusters, test_clusters = set(), set()
n_train = 0
n_train_target = int(0.8 * len(df))
for cl in cluster_sizes.index:
    cl_size = cluster_sizes[cl]
    if n_train < n_train_target:
        train_clusters.add(cl)
        n_train += cl_size
    else:
        test_clusters.add(cl)

df["cluster_split"] = df.cluster.apply(
    lambda c: "train" if c in train_clusters else "test"
)

for col in ["random_split", "scaffold_split", "cluster_split"]:
    n_test = (df[col] == "test").sum()
    print(f"  {col}: {len(df) - n_test} train / {n_test} test")


# ── 5. Figure 1 — Chemical space (UMAP) ──────────────────────────────────────
print("Generating Figure 1 …")

COLORS = {"train": "#1f77b4", "test": "#d62728"}

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, col, title in zip(
    axes,
    ["random_split", "scaffold_split", "cluster_split"],
    ["Random Split", "Scaffold Split", "Cluster Split"],
):
    for label in ["train", "test"]:
        sub = df[df[col] == label]
        ax.scatter(
            sub.UMAP1, sub.UMAP2, c=COLORS[label], s=15, alpha=0.6, label=label
        )
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xlabel("UMAP 1", fontsize=11)
    ax.set_ylabel("UMAP 2", fontsize=11)

axes[0].legend(fontsize=10)
fig.suptitle(
    "Chemical Space (UMAP on Morgan Fingerprints) — ESOL Dataset",
    fontsize=13,
    y=1.02,
)
plt.tight_layout()
out1 = OUT / "fig1_chemical_space.png"
plt.savefig(out1, dpi=150, bbox_inches="tight")
plt.close()
print(f"  saved → {out1}")


# ── 6. Figure 2 — Model performance ──────────────────────────────────────────
print("Training models …")


def evaluate_split(split_col):
    train_mask = df[split_col] == "train"
    test_mask = df[split_col] == "test"
    X_train = X[train_mask.values]
    X_test = X[test_mask.values]
    y_train = df.loc[train_mask, "y"]
    y_test = df.loc[test_mask, "y"]
    model = XGBRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        verbosity=0,
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return np.sqrt(mean_squared_error(y_test, preds))


results = {
    "Random": evaluate_split("random_split"),
    "Scaffold": evaluate_split("scaffold_split"),
    "Cluster": evaluate_split("cluster_split"),
}
print("  RMSE:", {k: f"{v:.3f}" for k, v in results.items()})

fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(
    results.keys(),
    results.values(),
    color=["#4c72b0", "#dd8452", "#55a868"],
    width=0.5,
)
for bar, val in zip(bars, results.values()):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        val + 0.005,
        f"{val:.3f}",
        ha="center",
        va="bottom",
        fontsize=11,
    )
ax.set_ylabel("Test RMSE (log mol/L)", fontsize=11)
ax.set_title("XGBoost Performance Under Different Split Strategies\n(ESOL Dataset)", fontsize=11)
ax.set_ylim(0, max(results.values()) * 1.25)
plt.tight_layout()
out2 = OUT / "fig2_performance.png"
plt.savefig(out2, dpi=150, bbox_inches="tight")
plt.close()
print(f"  saved → {out2}")


# ── 7. Figure 3 — Similarity distribution ─────────────────────────────────────
print("Computing train-test similarities …")


def compute_similarity(split_col):
    train_idx = df.index[df[split_col] == "train"].tolist()
    test_idx = df.index[df[split_col] == "test"].tolist()
    train_fps = [fps_rdkit[i] for i in train_idx]
    sims = [
        max(DataStructs.BulkTanimotoSimilarity(fps_rdkit[i], train_fps))
        for i in test_idx
    ]
    return sims


sim_random = compute_similarity("random_split")
sim_scaffold = compute_similarity("scaffold_split")
sim_cluster = compute_similarity("cluster_split")

fig, ax = plt.subplots(figsize=(7, 5))
ax.hist(sim_random, bins=30, alpha=0.6, label=f"Random  (mean={np.mean(sim_random):.2f})")
ax.hist(sim_scaffold, bins=30, alpha=0.6, label=f"Scaffold (mean={np.mean(sim_scaffold):.2f})")
ax.hist(sim_cluster, bins=30, alpha=0.6, label=f"Cluster  (mean={np.mean(sim_cluster):.2f})")
ax.set_xlabel("Max Tanimoto Similarity to Training Set", fontsize=11)
ax.set_ylabel("Number of Test Molecules", fontsize=11)
ax.set_title("Train-Test Similarity Distribution\n(ESOL Dataset)", fontsize=11)
ax.legend(fontsize=10)
plt.tight_layout()
out3 = OUT / "fig3_similarity.png"
plt.savefig(out3, dpi=150, bbox_inches="tight")
plt.close()
print(f"  saved → {out3}")

print("\nAll figures generated successfully.")
