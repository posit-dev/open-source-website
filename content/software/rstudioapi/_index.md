---
description: Safely access RStudio's API (when available)
github: rstudio/rstudioapi
image: logo.png
languages:
- R
latest_release: '2024-10-16T22:39:47+00:00'
people:
- JJ Allaire
- Hadley Wickham
- Jenny Bryan
title: rstudioapi
website: http://rstudio.github.io/rstudioapi

external:
  contributors:
  - kevinushey
  - jjallaire
  - gtritchie
  - jmcphers
  - zachhannum
  - javierluraschi
  - hadley
  - jgutman
  - melissa-barca
  - andrie
  - MariaSemple
  - AshesITR
  - jennybc
  - romainfrancois
  - olivroy
  - atheriel
  - MichaelChirico
  - randyzwitch
  - salim-b
  - yihui
  - mutterer
  - shrektan
  - trestletech
  description: Safely access RStudio's API (when available)
  first_commit: '2014-01-10T11:37:40+00:00'
  forks: 36
  languages:
  - R
  last_updated: '2026-02-13T14:17:01.385614+00:00'
  latest_release: '2024-10-16T22:39:47+00:00'
  license: NOASSERTION
  people:
  - JJ Allaire
  - Hadley Wickham
  - Jenny Bryan
  readme_image: man/figures/logo.png
  repo: rstudio/rstudioapi
  stars: 173
  title: rstudioapi
  website: http://rstudio.github.io/rstudioapi
---

rstudioapi is an essential R package that provides a safe and reliable bridge between your R code and the RStudio IDE's powerful features. Designed specifically for package developers, it enables you to programmatically access RStudio's API while maintaining full CRAN compliance and gracefully handling environments where RStudio may not be available. The package includes built-in version checking and conditional execution capabilities, ensuring your code can leverage IDE features like the viewer pane, document manipulation, and project management without breaking when run in other R environments.

What makes rstudioapi particularly valuable is its defensive design philosophy. Rather than assuming RStudio is always present, the package provides functions to detect availability and verify version requirements before attempting API calls. This allows you to write robust packages that enhance the user experience within RStudio while maintaining full compatibility with command-line R, R GUI, and other development environments. Whether you're building interactive visualizations that leverage RStudio's viewer, creating document templates, or integrating with project workflows, rstudioapi provides the foundation for seamless IDE integration without sacrificing portability.
