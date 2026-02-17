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
  description: Chrome Remote Interface for R
  first_commit: '2019-02-02T04:37:53+00:00'
  forks: 22
  languages:
  - R
  last_updated: '2026-02-17T11:21:46.372673+00:00'
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

Chromote provides an R interface to the Chrome DevTools Protocol, allowing you to programmatically control Chrome and Chromium-based browsers from R. It works with headless or visible browser sessions to automate browser interactions, take screenshots, and execute JavaScript.

The package offers both synchronous and asynchronous APIs for different use cases, includes convenience methods for common tasks like screenshots and viewport control, and automatically reconnects after connection interruptions. It provides full support for all Chrome DevTools Protocol commands and powers higher-level tools like shinytest2 and rvest's live HTML reading. The package can also install and manage specific Chrome versions through the Chrome for Testing service.
