---
layout: portfolio_page
permalink: /projects/molecular-generalization/
title: Testing whether molecular models actually generalize
kicker: molecular ml · benchmarking
description: A case study in representation, chemistry-aware validation, and honest comparison between classical baselines and pretrained molecular embeddings.
---

<div class="case-study-shell">
  <p class="lead">A central question in molecular ML is not simply <strong>which model scores best on a benchmark</strong>, but <strong>which model actually generalizes when the chemistry shifts</strong>.</p>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/molecular-generalization-overview.svg' | relative_url }}" alt="Workflow showing molecules, similarity graph, chemistry-aware split, and comparison between descriptor baseline and pretrained embeddings">
    <p class="figure-caption">Figure 1. The benchmark was designed around a chemistry-aware notion of generalization rather than a random split.</p>
  </div>

  <h2>The scientific problem</h2>
  <p>Molecular ML results can look strong when train and test molecules are highly similar. I wanted to build a more realistic benchmark that asked whether a model could extrapolate to structurally less familiar compounds. That required thinking carefully about the split policy, not only the model family.</p>

  <h2>Approach</h2>
  <p>I used similarity-based grouping to define train/test partitions, then compared classical descriptor-based models against pretrained molecular embeddings. The benchmark emphasized reproducibility and fair comparison rather than chasing a single headline number.</p>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/molecular-generalization-benchmark.svg' | relative_url }}" alt="Benchmark comparison chart showing 2D descriptors plus XGBoost outperforming pretrained embeddings under the selected split">
    <p class="figure-caption">Figure 2. Under the similarity-aware evaluation used here, a descriptor-based XGBoost model outperformed a pretrained-embedding baseline on the critical-temperature benchmark.</p>
  </div>

  <h2>Key result</h2>
  <p>One of the clearest outcomes was conceptual rather than purely numerical: <strong>model sophistication is not the same as robust generalization</strong>. In this benchmark, the classical descriptor baseline remained stronger under the selected test of structural novelty.</p>

  <h2>Why this matters</h2>
  <p>This work reinforced an idea that cuts across many scientific ML settings: evaluation design determines what a benchmark really measures. If the question is generalization under chemical distribution shift, then the split policy must reflect that question.</p>

  <p><a class="text-button" href="{{ '/blog/2026/data-splitting-molecular-ml/' | relative_url }}">Read the related note on molecular data splitting</a></p>
</div>
