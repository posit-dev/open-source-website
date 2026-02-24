---
description: Application-level automated tests for Shiny
github: rstudio/shinycoreci
languages:
- HTML
people:
- Barret Schloerke
- Carson Sievert
- Garrick Aden-Buie
- Winston Chang
- Joe Cheng
title: shinycoreci
website: https://rstudio.github.io/shinycoreci/

external:  # updated automatically, do not edit
  description: Application-level automated tests for Shiny
  first_commit: '2019-12-10T21:46:45+00:00'
  forks: 7
  languages:
  - HTML
  last_updated: '2026-02-24T09:26:18.475693+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  - Carson Sievert
  - Garrick Aden-Buie
  - Winston Chang
  - Joe Cheng
  repo: rstudio/shinycoreci
  stars: 48
  title: shinycoreci
  website: https://rstudio.github.io/shinycoreci/
---

shinycoreci is an R package designed for continuous integration testing of Shiny and related packages. It installs bleeding-edge development versions of Shiny ecosystem packages and runs comprehensive automated tests across multiple platforms and deployment environments.

The package provides tools to test Shiny apps in different environments including RStudio IDE, web browsers, shinyapps.io, Posit Connect, and Docker-based server configurations. It uses GitHub Actions workflows to automatically test apps on multiple operating systems and R versions, deploy to hosting platforms, and generate test result reports. The package leverages r-universe for hourly package updates and avoids GitHub API rate limits during testing.
