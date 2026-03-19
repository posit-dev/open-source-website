---
title: devtools 1.9.1
people:
  - Hadley Wickham
date: '2015-09-13'
categories:
  - Best Practices
slug: devtools-1-9-1
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


Devtools 1.9.1 is now available on CRAN. Devtools makes package building so easy a package can become your default way to organise code, data, and documentation. You can learn more about developing packages in [R packages](http://r-pkgs.had.co.nz/), my book about package development that's freely available online..

Get the latest version of devtools with:

```r
install.packages("devtools")
```

There are three major improvements that I contributed:

  * `check()` is now much closer to what CRAN does - it passes on `--as-cran` to `R CMD check`, using an env var to turn off the incoming CRAN checks. These are turned off because they're slow (they have to retrieve data from CRAN), and are not necessary except just prior to release (so `release()` turns them back on again).

  * `install_deps()` now automatically upgrades out of date dependencies. This is typically what you want when you're working on a development version of a package: otherwise you can get an unpleasant surprise when you go to submit your package to CRAN and discover it doesn't work with the latest version of its dependencies. To suppress this behaviour, set `upgrade_dependencies = FALSE`.

  * `revdep_check()` received a number of tweaks that I've found helpful when preparing my packages for CRAN:

    * Suggested dependencies of the revdeps are installed by default.

    * The `NOT_CRAN` env var is set to `false` so tests that are skipped on CRAN are also skipped for you.

    * The `RGL_USE_NULL` env var is set to `true` to stop rgl windows from popping up during testing.

    * All revdep sources are downloaded at the start of the checks. This makes life a bit easier if you're on a flaky internet connection.

But like many recent devtools releases, most of the coolest new features have been contributed by the community:

  * [Jim Hester](http://www.jimhester.com) implemented experimental remote depedencies for `install()`. You can now tell devtools where to find dependencies with a remotes field:

    Imports:
      MASS,
      testthat
    Remotes:
      hadley/testthat

The default allows you to refer to github repos, but you can easily add deps from any of the other sources that devtools supports: see `vignette("dependencies")` for more details.

Support for installing development dependencies is still experimental so we appreciate any feedback.

  * [Jenny Bryan](http://www.stat.ubc.ca/~jenny/) considerably improved the existing GitHub integration. `use_github()` now pushes to the newly created GitHub repo, and sets a remote tracking branch. It also populates the URL and BugReports fields of your `DESCRIPTION`.

  * [Kirill Müller](https://github.com/krlmlr) contributed many bug fixes, minor improvements and test cases.

See the [release notes](https://github.com/hadley/devtools/releases/tag/v1.9.1) for complete bug fixes and other minor changes.

