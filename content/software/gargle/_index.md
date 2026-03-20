---
color: '#404041'
description: Infrastructure for calling Google APIs from R, including auth
github: r-lib/gargle
image: logo.svg
languages:
- R
latest_release: '2026-01-28T21:11:46+00:00'
people:
- Jenny Bryan
- Joe Cheng
- Hadley Wickham
- Gábor Csárdi
title: gargle
website: https://gargle.r-lib.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Infrastructure for calling Google APIs from R, including auth
  first_commit: '2015-12-24T19:53:03+00:00'
  forks: 39
  languages:
  - R
  last_updated: '2026-03-20T10:27:52.305283+00:00'
  latest_release: '2026-01-28T21:11:46+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Joe Cheng
  - Hadley Wickham
  - Jeroen Janssens
  - Gábor Csárdi
  repo: r-lib/gargle
  stars: 114
  title: gargle
  website: https://gargle.r-lib.org/
---

gargle is an R package that simplifies working with Google APIs by handling authentication and HTTP request/response processing. It's primarily designed for R package developers who are building wrappers around Google's ~250 APIs, serving a similar role to Google's official client libraries.

The package supports multiple authentication methods including service accounts, application default credentials, Google Compute Engine, workload identity federation, and OAuth2 browser flow. It provides enhanced OAuth2 token management with user-level caching and email-based identity tracking. gargle also includes utilities for preparing API requests (optionally using Discovery Document specifications), executing them, and processing responses.
