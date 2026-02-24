---
description: Construct Modeling Packages
github: tidymodels/hardhat
image: logo.png
languages:
- R
latest_release: '2025-08-20T08:57:28+00:00'
people:
- Davis Vaughan
- Hannah Frick
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Simon Couch
- Gábor Csárdi
- Jeroen Janssens
title: hardhat
website: https://hardhat.tidymodels.org

external:  # updated automatically, do not edit
  description: Construct Modeling Packages
  first_commit: '2019-02-11T16:31:00+00:00'
  forks: 21
  languages:
  - R
  last_updated: '2026-02-24T09:26:27.216950+00:00'
  latest_release: '2025-08-20T08:57:28+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Hannah Frick
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Simon Couch
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/hardhat
  stars: 108
  title: hardhat
  website: https://hardhat.tidymodels.org
---

hardhat is a developer-focused R package designed to simplify the creation of new modeling packages while promoting consistent standards for R modeling interfaces. It provides infrastructure for preprocessing data at both fit time and prediction time.

The package offers four main capabilities: consistent data preprocessing with `mold()` and `forge()` functions, input validation to ensure prediction data matches training data structure, utility functions for common modeling tasks like adding intercepts and standardizing outputs, and a stricter reimagining of base R's preprocessing functions. This standardization reduces the implementation burden on package developers and creates predictable interfaces that benefit end users.
