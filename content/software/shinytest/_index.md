---
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

external:
  contributors:
  - wch
  - gaborcsardi
  - cpsievert
  - hadley
  - trestletech
  - schloerke
  - javierluraschi
  - daattali
  - rpodcast
  - maxheld83
  - farrjere
  - alexkgold
  - cderv
  - FerandDalatieh
  - jcheng5
  - jmcphers
  - krlmlr
  - mpaulacaldas
  - octaviancorlade
  description: Automated testing for shiny apps
  first_commit: '2016-08-24T12:19:09+00:00'
  forks: 51
  languages:
  - JavaScript
  last_updated: '2026-02-13T14:17:02.483360+00:00'
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

shinytest was an R package designed to bring automated testing capabilities to Shiny applications through a snapshot-based testing approach. It enabled developers to script interactions with their apps, capture application states as baseline snapshots, and automatically detect regressions by comparing subsequent test runs against these baselines. This workflow helped teams maintain quality and catch bugs early by verifying that user interactions produced consistent, expected results without manual testing.

Note that shinytest is now deprecated and may not work with Shiny versions after 1.8.1 due to its dependency on PhantomJS, an outdated headless browser that is no longer maintained. For automated testing of modern Shiny applications, please use shinytest2, which leverages contemporary Chromium-based browser technology and provides enhanced testing capabilities for today's Shiny apps.
