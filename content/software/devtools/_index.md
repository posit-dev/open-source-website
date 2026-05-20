---
color: '#056793'
description: Tools to make an R developer's life easier
github: r-lib/devtools
image: logo.png
languages:
- R
latest_release: '2026-04-29T15:42:10+00:00'
people:
- Hadley Wickham
- Winston Chang
- Jenny Bryan
- Gábor Csárdi
- Jeroen Ooms
- Lionel Henry
- Thomas Lin Pedersen
- JJ Allaire
- Joe Cheng
- Julia Silge
title: devtools
topics:
- Best Practices
website: https://devtools.r-lib.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Tools to make an R developer's life easier
  first_commit: '2010-05-03T04:08:49+00:00'
  forks: 761
  languages:
  - R
  last_updated: '2026-05-20T08:05:54.553234+00:00'
  latest_release: '2026-04-29T15:42:10+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  - Jenny Bryan
  - Gábor Csárdi
  - Jeroen Ooms
  - Lionel Henry
  - Thomas Lin Pedersen
  - JJ Allaire
  - Joe Cheng
  - Julia Silge
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/devtools
  stars: 2509
  title: devtools
  website: https://devtools.r-lib.org
---

devtools is an R package that simplifies the workflow of developing R packages by providing functions for common tasks like loading code, generating documentation, running tests, and building packages.

The package streamlines iterative development through functions like `load_all()` for instantly testing changes without reinstalling, `document()` for updating documentation, and `check()` for validating package structure. It also provides installation helpers for packages from GitHub, GitLab, and other sources. devtools has been modularized into focused packages (like testthat, roxygen2, and usethis) that it automatically loads, giving developers a comprehensive toolkit through a single library call.
