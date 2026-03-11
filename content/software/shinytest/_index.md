---
image: logo.svg
color: "#419599"
description: Automated testing for shiny apps
github: rstudio/shinytest
languages:
- JavaScript
latest_release: '2024-03-02T17:37:21+00:00'
people:
- Winston Chang
- Gábor Csárdi
- Carson Sievert
- Hadley Wickham
- Barret Schloerke
- Christophe Dervieux
- Joe Cheng
title: shinytest
website: https://rstudio.github.io/shinytest/

external:  # updated automatically, do not edit
  description: Automated testing for shiny apps
  first_commit: '2016-08-24T12:19:09+00:00'
  forks: 51
  languages:
  - JavaScript
  last_updated: '2026-03-05T16:11:08.942253+00:00'
  latest_release: '2024-03-02T17:37:21+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Gábor Csárdi
  - Carson Sievert
  - Hadley Wickham
  - Barret Schloerke
  - Christophe Dervieux
  - Joe Cheng
  repo: rstudio/shinytest
  stars: 226
  title: shinytest
  website: https://rstudio.github.io/shinytest/
---

shinytest provides automated testing for Shiny applications through a simulation-based approach that you can control programmatically. It enables you to script interactions with your app and verify behavior remains consistent across changes.

The package uses snapshot-based testing where initial test runs capture application state, and subsequent runs compare against those snapshots to detect regressions. However, shinytest is deprecated and relies on PhantomJS, which is no longer maintained, so it may not work with Shiny versions after 1.8.1. Users should migrate to shinytest2, which uses modern Chromium-based browsers.
