---
description: Test coverage reports for R
github: r-lib/covr
image: logo.png
languages:
- R
latest_release: '2022-08-24T14:15:38+00:00'
people:
- Tomasz Kalinowski
- Hadley Wickham
- Gábor Csárdi
- Jeroen Ooms
title: covr
website: https://covr.r-lib.org

external:
  description: Test coverage reports for R
  first_commit: '2014-12-21T03:26:04+00:00'
  forks: 120
  languages:
  - R
  last_updated: '2026-02-17T11:32:38.609052+00:00'
  latest_release: '2022-08-24T14:15:38+00:00'
  license: NOASSERTION
  people:
  - Tomasz Kalinowski
  - Hadley Wickham
  - Gábor Csárdi
  - Jeroen Ooms
  readme_image: man/figures/logo.png
  repo: r-lib/covr
  stars: 344
  title: covr
  website: https://covr.r-lib.org
---

covr is an R package that tracks test coverage for R packages and generates coverage reports. It can display results locally or upload them to services like Codecov or Coveralls.

The package works by modifying package code to add tracking calls, measuring coverage for both R and compiled code. It supports flexible exclusion of files, functions, or individual lines from coverage analysis using various methods including special comments, configuration files, and function arguments. covr integrates with any R testing framework and includes an RStudio addin for convenient access during development.
