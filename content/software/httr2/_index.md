---
description: Make HTTP requests and process their responses. A modern reimagining
  of httr.
github: r-lib/httr2
image: logo.png
languages:
- R
latest_release: '2025-12-05T17:45:53+00:00'
people:
- Hadley Wickham
- Charlie Gao
- Jeroen Ooms
- Jenny Bryan
- Joe Cheng
- Neal Richardson
- Gábor Csárdi
- Jeroen Janssens
title: httr2
website: https://httr2.r-lib.org

external:  # updated automatically, do not edit
  description: Make HTTP requests and process their responses. A modern reimagining
    of httr.
  first_commit: '2018-11-22T15:32:29+00:00'
  forks: 85
  languages:
  - R
  last_updated: '2026-02-24T09:26:35.884455+00:00'
  latest_release: '2025-12-05T17:45:53+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Charlie Gao
  - Jeroen Ooms
  - Jenny Bryan
  - Joe Cheng
  - Neal Richardson
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/httr2
  stars: 259
  title: httr2
  website: https://httr2.r-lib.org
---

httr2 is a comprehensive HTTP client for R that provides a modern, pipeable API for working with web APIs. It allows you to create and modify request objects before executing them with `req_perform()`, replacing the need for separate `GET()`, `POST()`, and `DELETE()` functions.

The package includes built-in rate limiting and automatic retry capabilities for handling transient errors and API rate limits. It provides comprehensive OAuth support with customizable flows, automatic caching for cacheable responses, and tools for managing secrets and credentials securely. HTTP errors are automatically converted to R errors, and the package builds on curl to deliver robust functionality for API interactions.
