---
title: New Version of RStudio (v0.99) Available Now
people:
  - RStudio Team
date: '2015-05-26'
categories:
- News
- RStudio IDE
slug: new-version-of-rstudio-v0-99
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


We're pleased to announce that the final version of RStudio v0.99 is [available for download](https://www.rstudio.com/ide/download) now. Highlights of the release include:

  * A new [data viewer](https://support.rstudio.com/hc/en-us/articles/205175388-Using-the-Data-Viewer) with support for large datasets, filtering, searching, and sorting.

  * Complete overhaul of R [code completion](https://support.rstudio.com/hc/en-us/articles/205273297-Code-Completion) with many new features and capabilities.

  * The source editor now provides [code diagnostics](https://support.rstudio.com/hc/en-us/articles/205753617-Code-Diagnostics) (errors, warnings, etc.) as you work.

  * User customizable [code snippets](https://support.rstudio.com/hc/en-us/articles/204463668-Code-Snippets) for automating common editing tasks.

  * [Tools for Rcpp](https://blog.rstudio.com/2015/04/14/rstudio-v0-99-preview-tools-for-rcpp/): completion, diagnostics, code navigation, find usages, and automatic indentation.

  * Many additional [source editor improvements](https://blog.rstudio.com/2015/05/06/rstudio-v0-99-preview-more-editor-enhancements/) including multiple cursors, tab re-ordering, and several new themes.

  * An [enhanced Vim mode](https://blog.rstudio.com/2015/02/23/rstudio-0-99-preview-vim-mode-improvements/) with visual block selection, macros, marks, and subset of : commands.

There are also lots of smaller improvements and bug fixes across the product. Check out the [v0.99 release notes](https://www.rstudio.com/products/rstudio/release-notes/) for details on all of the changes.

### Data Viewer

We've completely overhauled the data viewer with many new capabilities including live update, sorting and filtering, full text searching, and no row limit on viewed datasets.

![data-viewer](https://rstudioblog.files.wordpress.com/2015/05/screen-shot-2015-05-06-at-12-01-14-pm.png)

See the [data viewer documentation](https://support.rstudio.com/hc/en-us/articles/205175388-Using-the-Data-Viewer) for more details.

### Code Completion

Previously RStudio only completed variables that already existed in the global environment. Now completion is done based on source code analysis so is provided even for objects that haven't been fully evaluated:

![completion-scopes](https://rstudioblog.files.wordpress.com/2015/05/screen-shot-2015-05-06-at-11-50-41-am.png)

Completions are also provided for a wide variety of specialized contexts including dimension names in [ and [[:

![completion-bracket](https://rstudioblog.files.wordpress.com/2015/05/screen-shot-2015-05-06-at-11-54-22-am.png)

### Code Diagnostics

We've added a new inline code diagnostics feature that highlights various issues in your R code as you edit.

For example, here we're getting a diagnostic that notes that there is an extra parentheses:

![Screen Shot 2015-04-08 at 12.04.14 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-08-at-12-04-14-pm.png)

Here the diagnostic indicates that we've forgotten a comma within a shiny UI definition:

![diagnostics-comma](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-28-at-11-29-46-am.png)

A wide variety of diagnostics are supported, including optional diagnostics for code style issues (e.g. the inclusion of unnecessary whitespace). Diagnostics are also available for several other languages including C/C++, JavaScript, HTML, and CSS. See the [code diagnostics documentation](https://support.rstudio.com/hc/en-us/articles/205753617-Code-Diagnostics) for additional details.

### Code Snippets

Code snippets are text macros that are used for quickly inserting common snippets of code. For example, the `fun` snippet inserts an R function definition:

![Insert Snippet](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-07-at-10-39-50-am.png)

If you select the snippet from the completion list it will be inserted along with several text placeholders which you can fill in by typing and then pressing **Tab** to advance to the next placeholder:

![Screen Shot 2015-04-07 at 10.44.39 AM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-07-at-10-44-39-am.png)

Other useful snippets include:

  * `lib`, `req`, and `source` for the library, require, and source functions

  * `df` and `mat` for defining data frames and matrices

  * `if`, `el`, and `ei` for conditional expressions

  * `apply`, `lapply`, `sapply`, etc. for the apply family of functions

  * `sc`, `sm`, and `sg` for defining S4 classes/methods.

See the [code snippets documentation](https://support.rstudio.com/hc/en-us/articles/204463668-Code-Snippets) for additional details.

### Try it Out

RStudio v0.99 is [available for download](https://www.rstudio.com/products/rstudio/download/) now. We hope you enjoy the new release and as always please [let us know](https://support.rstudio.com) how it's working and what else we can do to make the product better.

