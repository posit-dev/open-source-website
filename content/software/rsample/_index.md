---
description: Classes and functions to create and summarize resampling objects
github: tidymodels/rsample
image: logo.png
languages:
- R
latest_release: '2026-01-30T11:52:49+00:00'
people:
- Hannah Frick
- Max Kuhn
- Julia Silge
- Davis Vaughan
- Emil Hvitfeldt
- Simon Couch
- Jeroen Janssens
- Gábor Csárdi
title: rsample
website: https://rsample.tidymodels.org

external:  # updated automatically, do not edit
  description: Classes and functions to create and summarize resampling objects
  first_commit: '2017-04-22T19:19:58+00:00'
  forks: 68
  languages:
  - R
  last_updated: '2026-02-24T09:26:26.957593+00:00'
  latest_release: '2026-01-30T11:52:49+00:00'
  license: NOASSERTION
  people:
  - Hannah Frick
  - Max Kuhn
  - Julia Silge
  - Davis Vaughan
  - Emil Hvitfeldt
  - Simon Couch
  - Jeroen Janssens
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: tidymodels/rsample
  stars: 340
  title: rsample
  website: https://rsample.tidymodels.org
---

rsample provides functions to create different types of resamples (like bootstraps, cross-validation folds, and train/test splits) for R data analysis. It's designed as a modular toolset for generating resampled datasets to estimate sampling distributions or evaluate model performance using holdout sets.

The package uses a memory-efficient approach where resampled datasets don't duplicate the original data in memory—creating 50 bootstrap samples uses only about 2.5 times the memory of the original dataset rather than 50 times. rsample focuses specifically on creating and managing resamples rather than modeling or statistics calculation, making it a foundational building block that integrates with other tidymodels packages. It's part of the tidymodels ecosystem for machine learning workflows in R.
