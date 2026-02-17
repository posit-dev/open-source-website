---
description: ''
github: posit-dev/r-shinylive
languages:
- R
latest_release: '2024-11-13T16:30:05+00:00'
people:
- Barret Schloerke
- Garrick Aden-Buie
- George Stagg
- Winston Chang
title: r-shinylive
website: https://posit-dev.github.io/r-shinylive/

external:
  description: ''
  first_commit: '2023-09-07T14:44:00+00:00'
  forks: 20
  languages:
  - R
  last_updated: '2026-02-17T11:11:34.003867+00:00'
  latest_release: '2024-11-13T16:30:05+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  - Garrick Aden-Buie
  - George Stagg
  - Winston Chang
  repo: posit-dev/r-shinylive
  stars: 225
  title: r-shinylive
  website: https://posit-dev.github.io/r-shinylive/
---

The `{shinylive}` R package converts your Shiny for R applications into standalone web applications that run entirely in the browser using WebAssembly, eliminating the need for a server. It exports your local Shiny app to a directory of static files that can be hosted on any static web server, downloads and manages the necessary Shinylive web assets, and handles package dependencies automatically.

This approach solves deployment complexity by removing server infrastructure requirements, making Shiny apps portable and easy to share. The package automatically detects R package dependencies and includes them as precompiled WebAssembly binaries via the webR project. It integrates with common workflows including GitHub Pages deployment and Quarto documents, and supports managing multiple applications on the same site by sharing web assets across apps.
