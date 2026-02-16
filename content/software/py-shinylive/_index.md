---
description: Python package for deploying Shinylive applications
github: posit-dev/py-shinylive
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

external:
  contributors:
  - wch
  - cpsievert
  - schloerke
  - gadenbuie
  - chendaniely
  - dlukes
  - georgestagg
  description: Python package for deploying Shinylive applications
  first_commit: '2022-08-29T22:44:07+00:00'
  forks: 5
  languages:
  - Python
  last_updated: '2026-02-13T14:16:45.519723+00:00'
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

py-shinylive is a Python package that transforms Shiny for Python applications into standalone web applications that run entirely in the browser. By leveraging WebAssembly technology through Pyodide, py-shinylive eliminates the need for a traditional Python server, allowing your interactive data applications to execute client-side. This breakthrough means you can deploy Shiny applications to any static web hosting service, from GitHub Pages to simple file servers, without worrying about server infrastructure, scaling, or backend maintenance.

What makes py-shinylive particularly valuable for data scientists and developers is its seamless deployment workflow and infrastructure-free approach. The package intelligently manages all necessary web assets and dependencies, automatically handling version control and caching to streamline the export process. Whether you're sharing a quick data exploration tool with colleagues, embedding an interactive visualization in documentation, or publishing educational materials, py-shinylive provides a frictionless path from development to deployment. It works as part of a broader Shinylive ecosystem that includes support for both Python and R, making it easy to create portable, shareable data applications that run anywhere a web browser does.
