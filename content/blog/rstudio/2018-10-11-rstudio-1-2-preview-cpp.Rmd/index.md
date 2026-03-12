---
title: 'RStudio 1.2 Preview: C/C++ and Rcpp'
people:
  - RStudio Team
date: '2018-10-11'
slug: rstudio-1-2-preview-cpp
categories:
- RStudio IDE
tags:
- C / C++
- RStudio
- RStudio IDE
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: in-progress
---


```r include=FALSE
image <- function(path) {
   root <- here::here()
   img <- png::readPNG(file.path(root, path))
   width <- ncol(img)
   path <- sub("^static", "", path)
   writeLines(sprintf("<img src=\"%s\" width=\"%ipx\" />", path, width / 2))
}
```

We've now discussed the improved support in RStudio v1.2 for  [SQL](https://blog.rstudio.com/2018/10/02/rstudio-1-2-preview-sql/), [D3](https://blog.rstudio.com/2018/10/05/r2d3-r-interface-to-d3-visualizations/), and [Python](https://blog.rstudio.com/2018/10/09/rstudio-1-2-preview-reticulated-python/). Today, we'll talk about IDE support for C/C++ and [Rcpp](http://www.rcpp.org/).

The IDE has had excellent support for C/C++ since RStudio v0.99, including:

- Tight integration with the [Rcpp](http://www.rcpp.org/) package
- Code completion
- Source diagnostics as you edit
- Code snippets
- Auto-indentation
- Navigable list of compilation errors
- Code navigation (go to definition)

The major new C/C++ feature in RStudio v1.2 is an upgrade to [libclang](https://clang.llvm.org/docs/Tooling.html) (our underlying completion and diagnostics engine). The update improves performance as well as adds compatibility with modern [C++ 17](https://en.wikipedia.org/wiki/C%2B%2B17) language features.

## Rcpp

RStudio integrates closely with  [Rcpp](http://www.rcpp.org/), which allows you to easily write performant C++ code and use that code in your R session. For example, the following chunk defines a simple Gibbs sampler:

```Rcpp
#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
NumericMatrix gibbs(int N, int thin) {

   NumericMatrix mat(N, 2);
   double x = 0, y = 0;

   for(int i = 0; i < N; i++) {
      for(int j = 0; j < thin; j++) {
         x = R::rgamma(3.0, 1.0 / (y * y + 4));
         y = R::rnorm(1.0 / (x + 1), 1.0 / sqrt(2 * x + 2));
      }
      mat(i, 0) = x;
      mat(i, 1) = y;
   }

   return(mat);
}
```

Such C++ code can be used both in standalone files (e.g. when used as part of an R package, or when prototyping locally) or within an R Markdown document (within an `Rcpp` chunk). In each case, we use `Rcpp::sourceCpp()` to compile and link the code -- after this, any exported functions can be called like any other R function in your session.

```r
gibbs(10, 10)
```

Thanks to the abstractions provided by Rcpp, the code implementing `gibbs()` in C++ is nearly identical to the code you’d write in R, but runs [20 times faster](http://dirk.eddelbuettel.com/blog/2011/07/14/).

## Code Completion

RStudio provides autocompletion support in C++ source files, and can autocomplete symbols used from R's C API, Rcpp, and any other libraries you may have imported.

```r echo=FALSE, results='asis'
image("static/blog-images/2018-10-11-rstudio-preview-cpp-autocomplete.png")
```

We also now provide autocompletion results for the headers you'd like to use in your program.

```r echo=FALSE, results='asis'
image("static/blog-images/2018-10-11-rstudio-preview-cpp-autocomplete-2.png")
```

## Diagnostics

RStudio also provides code diagnostics, alerting you to any issues that might exist in your code.

```r echo=FALSE, results='asis'
image("static/blog-images/2018-10-11-rstudio-preview-cpp-diagnostics.png")
```

## Updated Libclang

On Windows and macOS, we've updated the bundled version of `libclang` from 3.5.0 to 5.0.2. With this, RStudio gains improved support for modern C++: all standards from C++ 11, C++ 14 and C++ 17 are now supported.

On Linux, we now default to the version of `libclang` provided by your package manager, so that RStudio can make use of new and improved C++ tooling as it becomes available on your system. (Currently, Ubuntu 18.04 provides `libclang` 6.0.0)

## Try it Out

If you are new to C++ or Rcpp, you might be surprised at how easy it is to get started. There are lots of great resources available, including:

- Rcpp website: http://www.rcpp.org/

- Rcpp book: http://www.rcpp.org/book/

- Tutorial for users new to C++: http://adv-r.had.co.nz/Rcpp.html

- Gallery of examples: http://gallery.rcpp.org/

You can download the RStudio 1.2 Preview Release at <https://www.rstudio.com/products/rstudio/download/preview/>. If you have any questions or comments, please get in touch with us on the [community forums](https://community.rstudio.com/c/rstudio-ide).



