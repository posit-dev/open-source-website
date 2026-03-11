---
description: Explore correlations in R
github: tidymodels/corrr
image: logo.png
color: "#8CC4FC"
languages:
- R
latest_release: '2022-08-16T19:52:49+00:00'
people:
- Julia Silge
- Edgar Ruiz
- Max Kuhn
- Emil Hvitfeldt
- Hannah Frick
title: corrr
website: https://corrr.tidymodels.org

external:  # updated automatically, do not edit
  description: Explore correlations in R
  first_commit: '2016-06-24T06:09:09+00:00'
  forks: 58
  languages:
  - R
  last_updated: '2026-03-05T16:22:05.303962+00:00'
  latest_release: '2022-08-16T19:52:49+00:00'
  license: NOASSERTION
  people:
  - Julia Silge
  - Edgar Ruiz
  - Max Kuhn
  - Emil Hvitfeldt
  - Hannah Frick
  readme_image: man/figures/logo.png
  repo: tidymodels/corrr
  stars: 590
  title: corrr
  website: https://corrr.tidymodels.org
---

corrr is an R package for exploring correlations by creating and working with data frames of correlations instead of matrices. It's designed to integrate with tidyverse tools and data pipelines, making correlation analysis more accessible through data frame operations.

The package returns correlations as tidy data frames with standardized variances set to NA and uses pairwise deletion by default. It provides functions to reshape correlation data (shave triangles, rearrange by strength, focus on subsets, stretch to long format), visualize correlations (rplot with shapes, network plots), and format output for printing. The correlate() function also works directly with database tables, automatically pushing calculations to the database and returning results that integrate with the rest of the corrr API.
