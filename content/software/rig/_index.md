---
color: '#24345D'
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

external:  # updated automatically, do not edit
  description: The R Installation Manager
  first_commit: '2021-11-09T12:13:28+00:00'
  forks: 31
  languages:
  - Rust
  last_updated: '2026-03-20T10:27:56.853867+00:00'
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
  stars: 903
  title: rig
  website: ''
---

Rig is an R installation manager that lets you install, configure, and switch between multiple R versions on macOS, Windows, and Linux. It provides quick links for running different R versions simultaneously and handles system requirements, package managers, and development tools automatically.

The tool simplifies managing multiple R installations by automatically setting up user package libraries, configuring CRAN mirrors and Posit Package Manager, and installing pak for efficient package management. On macOS it includes a menu bar app for switching versions and launching RStudio, on Windows it manages Rtools installations, and on Linux it supports binary packages across major distributions. It creates version-specific quick links (like `R-4.1`) that work alongside your default R installation.
