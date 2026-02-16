---
description: parsnip wrappers for tree-based models
github: tidymodels/bonsai
image: logo.png
languages:
- R
latest_release: '2025-06-23T20:18:05+00:00'
people:
- Simon Couch
- Emil Hvitfeldt
- Max Kuhn
- Hannah Frick
- Jeroen Janssens
title: bonsai
website: https://bonsai.tidymodels.org

external:
  contributors:
  - simonpcouch
  - EmilHvitfeldt
  - jameslamb
  - topepo
  - hfrick
  - bcjaeger
  - jeroenjanssens
  - p-schaefer
  description: parsnip wrappers for tree-based models
  first_commit: '2022-04-29T13:33:22+00:00'
  forks: 8
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.782671+00:00'
  latest_release: '2025-06-23T20:18:05+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Emil Hvitfeldt
  - Max Kuhn
  - Hannah Frick
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/bonsai
  stars: 54
  title: bonsai
  website: https://bonsai.tidymodels.org
---

bonsai extends the parsnip package by providing additional engines for tree-based models within the tidymodels ecosystem. It brings powerful machine learning algorithms like LightGBM, CatBoost, and conditional inference trees into tidymodels' unified modeling interface, allowing you to leverage cutting-edge tree-based methods using the familiar parsnip syntax. Whether you're building boosted trees for high-performance predictions, decision trees for interpretable models, or random forests for robust ensemble learning, bonsai makes these algorithms accessible through consistent, tidy R code.

What makes bonsai particularly valuable for data scientists is its integration of diverse tree-based engines into a single framework, eliminating the need to learn different syntaxes for each algorithm. The package supports both regression and classification tasks across all its engines, including specialized options like AORSF for oblique random survival forests and partykit for conditional inference procedures. By standardizing access to these powerful tools within the tidymodels workflow, bonsai enables you to experiment with different tree-based approaches while maintaining clean, reproducible code that fits seamlessly into your existing modeling pipelines.
