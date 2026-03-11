---
title: RStudio and Rcpp
people:
  - RStudio Team
date: '2012-11-29'
categories:
- Packages
- RStudio IDE
slug: rstudio-and-rcpp
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


Earlier this month a new version of the Rcpp package by [Dirk Eddelbuettel](http://dirk.eddelbuettel.com/) and [Romain François](http://romainfrancois.blog.free.fr)  was released to CRAN and today we're excited to announce a [new version of RStudio](https://www.rstudio.com/ide/download/) that integrates tightly with Rcpp.

First though more about some exciting new features in [Rcpp 0.10.1](http://dirk.eddelbuettel.com/blog/2012/11/27/#rcpp_0.10.1). This release includes [Rcpp attributes](http://cran.rstudio.com/web/packages/Rcpp/vignettes/Rcpp-attributes.pdf), which are simple annotations that you add to C++ source files to streamline calling C++ from R.  This makes it possible to write C++ functions and simply source them into R just as you'd source an R script. Here's an example:

````cpp
#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
NumericMatrix gibbs(int N, int thin) {

   NumericMatrix mat(N, 2);
   double x = 0, y = 0;

   RNGScope scope;
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
````

By annotating the gibbs function with the `Rcpp::export` attribute, we indicate we'd like that function to be callable from R. As a result we can now call the function like this:

````r
sourceCpp("gibbs.cpp")
gibbs(100, 10)
````

Thanks to the abstractions provided by Rcpp, the code implementing gibbs in C++ is nearly identical to the code you'd write in R, but runs [20 times faster](http://dirk.eddelbuettel.com/blog/2011/07/14/).

The `sourceCpp` function makes it much easier to use C++ within interactive R sessions. In the new version of RStudio we did a few things to support this workflow. Here's a screenshot showing the RStudio C++ editing mode:

![](https://www.rstudio.com/images/docs/rcpp_sourcecpp.png)

In RStudio you can now source a C++ file in the same way as an R script, using the source button on the toolbar or Cmd+Shift+Enter. If errors occur during compilation then RStudio parses the GCC error log and presents the errors as a navigable list.

When using `sourceCpp` it's also possible to embed R code within a C++ source file using a special block comment. RStudio treats this code as an R code chunk (similar to Sweave or R Markdown code chunks):

![](https://www.rstudio.com/images/docs/rcpp_sourcecpp_rchunks.png)

RStudio also includes extensive support for package development with Rcpp. For more details see the [Using Rcpp with RStudio](https://www.rstudio.com/ide/docs/advanced/using_rcpp) document on our website.

Note that if you want to try out the new features be sure you are running [RStudio v0.97.237](https://www.rstudio.com/ide/download/) as well as the very latest version of [Rcpp](http://cran.rstudio.com/web/packages/Rcpp/) (0.10.1) .

