---
title: Packrat on CRAN
people:
  - Kevin Ushey
date: '2014-09-05'
categories:
  - Best Practices
slug: packrat-on-cran
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["packrat"]
languages: ["R"]
ported_categories:
  - Packages
---


Packrat is now available [on CRAN](http://cran.r-project.org/web/packages/packrat/), with version 0.4.1-1! Packrat is an R package that helps you manage your project's R package dependencies in an isolated, reproducible and portable way.

Install packrat from CRAN with:

```r
install.packages("packrat")
```

In particular, this release provides better support for local repositories. Local repositories are just folders containing package sources (currently as folders themselves).

One can now specify local repositories on a per-project basis by using:

    packrat::set_opts(local.repos = <pathToRepo>)

and then using

    packrat::install_local(<pkgName>)

to install that package from the local repository.

There is also experimental support for a global 'cache' of packages, which can be used across projects. If you wish to enable this feature, you can use (note that it is disabled by default):

```r
packrat::set_opts(use.cache = TRUE)
```

in each project where you would utilize the cache.

By doing so, if one project installs or uses e.g. Shiny 0.10.1 for CRAN, and another version uses that same package, packrat will look up the installed version of that package in the cache — this should greatly speed up project initialization for new projects that use projects overlapping with other packrat projects with large, overlapping dependency chains.

In addition, this release provides a number of usability improvements and bug fixes for Windows.

Please visit [rstudio.github.io/packrat](http://rstudio.github.io/packrat/) for more information and a guide to getting started with Packrat.

