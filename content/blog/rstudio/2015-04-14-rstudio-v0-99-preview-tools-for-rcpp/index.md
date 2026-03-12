---
title: 'RStudio v0.99 Preview: Tools for Rcpp'
people:
  - RStudio Team
date: '2015-04-14'
categories:
- RStudio IDE
slug: rstudio-v0-99-preview-tools-for-rcpp
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


Over the past several years the [Rcpp](http://www.rcpp.org/) package has become an indispensable tool for creating high-performance R code. Its power and ease of use have made C++ a natural second language for many R users. There are over 400 packages on [CRAN](http://cran.r-project.org/) and [Bioconductor](http://www.bioconductor.org/) that depend on Rcpp and it is now the most downloaded R package.

In RStudio v0.99 we have added extensive additional tools to make working with Rcpp more pleasant, productive, and robust, these include:

  * Code completion

  * Source diagnostics as you edit

  * Code snippets

  * Auto-indentation

  * Navigable list of compilation errors

  * Code navigation (go to definition)

We think these features will go a long way to helping even more R users succeed with Rcpp. You can try the new features out now by downloading the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).

### Code Completion

RStudio v0.99 includes comprehensive code completion for C++ based on [Clang](http://en.wikipedia.org/wiki/Clang) (the same underlying engine used by XCode and many other C/C++ tools):

![Screen Shot 2015-04-07 at 12.13.31 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-07-at-12-13-31-pm.png)

Completions are provided for the C++ language, Rcpp, and any other libraries you have imported.

### Diagnostics

As you edit C++ source files RStudio uses Clang to scan your code looking for errors, incomplete code, or other conditions worthy of warnings or informational notes. For example:

![Screen Shot 2015-04-07 at 12.16.38 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-07-at-12-16-38-pm.png)

Diagnostics alert you to the possibility of subtle problems and flag outright incorrect code as early as possible, substantially reducing iteration/debugging time.

### Interactive C++

Rcpp includes some nifty tools to help make working with C++ code just as simple and straightforward as working with R code. You can "source" C++ code into R just like you'd source an R script (no need to deal with Makefiles or build systems). Here's a Gibbs Sampler implemented with Rcpp:

![Screen Shot 2015-04-13 at 4.40.36 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-13-at-4-40-36-pm.png)

We can make this function available to R by simply sourcing the C++ file (much like we'd source an R script):

```r
sourceCpp("gibbs.cpp")
gibbs(100, 10)
```

Thanks to the abstractions provided by Rcpp, the code implementing the Gibbs Sampler in C++ is nearly identical to the code you'd write in R, but runs [20 times faster](http://gallery.rcpp.org/articles/gibbs-sampler/). RStudio includes full support for Rcpp's `sourceCpp` via the **Source** button and **Ctrl+Shift+Enter** keyboard shortcut.

### Try it Out

If you are new to C++ or Rcpp you might be surprised at how easy it is to get started. There are lots of great resources available, including:

  * Rcpp website: <http://www.rcpp.org/>

  * Rcpp book: <http://www.rcpp.org/book/>

  * Tutorial for users new to C++:  <http://adv-r.had.co.nz/Rcpp.html>

  * Gallery of examples: <http://gallery.rcpp.org/>

You can give the new Rcpp features a try now by downloading the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/). If you run into problems or have feedback on how we could make things better let us know on our [Support Forum](https://support.rstudio.com).

