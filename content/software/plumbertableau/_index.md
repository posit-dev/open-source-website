---
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

external:
  contributors:
  - blairj09
  - toph-allen
  - sagerb
  - jcheng5
  - yihui
  description: R package for creating Plumber APIs that function as Tableau Analytics
    Extensions
  first_commit: '2021-01-22T23:54:49+00:00'
  forks: 0
  languages:
  - R
  last_updated: '2026-02-13T14:17:05.058203+00:00'
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

plumbertableau is an R package that bridges the gap between R's statistical capabilities and Tableau's visualization power by enabling you to create Tableau Analytics Extensions from Plumber APIs. It allows R developers to expose sophisticated R functions that Tableau users can invoke directly from calculated fields within their workbooks, bringing real-time statistical modeling, machine learning predictions, and advanced analytics into Tableau dashboards without requiring Tableau users to write any R code themselves.

What makes plumbertableau particularly valuable is its annotation-based approach that dramatically simplifies extension development. Instead of manually implementing Tableau's Analytics Extensions protocol, you simply add special annotations to your Plumber endpoints, and the package handles all the technical integration automatically. This separation of concerns means R developers can build and maintain robust, version-controlled analytics endpoints that deploy seamlessly to RStudio Connect, while Tableau users gain access to powerful R functionality through familiar calculated field syntax. Whether you're deploying custom forecasting models, implementing domain-specific algorithms, or extending Tableau's native capabilities with R's vast ecosystem of packages, plumbertableau provides an enterprise-ready framework for collaborative analytics.
