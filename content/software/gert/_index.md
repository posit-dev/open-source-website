---
description: Simple git client for R
github: r-lib/gert
image: logo.png
languages:
- C
latest_release: '2024-07-18T11:32:08+00:00'
people:
- Jeroen Ooms
- Jenny Bryan
- Mine Çetinkaya-Rundel
- Davis Vaughan
title: gert
website: https://docs.ropensci.org/gert/

external:
  contributors:
  - jeroen
  - jennybc
  - maelle
  - rundel
  - krlmlr
  - M-Kusumgar
  - zkamvar
  - spaette
  - richfitz
  - olivroy
  - romainfrancois
  - pat-s
  - nanhung
  - mine-cetinkaya-rundel
  - MichaelChirico
  - Fazendaaa
  - HenningLorenzen-ext-bayer
  - QuLogic
  - DavisVaughan
  - csgillespie
  description: Simple git client for R
  first_commit: '2018-10-19T09:11:55+00:00'
  forks: 36
  languages:
  - C
  last_updated: '2026-02-13T14:17:19.912289+00:00'
  latest_release: '2024-07-18T11:32:08+00:00'
  license: NOASSERTION
  people:
  - Jeroen Ooms
  - Jenny Bryan
  - Mine Çetinkaya-Rundel
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: r-lib/gert
  stars: 156
  title: gert
  website: https://docs.ropensci.org/gert/
---

Gert is a simple and user-friendly Git client for R that makes version control accessible without requiring deep knowledge of Git internals. Built on the robust libgit2 library, gert provides a clean R interface to essential Git operations, using familiar R data types like vectors and data frames for inputs and outputs. The package seamlessly handles authentication through OS credential stores and supports both HTTPS and SSH protocols, automatically discovering credentials just as command-line Git would. This means you can clone repositories, create branches, commit changes, and manage your version control workflow entirely from R, without manually passing credentials for each operation.

What sets gert apart is its emphasis on simplicity and practical usability for R developers. Unlike other Git packages that expose low-level pointer objects and complex internals, gert abstracts away the complexity while maintaining full functionality. The API mirrors familiar command-line Git operations, making it intuitive for anyone with basic Git knowledge. Whether you're automating repository management, building data pipelines that interact with Git, or simply want to version control your R projects programmatically, gert provides the tools you need with minimal friction. The package links to prebuilt system libraries ensuring consistent, reliable performance across different platforms.
