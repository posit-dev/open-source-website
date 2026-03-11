---
description: Tidy methods for measuring model performance
github: tidymodels/yardstick
image: logo.png
color: "#DB1E25"
languages:
- R
latest_release: '2025-01-22T22:13:45+00:00'
people:
- Emil Hvitfeldt
- Davis Vaughan
- Max Kuhn
- Simon Couch
- Hannah Frick
- Julia Silge
- Jeroen Janssens
title: yardstick
website: https://yardstick.tidymodels.org/

external:  # updated automatically, do not edit
  description: Tidy methods for measuring model performance
  first_commit: '2017-10-30T19:26:54+00:00'
  forks: 61
  languages:
  - R
  last_updated: '2026-03-05T16:22:21.729383+00:00'
  latest_release: '2025-01-22T22:13:45+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Davis Vaughan
  - Max Kuhn
  - Simon Couch
  - Hannah Frick
  - Julia Silge
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/yardstick
  stars: 398
  title: yardstick
  website: https://yardstick.tidymodels.org/
---

yardstick is an R package for estimating model performance using tidy data principles. It provides a consistent, dplyr-like syntax for calculating accuracy metrics on classification and regression models.

The package supports both binary and multiclass classification metrics with multiple estimation methods (macro, micro, hand-till). It works seamlessly with grouped data frames for calculating metrics across resamples, and includes autoplot methods for visualizing performance curves like ROC, precision-recall, and gain curves. All metrics return results in a consistent tibble format that integrates naturally with tidymodels workflows.
