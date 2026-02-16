---
description: ':closed_lock_with_key: Access the system credential store from R'
github: r-lib/keyring
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

external:
  contributors:
  - gaborcsardi
  - awong234
  - javierluraschi
  - krlmlr
  - maelle
  - andrie
  - cfhammill
  - hadley
  - jeroenjanssens
  - jeroen
  - jonthegeek
  - mikebirdgeneau
  - MikeJohnPage
  - pnacht
  - tobadia
  - uroshercog
  - shrektan
  - nbenn
  - ras44
  description: ':closed_lock_with_key: Access the system credential store from R'
  first_commit: '2017-01-27T16:18:55+00:00'
  forks: 31
  languages:
  - C
  last_updated: '2026-02-13T14:17:19.304149+00:00'
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

Storing sensitive information like API keys, database passwords, and authentication tokens is a common challenge for data scientists and developers. The keyring package provides a secure solution by integrating with your operating system's native credential storage systems—macOS Keychain, Windows Credential Store, and Linux Secret Service API. Instead of hardcoding secrets in scripts or relying on plain-text environment variables that could accidentally be committed to version control, keyring keeps your credentials encrypted and persistent across R sessions while preventing accidental exposure.

The package offers flexible security options to match your workflow needs. By default, it uses your OS keyring that unlocks automatically at login, making it convenient for daily development work. For projects requiring heightened security, you can create custom keyrings that require manual password entry each time secrets are accessed. Keyring supports multiple backends for maximum compatibility and provides a simple, consistent API for storing, retrieving, and managing credentials across different platforms, making it an essential tool for any R user working with sensitive data or external services.