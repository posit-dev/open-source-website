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
  contributors:
  - jeroen
  - gaborcsardi
  description: Password Entry for R, Git, and SSH
  first_commit: '2018-11-17T12:32:43+00:00'
  forks: 0
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.979156+00:00'
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

askpass provides cross-platform utilities for securely prompting users for credentials and passphrases in R. Whether you need to authenticate with a server, read a protected SSH key, or access password-protected resources, askpass delivers a seamless experience across different environments including RStudio, macOS, Windows, and terminal sessions. The package includes native programs for macOS and Windows, eliminating the need for additional dependencies like tcltk.

Beyond direct use in R scripts, askpass integrates elegantly with your development workflow by serving as a password-entry backend for Git and SSH operations. By configuring the SSH_ASKPASS and GIT_ASKPASS environment variables, askpass ensures that when R calls out to git or ssh, users are automatically prompted for credentials in a secure, platform-appropriate manner. This makes it particularly valuable for data scientists and developers working with version control systems, remote repositories, and encrypted resources as part of their daily workflow.
