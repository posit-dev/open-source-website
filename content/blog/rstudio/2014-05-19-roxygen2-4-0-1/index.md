---
title: roxygen2 4.0.1
people:
  - Hadley Wickham
date: '2014-05-19'
categories:
- Packages
slug: roxygen2-4-0-1
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


We're pleased to announce a new version of roxygen2. Roxygen2 allows you to write documentation comments that are automatically converted to R's standard Rd format, saving you time and reducing duplication. This release is a major update that provides enhanced error handling and considerably safer default behaviour. Roxygen2 now adds a comment to all generated files so that you know they shouldn't be edited by hand. This also ensures that roxygen2 will never overwrite a file that it did not create, and can automatically remove files that are no longer needed.

I've also written some vignettes to help you understand how to use roxygen2. Six new vignettes provide a comprehensive overview of using roxygen2 in practice. Run `browseVignettes("roxygen2")` to read them. In an effort to make roxygen2 easier to use and more consistent between package authors, I've made parsing considerably stricter, and made sure that all errors give you the line number of the associated roxygen block. Every input is now checked to make sure that it has (e.g. every `{` has a matching `}`). This should prevent frustrating errors that require careful reading of `.Rd` files. Similarly, `@section` titles and `@export` tags can now only span a single line as this prevents a number of common bugs.

Other features include two new tags `@describeIn` and `@field`, and you can document objects (like datasets) by documenting their name as a string. For example, to document a dataset called `mydata`, you can do:

```r
#' Mydata set
#'
#' Some data I collected about myself
"mydata"
```

To see a complete list of all bug fixes and improvements, please see the release notes for [roxygen2 4.0.0](https://github.com/klutometis/roxygen/releases/tag/v4.0.0) for details. [Roxygen2 4.0.1](https://github.com/klutometis/roxygen/releases/tag/v4.0.1) fixed a couple of minor bugs and majorly improved the upgrade process.

