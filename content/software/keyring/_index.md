---
color: '#447099'
description: ':closed_lock_with_key: Access the system credential store from R'
github: r-lib/keyring
image: logo.svg
languages:
- C
latest_release: '2025-06-15T20:21:06+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jeroen Janssens
- Jeroen Ooms
title: keyring
website: https://keyring.r-lib.org/

external:  # updated automatically, do not edit
  description: ':closed_lock_with_key: Access the system credential store from R'
  first_commit: '2017-01-27T16:18:55+00:00'
  forks: 31
  languages:
  - C
  last_updated: '2026-03-05T16:26:57.367683+00:00'
  latest_release: '2025-06-15T20:21:06+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/keyring
  stars: 200
  title: keyring
  website: https://keyring.r-lib.org/
---

keyring provides secure management of secrets and credentials in R by integrating with your operating system's native credential store. It allows secrets to persist across R sessions without storing them in plain text, reducing the risk of accidental exposure through code sharing or version control.

The package supports multiple backends including macOS Keychain, Windows Credential Store, and Linux Secret Service API, with cross-platform fallbacks for encrypted files and environment variables. For enhanced security, you can create custom keyrings that require password authentication, ensuring secrets are protected even from other processes running on your machine. This makes it a more secure alternative to storing credentials directly in environment variables or configuration files.
