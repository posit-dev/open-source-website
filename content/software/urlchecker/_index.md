---
description: Run CRAN URL checks from older versions of R
github: r-lib/urlchecker
languages:
- R
latest_release: '2021-11-30T00:26:11+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jeroen Janssens
title: urlchecker
website: https://urlchecker.r-lib.org/

external:
  contributors:
  - jimhester
  - gaborcsardi
  - ateucher
  - dpprdan
  - hadley
  - jeroenjanssens
  - krlmlr
  description: Run CRAN URL checks from older versions of R
  first_commit: '2020-10-02T13:26:31+00:00'
  forks: 5
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.455183+00:00'
  latest_release: '2021-11-30T00:26:11+00:00'
  license: GPL-3.0
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jeroen Janssens
  repo: r-lib/urlchecker
  stars: 44
  title: urlchecker
  website: https://urlchecker.r-lib.org/
---

urlchecker is a lightweight tool designed to help R package developers maintain healthy, functional URLs throughout their documentation, vignettes, and code. When submitting packages to CRAN, all URLs are checked for validity, but this checking functionality is only available in newer versions of R. urlchecker brings these essential URL checks to older R versions, allowing you to catch broken links, outdated redirects, and invalid URLs before submission. The package leverages concurrent requests to scan URLs much faster than the built-in tools package, saving valuable time during package development and maintenance.

Beyond simple checking, urlchecker can automatically update URLs that have moved to new locations (301 redirects), ensuring your package documentation always points to the right place. Whether you're preparing a CRAN submission, maintaining an existing package, or simply want to keep your documentation links up-to-date, urlchecker provides a fast and reliable solution that integrates seamlessly into your R package development workflow.
