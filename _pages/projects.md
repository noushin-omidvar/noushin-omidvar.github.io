---
layout: portfolio_page
permalink: /projects/
title: Projects
kicker: selected work
description: Case studies on scientific machine learning for chemistry, materials, and engineering R&D.
---

<div class="project-grid">
  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/closed-loop-overview.png' | relative_url }}" alt="Closed loop: predict properties, optimize, test in the lab, and refine constraints from lab feedback">
    <div class="project-card-body">
      <div class="project-card-meta">Industry · Battery R&amp;D · Lab-in-the-loop</div>
      <h2><a href="{{ '/projects/closed-loop-electrolytes/' | relative_url }}">Closed-loop design of battery electrolytes</a></h2>
      <p>Mixture-property models and constrained multi-objective optimization proposed formulations; lab results then changed the search constraints and the trust placed in the model.</p>
      <div class="tag-row"><span>mixture GNN</span><span>NSGA-III</span><span>lab feedback</span></div>
    </div>
  </article>

  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/ranking-workflow.png' | relative_url }}" alt="Workflow from molecules to descriptors, mixture representation, ranking model, and prioritized formulations">
    <div class="project-card-body">
      <div class="project-card-meta">Industry · Battery R&amp;D · Experiment prioritization</div>
      <h2><a href="{{ '/projects/electrolyte-ranking/' | relative_url }}">Learning to rank electrolyte formulations by cycle life</a></h2>
      <p>Ranking 158 formulations from 1,424 cycling experiments, validated on held-out component combinations.</p>
      <div class="tag-row"><span>learning to rank</span><span>mixture features</span><span>grouped CV</span></div>
    </div>
  </article>

  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/catalyst-tinnet-architecture.png' | relative_url }}" alt="TinNet: a graph network predicts electronic parameters that feed a differentiable Newns–Anderson chemisorption model">
    <div class="project-card-body">
      <div class="project-card-meta">Research · Electrocatalysis · Active learning</div>
      <h2><a href="{{ '/projects/catalyst-discovery/' | relative_url }}">Physics-informed graph learning for catalyst discovery</a></h2>
      <p>A theory-infused GNN with active learning screened ~17,700 Pt-monolayer surfaces and explained why the promising ones bind *OH differently.</p>
      <div class="tag-row"><span>DFT</span><span>physics-informed GNN</span><span>SHAP</span></div>
    </div>
  </article>

  <article class="project-card">
    <img class="project-card-figure" src="{{ '/assets/img/projects/orc-screening-funnel.png' | relative_url }}" alt="Funnel from hundreds of millions of candidate molecules to a small engineering review set">
    <div class="project-card-body">
      <div class="project-card-meta">Scientific screening · Thermodynamics</div>
      <h2><a href="{{ '/projects/orc-screening/' | relative_url }}">Physics-constrained screening across chemical space</a></h2>
      <p>ML-predicted properties fed equation-of-state and cycle calculations to narrow ~800M molecules to 19 for engineering review.</p>
      <div class="tag-row"><span>screening</span><span>equation of state</span><span>constraints</span></div>
    </div>
  </article>
</div>
