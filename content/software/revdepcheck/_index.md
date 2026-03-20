---
color: '#D44000'
description: R package reverse dependency checking
github: r-lib/revdepcheck
image: logo.svg
languages:
- R
people:
- Gábor Csárdi
- Hadley Wickham
- Jenny Bryan
- Lionel Henry
- Davis Vaughan
- Christophe Dervieux
title: revdepcheck
website: https://revdepcheck.r-lib.org

external:  # updated automatically, do not edit
  description: R package reverse dependency checking
  first_commit: '2016-08-06T20:40:42+00:00'
  forks: 33
  languages:
  - R
  last_updated: '2026-03-20T10:27:52.733998+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jenny Bryan
  - Lionel Henry
  - Davis Vaughan
  - Christophe Dervieux
  repo: r-lib/revdepcheck
  stars: 103
  title: revdepcheck
  website: https://revdepcheck.r-lib.org
---

revdepcheck runs R CMD check on all reverse dependencies of your package to identify if your changes break any dependent packages. It compares check results between the CRAN version and your development version, reporting only the differences.

The package addresses the false positive problem by running checks twice (once for each version) and uses crancache to speed up dependency installation. Checks run in parallel with a 10-minute timeout per package, and it can resume interrupted runs from where they left off. It generates summary reports showing which packages have new failures, helping you assess the downstream impact of your changes before releasing to CRAN.
