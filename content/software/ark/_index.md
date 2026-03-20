---
color: '#E6B7A5'
description: Ark, an R kernel
github: posit-dev/ark
image: logo.png
languages:
- R
latest_release: '2026-03-03T20:32:26+00:00'
people:
- Lionel Henry
- Davis Vaughan
- Daniel Falbel
- Julia Silge
- Jenny Bryan
- Isabel Zimmerman
- JJ Allaire
- Simon Couch
title: Ark
website: ''

override:
  languages:
  - R
  title: Ark

external:  # updated automatically, do not edit
  description: Ark, an R kernel
  first_commit: '2023-05-18T17:08:46+00:00'
  forks: 26
  languages:
  - Rust
  last_updated: '2026-03-20T10:27:14.051093+00:00'
  latest_release: '2026-03-03T20:32:26+00:00'
  license: MIT
  people:
  - Lionel Henry
  - Davis Vaughan
  - Daniel Falbel
  - Julia Silge
  - Jenny Bryan
  - Isabel Zimmerman
  - JJ Allaire
  - Simon Couch
  readme_image: doc/logo.png
  repo: posit-dev/ark
  stars: 295
  title: ark
  website: ''
---

Ark is an R kernel for Jupyter applications that serves as the interface between R and the Positron IDE. It provides structured interaction between R and any Jupyter-compatible frontend.

Ark combines three protocols in one tool: a Jupyter kernel for interactive R evaluation, an LSP server for IDE features like completions and jump-to-definition, and a DAP server for step-debugging R functions. Unlike similar tools written primarily in R (IRKernel, languageserver, vscDebugger), Ark is implemented as a native frontend that binds directly to R's C API, with its LSP and DAP components written in Rust for performance and tight integration with the kernel. This architecture enables introspective features based on the live R session state and supports both Console and Notebook modes.
