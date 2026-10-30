---
layout: portfolio_page
title: Closed-loop electrolyte design
display_title: Closed-loop design of battery electrolytes
kicker: Industry · Battery R&D · Lab-in-the-loop
permalink: /projects/closed-loop-electrolytes/
description: Predicting mixture properties, optimizing under constraints, and letting laboratory evidence reshape the next search.
---

<div class="case-study-shell">

<div class="case-summary">
  <div><span class="label">Question</span><p>Can we propose new electrolyte formulations, test them in the lab, and use what the lab finds to improve the next round?</p></div>
  <div><span class="label">Approach</span><p>Mixture-aware GNN surrogates (DiffMix) for conductivity, viscosity, and flash point, with constrained multi-objective optimization (NSGA-III).</p></div>
  <div><span class="label">Result</span><p>Diverse candidates went to lab testing. Lab results led to revised composition bounds and a flagged unreliable viscosity regime.</p></div>
  <div><span class="label">My role</span><p>Built the training data, trained and validated the surrogates, connected them to the optimizer, and worked with experimental collaborators on the feedback.</p></div>
</div>

<figure class="project-figure-block">
  <img src="{{ '/assets/img/projects/closed-loop-overview.png' | relative_url }}" alt="Closed-loop workflow: predict properties with a mixture model, search with constrained multi-objective optimization, test in the lab, and refine the search from lab feedback">
  <figcaption class="figure-caption">The workflow: a mixture-aware surrogate predicts properties, a constrained multi-objective optimizer proposes formulations, collaborators test a shortlist, and lab evidence refines the next search.</figcaption>
</figure>

<h2>The problem</h2>

<p>An electrolyte is a mixture of solvents, salts, and additives. Its properties depend on which components are present, how much of each, and how they interact. We wanted three things at once: higher ionic conductivity, lower viscosity, and a higher flash point for safety. These objectives pull against each other, and every candidate also had to use allowed components, stay within composition limits, and be something the lab could actually prepare.</p>

<h2>Predicting mixture properties</h2>

<p>Single-molecule models are not enough here: the same molecules at different fractions behave differently. I trained mixture-aware graph neural network surrogates for viscosity, ionic conductivity, and flash point, based on the published DiffMix architecture (<a href="https://doi.org/10.1038/s41467-024-51653-7">Zhu et al., Nature Communications, 2024</a>). My work was building the training data from the literature, training and validating the models, and connecting them to the optimizer. Validation held out whole component combinations, so the models were tested on mixtures whose component sets they had not seen.</p>

<h2>Searching for trade-offs, not one optimum</h2>

<figure class="project-figure-block">
  <img src="{{ '/assets/img/projects/closed-loop-fg5000-search.png' | relative_url }}" alt="Constrained multi-objective search: define objectives and constraints, generate candidates, predict with the surrogate, select non-dominated diverse candidates, evolve">
  <figcaption class="figure-caption">The surrogate scores each candidate in milliseconds, so the optimizer can evaluate many formulations before any experiment. NSGA-III keeps survivors spread across the whole trade-off front. Schematic.</figcaption>
</figure>

<p>The optimizer generated candidate compositions, scored them with the surrogates, checked feasibility, kept the non-dominated set while preserving diversity, and evolved the next generation. The result was a set of formulations spanning the trade-offs: some safety-leaning, some conductivity-leaning, some balanced. From these we shortlisted diverse candidates for laboratory testing.</p>

<h2>When the lab changed the problem</h2>

<p>Two results from the lab changed the computational workflow itself.</p>

<p><strong>Feasibility.</strong> Some proposed formulations would not mix during preparation. The property predictions were not wrong as such: miscibility was simply not part of the problem the optimizer had been given. We confirmed the failures, located the composition region where they occurred, and revised the optimizer's composition bounds so the next search stayed in the region that can actually be made.</p>

<figure class="project-figure-block">
  <img src="{{ '/assets/img/projects/closed-loop-feasible-region.png' | relative_url }}" alt="Composition triangle before feedback with failures near one corner, and after feedback with that corner excluded by a revised bound">
  <figcaption class="figure-caption">Lab feedback changed where the optimizer was allowed to search, not just which candidates it proposed. Schematic, not actual compositions.</figcaption>
</figure>

<p><strong>Model reliability.</strong> For a group of measured formulations, viscosity was systematically overpredicted, with every error in the same direction. After repeat measurements and calibration checks ruled out the instrument, the poorly predicted formulations turned out to share a concentrated-electrolyte regime that was underrepresented in the training data. We flagged predictions in that regime as unreliable for candidate prioritization and targeted it for new training data.</p>

<h2>Limitations</h2>

<ul>
  <li>Miscibility was not modeled; it is handled through constraints learned from lab failures, so new chemistries can still fail in new ways.</li>
  <li>Surrogate reliability varies by regime; predictions in the flagged concentrated regime need more training data before they can drive selection.</li>
</ul>

<!-- FILL IN only if Aionics approves (one or two sentences):
<p>Across __ design rounds, __ candidates were shortlisted and __ tested. After the bounds were revised, the share of proposals that could be prepared rose from __% to __%. On held-out component combinations the surrogates reached [metric] of __ for viscosity and __ for conductivity.</p>
-->

<h2>What I took from it</h2>

<ul>
  <li>A surrogate that is accurate on average can still fail systematically in exactly the regions an optimizer finds most interesting.</li>
  <li>Experimental feedback can change the constraints and the trust placed in a model, not only its training data.</li>
  <li>A model and an optimizer help only when the objectives and constraints reflect physical reality, and the lab is how you find out whether they do.</li>
</ul>

<p class="case-study-note">Public-facing summary of private industry work. Figures are schematic; no proprietary data is shown.</p>

</div>
