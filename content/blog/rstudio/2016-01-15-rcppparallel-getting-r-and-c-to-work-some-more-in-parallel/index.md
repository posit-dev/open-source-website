---
title: 'RcppParallel: Getting R and C++ to work (some more) in parallel'
people:
  - RStudio Team
date: '2016-01-15'
categories:
  - Best Practices
slug: rcppparallel-getting-r-and-c-to-work-some-more-in-parallel
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
ported_from: rstudio
port_status: in-progress
languages: ["R"]
ported_categories:
  - Packages
---


(Post by [Dirk Eddelbuettel](http://dirk.eddelbuettel.com/) and [JJ Allaire](https://github.com/jjallaire))

A common theme over the last few decades was that we could afford to simply sit back and let computer (hardware) engineers take care of increases in computing speed thanks to [Moore's law](http://en.wikipedia.org/wiki/Moore%27s_law). That same line of thought now frequently points out that we are getting closer and closer to the physical limits of what Moore's law can do for us.

So the new best hope is (and has been) parallel processing. Even our smartphones have multiple cores, and most if not all retail PCs now possess two, four or more cores. Real computers, aka somewhat decent servers, can be had with 24, 32 or more cores as well, and all that is before we even consider GPU coprocessors or [other upcoming changes](http://en.wikipedia.org/wiki/Xeon_Phi).

Sometimes our tasks are embarrassingly simple as is the case with many data-parallel jobs: we can use higher-level operations such as those offered by the base R package [parallel](https://stat.ethz.ch/R-manual/R-devel/library/parallel/doc/parallel.pdf) to spawn multiple processing tasks and gather the results. Dirk covered all this in some detail in previous [talks](http://dirk.eddelbuettel.com/presentations.html) on High Performance Computing with R (and you can also consult the [CRAN ](http://cran.r-project.org/web/views/HighPerformanceComputing.html)[Task View on High Performance Computing with R](http://cran.r-project.org/web/views/HighPerformanceComputing.html)).

But sometimes we cannot use data-parallel approaches. Hence we have to redo our algorithms. Which is _really hard_. R itself has been relying on the (fairly mature) [OpenMP](http://openmp.org/wp/) standard for some of its operations. [Luke Tierney's ](http://www.rinfinance.com/agenda/2014/talk/LukeTierney.pdf)[keynote](http://www.rinfinance.com/agenda/2014/talk/LukeTierney.pdf) at the 2014 R/Finance conference mentioned some of the issues related to OpenMP, which works really well on Linux but currently not so well on other platforms. R is expected to make wider use of it in future versions once compiler support for OpenMP on Windows and OS X improves.

In the meantime, the [RcppParallel](http://rcppcore.github.io/RcppParallel) package provides a complete toolkit for creating portable, high-performance parallel algorithms without requiring direct manipulation of operating system threads. RcppParallel includes:

  * [Intel Thread Building Blocks](https://www.threadingbuildingblocks.org/) (v4.3), a C++ library for task parallelism with a wide variety of parallel algorithms and data structures (Windows, OS X, Linux, and Solaris x86 only).

  * [TinyThread](http://tinythreadpp.bitsnbites.eu/), a C++ library for portable use of operating system threads.

  * `RVector` and `RMatrix` wrapper classes for safe and convenient access to R data structures in a multi-threaded environment.

  * High level parallel functions (`parallelFor` and `parallelReduce`) that use Intel TBB as a back-end on systems that support it and TinyThread on other platforms.

RcppParallel is [available on CRAN](https://cran.r-project.org/web/packages/RcppParallel/index.html) now and several packages including [dbmss](https://cran.r-project.org/web/packages/dbmss/index.html), [gaston](https://cran.r-project.org/web/packages/gaston/index.html), [markovchain](https://cran.r-project.org/web/packages/markovchain/index.html), [rPref](https://cran.r-project.org/web/packages/rPref/index.html), [SpatPCA](https://cran.r-project.org/web/packages/SpatPCA/index.html), [StMoSim](https://cran.r-project.org/web/packages/StMoSim/index.html), and [text2vec](https://cran.r-project.org/web/packages/text2vec/index.html) are already taking advantage of it (you can read more about the tex2vec implementation [here](http://dsnotes.com/blog/text2vec/2016/01/09/fast-parallel-async-adagrad/)).

For more background and documentation see the [RcppParallel web site](http://rcppcore.github.io/RcppParallel) as well as the slides from the [talk we gave on RcppParallel](http://dirk.eddelbuettel.com/papers/rcpp_parallel_talk_jan2015.pdf) at the Workshop for Distributed Computing in R.

In addition, the [Rcpp Gallery](http://gallery.rcpp.org/) includes several pieces demonstrating the use of RcppParallel, including:

  * [A parallel matrix transformation](http://gallery.rcpp.org/articles/parallel-matrix-transform)

  * [A parallel vector summation](http://gallery.rcpp.org/articles/parallel-vector-sum)

  * [A parallel inner product](http://gallery.rcpp.org/articles/parallel-inner-product)

  * [A parallel distance matrix calculation ](http://gallery.rcpp.org/articles/parallel-distance-matrix)

All four are interesting and demonstrate different aspects of parallel computing via [RcppParallel](http://rcppcore.github.io/RcppParallel). But the last article is key—it shows how a particular matrix distance metric (which is missing from R) can be implemented in a serial manner in both R, and also via Rcpp. The fastest implementation, however, uses both Rcpp and [RcppParallel](http://rcppcore.github.io/RcppParallel) and thereby achieves a truly impressive speed gain as the gains from using compiled code (via Rcpp) and from using a parallel algorithm (via RcppParallel) are multiplicative. On a couple of four-core machines the RcppParallel version was between 200 and 300 times faster than the R version.

Exciting times for parallel programming in R! To learn more head over to the [RcppParallel](http://rcppcore.github.io/RcppParallel) package and start playing.

