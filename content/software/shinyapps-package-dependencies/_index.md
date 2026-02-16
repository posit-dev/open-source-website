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
  contributors:
  - jspiewak
  - muschellij2
  - jforest
  - kippandrew
  - cbarraford
  - stevenolen
  - colearendt
  - bronsonk0619
  - RLesur
  - samperman
  - mbaynton
  - edzer
  - michaelmayer2
  - jjallaire
  - vrsarah
  - jeroen
  - davidfstein
  - mslynch
  - mcbex
  - oganm
  - cpsievert
  - fBedecarrats
  - maxheld83
  - jacobaclarke
  - ssinnott
  - kimsjune
  - aoles
  - vjcitn
  - noamross
  - Matt-Brigida
  - kgilds
  - Marlin-Na
  - jacobclarke
  - pyltime
  - schloerke
  - anamariaelek
  description: Collection of bash scripts that install R package system dependencies
  first_commit: '2014-08-08T04:57:26+00:00'
  forks: 57
  languages:
  - R
  last_updated: '2026-02-13T14:17:01.526264+00:00'
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

Many R packages require external software libraries and system-level dependencies to function properly. When deploying Shiny applications to shinyapps.io, these dependencies need to be installed on the hosting environment, which can create deployment friction and mysterious failures. The shinyapps-package-dependencies project solves this problem by automatically installing the necessary system dependencies for R packages deployed to the platform.

This community-driven collection of bash scripts ensures that data scientists and developers can deploy their applications with confidence, knowing that the underlying system requirements will be handled transparently. By maintaining a comprehensive repository of dependency installation scripts, the project enables broader package compatibility on shinyapps.io and eliminates the need for manual dependency configuration. Developers can also contribute support for new packages or request additions through GitHub issues, making the system continuously adaptable to the evolving R ecosystem.
