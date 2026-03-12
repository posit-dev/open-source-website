---
title: New version of RStudio (v0.97)
people:
  - RStudio Team
date: '2012-11-01'
categories:
- RStudio IDE
slug: new-version-of-rstudio-v0-97
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


Today a new version of RStudio (v0.97) is [available for download](https://www.rstudio.com/ide/download) from our website.  The principal focus of this release was creating comprehensive tools for R package development. We also implemented many other frequently requested enhancements including a new [Vim](http://en.wikipedia.org/wiki/Vim_(text_editor)) editing mode and a much improved Find and Replace pane. Here's a summary of what's new in the release:

#### Package Development

  * A new Build tab with package development commands and a view of build output and errors

  * Build and Reload command that rebuilds the package and reloads it in a fresh R session

  * Create a new package using existing source files via New Project

  * R documentation tools including previewing, spell-checking, and [Roxygen](https://github.com/klutometis/roxygen) aware editing

  * Integration with [devtools](https://github.com/hadley/devtools) package development functions

  * Support for [Rcpp](http://dirk.eddelbuettel.com/code/rcpp.html) including syntax highlighting for C/C++ and gcc error navigation

#### Source Editor

  * [Vim](http://en.wikipedia.org/wiki/Vim_(text_editor)) editing mode

  * [Tomorrow](https://github.com/chriskempson/tomorrow-theme#readme) suite of editor themes

  * Find and replace: incremental search, find/replace in selection, and backwards find

  * Auto-indenting: improved intelligence and new options to customize indenting behavior

  * New options: show whitespace, show indent guides, non-blinking cursor, focus console after executing code

#### More

  * New Restart R and Terminate R commands

  * More intelligent console history navigation with up/down arrow keys

  * View plots within a separate window/monitor.

  * Ability to set a global UI zoom-level

  * RStudio CRAN mirror (via Amazon CloudFront) for fast package downloads

There are also many more small improvements and bug fixes. Check out the [v0.97 release notes](https://www.rstudio.com/ide/docs/release_notes_v0.97.html) for details on all of the changes.

