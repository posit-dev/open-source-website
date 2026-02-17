---
description: Modeling Workflows
github: tidymodels/workflows
image: logo.png
languages:
- R
latest_release: '2025-08-27T09:07:53+00:00'
people:
- Davis Vaughan
- Hannah Frick
- Simon Couch
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Gábor Csárdi
- Jeroen Janssens
title: workflows
website: https://workflows.tidymodels.org/

external:
  description: Modeling Workflows
  first_commit: '2019-09-25T15:45:32+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-02-17T11:30:11.518118+00:00'
  latest_release: '2025-08-27T09:07:53+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Hannah Frick
  - Simon Couch
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/workflows
  stars: 210
  title: workflows
  website: https://workflows.tidymodels.org/
---

The workflows package bundles together pre-processing recipes, modeling specifications, and post-processing steps into a single object for machine learning workflows in R. It integrates with the tidymodels ecosystem, particularly the recipes and parsnip packages, to streamline the modeling process.

This package solves the problem of managing multiple separate objects (like prepared recipes and fitted models) in your workspace and ensures they stay paired correctly. It simplifies the modeling process by allowing you to prepare data, fit models, and make predictions through a single unified interface, reducing the risk of mixing up model/recipe combinations. The package also integrates with the tune package to simplify hyperparameter tuning workflows.
