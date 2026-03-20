---
color: '#87C9D8'
description: R package for creating Plumber APIs that function as Tableau Analytics
  Extensions
github: rstudio/plumbertableau
image: logo.svg
languages:
- R
latest_release: '2021-08-05T14:49:01+00:00'
people:
- Joe Cheng
title: plumbertableau
website: https://rstudio.github.io/plumbertableau/

external:  # updated automatically, do not edit
  description: R package for creating Plumber APIs that function as Tableau Analytics
    Extensions
  first_commit: '2021-01-22T23:54:49+00:00'
  forks: 0
  languages:
  - R
  last_updated: '2026-03-20T10:27:36.678472+00:00'
  latest_release: '2021-08-05T14:49:01+00:00'
  license: NOASSERTION
  people:
  - Joe Cheng
  readme_image: man/figures/logo.svg
  repo: rstudio/plumbertableau
  stars: 31
  title: plumbertableau
  website: https://rstudio.github.io/plumbertableau/
---

plumbertableau enables R developers to create Analytics Extensions for Tableau workbooks using the Plumber API framework. These extensions allow Tableau users to call R functions in real time from calculated fields without writing R code themselves.

The package automatically handles Tableau's Analytics Extension protocol by generating required endpoints and routing requests to specific R functions defined by developers. This separation lets R developers build and publish extensions that Tableau users can call with simple syntax, and it integrates with RStudio Connect to host multiple extensions through a single endpoint while providing package management, security, and sandboxing features.
