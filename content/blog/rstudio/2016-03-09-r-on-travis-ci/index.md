---
title: R on Travis-CI
people:
  - Jim Hester
date: '2016-03-09'
categories:
- Packages
slug: r-on-travis-ci
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


Support for building R projects on Travis has recently undergone improvements which we hope will make it an even better tool for the R community. Feature highlights include:

  * Support for Travis' [container-based infrastructure](https://docs.travis-ci.com/user/workers/container-based-infrastructure/).

  * Package dependency caching (on the container-based builds).

  * Building with multiple R versions (R-devel, R-release (3.2.3) and R-oldrel (3.1.3)).

  * Log filtering to improve readability and hide less relevant information.

  * Updated dependencies TexLive (2015) and pandoc (1.15.2).

See the Travis documentation on [building an R project](https://docs.travis-ci.com/user/languages/r) for complete details on the available options.

Using the container-based infrastructure with package caching is now recommended for nearly all projects. There are more compute and network resources available for container based builds, which means they start processing in less time and run faster. The package caching makes package installation comparable or faster than using binary packages.

A minimal .travis.yml file that is suitable for most cases is

    language: r
    sudo: false
    cache: packages

New packages can omit `sudo: false`, as it is the default for new repositories. However older repositories will have to explicitly set `sudo: false` to use the container based infrastructure.

If your package depends on development packages that are not on CRAN (such as GitHub) we recommend you use the [Remotes:](https://github.com/hadley/devtools/blob/master/vignettes/dependencies.Rmd) annotation in your package `DESCRPITION` file. This will allow your package and dependencies to be easily installed by `devtools::install_github()` as well as on Travis ([Examples](https://github.com/search?utf8=%E2%9C%93&q=filename%3ADESCRIPTION+path%3A%2F+Remotes&type=Code&ref=searchresults)). It is generally no longer necessary to use `r_github_packages`, `r_packages`, `r_binary_packages`, etc. as this can be handled with `Remotes`.

If you need system dependencies, first check to see if they're available with the [apt-addon](https://docs.travis-ci.com/user/installing-dependencies/#Installing-Packages-with-the-APT-Addon) and include them in your `.travis.yml`. This will allow you to install them without sudo and still use the container based infrastructure.

    addons:
      apt:
        packages:
          - libv8-dev

We hope these improvements will make your use of Travis with R simple and useful. Please file any issues found at <https://github.com/travis-ci/travis-ci/issues> and mention @craigcitro, @hadley and @jimhester in the issue.

