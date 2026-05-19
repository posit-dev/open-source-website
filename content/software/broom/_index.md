---
color: '#E17817'
description: Convert statistical analysis objects from R into tidy format
github: tidymodels/broom
image: logo.png
languages:
- R
latest_release: '2026-05-13T23:36:12+00:00'
people:
- Simon Couch
- Max Kuhn
- Emil Hvitfeldt
- Hadley Wickham
- Julia Silge
- Davis Vaughan
- Hannah Frick
- Jenny Bryan
tags:
- tidyverse
title: broom
topics:
- Data Wrangling
- Machine Learning
- Visualization
website: https://broom.tidymodels.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Convert statistical analysis objects from R into tidy format
  first_commit: '2014-09-11T19:17:04+00:00'
  forks: 303
  languages:
  - R
  last_updated: '2026-05-19T11:50:25.230574+00:00'
  latest_release: '2026-05-13T23:36:12+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Max Kuhn
  - Emil Hvitfeldt
  - Hadley Wickham
  - Julia Silge
  - Davis Vaughan
  - Hannah Frick
  - Jeroen Janssens
  - Jenny Bryan
  readme_image: man/figures/logo.png
  repo: tidymodels/broom
  stars: 1514
  title: broom
  website: https://broom.tidymodels.org
---

broom summarizes statistical model outputs into tidy tibbles, making model information easy to work with in R. It provides three main functions: `tidy()` extracts component-level information like regression coefficients, `glance()` returns model-level statistics like R-squared, and `augment()` adds observation-level data like fitted values and residuals to datasets.

The package supports over 100 models from popular R packages plus most base R statistical models. It solves the problem of inconsistent model output formats by converting them into consistent, rectangular data structures that work seamlessly with tidyverse tools for visualization and analysis. All augmented columns use a `.` prefix to avoid overwriting existing data.
