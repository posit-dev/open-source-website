---
description: Packrat is a dependency management system for R
github: rstudio/packrat
languages:
- R
latest_release: '2025-06-16T19:36:33+00:00'
people:
- Joe Cheng
- JJ Allaire
- Barret Schloerke
- Christophe Dervieux
- Hadley Wickham
title: packrat
website: http://rstudio.github.io/packrat/

external:  # updated automatically, do not edit
  description: Packrat is a dependency management system for R
  first_commit: '2013-10-08T21:29:27+00:00'
  forks: 89
  languages:
  - R
  last_updated: '2026-02-24T09:26:14.517852+00:00'
  latest_release: '2025-06-16T19:36:33+00:00'
  people:
  - Joe Cheng
  - JJ Allaire
  - Barret Schloerke
  - Christophe Dervieux
  - Hadley Wickham
  repo: rstudio/packrat
  stars: 407
  title: packrat
  website: http://rstudio.github.io/packrat/
---

Packrat is a dependency management system for R that creates isolated, private package libraries for individual projects. It records the exact package versions a project depends on and ensures those specific versions are installed consistently across different computers and platforms.

Packrat solves the problem of package version conflicts between projects by giving each project its own private library, preventing changes in one project from affecting others. It makes projects portable and reproducible by bundling package dependencies with the project and maintaining a snapshot of exact package versions. The package has been superseded by renv, but continues to be maintained, and projects can migrate using `renv::migrate()`.
