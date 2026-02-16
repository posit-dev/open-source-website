---
description: A lightweight, cross-platform, portable, and easy-to-maintain LaTeX distribution
  based on TeX Live
github: rstudio/tinytex
image: logo-tinytex.png
languages:
- R
latest_release: '2025-11-19T14:28:59+00:00'
people:
- Christophe Dervieux
- JJ Allaire
title: tinytex
website: https://yihui.org/tinytex/

external:
  contributors:
  - yihui
  - cderv
  - dragonstyle
  - jonkeane
  - billdenney
  - naveen521kk
  - boltomli
  - github-actions[bot]
  - superruzafa
  - AlfonsoMuskedunder
  - ateucher
  - dpryan79
  - delmendo
  - eheinzen
  - efcaguab
  - ivan-krukov
  - jjallaire
  - jooyoungseo
  - benz0li
  - krivit
  - rhurlin
  - StevenTammen
  - thomasrockhu-codecov
  - XiangyunHuang
  - yzhang-gh
  - olivroy
  - sixvable
  - steveb-cirina
  description: A lightweight, cross-platform, portable, and easy-to-maintain LaTeX
    distribution based on TeX Live
  first_commit: '2017-11-16T21:24:02+00:00'
  forks: 122
  languages:
  - R
  last_updated: '2026-02-13T14:17:03.161774+00:00'
  latest_release: '2025-11-19T14:28:59+00:00'
  license: NOASSERTION
  people:
  - Christophe Dervieux
  - JJ Allaire
  readme_image: https://yihui.org/images/logo-tinytex.png
  repo: rstudio/tinytex
  stars: 1085
  title: tinytex
  website: https://yihui.org/tinytex/
---

TinyTeX is a lightweight LaTeX distribution built on TeX Live that solves the traditional installation dilemma faced by data scientists and developers. Instead of choosing between a minimal LaTeX installation that lacks essential packages or a multi-gigabyte full distribution with mostly unused components, TinyTeX provides an intelligent middle ground. It starts with a compact core and automatically installs missing LaTeX packages as needed, making it particularly valuable for R Markdown users who need reliable PDF rendering without becoming LaTeX experts.

What makes TinyTeX especially powerful is its user-friendly approach to package management and maintenance. Rather than forcing users to navigate complex LaTeX documentation when encountering missing package errors, TinyTeX handles dependencies transparently and provides clear, actionable guidance when issues arise. This automation and simplicity allow you to focus on creating documents and reports rather than wrestling with LaTeX configuration, making professional-quality PDF output accessible whether you're generating reproducible research papers, technical documentation, or data analysis reports.