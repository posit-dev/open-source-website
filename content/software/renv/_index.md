---
description: 'renv: Project environments for R.'
github: rstudio/renv
image: logo.svg
languages:
- R
latest_release: '2025-07-24T22:49:27+00:00'
people:
- Hadley Wickham
- Christophe Dervieux
- JJ Allaire
- Jenny Bryan
- Garrick Aden-Buie
- Neal Richardson
title: renv
website: https://rstudio.github.io/renv/

external:  # updated automatically, do not edit
  description: 'renv: Project environments for R.'
  first_commit: '2018-11-28T20:25:39+00:00'
  forks: 163
  languages:
  - R
  last_updated: '2026-02-24T09:26:17.552858+00:00'
  latest_release: '2025-07-24T22:49:27+00:00'
  license: MIT
  people:
  - Hadley Wickham
  - Christophe Dervieux
  - JJ Allaire
  - Jenny Bryan
  - Garrick Aden-Buie
  - Neal Richardson
  readme_image: man/figures/logo.svg
  repo: rstudio/renv
  stars: 1134
  title: renv
  website: https://rstudio.github.io/renv/
---

renv helps you create reproducible environments for R projects by managing package dependencies. It ensures that each project has its own isolated library of packages with specific versions recorded in a lockfile.

renv solves the problem of projects breaking when packages are updated for other work by giving each project its own private package library. It makes projects portable across different computers and platforms by recording exact package versions in a lockfile that can be used to restore the same environment anywhere. The package uses a shared cache to make installing packages across multiple projects fast and efficient.
