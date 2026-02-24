---
description: A lightweight, cross-platform, portable, and easy-to-maintain LaTeX distribution
  based on TeX Live
github: rstudio/tinytex
image: logo-tinytex.png
languages:
- R
latest_release: '2025-11-19T14:28:59+00:00'
people:
- Christophe Dervieux
- JJ Allaire
title: tinytex
website: https://yihui.org/tinytex/

external:  # updated automatically, do not edit
  description: A lightweight, cross-platform, portable, and easy-to-maintain LaTeX
    distribution based on TeX Live
  first_commit: '2017-11-16T21:24:02+00:00'
  forks: 123
  languages:
  - R
  last_updated: '2026-02-24T09:26:16.807973+00:00'
  latest_release: '2025-11-19T14:28:59+00:00'
  license: NOASSERTION
  people:
  - Christophe Dervieux
  - JJ Allaire
  readme_image: https://yihui.org/images/logo-tinytex.png
  repo: rstudio/tinytex
  stars: 1089
  title: tinytex
  website: https://yihui.org/tinytex/
---

TinyTeX is a lightweight LaTeX distribution based on TeX Live that starts small but automatically installs missing packages as needed. It solves the common problem where basic LaTeX installations are too minimal to work while full installations waste gigabytes on packages you'll never use.

The package handles LaTeX package management automatically, particularly for R Markdown users who won't need to manually install missing `.sty` files or learn complex `tlmgr` commands. This repo includes both the TinyTeX installation scripts and an R companion package that integrates LaTeX compilation into R workflows. The automatic package installation means you can focus on document creation rather than LaTeX distribution maintenance.
