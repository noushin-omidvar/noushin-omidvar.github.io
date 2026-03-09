# ============================================================
# Figure 2: Model performance comparison across split methods
#
# Purpose:
#   Train an XGBoost regressor under random, scaffold, and
#   cluster splits and compare the resulting test RMSE to
#   show how the evaluation protocol affects reported results.
#
# Output:
#   fig2_performance.png  — bar chart of test RMSE per split
#
# Requirements:
#   rdkit, xgboost, scikit-learn, numpy, pandas, matplotlib
#
# Usage:
#   Supply a DataFrame `df` with columns:
#       smiles         — SMILES strings
#       y              — target property (numeric)
#       random_split   — "train" / "test"
#       scaffold_split — "train" / "test"
#       cluster_split  — "train" / "test"
#   and a pre-computed fingerprint matrix X aligned with df.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor


# ---- Evaluation helper ----

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


# ---- Collect results ----

results = {
    "Random":   evaluate_split("random_split"),
    "Scaffold": evaluate_split("scaffold_split"),
    "Cluster":  evaluate_split("cluster_split"),
}

print("Test RMSE by split strategy:")
for name, rmse in results.items():
    print(f"  {name:<10} {rmse:.4f}")


# ---- Bar chart ----

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
