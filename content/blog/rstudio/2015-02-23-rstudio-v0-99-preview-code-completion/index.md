---
title: 'RStudio v0.99 Preview: Code Completion'
people:
  - RStudio Team
date: '2015-02-23'
categories:
- RStudio IDE
slug: rstudio-v0-99-preview-code-completion
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


We're busy at work on the next version of RStudio (v0.99) and this week will be blogging about some of the noteworthy new features. If you want to try out any of the new features now you can do so by downloading the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).

The first feature to highlight is a fully revamped implementation of code completion for R. We've always supported a limited form of completion however (a) it only worked on objects in the global environment; and (b) it only worked when expressly requested via the tab key. As a result not nearly enough users discovered or benefitted from code completion. In this release code completion is much more comprehensive.

### Smarter Completion Engine

Previously RStudio only completed variables that already existed in the global environment, now completion is done based on source code analysis so is provided even for objects that haven't been fully evaluated:

![document-inferred](https://rstudioblog.files.wordpress.com/2015/02/document-inferred.png)

Completions are also provided for a wide variety of specialized contexts including dimension names in [ and [[:

![bracket](https://rstudioblog.files.wordpress.com/2015/02/bracket.png)

RStudio now provides completions for function arguments within function chains using [magrittr's](http://cran.r-project.org/web/packages/magrittr/index.html) %>% operator, for e.g. [dplyr](http://cran.r-project.org/web/packages/dplyr/index.html) data transformation pipelines. Extending this behavior, we also provide the appropriate completions for the various 'verbs' used by dplyr:

![dplyr](https://rstudioblog.files.wordpress.com/2015/02/dplyr.png)        ![dplyr_verb](https://rstudioblog.files.wordpress.com/2015/02/dplyr_verb.png)

In addition, certain functions, such as library() and require(), expect package names for completions. RStudio automatically infers whether a particular function expects a package name and provides those names as completion results:

![library](https://rstudioblog.files.wordpress.com/2015/02/library.png)

Completion is now also S3 and S4 aware. If RStudio is able to determine which method a particular function call will be dispatched to it will attempt to retrieve completions from that method. For example, the sort.default() method provides an extra argument, na.last, not available in the sort() generic. RStudio will provide completions for that argument if S3 dispatch would choose sort.default()

![s3](https://rstudioblog.files.wordpress.com/2015/02/s3.png)

Beyond what's described above there are lots more new places where completions are provided:

  * For Shiny applications, completions for ui.R + server.R pairs

  * Completions for knitr options, e.g. in `opts_chunk$get()`, are now supplied

  * Completions for dynamic symbols within .C, .Call, .Fortran, .External

### Additional Enhancements

#### Always On Completion

Previously RStudio only displayed completions "on-demand" in response to the tab key. Now, RStudio will proactively display completions after a `$` or `::` as well as after a period of typing inactivity. All of this behavior is configurable via the new completion options panel:

![options](https://rstudioblog.files.wordpress.com/2015/02/options.png)

#### File Completions

When within an RStudio project, completions will be applied recursively to all file names matching the current token. The enclosing parent directory is printed on the right:

![file](https://rstudioblog.files.wordpress.com/2015/02/file.png)

#### Fuzzy Narrowing

Got a completion with an excessively long name, perhaps a particularly long named Bioconductor package, or another variable or function name of long length? RStudio now uses 'fuzzy narrowing' on the completion list, by checking to see if the completion matches a 'subsequence' within each completion. By subsequence, we mean a sequence of characters not necessarily connected within the completion, so that for example, 'fpse' could match 'file_path_sans_extension'. We hope that users will quickly become accustomed to this behavior and find it very useful.

![fuzzy](https://rstudioblog.files.wordpress.com/2015/02/fuzzy.png)

### Trying it Out

We think that the new completion features make for a qualitatively better experience of writing R code for beginning and expert users alike.  You can give the new features a try now by downloading the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).  If you run into problems or have feedback on how we could make things better let us know on our [Support Forum](https://support.rstudio.com).

