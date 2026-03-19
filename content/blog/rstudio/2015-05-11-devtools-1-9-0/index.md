---
title: devtools 1.8.0
people:
  - Hadley Wickham
date: '2015-05-11'
categories:
- Packages
slug: devtools-1-9-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["devtools"]
languages: ["R"]
---


Devtools 1.8 is now available on CRAN. Devtools makes it so easy to build a package that it becomes your default way to organise code, data and documentation. You can learn more about developing packages at <http://r-pkgs.had.co.nz/>.

Get the latest version of devtools with:

```r
install.packages("devtools")
```

There are three main improvements:

  * More helpers to get you up and running with package development as quickly as possible.

  * Better tools for package installation (including checking that all dependencies are up to date).

  * Improved reverse dependency checking for CRAN packages.

There were many other minor improvements and bug fixes. See the [release notes](https://github.com/hadley/devtools/releases/tag/v1.8.0) for complete list of changes. The last release announcement was for devtools 1.6 since there weren't many big changes in devtools 1.7. I've included the most important points in this announcement labelled with [1.7]. ## Helpers

The number of functions designed to get you up and going with package development continues to grow. This version sees the addition of:

  * `dr_devtools()`, which runs some common diagnostics: are you using the latest version of R and devtools? Similarly, `dr_github()` checks for common git/github configuration problems.

  * `lint()` runs `lintr::lint_package()` to check the style of package code [1.7].

  * `use_code_of_conduct()` adds a contributor code of conduct from <http://contributor-covenant.org>.

  * `use_cran_badge()` adds a CRAN status badge that you can copy into a README file. Green indicates package is on CRAN. Packages not yet submitted or accepted to CRAN get a red badge.

  * `use_cran_comments()` creates a `cran-comments.md` template and adds it to `.Rbuildignore` to help with CRAN submissions. [1.7]

  * `use_coveralls()` allows you to easily add test coverage with [coveralls](https://coveralls.io).

  * `use_git()` sets up a package to use git, initialising the repo and checking the existing files.

  * `use_test()` adds a new test file in `tests/testthat`.

  * `use_readme_rmd()` sets up a template to generate a `README.md` from a `README.Rmd` with knitr. [1.7]

## Package installation and info

When developing packages it's common to run into problems because you've updated a package, but you've forgotten to update it's dependencies (`install.packages()` doesn't this automatically). The new `package_deps()` solves this problem by finding all recursive dependencies of a package and determining if they're out of date:

```r
# Find out which dependencies are out of date
devtools::package_deps("devtools")
# Update them
update(devtools::package_deps("devtools"))
```

This code is used in `install_deps()` and `revdep_check()` - devtools is now aggressive about updating packages, which should avoid potential problems in CRAN submissions.
New `update_packages()` uses these tools to install a package (and its dependencies) only if they're not already installed and current.

## Reverse dependency checking

Devtools 1.7 included considerable improvement to reverse dependency checking. This sort of checking is important if your package gets popular, and is used by other CRAN packages. Before submitting updates to CRAN, you need to make sure that you have not broken the CRAN packages that use your package. Read more about it in the [R packages book](http://r-pkgs.had.co.nz/release.html#release-deps). To get started, run `use_revdep()`, then run the code in `revdep/check.R`.

