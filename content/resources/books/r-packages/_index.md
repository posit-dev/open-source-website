---
title: R Packages
subtitle: Organize, Test, Document, and Share Your Code
date: '2023-06-01'
description: Learn how to turn your R code into packages that are documented, tested, and easy to share, using devtools, usethis, testthat, and roxygen2, all the way to a pkgdown website and a CRAN release.
image: cover.jpg
color: '#944739'
resource_type: book
edition: 2
publisher: O'Reilly Media
isbn: '9781098134945'
pages: 381
people:
- Hadley Wickham
- Jenny Bryan
website: https://r-pkgs.org/
read_url: https://r-pkgs.org/
buy_url: https://www.oreilly.com/library/view/r-packages-2nd/9781098134938/
github: hadley/r-pkgs
software:
- devtools
- usethis
- testthat
- roxygen2
- pkgdown
languages:
- R
topics:
- Best Practices
---

In R, the package is the fundamental unit of shareable, reusable code: it bundles functions, documentation, sample data, and tests in a form that any R user knows how to install and use.
Hadley Wickham and Jennifer Bryan show you how to turn your own code into packages, whether you plan to share them widely or simply want to save yourself time by following well-established conventions.

The book follows a guiding principle: anything that can be automated should be automated.
It relies on `devtools`, `usethis`, `testthat`, `roxygen2`, and the RStudio IDE to handle routine tasks, so you can focus on what your package should do instead of the mechanics of its structure.
This fully updated second edition reflects the practices of the team at Posit that maintains the tidyverse and hundreds of other open source packages.
It encourages you to start simple and improve your package over time.

You will learn how to:

- Build a small package from start to finish to see the whole workflow
- Set up your system and understand how packages are structured
- Organize R code, data, and other package components
- Write the DESCRIPTION file, manage dependencies, and choose a license
- Write and organize tests with the third edition of `testthat`
- Document functions with `roxygen2`, write vignettes, and build a website with `pkgdown`
- Use Git, GitHub, and continuous integration to maintain your package
- Manage the package lifecycle and release to CRAN

The second edition is free to read online at the book's website.
