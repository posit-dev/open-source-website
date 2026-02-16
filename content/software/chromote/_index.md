---
description: Chrome Remote Interface for R
github: rstudio/chromote
image: logo.png
languages:
- R
latest_release: '2025-04-24T12:46:38+00:00'
people:
- Winston Chang
- Garrick Aden-Buie
- Barret Schloerke
- Hadley Wickham
- Nick Strayer
title: chromote
website: https://rstudio.github.io/chromote/

external:
  contributors:
  - wch
  - gadenbuie
  - schloerke
  - alandipert
  - hadley
  - RLesur
  - colearendt
  - nstrayer
  - yutannihilation
  - zeloff
  - actions-user
  - bersbersbers
  - olivroy
  - stla
  description: Chrome Remote Interface for R
  first_commit: '2019-02-02T04:37:53+00:00'
  forks: 22
  languages:
  - R
  last_updated: '2026-02-13T14:17:03.926795+00:00'
  latest_release: '2025-04-24T12:46:38+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Garrick Aden-Buie
  - Barret Schloerke
  - Hadley Wickham
  - Nick Strayer
  readme_image: man/figures/logo.png
  repo: rstudio/chromote
  stars: 178
  title: chromote
  website: https://rstudio.github.io/chromote/
---

chromote is an R package that implements the Chrome DevTools Protocol, giving you programmatic control over Chrome and Chromium-based browsers directly from your R code. Whether you need to capture screenshots of visualizations, automate web interactions, or test web applications, chromote provides both user-friendly synchronous methods and powerful asynchronous interfaces to meet your needs. It works seamlessly with Chrome, Chromium, Opera, Vivaldi, and other compatible browsers, and even allows you to specify and control particular browser versions through the Chrome for Testing service.

As the foundation for popular tools like shinytest2 and rvest's live HTML reading capabilities, chromote brings professional-grade browser automation to the R ecosystem. It offers convenient helper functions for common tasks like taking screenshots and adjusting viewport sizes, while also providing full access to the complete Chrome DevTools Protocol for advanced use cases. The package automatically manages browser sessions and maintains persistent connections, letting you focus on your automation workflow rather than connection management. Whether you're building reproducible testing pipelines, scraping dynamic web content, or generating automated reports with web-based visualizations, chromote delivers reliable browser control that integrates naturally into your R-based data science workflows.