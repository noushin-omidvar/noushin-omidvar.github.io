---
layout: portfolio_page
permalink: /projects/
title: Projects
kicker: selected work
description: Case studies on scientific machine learning for chemistry, materials, and engineering R&D.
---

<div class="project-grid">
  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/electrolyte-overview.svg' | relative_url }}" alt="Diagram of molecules, mixture representation, ranking model, and prioritized formulations">
    <div class="project-card-body">
      <div class="project-card-meta">Industry · Battery R&amp;D</div>
      <h2><a href="{{ '/projects/electrolyte-ranking/' | relative_url }}">Learning to rank electrolyte formulations</a></h2>
      <p>How to move from component chemistry to a formulation-level representation and prioritize candidates for experimental follow-up.</p>
      <div class="tag-row"><span>ranking</span><span>mixture ML</span><span>battery R&amp;D</span></div>
    </div>
  </article>

  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/molecular-generalization-overview.svg' | relative_url }}" alt="Diagram showing molecular similarity, chemistry-aware splitting, and benchmark comparison">
    <div class="project-card-body">
      <div class="project-card-meta">Molecular ML · Generalization</div>
      <h2><a href="{{ '/projects/molecular-generalization/' | relative_url }}">Testing whether molecular models actually generalize</a></h2>
      <p>A case study in building chemistry-aware validation splits and comparing classical descriptor baselines to pretrained embeddings.</p>
      <div class="tag-row"><span>benchmarking</span><span>similarity splits</span><span>XGBoost</span></div>
    </div>
  </article>

  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/orc-screening-overview.svg' | relative_url }}" alt="Funnel showing many candidate molecules filtered by ML and physics constraints to a small final set">
    <div class="project-card-body">
      <div class="project-card-meta">Scientific Screening · Thermodynamics</div>
      <h2><a href="{{ '/projects/orc-screening/' | relative_url }}">Physics-constrained screening across chemical space</a></h2>
      <p>Combining ML-predicted properties with equation-of-state calculations and engineering constraints to reduce an enormous design space.</p>
      <div class="tag-row"><span>screening</span><span>thermodynamics</span><span>constraints</span></div>
    </div>
  </article>

  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/Physics-Informed Workflow for ORR Catalyst Discovery.png' | relative_url }}" alt="Workflow from atomic structures to graph representation to graph neural network and design principles">
    <div class="project-card-body">
      <div class="project-card-meta">Research · Catalysis</div>
      <h2><a href="{{ '/projects/catalyst-discovery/' | relative_url }}">Interpretable ML for catalyst discovery</a></h2>
      <p>Using first-principles descriptors, graph neural networks, and interpretable ML to extract chemical insight and guide catalyst design.</p>
      <div class="tag-row"><span>DFT</span><span>GNNs</span><span>interpretability</span></div>
    </div>
  </article>
</div>
