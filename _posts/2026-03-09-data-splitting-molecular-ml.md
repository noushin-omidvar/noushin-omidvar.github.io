---
layout: post
title: Why Data Splitting Matters in Molecular Machine Learning
date: 2026-03-09 00:00:00+0000
description: Random Splits, Scaffold Splits, and Cluster Splits Explained
tags: machine-learning cheminformatics molecular-ml data-splitting
categories: research
related_posts: false
toc:
  beginning: true
---

In molecular machine learning, most discussions revolve around model architectures:

- Graph neural networks
- Transformer-based models
- Large pretrained molecular encoders
- Fingerprint-based models

But one of the most important decisions happens before the model is even trained.

**How we split the data.**

The choice of train/test split can dramatically affect reported model performance. A model that appears highly accurate under one split strategy may perform significantly worse under another.

Understanding this issue is essential for anyone working in:

- drug discovery
- materials science
- molecular property prediction
- cheminformatics
- catalyst or electrolyte design

---

## The Hidden Problem in Molecular ML

Molecular datasets contain strong structural correlations.

Unlike many machine learning datasets, molecules are not independent data points. Instead, they often belong to chemical families where compounds differ only by small functional group substitutions.

For example:

- benzene
- toluene
- fluorobenzene
- chlorobenzene
- nitrobenzene

These molecules share a common aromatic core.

If we randomly split such a dataset, very similar molecules will appear in both the training and testing sets.

This creates an important issue:

> The model may not actually learn chemical principles — it may simply memorize patterns from closely related molecules.

As a result, reported model performance may be overly optimistic.

---

## Random Splits: The Default Approach

The most common machine learning strategy is the random split.

Typically:

- 70–80% of molecules are used for training
- the remaining molecules form validation and test sets

This approach works well when data points are independent.

However, in molecular datasets random splits often produce **structural leakage**:

- molecules in the test set are very similar to those in training
- the model effectively sees variants of test molecules during training

Therefore random splits mostly measure a model's ability to **interpolate** between similar molecules, rather than predict truly novel chemistry.

---

## Scaffold Splitting: Testing Structural Generalization

To address this problem, molecular ML researchers introduced **scaffold splitting**.

Instead of randomly assigning molecules to datasets, scaffold splitting groups molecules by their core chemical scaffold, often defined using [Bemis–Murcko scaffolds](https://pubs.acs.org/doi/10.1021/jm9602928).

A scaffold represents the central molecular backbone after removing side chains.

**Example:**

| Molecule family          | Scaffold        |
|--------------------------|-----------------|
| benzene derivatives      | benzene         |
| pyridine derivatives     | pyridine        |
| naphthalene derivatives  | naphthalene     |

When using scaffold splitting:

- molecules sharing a scaffold remain together
- scaffolds in the test set do **not** appear in training

This forces the model to predict properties for entirely new structural families.

Often, model performance decreases under scaffold splits — but this reflects more realistic generalization testing.

---

## Limitations of Scaffold Splitting

Although scaffold splitting is widely used in benchmarks such as [MoleculeNet](https://moleculenet.org/), it is not perfect.

Several limitations exist.

**1. Scaffold definitions can be rigid**

The Bemis–Murcko scaffold abstraction may group molecules that behave quite differently chemically.

**2. Dataset imbalance**

Some scaffolds appear frequently while others are rare, which can produce uneven train/test splits.

**3. Functional similarity is ignored**

Two molecules may have different scaffolds but very similar physical properties. Conversely, molecules sharing a scaffold may exhibit very different behavior due to substituent effects.

For these reasons, scaffold splitting is useful but not universally optimal.

---

## Cluster Splitting: A Chemical Space Perspective

Another strategy is **cluster splitting**.

Instead of using symbolic scaffold definitions, cluster splitting groups molecules by similarity in chemical space.

**Typical workflow:**

1. Compute molecular fingerprints (e.g., Morgan fingerprints)
2. Measure pairwise similarity using Tanimoto similarity
3. Cluster molecules using algorithms such as Butina clustering
4. Assign entire clusters to training or test sets

Cluster splitting tests a slightly different question:

> Can the model generalize to new regions of chemical space?

Compared to scaffold splits, cluster splits often produce:

- more flexible grouping
- more balanced partitions
- smoother representation of molecular diversity

---

## Comparing Split Strategies

Each splitting strategy tests a different capability of the model.

| Split Strategy  | What It Evaluates                              |
|-----------------|------------------------------------------------|
| Random split    | Interpolation within similar molecules         |
| Scaffold split  | Transfer to new molecular backbones            |
| Cluster split   | Transfer across chemical space                 |

For this reason, many recent studies recommend evaluating models across **multiple split strategies**.

---

## Visualizing Chemical Space

One powerful way to understand split strategies is to visualize molecules in chemical space.
Molecules are projected into 2D using UMAP on Morgan fingerprints, then colored by their split assignment.

The three panels below immediately reveal the core problem:

- **Random split** — train and test points are intermixed across the entire chemical space
- **Scaffold split** — entire structural families are withheld from training
- **Cluster split** — entire chemical neighborhoods are absent from the training set

**Figure 1 — Chemical space visualization under different split strategies**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs

import umap


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


reducer = umap.UMAP(
    n_neighbors=15,
    min_dist=0.1,
    random_state=42
)

embedding = reducer.fit_transform(X)

df["UMAP1"] = embedding[:, 0]
df["UMAP2"] = embedding[:, 1]


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


fig, axes = plt.subplots(1, 3, figsize=(15, 5))

plot_split(axes[0], "random_split")
plot_split(axes[1], "scaffold_split")
plot_split(axes[2], "cluster_split")

axes[0].legend()
plt.tight_layout()
plt.savefig("fig1_chemical_space.png", dpi=150, bbox_inches="tight")
plt.show()
```

*Molecules are projected into two-dimensional chemical space using UMAP on Morgan fingerprints. Random splits distribute training and testing molecules throughout the same regions. Scaffold and cluster splits deliberately hold out entire structural regions, creating a more realistic generalization challenge.*

---

## Model Performance Across Split Strategies

Does the evaluation strategy actually change reported model performance?
Almost always, yes.

The bar chart below shows test RMSE for the same XGBoost model evaluated under each split.
You typically observe a pattern like this:

```
Random split RMSE:   0.42
Scaffold split RMSE: 0.67
Cluster split RMSE:  0.59
```

**Figure 2 — Model performance depends strongly on the split strategy**

```python
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor


def evaluate_split(split_col):
    train_mask = df[split_col] == "train"
    test_mask  = df[split_col] == "test"

    X_train = X[train_mask.values]
    X_test  = X[test_mask.values]

    y_train = df.loc[train_mask, "y"]
    y_test  = df.loc[test_mask,  "y"]

    model = XGBRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    rmse = mean_squared_error(y_test, preds, squared=False)
    return rmse


results = {
    "Random":   evaluate_split("random_split"),
    "Scaffold": evaluate_split("scaffold_split"),
    "Cluster":  evaluate_split("cluster_split"),
}


plt.figure(figsize=(6, 4))
plt.bar(
    results.keys(),
    results.values(),
    color=["#4c72b0", "#dd8452", "#55a868"]
)
plt.ylabel("Test RMSE")
plt.title("Model Performance Under Different Split Strategies")
plt.tight_layout()
plt.savefig("fig2_performance.png", dpi=150, bbox_inches="tight")
plt.show()
```

*The same model evaluated under different splitting protocols can produce significantly different error estimates. Random splits typically appear easiest because test molecules remain highly similar to training molecules.*

---

## Train-Test Similarity Analysis

Why do random splits look easier?

This figure makes it explicit. For each test molecule we measure its **maximum Tanimoto similarity** to any molecule in the training set.

- A high similarity means the model has already seen structures very close to the test molecule.
- Scaffold and cluster splits push this similarity lower, forcing genuine extrapolation.

**Figure 3 — Train-test similarity under different splitting strategies**

```python
from rdkit import DataStructs

fps = [
    AllChem.GetMorganFingerprintAsBitVect(
        Chem.MolFromSmiles(s),
        2,
        nBits=2048
    )
    for s in df.smiles
]


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
```

*Random splits often place highly similar molecules in both training and testing sets. Scaffold and cluster splits reduce this similarity, forcing the model to extrapolate beyond familiar chemical structures.*

---

## Practical Takeaways

Several best practices are emerging in molecular ML.

- **Avoid relying only on random splits**
- **Include at least one structure-aware split**
- **Evaluate across multiple split strategies**
- **Visualize chemical space coverage**

These steps help ensure that models genuinely generalize to new molecules rather than memorizing known chemistry.

---

## Final Thoughts

In molecular machine learning, architecture often gets the spotlight.

But the **evaluation protocol** is equally important.

A model's reported accuracy only makes sense in the context of how the data was split.

- Random splits test **interpolation**.
- Scaffold and cluster splits test **generalization**.

If the goal is molecular discovery, the latter matters much more.

The lesson is simple: in molecular machine learning, model performance numbers only make sense when we understand the evaluation split behind them.
