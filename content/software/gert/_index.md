---
color: '#4F8DDC'
description: Simple git client for R
github: r-lib/gert
image: logo.png
languages:
- R
latest_release: '2024-07-18T11:32:08+00:00'
people:
- Jeroen Ooms
- Jenny Bryan
- Mine Çetinkaya-Rundel
- Davis Vaughan
title: gert
website: https://docs.ropensci.org/gert/

external:  # updated automatically, do not edit
  description: Simple git client for R
  first_commit: '2018-10-19T09:11:55+00:00'
  forks: 38
  languages:
  - R
  last_updated: '2026-03-20T10:27:54.832102+00:00'
  latest_release: '2024-07-18T11:32:08+00:00'
  license: NOASSERTION
  people:
  - Jeroen Ooms
  - Jenny Bryan
  - Mine Çetinkaya-Rundel
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: r-lib/gert
  stars: 157
  title: gert
  website: https://docs.ropensci.org/gert/
---

Gert is a Git client for R that provides a simple interface to Git operations through R functions. It's built on libgit2 and designed for users who need programmatic Git access without leaving R.

Gert handles authentication automatically by integrating with your system's credential store and SSH agent, so it works with the same credentials as command-line Git. It uses standard R data types (vectors and data frames) for all inputs and outputs, making it straightforward to work with Git repositories programmatically. The package supports both HTTPS and SSH remotes, with built-in support for GitHub personal access tokens and SSH keys.
