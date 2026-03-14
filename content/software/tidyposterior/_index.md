---
color: '#D7B79F'
description: Bayesian comparisons of models using resampled statistics
github: tidymodels/tidyposterior
image: logo.png
languages:
- R
latest_release: '2025-07-30T23:43:16+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Julia Silge
- Hannah Frick
- Davis Vaughan
- Gábor Csárdi
title: tidyposterior
website: https://tidyposterior.tidymodels.org

external:  # updated automatically, do not edit
  description: Bayesian comparisons of models using resampled statistics
  first_commit: '2017-10-15T17:39:33+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-03-05T16:22:18.787229+00:00'
  latest_release: '2025-07-30T23:43:16+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Julia Silge
  - Hannah Frick
  - Davis Vaughan
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: tidymodels/tidyposterior
  stars: 102
  title: tidyposterior
  website: https://tidyposterior.tidymodels.org
---

The tidyposterior package performs Bayesian post hoc analysis of resampling results to compare the performance of different models. It works with cross-validation or other resampling methods to make statistically rigorous comparisons between models without needing a separate test set.

The package uses Bayesian generalized linear models to analyze paired resampling statistics, treating them as posterior distributions that can be compared directly. This approach accounts for the correlation structure in resampled data and provides probabilistic statements about model differences. It integrates with the tidymodels ecosystem but can also work with any resampling results stored in a data frame.
