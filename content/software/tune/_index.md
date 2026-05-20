---
color: '#A545B6'
description: Tools for tidy parameter tuning
github: tidymodels/tune
image: logo.png
languages:
- R
latest_release: '2026-04-17T16:43:58+00:00'
people:
- Max Kuhn
- Hannah Frick
- Simon Couch
- Davis Vaughan
- Julia Silge
- Emil Hvitfeldt
- Edgar Ruiz
- Lionel Henry
- Gábor Csárdi
title: tune
topics:
- Data Wrangling
- Machine Learning
website: https://tune.tidymodels.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Tools for tidy parameter tuning
  first_commit: '2019-08-09T20:49:40+00:00'
  forks: 48
  languages:
  - R
  last_updated: '2026-05-20T08:05:48.309032+00:00'
  latest_release: '2026-04-17T16:43:58+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Hannah Frick
  - Simon Couch
  - Davis Vaughan
  - Julia Silge
  - Emil Hvitfeldt
  - Edgar Ruiz
  - Lionel Henry
  - Jeroen Janssens
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: tidymodels/tune
  stars: 334
  title: tune
  website: https://tune.tidymodels.org
---

The tune package provides tools for hyperparameter tuning within the tidymodels ecosystem. It works with recipes for preprocessing, parsnip for model specification, and dials for defining parameter grids.

The package supports both grid search and iterative Bayesian optimization approaches to find optimal model parameters. It integrates with tidymodels workflows to evaluate different parameter combinations across resampling strategies like cross-validation. The package handles parallel processing for efficiency and provides acquisition functions for scoring parameter combinations during optimization.
