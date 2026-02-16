---
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

external:
  contributors:
  - topepo
  - EmilHvitfeldt
  - juliasilge
  - hfrick
  - aeklant
  - DavisVaughan
  - ezequielpaura
  - gaborcsardi
  - lawwu
  - mikemahoney218
  - mone27
  description: Bayesian comparisons of models using resampled statistics
  first_commit: '2017-10-15T17:39:33+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.100502+00:00'
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

When building machine learning models, you often need to compare different approaches to determine which performs best. tidyposterior provides a statistically rigorous way to make these comparisons using Bayesian methods applied to resampling results from cross-validation or other resampling techniques. Rather than simply comparing point estimates of model performance metrics, the package generates full posterior probability distributions that quantify uncertainty and enable you to make probabilistic statements about which model truly performs better.

Built as part of the tidymodels ecosystem, tidyposterior seamlessly integrates with rsample objects and other tidymodels tools, though it works with any resampling results in a data frame. The package leverages the power of paired observations across resampling folds, applying Bayesian generalized linear models to extract meaningful comparisons without requiring a separate test set. Whether you're evaluating competing algorithms or tuning hyperparameters, tidyposterior helps you move beyond simple accuracy comparisons to make informed, statistically sound decisions about model selection.
