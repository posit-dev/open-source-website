---
description: An R package for interacting with the Posit Connect server API
github: posit-dev/connectapi
image: logo.svg
languages:
- R
latest_release: '2026-01-14T19:19:58+00:00'
people:
- Neal Richardson
- Hadley Wickham
- Barret Schloerke
title: connectapi
website: https://posit-dev.github.io/connectapi/

external:
  contributors:
  - colearendt
  - toph-allen
  - nealrichardson
  - tbradley1013
  - andrie
  - aronatkins
  - karawoo
  - ian-flores
  - hadley
  - jonkeane
  - mconflitti-pbc
  - schloerke
  - AntLP
  - christierney
  - csgillespie
  - cormach
  - dbkegley
  - jonthegeek
  - JoshRosenstein
  - MichaelChirico
  - fh-mthomson
  - slodge
  - olivroy
  description: An R package for interacting with the Posit Connect server API
  first_commit: '2019-01-23T20:32:57+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-02-13T14:16:45.276018+00:00'
  latest_release: '2026-01-14T19:19:58+00:00'
  license: NOASSERTION
  people:
  - Neal Richardson
  - Hadley Wickham
  - Barret Schloerke
  readme_image: man/figures/logo.svg
  repo: posit-dev/connectapi
  stars: 52
  title: connectapi
  website: https://posit-dev.github.io/connectapi/
---

connectapi is an R client for the Posit Connect Server API that enables data scientists and administrators to programmatically manage and interact with Posit Connect. It provides a comprehensive suite of functions to automate common tasks such as deploying content, managing user access and permissions, retrieving usage analytics, and configuring content settings like vanity URLs and thumbnails. By putting Connect administration and deployment workflows directly into R, connectapi eliminates manual repetition and enables version-controlled, reproducible management of your data science infrastructure.

What makes connectapi particularly valuable is its focus on real-world deployment scenarios and cross-environment workflows. Whether you need to migrate content between development and production servers, automate bulk operations across multiple dashboards, or programmatically retrieve user and group information for reporting, connectapi streamlines these tasks with intuitive functions. The package maintains backwards compatibility with Posit Connect versions dating back to 2022.10.0, providing clear error messages when version-specific features are unavailable, so teams can confidently build automation tools that work across their entire Connect infrastructure.
