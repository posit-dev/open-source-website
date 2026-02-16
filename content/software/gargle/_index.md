---
description: Infrastructure for calling Google APIs from R, including auth
github: r-lib/gargle
languages:
- R
latest_release: '2026-01-28T21:11:46+00:00'
people:
- Jenny Bryan
- Joe Cheng
- Hadley Wickham
- Jeroen Janssens
- Gábor Csárdi
title: gargle
website: https://gargle.r-lib.org/

external:
  contributors:
  - jennybc
  - craigcitro
  - jcheng5
  - hadley
  - batpigandme
  - maelle
  - jimhester
  - MarkEdmondson1234
  - wlongabaugh
  - yihui
  - tanho63
  - samterfa
  - michaelquinn32
  - MichaelChirico
  - jdtrat
  - jeroenjanssens
  - jimjam-slam
  - gaborcsardi
  - collinberke
  - drmowinckels
  - acroz
  - pettyalex
  - alexkgold
  - campbead
  description: Infrastructure for calling Google APIs from R, including auth
  first_commit: '2015-12-24T19:53:03+00:00'
  forks: 39
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.937100+00:00'
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

Gargle provides robust infrastructure for working with Google's extensive ecosystem of APIs from R. Whether you're accessing Google Sheets, Drive, Analytics, or any of Google's 250+ available APIs, gargle eliminates the complexity of authentication and HTTP request management, allowing you to focus on your data analysis rather than the technical plumbing. The package serves as the foundation for many popular R packages that wrap Google APIs, offering a battle-tested solution for credential management and API communication.

At its core, gargle solves two critical challenges: authentication and request handling. Its intelligent `token_fetch()` function automatically attempts multiple authentication methods including service accounts, application default credentials, and OAuth2 flows, with user-level token caching for seamless workflow integration. For package developers building Google API wrappers, gargle provides a comprehensive toolkit for constructing API calls, submitting requests, and processing responses using Google's Discovery Document specifications. While primarily designed for package authors, data scientists working directly with Google APIs will appreciate gargle's low-level control and flexibility for custom integrations.
