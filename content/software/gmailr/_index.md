---
description: Access the Gmail RESTful API from R.
github: r-lib/gmailr
languages:
- R
latest_release: '2026-01-29T22:39:25+00:00'
people:
- Jenny Bryan
- Jeroen Janssens
- Joe Cheng
title: gmailr
website: https://gmailr.r-lib.org

external:
  contributors:
  - jimhester
  - jennybc
  - lawremi
  - kazuya030
  - batpigandme
  - prithajnath
  - alkashef
  - absuag
  - ismayc
  - jeroenjanssens
  - jcheng5
  - jlegewie
  - lwjohnst86
  - maelle
  - obarisk
  description: Access the Gmail RESTful API from R.
  first_commit: '2014-07-09T16:54:55+00:00'
  forks: 55
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.606601+00:00'
  latest_release: '2026-01-29T22:39:25+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Jeroen Janssens
  - Joe Cheng
  repo: r-lib/gmailr
  stars: 236
  title: gmailr
  website: https://gmailr.r-lib.org
---

gmailr is an R package that provides programmatic access to Gmail's RESTful API, enabling you to manage email directly from your R scripts and workflows. Whether you need to automatically send analysis reports, monitor incoming data requests, or integrate email communications into your data pipelines, gmailr eliminates the need for manual email management. The package handles OAuth authentication seamlessly, so after a one-time setup through Google's developer console, you can focus on building email workflows that integrate naturally with your R code.

The package offers a comprehensive set of tools for composing, sending, and retrieving emails. You can construct messages using intuitive helper functions like gm_mime(), gm_to(), and gm_subject(), create drafts for review before sending, and programmatically access your inbox to retrieve threads and messages. With accessor functions for email metadata and content, gmailr makes it easy to extract information like dates, subjects, and message bodies for analysis. This makes gmailr particularly valuable for data scientists who need to automate reporting workflows, researchers managing collaborative projects via email, or developers building R-based applications that require email integration.