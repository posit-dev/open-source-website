---
color: '#62BC3D'
description: Quantify extrapolation of new samples given a training set
github: tidymodels/applicable
image: logo.png
languages:
- R
latest_release: '2026-02-26T03:05:08+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Julia Silge
- Hannah Frick
- Jeroen Janssens
title: applicable
website: https://applicable.tidymodels.org/

external:  # updated automatically, do not edit
  description: Quantify extrapolation of new samples given a training set
  first_commit: '2019-07-08T18:53:53+00:00'
  forks: 8
  languages:
  - R
  last_updated: '2026-03-20T10:27:44.834280+00:00'
  latest_release: '2026-02-26T03:05:08+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Julia Silge
  - Hannah Frick
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/applicable
  stars: 47
  title: applicable
  website: https://applicable.tidymodels.org/
---

The applicable package helps determine when model predictions may be unreliable by measuring how much new data points differ from the training set. It implements "applicability domain" methods to detect potential extrapolation.

This package is valuable for identifying when predictions should be treated with skepticism because the input data falls outside the model's training domain. It provides multiple methods for both binary and continuous data to quantify the degree of extrapolation. This is particularly useful in fields like chemistry and other scientific domains where prediction reliability is critical.
