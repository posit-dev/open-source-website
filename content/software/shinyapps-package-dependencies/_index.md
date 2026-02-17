---
description: Collection of bash scripts that install R package system dependencies
github: rstudio/shinyapps-package-dependencies
languages:
- R
people:
- JJ Allaire
- Jeroen Ooms
- Carson Sievert
- Barret Schloerke
title: shinyapps-package-dependencies
website: https://www.shinyapps.io/

external:
  description: Collection of bash scripts that install R package system dependencies
  first_commit: '2014-08-08T04:57:26+00:00'
  forks: 57
  languages:
  - R
  last_updated: '2026-02-17T11:16:41.112768+00:00'
  license: NOASSERTION
  people:
  - JJ Allaire
  - Jeroen Ooms
  - Carson Sievert
  - Barret Schloerke
  repo: rstudio/shinyapps-package-dependencies
  stars: 79
  title: shinyapps-package-dependencies
  website: https://www.shinyapps.io/
---

This repository defines system-level dependencies required by R packages when deploying to shinyapps.io. When your Shiny application uses an R package that needs external libraries or software (beyond R itself), this repository ensures those dependencies are automatically installed on the hosting server.

The repository solves the problem of R packages failing at runtime due to missing system libraries. It provides a centralized, tested mapping between R packages and their required system dependencies. Contributors can add support for additional packages by opening issues or submitting pull requests following the contribution guidelines.
