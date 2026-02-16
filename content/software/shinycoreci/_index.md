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

external:
  contributors:
  - schloerke
  - cpsievert
  - gadenbuie
  - wch
  - MadhulikaTanuboddi
  - karangattu
  - alandipert
  - guspan-tanadi
  - jcheng5
  - olivroy
  description: Application-level automated tests for Shiny
  first_commit: '2019-12-10T21:46:45+00:00'
  forks: 7
  languages:
  - HTML
  last_updated: '2026-02-13T14:17:04.463973+00:00'
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

shinycoreci is a comprehensive testing infrastructure package that ensures the stability and reliability of the Shiny ecosystem. Built by the core Shiny development team, it maintains an extensive suite of automated tests that continuously validate Shiny applications across multiple platforms including Ubuntu, macOS, and Windows. The package automatically tests the bleeding edge versions of 30+ critical Shiny-related packages such as bslib, htmltools, and shinytest2, catching integration issues and breaking changes before they reach production environments.

What sets shinycoreci apart is its ability to orchestrate tests across diverse deployment scenarios, from local RStudio IDE sessions to production environments like shinyapps.io and Posit Connect. By providing standardized testing frameworks and automated snapshot management, shinycoreci streamlines the development and contribution process for anyone working with Shiny. The public test results dashboard offers complete transparency into package health, helping both maintainers and contributors make informed decisions about ecosystem compatibility and stability.
