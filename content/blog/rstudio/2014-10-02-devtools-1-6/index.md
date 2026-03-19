---
title: devtools 1.6
people:
  - Hadley Wickham
date: '2014-10-02'
categories:
  - Best Practices
slug: devtools-1-6
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
ported_from: rstudio
port_status: in-progress
software: ["devtools"]
languages: ["R"]
ported_categories:
  - Packages
---


Devtools 1.6 is now available on CRAN. Devtools makes it so easy to build a package that it becomes your default way to organise code, data and documentation. Learn more at <http://r-pkgs.had.co.nz/>. You can get the latest version with:

```r
install.packages("devtools")
```

We've made a lot of improvements to the install and release process:

  * Installation functions now default to `build_vignettes = FALSE`, and only install required dependencies (not suggested). They also store a lot of useful metadata.

  * `install_github()` got a lot of love. `install_github("user/repo")` is now the preferred way to install a package from github (older forms with explicit username parameter are now deprecated). You can supply the `host` argument to install packages from a local github enterprise installation. You can get the latest release with `user/repo@*release`.

  * `session_info()` uses package installation metdata to show you exactly how every package was installed (locally, from CRAN, from github, ...)

  * `release()` uses new webform-based submission process for CRAN, as implemented in `submit_cran()`.

  * You can add arbitrary extra questions to `release()` by defining a function `release_questions()` in your package. It should return a character vector of questions to ask.

We've also added a number of functions to make it easy to get started with various aspects of the package development:

  * `use_data()` adds data to a package, either in `data/` (external data) or in `R/sysdata.rda` (internal data). `use_data_raw()` sets up `data-raw/` for your reproducible data generation scripts.

  * `use_package()` sets dependencies and reminds you how to use them.

  * `use_rcpp()` gets you ready to use [Rcpp](http://www.rcpp.org).

  * `use_testthat()` sets up testing infrastructure with [testthat](http://r-pkgs.had.co.nz/tests.html).

  * `use_travis()` adds a `.travis.yml` file and tells you how to get started with [travis ci](https://travis-ci.org).

  * `use_vignette()` creates a draft vignette using [Rmarkdown](http://rmarkdown.rstudio.com).

There were many other minor improvements and bug fixes. See the [release notes](https://github.com/hadley/devtools/releases/tag/v1.6) for complete list of changes.

