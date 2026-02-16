---
description: Windows/macOS/Linux binaries and installation methods of TinyTeX
github: rstudio/tinytex-releases
image: logo-tinytex.png
languages:
- PowerShell
latest_release: '2026-02-01T07:35:46+00:00'
people:
- Christophe Dervieux
title: tinytex-releases
website: https://yihui.org/tinytex/

external:
  contributors:
  - yihui
  - github-actions[bot]
  - cderv
  - naveen521kk
  - andrihitz
  - fkohrt
  - LiNk-NY
  - remlapmot
  - tfiers
  - wirzu
  description: Windows/macOS/Linux binaries and installation methods of TinyTeX
  first_commit: '2020-09-14T17:27:48+00:00'
  forks: 34
  languages:
  - PowerShell
  last_updated: '2026-02-13T14:17:04.912422+00:00'
  latest_release: '2026-02-01T07:35:46+00:00'
  license: GPL-2.0
  people:
  - Christophe Dervieux
  readme_image: https://yihui.org/images/logo-tinytex.png
  repo: rstudio/tinytex-releases
  stars: 348
  title: tinytex-releases
  website: https://yihui.org/tinytex/
---

TinyTeX is a lightweight, cross-platform LaTeX distribution designed to eliminate the pain of traditional TeX installations. Built on TeX Live, TinyTeX offers a portable and easy-to-maintain alternative that strips away unnecessary bloat while retaining everything you need for compiling documents. Whether you're rendering R Markdown reports, creating technical documents, or working with LaTeX in production environments, TinyTeX provides pre-built binaries for Windows, macOS, and Linux that can be deployed in minutes rather than hours.

The project offers flexible bundle sizes to match your needs: from the minimal TinyTeX-0 (under 1 MB on Linux) containing just the infrastructure, to TinyTeX-1 with about 90 packages optimized for R Markdown workflows, to the comprehensive TinyTeX-2 with the complete TeX Live collection. Each bundle includes tlmgr, the TeX Live package manager, allowing you to install additional packages on-demand. Monthly releases ensure you have access to stable, tested distributions, while daily builds provide the latest updates for those who need cutting-edge features. This repository serves as the distribution hub, making it simple to integrate TinyTeX into automated workflows, container images, or continuous integration pipelines.
