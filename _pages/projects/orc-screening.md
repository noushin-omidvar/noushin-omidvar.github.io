---
layout: portfolio_page
permalink: /projects/orc-screening/
title: Physics-constrained screening across chemical space
kicker: scientific screening · thermodynamics
description: Combining ML property prediction with equation-of-state calculations and engineering constraints to reduce a massive candidate space.
---

<div class="case-study-shell">
  <p class="lead">This project asked how to move from a huge space of possible molecules to a short list that engineers could realistically review. The key idea was that <strong>ML was one component of a larger decision system</strong>, not the full solution by itself.</p>

  <div class="project-figure-block">
    <img src="{{ '/assets/img/projects/orc-screening-overview.svg' | relative_url }}" alt="Funnel showing 800 million candidate molecules filtered through ML prediction, physics calculations, and engineering constraints to 19 final candidates">
    <p class="figure-caption">Figure 1. A screening funnel from a very large chemical design space to a small engineering review set.</p>
  </div>

  <h2>The scientific problem</h2>
  <p>Candidate working fluids must satisfy multiple physical and operational requirements. Brute-force evaluation across an enormous design space is not practical, so the challenge was to combine prediction, thermodynamic modeling, and feasibility checks in a coherent pipeline.</p>

  <h2>Approach</h2>
  <p>I built a workflow that used ML-predicted thermophysical properties as inputs to downstream physics calculations. Equation-of-state calculations and operating constraints filtered the search further, ensuring that high-scoring molecules also remained plausible under engineering considerations.</p>

  <div class="stats-grid stats-grid-three">
    <div><span class="stat-number">~800M</span><span class="stat-label">candidate molecules screened</span></div>
    <div><span class="stat-number">ML + physics</span><span class="stat-label">integrated workflow</span></div>
    <div><span class="stat-number">19</span><span class="stat-label">candidates for review</span></div>
  </div>

  <h2>Why this matters</h2>
  <p>The value of the project was not only the scale. It demonstrated how scientific ML becomes more useful when it is embedded inside a physics-aware workflow and evaluated according to the quality of the final decisions it enables.</p>

  <p class="case-study-note">Public-facing summary of private industry work.</p>
</div>
