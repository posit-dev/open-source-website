---
description: Create a collection of modeling workflows
github: tidymodels/workflowsets
image: README-plot-1.png
languages:
- R
latest_release: '2025-05-28T13:18:33+00:00'
people:
- Max Kuhn
- Simon Couch
- Hannah Frick
- Davis Vaughan
- Julia Silge
- Emil Hvitfeldt
- Gábor Csárdi
- Jeroen Janssens
title: workflowsets
website: https://workflowsets.tidymodels.org/

external:
  contributors:
  - topepo
  - simonpcouch
  - hfrick
  - DavisVaughan
  - juliasilge
  - EmilHvitfeldt
  - gaborcsardi
  - jeroenjanssens
  - jonthegeek
  - jrosell
  description: Create a collection of modeling workflows
  first_commit: '2020-11-24T02:30:49+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.673325+00:00'
  latest_release: '2025-05-28T13:18:33+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Simon Couch
  - Hannah Frick
  - Davis Vaughan
  - Julia Silge
  - Emil Hvitfeldt
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/README-plot-1.png
  repo: tidymodels/workflowsets
  stars: 96
  title: workflowsets
  website: https://workflowsets.tidymodels.org/
---

workflowsets is an essential tidymodels package designed to streamline the process of comparing multiple modeling approaches. It enables you to efficiently create and evaluate large numbers of models by automatically combining different preprocessing methods with various model specifications. Instead of manually building and testing each combination of feature engineering steps and algorithms, workflowsets generates workflow sets that systematically explore your modeling options, making comprehensive model comparison both practical and reproducible.

What makes workflowsets particularly valuable is its ability to batch-process evaluations across all your workflows while providing intelligent tools to filter out impractical combinations and quickly identify top performers. Functions like workflow_map() enable streamlined tuning and resampling across your entire collection, while built-in visualization and ranking capabilities help you rapidly assess which preprocessing and model combinations deliver the best results. Whether you're exploring different feature engineering strategies, comparing algorithms, or fine-tuning hyperparameters, workflowsets removes the complexity from systematic model evaluation, letting you focus on insights rather than infrastructure.
