---
title: Announcing Packrat v0.4
people:
  - Kevin Ushey
date: '2014-07-22'
categories:
- Packages
- RStudio IDE
slug: announcing-packrat-v0-4
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- RStudio IDE
ported_from: rstudio
port_status: in-progress
software: ["packrat"]
languages: ["R"]
---


We're excited to announce a new release of [Packrat](http://rstudio.github.io/packrat/), a tool for making R projects more isolated and reproducible by managing their package dependencies.

This release brings a number of exciting features to Packrat that significantly improve the user experience:

  * **Automatic snapshots** ensure that new packages installed in your project library are automatically tracked by Packrat.

  * **Bundle and share your projects** with packrat::bundle() and packrat::unbundle() -- whether you want to freeze an analysis, or exchange it for collaboration with colleagues.

  * **Packrat mode** can now be turned on and off at will, allowing you to navigate between different Packrat projects in a single R session. Use packrat::on() to activate Packrat in the current directory, and packrat::off() to turn it off.

  * **Local repositories** (ie, directories containing R package sources) can now be specified for projects, allowing local source packages to be used in a Packrat project alongside CRAN, BioConductor and GitHub packages (see this and more with ?"packrat-options").

In addition, Packrat is now [tightly integrated with the RStudio IDE](http://rstudio.github.io/packrat/rstudio.html), making it easier to manage project dependencies than ever. Download today's [RStudio IDE 0.98.978 release](https://www.rstudio.com/products/rstudio/download/) and try it out!

[![Packrat RStudio package pane integration](https://rstudioblog.files.wordpress.com/2014/07/screen-shot-2014-07-22-at-10-32-12-am.png)](http://rstudio.github.io/packrat/rstudio.html)

You can install the latest version of Packrat from [GitHub](http://www.github.com/rstudio/packrat) with:

```r
devtools::install_github("rstudio/packrat")
```

Packrat will be coming to CRAN soon as well.

If you try it, we'd love to get your feedback. Leave a comment here or post in the [packrat-discuss Google group](https://groups.google.com/forum/#!forum/packrat-discuss).

