---
color: '#FBEE7E'
description: Tools for post-processing class probability estimates
github: tidymodels/probably
image: logo.png
languages:
- R
latest_release: '2025-10-16T12:05:16+00:00'
people:
- Davis Vaughan
- Max Kuhn
- Emil Hvitfeldt
- Edgar Ruiz
- Julia Silge
- Hannah Frick
- Simon Couch
- Gábor Csárdi
- Jeroen Janssens
title: probably
website: https://probably.tidymodels.org/

external:  # updated automatically, do not edit
  description: Tools for post-processing class probability estimates
  first_commit: '2018-09-11T19:02:58+00:00'
  forks: 17
  languages:
  - R
  last_updated: '2026-03-05T16:22:42.559640+00:00'
  latest_release: '2025-10-16T12:05:16+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Max Kuhn
  - Emil Hvitfeldt
  - Edgar Ruiz
  - Julia Silge
  - Hannah Frick
  - Simon Couch
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/probably
  stars: 120
  title: probably
  website: https://probably.tidymodels.org/
---

probably is an R package for working with predicted probabilities from classification and regression models. It converts probabilities to class predictions, identifies optimal probability thresholds, and handles cases where predictions are too uncertain to be reliable.

The package provides tools for model calibration assessment and correction, lets you define equivocal zones where probability predictions are too ambiguous to make a definitive call, and integrates with the tidymodels ecosystem for threshold optimization. It addresses the common problem that raw model probabilities often need post-processing before making final predictions, especially when uncertainty varies across the prediction space.
