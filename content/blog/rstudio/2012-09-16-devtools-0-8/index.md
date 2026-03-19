---
title: 'New version of devtools: 0.8'
people:
  - Hadley Wickham
date: '2012-09-16'
categories:
- Packages
slug: devtools-0-8
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


We're pleased to announce a new version of devtools, the package that makes R package development easy. The main features in this version are:

  * A complete rewrite of the code loading system which simulates namespace loading much more accurately - this means using `load_all` is much closer to installing and loading the package. It also compiles and loads C, C++ and Fortran code in the `src/` directory.

  * All devtools command now only take a path to a package and default to using the working directory if no path is supplied.

  * All R commands are run in `--vanilla` mode and print the console command that's run.

  * Install github now allows you to install from pull request and private repositories.

Plus much, much more - for a complete list of changes, see the [NEWS](https://github.com/hadley/devtools/blob/master/NEWS) on github. If you're interested in package development with devtools you may also want to join the [rdevtools](http://groups.google.com/group/rdevtools) mailing list.

