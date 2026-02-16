---
description: The R Installation Manager
github: r-lib/rig
image: rig-app.png
languages:
- Rust
latest_release: '2025-10-22T17:35:17+00:00'
people:
- Gábor Csárdi
- Christophe Dervieux
- Davis Vaughan
- Jenny Bryan
- Emil Hvitfeldt
title: rig
website: ''

external:
  contributors:
  - gaborcsardi
  - gvelasq
  - achubaty
  - cderv
  - DavisVaughan
  - jennybc
  - TymekDev
  - EmilHvitfeldt
  - Bisaloo
  - krlmlr
  - aspeddro
  - bahadzie
  - eitsupi
  description: The R Installation Manager
  first_commit: '2021-11-09T12:13:28+00:00'
  forks: 31
  languages:
  - Rust
  last_updated: '2026-02-13T14:17:20.586369+00:00'
  latest_release: '2025-10-22T17:35:17+00:00'
  license: MIT
  people:
  - Gábor Csárdi
  - Christophe Dervieux
  - Davis Vaughan
  - Jenny Bryan
  - Emil Hvitfeldt
  readme_image: tools/rig-app.png
  repo: r-lib/rig
  stars: 889
  title: rig
  website: ''
---

Rig is a cross-platform command-line tool that streamlines R version management for developers and data scientists. Whether you're maintaining legacy projects, testing packages across multiple R versions, or simply keeping up with the latest releases, rig makes it effortless to install, configure, and switch between different R installations. Instead of manually juggling versions, you can reference them symbolically using intuitive names like "devel," "release," or "oldrel," and run multiple versions simultaneously without conflicts.

Beyond basic version management, rig automates the tedious setup tasks that typically follow a fresh R installation. It configures your default CRAN mirror, installs the pak package manager, creates user-level package libraries with proper permissions, and on macOS, even provides a convenient menu bar application for quick version switching. Built in Rust for speed and reliability, rig works seamlessly across macOS, Windows, and Linux, making it an essential tool for anyone working with R in professional or research environments.
