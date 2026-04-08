---
title: Devtools 1.10.0
description: "devtools 1.10.0 improves Windows RTools detection, adds use_news_md() and use_mit_license(), with lazy GitHub installs."
auto-description: true
people:
  - Hadley Wickham
date: '2016-02-02'
categories:
  - Best Practices
slug: devtools-1-10-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["devtools"]
languages: ["R"]
ported_categories:
  - Packages
---


Devtools 1.10.0 is now available on CRAN. Devtools makes package building so easy that a package can become your default way to organise code, data, documentation, and tests. You can learn more about creating your own package in [R packages](http://r-pkgs.had.co.nz/). Install devtools with:

```r
install.packages("devtools")
```

This version is mostly a collection of bug fixes and minor improvements. For example:

  * Devtools employs a new strategy for detecting RTools on windows: we now only check for Rtools if you need to `load_all()` or `build()` a package with compiled code. This should make life easier for most windows users.

  * Package installation receieved a lot of tweaks from the community. Devtools now makes use of the `Additional_repositories` field, which is useful if youâ€™re using [drat](http://dirk.eddelbuettel.com/code/drat.html) for non-CRAN packages. `install_github()` is now lazy and wonâ€™t reinstall if the currently installed version is the same as the one on github. Local installs now add git and github metadata, if available.

  * `use_news_md()` adds a (very) basic `NEWS.md` template. CRAN now accepts `NEWS.md` files so `release()` warns if youâ€™ve previously added it to `.Rbuilignore`.

  * `use_mit_license()` writes the necessary infrastructure to declare that your package is MIT licensed (in a CRAN-compliant way).

  * `check(cran = TRUE)` automatically adds `--run-donttest` as this is a de facto CRAN standard.

To see the full list of changes, please read the [release notes](https://github.com/hadley/devtools/releases/tag/v1.10.0).

