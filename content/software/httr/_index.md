---
image: logo.svg
color: "#E7B10A"
description: 'httr: a friendly http package for R'
github: r-lib/httr
languages:
- R
latest_release: '2026-02-13T13:25:34+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Jeroen Ooms
- Christophe Dervieux
- Gábor Csárdi
- Charlotte Wickham
title: httr
website: https://httr.r-lib.org

external:  # updated automatically, do not edit
  description: 'httr: a friendly http package for R'
  first_commit: '2011-11-11T15:05:00+00:00'
  forks: 1966
  languages:
  - R
  last_updated: '2026-03-05T16:24:55.151127+00:00'
  latest_release: '2026-02-13T13:25:34+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Jeroen Ooms
  - Christophe Dervieux
  - Gábor Csárdi
  - Charlotte Wickham
  repo: r-lib/httr
  stars: 983
  title: httr
  website: https://httr.r-lib.org
---

httr is an R package that provides a user-friendly wrapper around the curl package for working with HTTP and web APIs. It's now superseded by httr2, which is recommended for new projects.

The package simplifies HTTP requests with dedicated functions for common verbs (GET, POST, PUT, DELETE, etc.) and handles connection management, cookies, and SSL certificates automatically. It provides flexible response parsing (raw, text, JSON, XML, HTML, images), authentication support including OAuth 1.0 and 2.0, and configuration helpers for timeouts, headers, proxies, and progress tracking. The standardized response object makes it straightforward to extract status, headers, and body content from API calls.
