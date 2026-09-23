---
description: Foundation Model for Tabular Data via reticulate
github: tidymodels/tabpfn
languages:
- R
latest_release: '2026-09-02T13:12:10+00:00'
people:
- Max Kuhn
- Edgar Ruiz
- Tomasz Kalinowski
title: tabpfn
website: http://tabpfn.tidymodels.org/
external:
  description: Foundation Model for Tabular Data via reticulate
  first_commit: '2025-01-27T16:59:44+00:00'
  forks: 5
  languages:
  - R
  last_updated: '2026-09-18T14:24:33.845761+00:00'
  latest_release: '2026-09-02T13:12:10+00:00'
  license: Apache-2.0
  people:
  - Max Kuhn
  - Edgar Ruiz
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: tidymodels/tabpfn
  stars: 34
  title: tabpfn
  website: http://tabpfn.tidymodels.org/
image: logo.png
color: "#9FFAEB"
---

The tabpfn R package provides an interface to TabPFN (Prior-Fitted Networks), a deep-learning foundation model for tabular data that handles both classification and regression tasks. It wraps the Python TabPFN library via reticulate and exposes it through idiomatic R syntax with standard S3 methods, including formula, x/y, and recipes interfaces.

TabPFN is particularly effective on small tabular datasets, where it can produce accurate predictions without the extensive hyperparameter tuning that traditional models require. The package follows tidymodels conventions, always returning predictions as tibbles with standardized column names. It automatically manages its Python dependencies, installing them into a virtual environment on first use. A GPU is strongly recommended for practical performance, and starting with model version 2.5, users must accept the PriorLabs license and set a `TABPFN_TOKEN` environment variable.
