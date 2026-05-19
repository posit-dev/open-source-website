---
color: '#2E5F13'
description: An R package for tidyverse-friendly statistical inference
github: tidymodels/infer
image: logo.png
languages:
- R
latest_release: '2025-12-18T14:07:39+00:00'
people:
- Simon Couch
- Mine Çetinkaya-Rundel
- Emil Hvitfeldt
- Hannah Frick
- Julia Silge
- Teun Van den Brand
- Max Kuhn
title: infer
topics:
- Community
- Data Wrangling
- Machine Learning
- Visualization
website: https://infer.tidymodels.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: An R package for tidyverse-friendly statistical inference
  first_commit: '2017-06-05T17:41:42+00:00'
  forks: 87
  languages:
  - R
  last_updated: '2026-05-19T11:50:39.908001+00:00'
  latest_release: '2025-12-18T14:07:39+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Mine Çetinkaya-Rundel
  - Emil Hvitfeldt
  - Hannah Frick
  - Jeroen Janssens
  - Julia Silge
  - Teun Van den Brand
  - Max Kuhn
  readme_image: man/figures/logo.png
  repo: tidymodels/infer
  stars: 788
  title: infer
  website: https://infer.tidymodels.org
---

The infer package performs statistical inference using a tidy, grammar-based approach that integrates with the tidyverse. It provides four main verbs—`specify()`, `hypothesize()`, `generate()`, and `calculate()`—that work together to conduct randomization-based hypothesis tests and construct null distributions.

The package makes simulation-based inference accessible through an expressive, pipeline-style workflow. It supports various statistical tests including t-tests, ANOVA, and chi-square tests using a consistent interface. The package includes visualization tools to compare observed statistics against null distributions and calculate p-values, making it particularly useful for teaching and applying modern resampling-based inference methods.
