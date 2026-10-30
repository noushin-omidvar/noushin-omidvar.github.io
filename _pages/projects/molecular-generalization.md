---
layout: portfolio_page
published: false
permalink: /projects/molecular-generalization/
title: Testing whether molecular models actually generalize
kicker: molecular ml · benchmarking
description: Chemistry-aware validation splits and a fair comparison between classical descriptor baselines and pretrained molecular embeddings.
---

<div class="case-study-shell">

  <div class="case-summary">
    <div><span class="label">Question</span><p>Which model still works when the test molecules are structurally unfamiliar?</p></div>
    <div><span class="label">Approach</span><p>Similarity-based train/test splits, comparing 2D descriptors + XGBoost against pretrained molecular embeddings.</p></div>
    <div><span class="label">Result</span><p>On critical temperature, the descriptor baseline outperformed the pretrained embeddings.</p></div>
    <div><span class="label">My role</span><p>Benchmark design, split policy, modeling, and analysis.</p></div>
  </div>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/orc-similarity-split.png' | relative_url }}" alt="Structurally similar molecules are grouped and kept in the same cross-validation fold">
    <p class="figure-caption">Similar molecules are grouped and kept in the same fold, so the test set is structurally unfamiliar to the model.</p>
  </div>

  <h2>Why the split matters</h2>
  <p>With a random split, test molecules usually have close analogues in the training set, so scores mostly measure interpolation. I grouped molecules by structural similarity and kept each group within a single fold. The benchmark then asks a harder, more realistic question: how well does the model predict chemistry it has not seen?</p>

  <h2>Result</h2>
  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/molecular-generalization-benchmark.svg' | relative_url }}" alt="Benchmark comparison: 2D descriptors with XGBoost outperform pretrained embeddings under the similarity-aware split">
    <p class="figure-caption">Under the similarity-aware split, the descriptor-based model outperformed the pretrained-embedding baseline on critical temperature.</p>
  </div>
  <!-- FILL IN (this is the number reviewers look for):
  <p>Descriptors + XGBoost reached [metric, e.g. MAE] = __ K versus __ K for [embedding model name]. Moving from a random to a similarity split increased error by __% for descriptors and __% for embeddings (mean ± std over folds).</p>
  -->

  <h2>Limitations</h2>
  <ul>
    <li>One property (critical temperature); the ranking of model families may differ for other properties.</li>
    <li>How hard the test is depends on the similarity threshold used to form the groups.</li>
  </ul>

  <h2>Takeaway</h2>
  <p>A more sophisticated model does not guarantee better generalization. The split policy decides what a benchmark actually measures.</p>

  <p><a class="text-button" href="{{ '/blog/2026/data-splitting-molecular-ml/' | relative_url }}">Read the related note on molecular data splitting</a></p>
</div>
