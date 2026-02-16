---
description: Tools for Managing SSH and Git Credentials
github: r-lib/credentials
image: logo.png
languages:
- R
latest_release: '2020-07-21T08:31:43+00:00'
people:
- Jeroen Ooms
- Jenny Bryan
title: credentials
website: https://docs.ropensci.org/credentials

external:
  contributors:
  - jeroen
  - jennybc
  - maelle
  description: Tools for Managing SSH and Git Credentials
  first_commit: '2018-11-06T19:40:03+00:00'
  forks: 4
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.962406+00:00'
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

The credentials package simplifies secure authentication for Git operations and SSH-based services in R. Instead of hardcoding passwords or tokens in your scripts, credentials provides a safe interface to Git's native credential store and SSH key management system. This eliminates the security risks of exposing sensitive information while streamlining your development workflow across multiple projects and sessions.

Whether you're pushing code to GitHub, cloning private repositories, or automating Git operations in your data pipelines, credentials handles the authentication complexity for you. The package automatically locates or generates SSH keys, retrieves GitHub Personal Access Tokens from your system's credential store, and seamlessly integrates with popular Git client libraries. For data scientists and developers working with version-controlled projects, credentials removes authentication friction so you can focus on your code rather than credential management.
