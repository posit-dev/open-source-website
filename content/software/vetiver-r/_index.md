---
color: '#F2CCAD'
description: Version, share, deploy, and monitor models
github: rstudio/vetiver-r
image: logo.png
languages:
- R
latest_release: '2025-12-13T20:36:56+00:00'
people:
- Julia Silge
- Barret Schloerke
- Daniel Falbel
- Emil Hvitfeldt
- Tomasz Kalinowski
title: vetiver-r
website: https://rstudio.github.io/vetiver-r/

external:  # updated automatically, do not edit
  description: Version, share, deploy, and monitor models
  first_commit: '2021-07-09T03:41:56+00:00'
  forks: 31
  languages:
  - R
  last_updated: '2026-03-20T10:27:36.906649+00:00'
  latest_release: '2025-12-13T20:36:56+00:00'
  license: NOASSERTION
  people:
  - Julia Silge
  - Barret Schloerke
  - Daniel Falbel
  - Emil Hvitfeldt
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: rstudio/vetiver-r
  stars: 198
  title: vetiver-r
  website: https://rstudio.github.io/vetiver-r/
---

Vetiver provides tooling for the full MLOps lifecycle of trained models in R. It handles versioning, sharing, deployment, and monitoring of models, with support for many modeling frameworks including tidymodels, caret, mlr3, XGBoost, keras, and base R functions like lm() and glm().

The package solves the deployment gap between training models and putting them into production. It uses pins for model versioning and storage across various backends (local folders, Posit Connect, S3), generates Plumber REST APIs for model serving, and maintains input data validation to catch prediction errors. Vetiver works alongside a Python implementation, making it suitable for multi-language data science teams.
