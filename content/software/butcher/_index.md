---
color: '#5CF8F2'
description: Reduce the size of model objects saved to disk
github: tidymodels/butcher
image: logo.png
languages:
- R
latest_release: '2025-12-09T11:27:57+00:00'
people:
- Davis Vaughan
- Julia Silge
- Simon Couch
- Max Kuhn
- Hannah Frick
- Emil Hvitfeldt
- Jeroen Janssens
title: butcher
website: https://butcher.tidymodels.org/

external:  # updated automatically, do not edit
  description: Reduce the size of model objects saved to disk
  first_commit: '2019-06-06T19:45:18+00:00'
  forks: 16
  languages:
  - R
  last_updated: '2026-03-20T10:27:44.814875+00:00'
  latest_release: '2025-12-09T11:27:57+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Julia Silge
  - Simon Couch
  - Max Kuhn
  - Hannah Frick
  - Emil Hvitfeldt
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/butcher
  stars: 137
  title: butcher
  website: https://butcher.tidymodels.org/
---

butcher reduces the memory footprint of fitted model objects in R by removing unnecessary components that often bloat models due to formula usage, captured environments, and non-selective object construction. The package preserves prediction functionality while stripping away redundant parts that aren't needed for post-fit estimation.

The package provides `weigh()` and `locate()` functions to identify memory-heavy components, plus five axe methods (`axe_call()`, `axe_ctrl()`, `axe_data()`, `axe_env()`, `axe_fitted()`) to selectively remove specific parts of model objects. A convenience function `butcher()` executes all axing operations at once. This is particularly valuable when deploying models to production or storing many fitted models, where a model that should be 22 KB might otherwise consume 8 MB due to captured environments and unnecessary data.
