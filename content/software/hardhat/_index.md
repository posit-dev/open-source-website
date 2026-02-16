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

external:
  contributors:
  - DavisVaughan
  - hfrick
  - EmilHvitfeldt
  - topepo
  - juliasilge
  - simonpcouch
  - brookslogan
  - dajmcdon
  - gaborcsardi
  - jeroenjanssens
  - LouisMPenrod
  - marlycormar
  description: Construct Modeling Packages
  first_commit: '2019-02-11T16:31:00+00:00'
  forks: 21
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.278389+00:00'
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

Hardhat is a developer-focused R package that streamlines the creation of new modeling packages by providing a standardized infrastructure aligned with tidymodels conventions. If you're building statistical or machine learning models in R, hardhat handles the boilerplate code so you can focus on writing the core implementation of your model, ensuring consistency across the tidymodels ecosystem and reducing development time.

The package offers essential tools for common modeling workflows, including `mold()` and `forge()` for data preprocessing at fitting and prediction time, centralized validation functions to ensure data consistency, and modernized alternatives to base R's preprocessing infrastructure. Hardhat also provides utilities for handling intercept columns, standardizing predict output, and managing predictor metadata like classes and factor levels, making it easier to build robust, production-ready modeling packages that work seamlessly with other tidymodels tools.
