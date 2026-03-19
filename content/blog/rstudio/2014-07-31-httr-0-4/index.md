---
title: httr 0.4
people:
  - Hadley Wickham
date: '2014-07-31'
categories:
  - Data Wrangling
slug: httr-0-4
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
ported_from: rstudio
port_status: in-progress
software: ["httr"]
languages: ["R"]
ported_categories:
  - Packages
---


httr 0.4 is now available on CRAN. The httr packages makes it easy to talk to web APIs from R.

The most important new features are two new vignettes to [help you get started](http://cran.r-project.org/web/packages/httr/vignettes/quickstart.html) and to help you make wrappers for [web APIs](http://cran.r-project.org/web/packages/httr/vignettes/api-packages.html). Other important improvements include:

  * New `headers()` and `cookies()` functions to extract headers and cookies from responses. `status_code()` returns HTTP status codes.

  * `POST()` (and `PUT()`, and `PATCH()`) now have an `encode` argument that determine how the `body` is encoded. Valid values are "multipart", "form" or "json", and the `multipart` argument is now deprecated.

  * `GET(..., progress())` will display a progress bar, useful if you're doing large uploads or downloads.

  * `verbose()` gives you considerably more control over degree of verbosity, and defaults have been selected to be more helpful for the most common cases.

  * NULL `query` parameters are now dropped automatically.

There are number of other minor improvements and bug fixes, as described by the [release notes](https://github.com/hadley/httr/releases/tag/v0.4).

