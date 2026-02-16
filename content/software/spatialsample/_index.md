---
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

external:
  contributors:
  - mikemahoney218
  - juliasilge
  - DavisVaughan
  - hfrick
  description: Create and summarize spatial resampling objects 🗺
  first_commit: '2021-01-19T21:06:51+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.688699+00:00'
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

When working with spatial data, traditional cross-validation methods can lead to overly optimistic model performance estimates due to spatial autocorrelation. The spatialsample package addresses this challenge by providing spatial resampling strategies designed specifically for geographic data. Building on the rsample framework within the tidymodels ecosystem, spatialsample creates efficient, memory-friendly resamples that account for the spatial structure in your data.

The package offers a suite of specialized resampling methods including spatial clustering cross-validation, spatial block cross-validation, spatially buffered cross-validation, and leave-location-out cross-validation. Each method helps ensure that your model evaluation reflects how well it will perform on truly independent spatial data. With built-in visualization tools through autoplot(), you can easily inspect your resampling strategy and verify that training and testing sets are appropriately separated in geographic space, making it an essential tool for geospatial machine learning workflows.
