---
title: Shiny 0.8.0 released; Yihui Xie joins RStudio
people:
  - Joe Cheng
date: '2013-11-15'
categories:
  - Interactive Apps
slug: shiny-0-8-0-released
blogcategories:
  - Products and Technology
  - Company News and Events
  - Open Source
tags:
  - Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - News
  - Shiny
---


We're very pleased to announce [Shiny 0.8.0](http://rstudio.com/shiny/) (which actually went up on CRAN about two weeks ago). This release features a vastly better way to display tabular data, and new debugging tools that make it much easier to fix errors in your app.

## DataTables support

![datatables](https://rstudioblog.files.wordpress.com/2013/11/datatables1.png)

We now support much more attractive and powerful displays of tabular data using the popular [DataTables](http://datatables.net/) library. Our DataTables integration features pagination, searching/filtering, sorting, and more. Check out [this demo](http://glimmer.rstudio.com/yihui/12_datatables/) to see it in action, and learn more about how to use it in your own apps by visiting the tutorial's [chapter on DataTables](http://rstudio.github.io/shiny/tutorial/#datatables).

## Debugging tools

In [version 0.8.0](http://cran.rstudio.com/web/packages/shiny/) of the [Shiny](http://rstudio.com/shiny/) package, we've greatly improved the set of debugging tools you can use with your Shiny apps. It's now much easier to figure out what's happening when things go wrong, thanks to two new features:

  * Integration with the new visual debugger that's available with [RStudio v0.98](https://www.rstudio.com/ide/download/preview). You can set breakpoints and step through your code much more easily than before.

  * A new option 'shiny.error' which can take a function as an error handler. It is called when an error occurs in a reactive observer (e.g. when running an output rendering function). You can use options(shiny.error=traceback) to simply print a traceback, options(shiny.error=recover) for debugging from a regular R console, or options(shiny.error=browser) to jump into the RStudio visual debugger.

There have also been a few smaller tweaks and bug fixes. For the full list, you can take a look at our [NEWS file](http://cran.rstudio.com/web/packages/shiny/NEWS).

## Welcome, Yihui Xie!

If you're reading this, there's a good chance you have heard of [Yihui Xie](http://yihui.name) or have used his software; during his time as a PhD student at Iowa State University, he created the [knitr](http://yihui.name/knitr/), [cranvas](http://cranvas.org/), and [animation](http://cran.r-project.org/web/packages/animation/index.html) packages, among others.

We're thrilled to announce that Yihui has joined the RStudio team! He will be one of the primary maintainers of the Shiny package and has already contributed some great improvements in the short time he has been with us.

