---
color: '#F7AD63'
description: High-Level Modeling Functions with 'torch'
github: tidymodels/brulee
image: logo.png
languages:
- R
latest_release: '2025-09-02T10:44:03+00:00'
people:
- Max Kuhn
- Daniel Falbel
- Hannah Frick
- Emil Hvitfeldt
- Gábor Csárdi
- Julia Silge
title: brulee
website: https://brulee.tidymodels.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: High-Level Modeling Functions with 'torch'
  first_commit: '2020-08-19T21:34:01+00:00'
  forks: 9
  languages:
  - R
  last_updated: '2026-03-20T10:27:45.234697+00:00'
  latest_release: '2025-09-02T10:44:03+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Daniel Falbel
  - Hannah Frick
  - Emil Hvitfeldt
  - Gábor Csárdi
  - Julia Silge
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/brulee
  stars: 74
  title: brulee
  website: https://brulee.tidymodels.org/
---

brulee provides basic statistical and machine learning models implemented using the torch package infrastructure in R. It includes neural networks, linear regression, logistic regression, and multinomial regression, all with consistent tidymodels-style interfaces.

The package offers formula, x/y, and recipe-based interfaces for model fitting, making it compatible with tidymodels workflows. It returns predictions as tibbles following tidymodels conventions, and supports preprocessing through the recipes package for tasks like transformations and standardization. By leveraging torch as the backend, it provides access to modern deep learning infrastructure while maintaining familiar R modeling syntax.
