---
color: '#447099'
description: Access the Gmail RESTful API from R.
github: r-lib/gmailr
image: logo.svg
languages:
- R
latest_release: '2026-01-29T22:39:25+00:00'
people:
- Jenny Bryan
- Jeroen Janssens
- Joe Cheng
title: gmailr
website: https://gmailr.r-lib.org

external:  # updated automatically, do not edit
  description: Access the Gmail RESTful API from R.
  first_commit: '2014-07-09T16:54:55+00:00'
  forks: 55
  languages:
  - R
  last_updated: '2026-03-20T10:27:51.665148+00:00'
  latest_release: '2026-01-29T22:39:25+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Jeroen Janssens
  - Joe Cheng
  repo: r-lib/gmailr
  stars: 237
  title: gmailr
  website: https://gmailr.r-lib.org
---

gmailr exposes the Gmail API from R, allowing you to programmatically send, read, and manage Gmail messages and threads directly from R. It handles OAuth authentication and provides functions to compose emails from parts, send messages or drafts, and retrieve email data.

The package requires you to configure your own OAuth client for authentication, which gives you full control over API access and avoids shared credential limitations. It provides intuitive functions for building MIME messages piece by piece, creating drafts for review before sending, and accessing structured components of received emails like subject lines, bodies, and dates. This makes it useful for automated email workflows, monitoring inboxes, and integrating Gmail with R-based data pipelines.
