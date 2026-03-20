---
color: '#D44000'
description: Python package for deploying Shinylive applications
github: posit-dev/py-shinylive
image: logo.svg
languages:
- Python
latest_release: '2025-12-08T21:03:47+00:00'
people:
- Winston Chang
- Carson Sievert
- Barret Schloerke
- Garrick Aden-Buie
- George Stagg
title: py-shinylive
website: https://shiny.posit.co/py/get-started/shinylive.html

external:  # updated automatically, do not edit
  description: Python package for deploying Shinylive applications
  first_commit: '2022-08-29T22:44:07+00:00'
  forks: 6
  languages:
  - Python
  last_updated: '2026-03-20T10:27:13.934487+00:00'
  latest_release: '2025-12-08T21:03:47+00:00'
  license: MIT
  people:
  - Winston Chang
  - Carson Sievert
  - Barret Schloerke
  - Garrick Aden-Buie
  - George Stagg
  repo: posit-dev/py-shinylive
  stars: 56
  title: py-shinylive
  website: https://shiny.posit.co/py/get-started/shinylive.html
---

The Shinylive Python package exports Shiny for Python applications to run entirely in the browser without requiring a hosted server. It converts your local Shiny apps into static web applications that use WebAssembly via pyodide.

This package solves the deployment problem for Shiny apps by eliminating server requirements entirely. It manages and bundles the necessary web assets, allows you to export single or multiple applications to static directories, and provides tools to cache and manage different versions of the Shinylive web components. The exported applications can be hosted on any static web server or integrated into Quarto documents.
