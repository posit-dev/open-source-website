---
color: '#E7B10A'
description: Run Shiny on Python and R (compiled to wasm) in the browser
github: posit-dev/shinylive
image: logo.svg
languages:
- TypeScript
latest_release: '2025-12-08T20:54:30+00:00'
people:
- Winston Chang
- George Stagg
- Nick Strayer
- Carson Sievert
- Garrick Aden-Buie
- Joe Cheng
- Barret Schloerke
title: shinylive
website: https://shinylive.io/py/examples/

external:  # updated automatically, do not edit
  description: Run Shiny on Python and R (compiled to wasm) in the browser
  first_commit: '2022-04-29T22:29:25+00:00'
  forks: 24
  languages:
  - TypeScript
  last_updated: '2026-03-20T10:27:13.853944+00:00'
  latest_release: '2025-12-08T20:54:30+00:00'
  license: MIT
  people:
  - Winston Chang
  - George Stagg
  - Nick Strayer
  - Carson Sievert
  - Garrick Aden-Buie
  - Joe Cheng
  - Barret Schloerke
  repo: posit-dev/shinylive
  stars: 244
  title: shinylive
  website: https://shinylive.io/py/examples/
---

Shinylive deploys Shiny applications that run entirely in the browser using Pyodide and webR, which are Python and R compiled to WebAssembly. This eliminates the need for a server to host Shiny apps.

The package handles building and bundling all necessary components to make Shiny applications work client-side in the browser. It manages package dependencies through a lockfile system, builds JavaScript resources from TypeScript sources, and creates a distribution that includes both the Shiny framework and additional Python/R packages beyond the base Pyodide installation. Developers can deploy Shiny apps that users can run without any backend infrastructure.
