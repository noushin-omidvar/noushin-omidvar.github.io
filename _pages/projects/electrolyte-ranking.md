---
layout: portfolio_page
permalink: /projects/electrolyte-ranking/
title: Learning to rank electrolyte formulations by cycle life
kicker: industry case study · battery r&d
description: Ranking electrolyte formulations for experimental prioritization, with features built from component chemistry and validation on held-out component combinations.
---

<div class="case-study-shell">

  <div class="case-summary">
    <div><span class="label">Question</span><p>Cycling experiments are slow and expensive. Which formulations should the lab test first?</p></div>
    <div><span class="label">Approach</span><p>Formulation features aggregated from component chemistry, with a tree-based learning-to-rank model.</p></div>
    <div><span class="label">Result</span><p>NDCG@10 ≈ 0.95 and Spearman ≈ 0.66 on held-out component combinations.</p></div>
    <div><span class="label">My role</span><p>Problem framing, featurization, modeling, and validation design.</p></div>
  </div>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/ranking-workflow.png' | relative_url }}" alt="Workflow from molecules to descriptors, mixture representation, ranking model, and prioritized formulations">
    <p class="figure-caption">From component chemistry to a ranked list of formulations for the lab.</p>
  </div>

  <div class="stats-grid">
    <div><span class="stat-number">1,424</span><span class="stat-label">cycling experiments</span></div>
    <div><span class="stat-number">158</span><span class="stat-label">formulations</span></div>
    <div><span class="stat-number">≈ 0.95</span><span class="stat-label">NDCG@10</span></div>
    <div><span class="stat-number">≈ 0.66</span><span class="stat-label">Spearman</span></div>
  </div>

  <h2>Why ranking, not regression</h2>
  <p>The lab's decision was not "what exact cycle life will this cell reach?" but "which candidates deserve the next experiments?" That made learning to rank the natural objective, and ranking metrics the natural way to judge it: NDCG@10 asks whether the best formulations reach the top of the list, and Spearman asks whether the overall order is meaningful.</p>

  <h2>Representing a mixture</h2>
  <p>An electrolyte is a mixture of solvents, salts, and additives. I computed molecular and DFT-derived descriptors for each component and aggregated them into fixed-length formulation features using composition-weighted means, minima, maxima, and ranges.</p>

  <h2>Validation</h2>
  <p>The 1,424 experiments include replicate cells of the same formulation, and formulations that share components are not independent, so a random split would leak information. I used nested grouped cross-validation that held out whole component combinations: the model was always scored on formulations whose component set it had not seen during training or tuning.</p>
  <!-- FILL IN if allowed (one sentence; strongly recommended):
  <p>For comparison, a [random ranking / simple heuristic, e.g. rank by salt concentration] scored NDCG@10 ≈ __ on the same folds. Reported values are mean ± std over outer folds (NDCG@10 0.95 ± __, Spearman 0.66 ± __).</p>
  -->

  <h2>Limitations</h2>
  <ul>
    <li>158 formulations is a small set, so the ranking is most reliable within the chemistry the campaign covered.</li>
    <li>Aggregate mixture features cannot represent specific component–component interactions.</li>
  </ul>

  <h2>Takeaway</h2>
  <p>The downstream decision should set the objective and the metric. Here that meant ranking, and validation that respects how mixtures share components.</p>

  <p class="case-study-note">Public-facing summary of private industry work.</p>
</div>
