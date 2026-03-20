---
color: '#637B8A'
description: parsnip wrappers for tree-based models
github: tidymodels/bonsai
image: logo.png
languages:
- R
latest_release: '2025-06-23T20:18:05+00:00'
people:
- Simon Couch
- Emil Hvitfeldt
- Max Kuhn
- Hannah Frick
- Jeroen Janssens
title: bonsai
website: https://bonsai.tidymodels.org

external:  # updated automatically, do not edit
  description: parsnip wrappers for tree-based models
  first_commit: '2022-04-29T13:33:22+00:00'
  forks: 8
  languages:
  - R
  last_updated: '2026-03-20T10:27:45.425451+00:00'
  latest_release: '2025-06-23T20:18:05+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Emil Hvitfeldt
  - Max Kuhn
  - Hannah Frick
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/bonsai
  stars: 54
  title: bonsai
  website: https://bonsai.tidymodels.org
---

bonsai provides bindings for additional tree-based model engines for use with the parsnip package in the tidymodels ecosystem. It extends parsnip's modeling capabilities by adding support for popular gradient boosting and tree-based algorithms.

The package adds engines for LightGBM, CatBoost, partykit, and aorsf to parsnip's boost_tree, decision_tree, and rand_forest model specifications. This allows users to access these high-performance tree-based algorithms through parsnip's unified interface, supporting both regression and classification tasks. bonsai is the official CRAN successor to the treesnip package, consolidating community work into a maintained tidymodels extension.
