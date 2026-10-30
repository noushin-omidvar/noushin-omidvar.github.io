---
layout: portfolio_page
permalink: /projects/electrolyte-ranking/
title: Learning to rank electrolyte formulations
kicker: industry case study · battery r&d
description: A scientific ML workflow for moving from component chemistry to formulation-level ranking and experimental prioritization.
---

<div class="case-study-shell">
  <div class="case-study-intro">
    <p class="lead">This project focused on a pragmatic question: <strong>when battery experiments are expensive, how do we decide which formulations to test first?</strong> The objective was not only to predict a response, but to build a model and evaluation framework aligned with prioritization.</p>
  </div>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/electrolyte-overview.svg' | relative_url }}" alt="Workflow from molecules to descriptors to formulation representation to ranking model to prioritized formulations">
    <p class="figure-caption">Figure 1. A simplified view of the end-to-end workflow, from component-level chemistry to a formulation-level ranking signal.</p>
  </div>

  <h2>The scientific problem</h2>
  <p>Electrolytes are mixtures, not single molecules. Their performance depends on the combination of solvents, salts, and additives, yet experimental cycling campaigns are costly and relatively sparse. The practical goal was to help R&amp;D teams identify strong candidates faster from a set of possible formulations.</p>

  <div class="stats-grid">
    <div><span class="stat-number">1,424</span><span class="stat-label">battery experiments</span></div>
    <div><span class="stat-number">158</span><span class="stat-label">formulations</span></div>
    <div><span class="stat-number">≈ 0.95</span><span class="stat-label">NDCG@10</span></div>
    <div><span class="stat-number">≈ 0.66</span><span class="stat-label">Spearman</span></div>
  </div>

  <h2>Why ranking instead of only regression?</h2>
  <p>The business decision was not simply “what exact lifetime will this cell achieve?” It was closer to “which candidates deserve attention first?” That made learning-to-rank a natural formulation. Regression still matters for understanding signals in the data, but ranking aligns better with top-candidate discovery.</p>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/electrolyte-ranking-metrics.svg' | relative_url }}" alt="Side-by-side comparison of a regression question and a ranking question, plus a visual summary of NDCG and Spearman metrics">
    <p class="figure-caption">Figure 2. The task framing drove the evaluation: top-K quality and order mattered, so I used ranking-oriented metrics such as NDCG alongside Spearman correlation.</p>
  </div>

  <h2>Representation</h2>
  <p>Each formulation was built from component-level chemistry. Molecular and physics-derived features were computed for individual ingredients, then aggregated into a formulation-level representation using composition-aware statistics such as weighted means, minima, maxima, ranges, and variation summaries. This created a fixed-length representation for mixtures while preserving chemical information from the components.</p>

  <h2>Modeling approach</h2>
  <p>I used a tree-based learning-to-rank workflow with strong classical descriptors as the baseline representation. The emphasis was not on using the most fashionable architecture, but on finding a robust workflow that generalized well under the available data and matched the experimental decision process.</p>

  <h2>Validation</h2>
  <p>Because top-candidate identification mattered, I used <strong>NDCG</strong> to measure whether the most promising formulations were surfaced near the top of the ranking, and <strong>Spearman</strong> to measure the quality of ordering more broadly. This helped evaluate both “did we recover the best candidates?” and “was the relative ordering meaningful?”</p>

  <h2>What this project taught me</h2>
  <ul>
    <li><strong>Prediction is not the same as a decision.</strong> In scientific ML, the right objective often comes from the downstream workflow.</li>
    <li><strong>Mixture problems need careful representation.</strong> Component-level descriptors must be translated into formulation-level features deliberately.</li>
    <li><strong>Metrics should follow the task.</strong> A ranking model should be judged with ranking-aware metrics, not only generic regression scores.</li>
  </ul>

  <p class="case-study-note">Public-facing summary of private industry work.</p>
</div>
