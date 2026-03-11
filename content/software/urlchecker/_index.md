---
color: '#447099'
description: Run CRAN URL checks from older versions of R
github: r-lib/urlchecker
image: logo.svg
languages:
- R
latest_release: '2021-11-30T00:26:11+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jeroen Janssens
title: urlchecker
website: https://urlchecker.r-lib.org/

external:  # updated automatically, do not edit
  description: Run CRAN URL checks from older versions of R
  first_commit: '2020-10-02T13:26:31+00:00'
  forks: 5
  languages:
  - R
  last_updated: '2026-03-05T16:29:41.804900+00:00'
  latest_release: '2021-11-30T00:26:11+00:00'
  license: GPL-3.0
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jeroen Janssens
  repo: r-lib/urlchecker
  stars: 45
  title: urlchecker
  website: https://urlchecker.r-lib.org/
---

urlchecker validates URLs in R packages and automatically updates redirected links. It provides the same URL checking functionality that CRAN performs during package submission, but works with older R versions (pre-4.1).

The package uses concurrent requests to check URLs much faster than R's built-in tools package. It can detect broken links and automatically update 301 redirects to their new locations, saving manual work during package maintenance. This helps developers ensure their package documentation and URLs stay current before CRAN submission.
