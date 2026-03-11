---
description: Tools for Managing SSH and Git Credentials
github: r-lib/credentials
image: logo.png
color: "#4F8DDC"
languages:
- R
latest_release: '2020-07-21T08:31:43+00:00'
people:
- Jeroen Ooms
- Jenny Bryan
title: credentials
website: https://docs.ropensci.org/credentials

external:  # updated automatically, do not edit
  description: Tools for Managing SSH and Git Credentials
  first_commit: '2018-11-06T19:40:03+00:00'
  forks: 4
  languages:
  - R
  last_updated: '2026-03-05T16:28:30.607711+00:00'
  latest_release: '2020-07-21T08:31:43+00:00'
  license: NOASSERTION
  people:
  - Jeroen Ooms
  - Jenny Bryan
  readme_image: man/figures/logo.png
  repo: r-lib/credentials
  stars: 75
  title: credentials
  website: https://docs.ropensci.org/credentials
---

The credentials package provides tools for managing SSH and Git credentials in R, interfacing with the git-credential utility for HTTPS authentication and providing functions to find or generate SSH keys. It helps users set up local git installations and provides a backend for git/ssh client libraries to authenticate with existing credentials.

The package solves the problem of securely managing authentication credentials without hardcoding secrets in plain text. It can automatically populate the GITHUB_PAT environment variable from the native credential store, prompt users for credentials when needed, and help locate or generate appropriate SSH keys for GitHub and other services. The package supports both HTTPS and SSH authentication workflows, making it useful for developers who need to programmatically access git repositories or integrate authentication into R packages.
