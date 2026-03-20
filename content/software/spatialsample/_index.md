---
color: '#286380'
description: Create and summarize spatial resampling objects 🗺
github: tidymodels/spatialsample
image: logo.png
languages:
- R
latest_release: '2024-10-02T16:28:40+00:00'
people:
- Julia Silge
- Davis Vaughan
- Hannah Frick
title: spatialsample
website: https://spatialsample.tidymodels.org

external:  # updated automatically, do not edit
  description: Create and summarize spatial resampling objects 🗺
  first_commit: '2021-01-19T21:06:51+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-03-20T10:27:45.297203+00:00'
  latest_release: '2024-10-02T16:28:40+00:00'
  license: NOASSERTION
  people:
  - Julia Silge
  - Davis Vaughan
  - Hannah Frick
  readme_image: man/figures/logo.png
  repo: tidymodels/spatialsample
  stars: 76
  title: spatialsample
  website: https://spatialsample.tidymodels.org
---

spatialsample provides spatial resampling methods for cross-validation with the rsample package. It implements spatial clustering, spatial block, buffered, and leave-location-out cross-validation strategies designed specifically for spatial data.

Standard cross-validation can fail with spatial data because nearby observations are often similar, leading to overly optimistic performance estimates. spatialsample addresses this by creating resampling folds that account for spatial structure, ensuring training and test sets are spatially separated. The package integrates with the tidymodels ecosystem and includes visualization tools for examining fold assignments on maps.
