---
description: Tools for creating tuning parameter values
github: tidymodels/dials
image: logo.png
languages:
- R
latest_release: '2025-09-04T09:26:12+00:00'
people:
- Hannah Frick
- Max Kuhn
- Emil Hvitfeldt
- Davis Vaughan
- Julia Silge
- Simon Couch
- Gábor Csárdi
- Jeroen Janssens
title: dials
website: https://dials.tidymodels.org/

external:  # updated automatically, do not edit
  description: Tools for creating tuning parameter values
  first_commit: '2018-07-23T03:07:49+00:00'
  forks: 33
  languages:
  - R
  last_updated: '2026-02-24T09:26:27.136812+00:00'
  latest_release: '2025-09-04T09:26:12+00:00'
  license: NOASSERTION
  people:
  - Hannah Frick
  - Max Kuhn
  - Emil Hvitfeldt
  - Davis Vaughan
  - Julia Silge
  - Simon Couch
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/dials
  stars: 116
  title: dials
  website: https://dials.tidymodels.org/
---

dials provides infrastructure for creating and managing tuning parameters in the tidymodels ecosystem. It defines parameter objects with their ranges, types, and transformations that other tidymodels packages use during model tuning.

The package standardizes how hyperparameters are represented across different modeling algorithms, making it easier to tune models consistently. It handles parameter transformations (like log scales), validates parameter ranges, and provides sensible defaults for common tuning parameters. dials serves as the foundation for the tune package, which performs the actual hyperparameter optimization.
