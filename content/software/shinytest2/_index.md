---
description: ''
github: rstudio/shinytest2
image: logo.svg
languages:
- R
latest_release: '2026-01-09T21:28:50+00:00'
people:
- Barret Schloerke
- Carson Sievert
- Garrick Aden-Buie
- Charlie Gao
- Jeroen Ooms
- Winston Chang
title: shinytest2
website: https://rstudio.github.io/shinytest2/

external:
  contributors:
  - schloerke
  - cpsievert
  - gadenbuie
  - russHyde
  - shikokuchuo
  - Copilot
  - kierisi
  - DivadNojnarg
  - olivroy
  - daattali
  - IndrajeetPatil
  - jeroen
  - LouisLeNezet
  - maxheld83
  - MikeJohnPage
  - AskPascal
  - Riraro
  - torockel
  - wch
  - gladkia
  description: ''
  first_commit: '2021-07-06T19:41:56+00:00'
  forks: 21
  languages:
  - R
  last_updated: '2026-02-13T14:17:05.215783+00:00'
  latest_release: '2026-01-09T21:28:50+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  - Carson Sievert
  - Garrick Aden-Buie
  - Charlie Gao
  - Jeroen Ooms
  - Winston Chang
  readme_image: man/figures/logo.svg
  repo: rstudio/shinytest2
  stars: 120
  title: shinytest2
  website: https://rstudio.github.io/shinytest2/
---

Testing Shiny applications manually is time-consuming, inconsistent, and doesn't scale well as your application grows. shinytest2 solves this problem by providing automated unit testing for Shiny apps that integrates seamlessly with the testthat framework. Using a headless Chrome browser, shinytest2 renders your application and lets you record your interactions as reproducible test code, ensuring that your app behaves correctly as you develop new features, fix bugs, or update dependencies.

The package is designed with developer experience in mind, offering intuitive functions like `record_test()` to visually capture user interactions, and `use_shinytest2()` to quickly set up your testing infrastructure. By automating the testing process, shinytest2 helps you catch regressions early, reduces the burden of manual testing, and gives you confidence that your Shiny applications will work as expected in production. Whether you're maintaining a small dashboard or a complex data application, shinytest2 makes it practical to establish a robust testing workflow.
