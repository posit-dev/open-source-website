---
description: Explore correlations in R
github: tidymodels/corrr
image: logo.png
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

external:
  contributors:
  - drsimonj
  - juliasilge
  - edgararuiz-zz
  - edgararuiz
  - thisisdaryn
  - topepo
  - cimentadaj
  - jameslairdsmith
  - EmilHvitfeldt
  - krlmlr
  - jsta
  - hfrick
  - antoine-sachet
  - michaelgrund
  - s-scherrer
  description: Explore correlations in R
  first_commit: '2016-06-24T06:09:09+00:00'
  forks: 58
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.008843+00:00'
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

corrr is an R package that makes exploring correlations intuitive and seamless by treating correlation data as data frames rather than matrices. This design philosophy enables data scientists to leverage familiar tidyverse workflows when analyzing relationships between variables. The package provides functions for creating correlation data frames with `correlate()`, then manipulating them with tools like `shave()` to remove triangular redundancies, `rearrange()` to organize by correlation strength, and `focus()` to zoom in on specific variables.

Beyond data manipulation, corrr excels at visualization and presentation. The package includes `rplot()` for shape-based correlation plots, `network_plot()` for network visualizations, and `fashion()` for producing publication-ready correlation tables. With full compatibility across dplyr, tidyr, and ggplot2, corrr integrates naturally into modern data analysis pipelines. The package even supports database and Spark operations, automatically pushing calculations to the database for efficient analysis of large datasets.
