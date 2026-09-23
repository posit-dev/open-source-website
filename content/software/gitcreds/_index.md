---
image: logo.svg
color: "#72994E"
description: Query git credentials from R
github: r-lib/gitcreds
languages:
- R
latest_release: '2022-09-08T10:27:52+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
- Jeroen Janssens
title: gitcreds
website: https://gitcreds.r-lib.org/

external:  # updated automatically, do not edit
  description: Query git credentials from R
  first_commit: '2020-08-20T10:04:48+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-09-18T14:30:18.050828+00:00'
  latest_release: '2022-09-08T10:27:52+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jenny Bryan
  - Jeroen Janssens
  repo: r-lib/gitcreds
  stars: 30
  title: gitcreds
  website: https://gitcreds.r-lib.org/
---

gitcreds is an R package that queries and manages git credentials directly from R, letting users set a GitHub token once and reuse it across command line git, R scripts, and the RStudio IDE.

It stores credentials through git's own credential system rather than `.Renviron` files, which is typically more secure. The package supports multiple users and hosts (including GitHub Enterprise), includes a cache for fast credential lookup, and falls back to environment variables when git credential helpers aren't available. It also provides a simple API for package authors who need GitHub authentication, with specific error classes for handling missing credentials gracefully.
