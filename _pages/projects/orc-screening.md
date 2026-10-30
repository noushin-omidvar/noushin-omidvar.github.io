---
layout: portfolio_page
permalink: /projects/orc-screening/
title: Physics-constrained screening across chemical space
kicker: scientific screening · thermodynamics
description: Combining ML property prediction with equation-of-state calculations and engineering constraints to narrow a very large candidate space.
---

<div class="case-study-shell">

  <div class="case-summary">
    <div><span class="label">Question</span><p>How do you get from a huge space of possible working fluids to a short list engineers can review?</p></div>
    <div><span class="label">Approach</span><p>ML-predicted properties feed equation-of-state and cycle calculations, and engineering constraints filter the results.</p></div>
    <div><span class="label">Result</span><p>About 800 million molecules narrowed to 19 candidates for engineering review.</p></div>
    <div><span class="label">My role</span><p>Designed and built the screening workflow, linking the ML models to the physics calculations.</p></div>
  </div>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/orc-screening-funnel.png' | relative_url }}" alt="Funnel from hundreds of millions of candidate molecules through ML prediction, physics calculations, and constraints to a small review set">
    <p class="figure-caption">Each stage is cheaper than the next, so expensive physics runs only on candidates that pass the earlier filters.</p>
  </div>

  <div class="stats-grid stats-grid-three">
    <div><span class="stat-number">~800M</span><span class="stat-label">candidate molecules</span></div>
    <div><span class="stat-number">ML + physics</span><span class="stat-label">integrated workflow</span></div>
    <div><span class="stat-number">19</span><span class="stat-label">candidates for review</span></div>
  </div>

  <h2>Why ML alone was not enough</h2>
  <p>A working fluid has to satisfy several physical and operating requirements at once. Brute-force physics on hundreds of millions of molecules is impractical, while ML predictions alone can rank molecules highly that are physically implausible. So ML handled the scale, and equation-of-state calculations and operating constraints made sure the survivors made physical sense.</p>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/orc-cycle-schematic.png' | relative_url }}" alt="Schematic of an organic Rankine cycle">
    <p class="figure-caption">The candidates are working fluids for an organic Rankine cycle, so their properties are judged by how the cycle performs.</p>
  </div>

  <h2>Limitations</h2>
  <ul>
    <li>Errors in the ML-predicted critical properties carry through to the cycle calculations, so the shortlist is a prioritization for expert review, not a final selection.</li>
    <li>Safety, toxicity, and cost need checks beyond this workflow.</li>
  </ul>
  <!-- FILL IN if true (one sentence):
  <p>Critical-property models had MAE of __ K (Tc) / __ bar (Pc) under similarity-aware validation; [N] of the 19 candidates were cross-checked against reference data (NIST / literature).</p>
  -->

  <h2>Takeaway</h2>
  <p>Scientific ML is most useful inside a physics-aware workflow, judged by the quality of the decisions it supports.</p>

  <p class="case-study-note">Public-facing summary of private industry work.</p>
</div>
