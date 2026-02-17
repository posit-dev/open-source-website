---
description: Password Entry for R, Git, and SSH
github: r-lib/askpass
languages:
- R
latest_release: '2023-09-03T17:44:05+00:00'
people:
- Jeroen Ooms
- Gábor Csárdi
title: askpass
website: ''

external:
  description: Password Entry for R, Git, and SSH
  first_commit: '2018-11-17T12:32:43+00:00'
  forks: 0
  languages:
  - R
  last_updated: '2026-02-17T11:35:27.218442+00:00'
  latest_release: '2023-09-03T17:44:05+00:00'
  license: NOASSERTION
  people:
  - Jeroen Ooms
  - Gábor Csárdi
  repo: r-lib/askpass
  stars: 88
  title: askpass
  website: ''
---

The askpass package provides cross-platform utilities for securely prompting users to enter passwords, passphrases, or credentials in R. It includes native programs for macOS and Windows, eliminating the need for tcltk dependencies.

The package can be called directly from R using the askpass() function to prompt for credentials, such as when reading password-protected key files. It also automatically integrates as a password-entry backend for SSH and Git operations through the SSH_ASKPASS and GIT_ASKPASS environment variables, allowing seamless credential prompting when R interacts with SSH or Git. The package works across different R environments including RStudio, RGui, and terminal sessions.
