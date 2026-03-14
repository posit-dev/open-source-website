---
color: '#5289B1'
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

external:  # updated automatically, do not edit
  description: Create a collection of modeling workflows
  first_commit: '2020-11-24T02:30:49+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-03-05T16:23:39.102414+00:00'
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

The workflowsets package allows users to create and fit multiple machine learning models simultaneously by organizing them into workflow sets. It generates combinations of preprocessors (like recipes and formulas) and model specifications, then provides functions to tune or resample all combinations efficiently.

This package solves the problem of testing different preprocessing approaches and model types on the same dataset without manually creating each combination. It integrates with the tidymodels framework to support systematic model comparison through grid search, resampling, and performance ranking. Users can easily filter out illogical combinations (like pairing PCA with regularized models) and evaluate all remaining workflows with a single function call.
