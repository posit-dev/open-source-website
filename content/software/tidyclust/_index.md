---
description: A tidy unified interface to clustering models
github: tidymodels/tidyclust
image: logo.svg
languages:
- R
latest_release: '2025-01-27T23:10:34+00:00'
people:
- Emil Hvitfeldt
- Hannah Frick
- Max Kuhn
title: tidyclust
website: https://tidyclust.tidymodels.org/

external:  # updated automatically, do not edit
  description: A tidy unified interface to clustering models
  first_commit: '2021-11-19T19:52:49+00:00'
  forks: 21
  languages:
  - R
  last_updated: '2026-02-24T09:26:27.824933+00:00'
  latest_release: '2025-01-27T23:10:34+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Hannah Frick
  - Max Kuhn
  readme_image: man/figures/logo.svg
  repo: tidymodels/tidyclust
  stars: 112
  title: tidyclust
  website: https://tidyclust.tidymodels.org/
---

tidyclust provides a unified interface for clustering models in R, following the same design principles as the tidymodels parsnip package. It allows you to specify, fit, and work with various clustering algorithms using consistent syntax and workflows.

The package supports multiple clustering algorithms (like k-means, hierarchical clustering, and others) through a common API. It integrates with the tidymodels ecosystem, making it straightforward to extract cluster assignments, centroids, and predictions using standard functions like `fit()`, `predict()`, and helper functions like `extract_cluster_assignment()` and `extract_centroids()`. This consistent interface eliminates the need to learn different function names and argument structures for each clustering implementation.
