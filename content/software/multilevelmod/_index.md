---
description: Parsnip wrappers for mixed-level and hierarchical models
github: tidymodels/multilevelmod
image: logo.png
color: "#FBB373"
languages:
- R
latest_release: '2022-06-17T12:13:05+00:00'
people:
- Hannah Frick
- Max Kuhn
- Emil Hvitfeldt
- Julia Silge
- Jeroen Janssens
title: multilevelmod
website: https://multilevelmod.tidymodels.org/

external:  # updated automatically, do not edit
  description: Parsnip wrappers for mixed-level and hierarchical models
  first_commit: '2020-04-23T22:54:06+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-03-05T16:23:17.485093+00:00'
  latest_release: '2022-06-17T12:13:05+00:00'
  license: NOASSERTION
  people:
  - Hannah Frick
  - Max Kuhn
  - Emil Hvitfeldt
  - Julia Silge
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/multilevelmod
  stars: 73
  title: multilevelmod
  website: https://multilevelmod.tidymodels.org/
---

multilevelmod enables the use of multi-level models (also called mixed-effects models, hierarchical models, or random effects models) within the tidymodels framework through the parsnip package. It provides a consistent interface for fitting these models across different computational engines.

The package supports multiple modeling engines including lme4, nlme, geepack, and rstanarm, covering linear, logistic, and Poisson regression with random effects. It allows you to specify models using standard mixed model formula syntax (like `(Days | Subject)`) while working within the tidymodels ecosystem. This makes it possible to use mixed models in tidymodels workflows alongside preprocessing, tuning, and validation tools.
