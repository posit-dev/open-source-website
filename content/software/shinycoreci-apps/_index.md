---
description: SUPERSEDED - Apps for Shiny continuous integration testing
github: rstudio/shinycoreci-apps
image: view-test-results.png
languages:
- JavaScript
people:
- Barret Schloerke
- Carson Sievert
- Winston Chang
- Joe Cheng
- Rich Iannone
title: shinycoreci-apps
website: ''

external:
  contributors:
  - MadhulikaTanuboddi
  - schloerke
  - cpsievert
  - wch
  - shalutiwari
  - actions-user
  - alandipert
  - jcheng5
  - rich-iannone
  description: SUPERSEDED - Apps for Shiny continuous integration testing
  first_commit: '2019-12-17T17:38:59+00:00'
  forks: 3
  languages:
  - JavaScript
  last_updated: '2026-02-13T14:17:04.479550+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  - Carson Sievert
  - Winston Chang
  - Joe Cheng
  - Rich Iannone
  readme_image: README_files/view-test-results.png
  repo: rstudio/shinycoreci-apps
  stars: 37
  title: shinycoreci-apps
  website: ''
---

Note: This repository is superseded. Its functionality has been merged into the main rstudio/shinycoreci project.

shinycoreci-apps provided comprehensive infrastructure for manual and automated testing of Shiny applications across diverse deployment environments. It enabled developers to validate their Shiny apps on multiple platforms including RStudio IDE, RStudio Server Pro, shinyapps.io, RStudio Connect, and specialized Docker environments. The project supported three complementary testing approaches: shinytest for screenshot-based validation, shinyjster for JavaScript DOM-level assertions, and testthat for server-side reactive logic testing, giving teams the flexibility to test every layer of their applications.

What made shinycoreci-apps particularly valuable was its integrated workflow combining manual testing capabilities with automated GitHub Actions workflows. Developers could view test results through an interactive Shiny dashboard, approve or reject visual baseline differences, and rely on automated nightly testing to catch regressions early. The system automatically managed dependencies and deployed test applications to various hosting platforms, providing a complete continuous integration solution specifically designed for the unique challenges of testing interactive Shiny applications.
