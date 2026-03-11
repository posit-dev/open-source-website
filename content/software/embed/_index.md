---
description: Extra recipes for predictor embeddings
github: tidymodels/embed
image: logo.png
color: "#D23D45"
languages:
- R
latest_release: '2026-01-29T21:24:25+00:00'
people:
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Hannah Frick
- Daniel Falbel
- Simon Couch
- Davis Vaughan
- Gábor Csárdi
- Jeroen Janssens
title: embed
website: https://embed.tidymodels.org

external:  # updated automatically, do not edit
  description: Extra recipes for predictor embeddings
  first_commit: '2018-05-16T18:28:10+00:00'
  forks: 22
  languages:
  - R
  last_updated: '2026-03-05T16:22:31.518608+00:00'
  latest_release: '2026-01-29T21:24:25+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Hannah Frick
  - Daniel Falbel
  - Simon Couch
  - Davis Vaughan
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/embed
  stars: 144
  title: embed
  website: https://embed.tidymodels.org
---

The embed package provides supervised preprocessing steps for the recipes package that transform categorical and numeric predictors into numeric embeddings. It exists as a separate package because it depends on heavier libraries like keras3, rstanarm, and lme4.

The package offers multiple encoding methods for categorical variables (including effect encoding via GLM/Bayesian models, neural network embeddings, weight of evidence, and feature hashing) and dimensionality reduction for numeric predictors (including supervised UMAP and tree-based discretization). It solves the problem of handling high-cardinality categorical variables and extracting meaningful numeric representations that incorporate information about the relationship between predictors and outcomes. Most preprocessing methods are supervised, meaning they use outcome information to create more predictive features.
