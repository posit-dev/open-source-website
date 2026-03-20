---
color: '#008272'
description: Turn your R code into a web API.
github: rstudio/plumber
image: logo.svg
languages:
- R
latest_release: '2026-02-09T15:06:24+00:00'
people:
- Barret Schloerke
- Thomas Lin Pedersen
- Joe Cheng
- Garrick Aden-Buie
- Charlie Gao
- Carson Sievert
title: plumber
website: https://www.rplumber.io

external:  # updated automatically, do not edit
  description: Turn your R code into a web API.
  first_commit: '2015-06-04T05:09:10+00:00'
  forks: 260
  languages:
  - R
  last_updated: '2026-03-20T10:27:31.667943+00:00'
  latest_release: '2026-02-09T15:06:24+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  - Thomas Lin Pedersen
  - Joe Cheng
  - Garrick Aden-Buie
  - Charlie Gao
  - Carson Sievert
  readme_image: man/figures/logo.svg
  repo: rstudio/plumber
  stars: 1435
  title: plumber
  website: https://www.rplumber.io
---

Plumber is an R package that turns R functions into web APIs by adding special comments to your code. It uses roxygen2-style annotations to define API endpoints, allowing you to expose R functions as HTTP services that accept parameters and return JSON, plots, or other data formats.

The package makes it simple to create RESTful APIs without learning a web framework, handling HTTP routing, parameter parsing, and response serialization automatically. It supports both GET and POST requests, accepts parameters from query strings or JSON bodies, and can return various output formats including JSON and images. This enables R developers to make their analysis and modeling work accessible to other applications and services.
