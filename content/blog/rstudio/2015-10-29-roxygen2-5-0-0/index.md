---
title: roxygen2 5.0.0
people:
  - Hadley Wickham
date: '2015-10-29'
slug: roxygen2-5-0-0
blogcategories:
- Products and Technology
- Open Source
tags:
ported_from: rstudio
port_status: in-progress
software: ["roxygen2"]
languages: ["R"]
categories:
  - Best Practices
ported_categories:
  - Packages
---


roxygen2 5.0.0 is now available on CRAN. roxygen2 helps you document your packages by turning specially formatted inline comments in R's standard Rd format. Learn more at <http://r-pkgs.had.co.nz/man.html>.

In this release:

  * Roxygen records its version in a single place: the `RoxygenNote` field in your `DESCRIPTION`. This should make it easier to see what's changed when you upgrade roxygen2, because only files with differences will be modified. Previously every Rd file was modified to update the version number.

  * You can now easily document functions that you've imported from another package:

```r
#' @importFrom magrittr %>%
#' @export
magrittr::`%>%`
```

All imported-and-re-exported functions will be documented in the same file (`rexports.Rd`), with a brief descrption and links to the original documentation.

  * You can more easily generate package documentation by documenting the special string "_PACKAGE":

```r
#' @details Details
"_PACKAGE"
```

The title and description will be automatically filled in from the `DESCRIPTION`.

  * New tags `@rawRd` and `@rawNamespace` allow you to insert raw (unescaped) text in Rd and the `NAMESPACE`. `@evalRd()` is similar, but instead of literal Rd, you give it R code that produces literal Rd code when run. This should make it easier to experiment with new types of output.

  * Roxygen2 now parses the source code files in the order specified in the `Collate` field in `DESCRIPTION`. This improves the ordering of the generated documentation when using `@describeIn` and/or `@rdname` split across several `.R` files, as often happens when working with S4.

  * The parser has been completely rewritten in C++. This gives a nice performance boost and adds improves the error messages: now get the line number of the tag, not the start of the block.

  * `@family` now cross-links each manual page only once, instread of linking to all aliases.

There were many other minor improvements and bug fixes; please see the [release notes](https://github.com/klutometis/roxygen/releases/tag/v5.0.0) for a complete list. A bug thanks goes to all the [contributors](https://github.com/klutometis/roxygen/graphs/contributors?from=2015-06-04&to=2015-10-29&type=c) who made this release possible.

