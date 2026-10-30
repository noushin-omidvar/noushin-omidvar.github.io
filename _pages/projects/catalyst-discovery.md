---
layout: portfolio_page
permalink: /projects/catalyst-discovery/
title: Explainable AI for ORR catalyst discovery
kicker: research · electrocatalysis · theory-infused ML
description: Using a theory-infused graph neural network, active learning, and explainable AI to screen Pt-monolayer core-shell catalysts and uncover the electronic origins of ORR reactivity.
---

<div class="case-study-shell">

  <p class="lead">
    Can a machine-learning model search a large catalyst design space
    <strong>and still explain why one catalytic site behaves differently from another?</strong>
    In this work, we combined graph neural networks, chemisorption theory,
    DFT, active learning, and explainable AI to search for Pt-monolayer
    core-shell catalysts for the oxygen reduction reaction.
  </p>

  <div class="project-figure-block">
    <img
      src="{{ '/assets/img/projects/orr-pt-monolayer-tinnet.png' | relative_url }}"
      alt="Theory-infused machine learning for oxygen reduction on Pt monolayer core-shell catalysts">
    <p class="figure-caption">
      Figure 1. Concept of the study: Pt-monolayer core-shell catalyst structures
      are represented as graphs, while TinNet connects learned representations
      to Newns-Anderson chemisorption theory. Explainability analysis then links
      changes in *OH binding to physically meaningful electronic factors.
    </p>
  </div>


  <h2>The scientific question</h2>

  <p>
    Oxygen reduction is a major source of efficiency loss in proton-exchange
    membrane fuel cells. Pt is the benchmark catalyst, but its activity can be
    improved by tuning the binding strength of reaction intermediates.
  </p>

  <p>
    We focused on <strong>{111}-oriented Pt-monolayer core-shell catalysts</strong>,
    where the composition and structure beneath the Pt surface can modify its
    reactivity through strain and ligand effects. The design space is enormous,
    making exhaustive DFT screening impractical.
  </p>

  <p>
    We used <strong>*OH chemisorption energy as a descriptor of ORR activity</strong>
    and asked two related questions:
  </p>

  <ul>
    <li>Can we rapidly identify Pt-monolayer structures with near-optimal *OH binding?</li>
    <li>Can the model explain the electronic mechanisms responsible for those changes in binding?</li>
  </ul>


  <div class="stats-grid">
    <div>
      <span class="stat-number">1,518</span>
      <span class="stat-label">bulk alloy structures</span>
    </div>

    <div>
      <span class="stat-number">~17K</span>
      <span class="stat-label">Pt-monolayer structures</span>
    </div>

    <div>
      <span class="stat-number">29,040</span>
      <span class="stat-label">distinct surface sites</span>
    </div>

    <div>
      <span class="stat-number">0.05 eV</span>
      <span class="stat-label">cross-validated MAE</span>
    </div>
  </div>


  <h2>Why a theory-infused neural network?</h2>

  <p>
    A conventional graph neural network can learn structure–property relationships,
    but its internal representation does not necessarily correspond to quantities
    that a surface scientist can interpret.
  </p>

  <p>
    We therefore used <strong>TinNet</strong>, a theory-infused graph neural network
    that couples a data-driven GNN with a physics module based on the
    <strong>Newns–Anderson model of chemisorption</strong>.
  </p>

  <p>
    The GNN learns from the atomic graph of the adsorbate–surface system, while
    the theory module describes adsorption in terms of physically meaningful
    electronic quantities. Training was multi-objective: the model learned not
    only the *OH adsorption energy, but also quantities connected to the underlying
    chemisorption physics, including d-band moments and projected density of states
    associated with the OH 3σ, 1π, and 4σ* orbitals.
  </p>

  <p>
    This was important because the goal was not simply to attach an explanation
    to a black-box prediction afterward. The aim was to make the learned
    representation itself more closely connected to established surface-science theory.
  </p>


  <h2>Searching the catalyst space with active learning</h2>

  <p>
    The candidate space was generated from thermodynamically stable alloy
    structures containing combinations of transition metals. These bulk structures
    were converted into first- and second-generation Pt-monolayer core-shell
    surface models.
  </p>

  <p>
    Instead of calculating every candidate with DFT, we used an
    <strong>active-learning loop</strong>. TinNet predicted *OH binding energies
    and associated uncertainty across the remaining candidates, and new DFT
    calculations were preferentially added where additional information was most useful.
  </p>

  <p>
    Prediction uncertainty progressively decreased during active learning.
    Nested 10-fold cross-validation produced an MAE of approximately
    <strong>0.05 eV</strong> with a standard deviation of approximately
    <strong>0.04 eV</strong>.
  </p>


  <h2>From prediction to catalyst screening</h2>

  <p>
    ORR activity follows a volcano-like dependence on intermediate binding:
    Pt binds oxygenated intermediates somewhat too strongly, while excessively
    weak binding is also unfavorable.
  </p>

  <p>
    We therefore searched for catalysts whose *OH adsorption energy was
    approximately <strong>0–0.15 eV weaker than Pt(111)</strong>, placing them
    near the predicted high-activity region.
  </p>

  <p>
    The screening recovered previously reported active Pt-monolayer catalysts
    and identified additional first- and second-generation core-shell compositions
    with near-optimal predicted reactivity. Cost filtering further highlighted
    candidate cores containing earth-abundant elements such as Fe, Co, and Ni.
  </p>


  <h2>What did the model actually learn?</h2>

  <p>
    Screening was only half of the project. The second objective was to understand
    <strong>why alloying perturbs the reactivity of the Pt surface</strong>.
  </p>

  <p>
    We applied SHAP at two levels:
  </p>

  <ul>
    <li>
      <strong>Global explanations</strong> identified which learned electronic
      factors systematically controlled changes in *OH chemisorption.
    </li>

    <li>
      <strong>Local explanations</strong> decomposed the change in binding energy
      for individual alloy surfaces relative to a reference such as Pt(111).
    </li>
  </ul>

  <p>
    The analysis showed that reactivity could not be understood through the
    d-band center alone. Important contributions also came from the
    <strong>renormalized OH 1π adsorbate resonance energy</strong> and the
    <strong>coupling between the 1π state and metal d-states</strong>.
  </p>

  <p>
    Together, these quantities determine the occupation and energetics of
    adsorbate–metal antibonding states and therefore help explain why apparently
    similar Pt sites can exhibit different *OH binding strengths.
  </p>


  <h2>A concrete example: Pt₃Co@Pt<sub>ML</sub></h2>

  <p>
    The explainability analysis provided a mechanistic interpretation of the
    well-known enhanced ORR activity of Pt₃Co@Pt<sub>ML</sub>.
  </p>

  <p>
    Relative to Pt(111), the alloy binds *OH about <strong>0.13 eV more weakly</strong>.
    TinNet and SHAP attributed much of this change to two coupled electronic effects:
    a downshift of the Pt d-band center and a change in the coupling between the
    OH 1π resonance and the metal d-states.
  </p>

  <p>
    The analysis connected these electronic changes back to the catalyst structure:
    compressive strain from the Pt₃Co core modifies Pt–Pt distances and orbital
    overlap at the surface, changing the balance between bonding and antibonding
    interactions with *OH.
  </p>


  <h2>The scientific insight</h2>

  <p>
    The most important result for me was not simply that the model could predict
    adsorption energies accurately.
  </p>

  <p>
    <strong>
      By embedding chemisorption theory into the learning problem and then
      interrogating the learned physical variables, we could use ML as a tool
      for scientific explanation as well as screening.
    </strong>
  </p>

  <p>
    The work showed that adsorbate resonance energies, including effects associated
    with substrate sp-state interactions, can play an important role in determining
    surface reactivity. This provides a richer picture of chemisorption than relying
    on a single conventional descriptor such as the d-band center.
  </p>


  <h2>What I took from this project</h2>

  <ul>
    <li>
      <strong>Domain theory can be part of the model, not just a post-processing step.</strong>
      Physics-derived latent quantities made the learned representation scientifically interpretable.
    </li>

    <li>
      <strong>Explainability is most useful when the features being explained have physical meaning.</strong>
      SHAP could be interpreted in terms of orbital interactions rather than arbitrary neural-network features.
    </li>

    <li>
      <strong>Scientific ML can connect discovery and understanding.</strong>
      The same framework was used to search a large catalyst space and investigate
      the physical origin of promising predictions.
    </li>

    <li>
      <strong>Model evaluation should support the scientific decision.</strong>
      Active learning, uncertainty estimation, DFT validation, and the ORR activity
      descriptor were all part of the discovery loop.
    </li>
  </ul>


  <p class="case-study-note">
    Omidvar et al., Electrochemical Science Advances, 2024.
    “Explainable AI for optimizing oxygen reduction on Pt monolayer core–shell catalysts.”
  </p>

  <p>
    <a class="text-button" href="{{ '/publications/' | relative_url }}">
      View publication
    </a>
  </p>

</div>