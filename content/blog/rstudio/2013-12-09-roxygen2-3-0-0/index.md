---
title: roxygen2 3.0.0
people:
  - Hadley Wickham
date: '2013-12-09'
categories:
- Packages
slug: roxygen2-3-0-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


We're pleased to announce a new version of roxygen2. The biggest news is that you can painlessly document your S4 classes, S4 methods and RC classes with roxygen2 - you can safely remove workarounds that used `@alias` and `@usage`, and simply rely on roxygen2 to do the right thing. Roxygen2 is also much smarter when it comes to S3: you can remove existing uses of `@method`, and can replace `@S3method` with `@export`.

Version 3.0 also includes many other improvements including better generation of usage, the ability to turn off wrapping in your Rd files and choose default roclets for a package, a safer `roxygenise()` (or `roxyngenize()` if you prefer) and many other bug fixes and improvement. See the full list on the [github release](https://github.com/klutometis/roxygen/releases/tag/v3.0.0).

As always, you can install the latest version with `install.packages("roxygen2")`

