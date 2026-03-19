---
title: 'Shiny 0.12: Interactive Plots with ggplot2'
people:
  - Joe Cheng
date: '2015-06-16'
categories:
- Packages
- Shiny
tags:
- ggplot2
- Packages
- Shiny
slug: shiny-0-12-interactive-plots-with-ggplot2
blogcategories:
- Products and Technology
- Open Source
ported_from: rstudio
port_status: in-progress
---


Shiny 0.12 has been released to CRAN!

Compared to version 0.11.1, the major changes are:

  * Interactive plots with base graphics and ggplot2

  * Switch from RJSONIO to jsonlite

For a full list of changes and bugfixes in this version, see the [NEWS](http://cran.r-project.org/web/packages/shiny/NEWS) file.

To install the new version of Shiny, run:

```r
install.packages(c("shiny", "htmlwidgets"))
```

htmlwidgets is not required, but shiny 0.12 will not work with older versions of htmlwidgets, so it's a good idea to install a fresh copy along with Shiny.

## Interactive plots with base graphics and ggplot2

![Excluding points](https://rstudioblog.files.wordpress.com/2015/06/exclude-points.gif)

The major new feature in this version of Shiny is the ability to create interactive plots using R's base graphics or ggplot2. Adding interactivity is easy: it just requires using one option in `plotOutput()`, and then the information about mouse events will be available via the `input` object.

You can use mouse events to read mouse coordinates, select or deselect points, and implement zooming. Here are some example applications:

  * [Basic interactions](https://shiny.rstudio.com/gallery/plot-interaction-basic.html)

  * [Zooming](https://shiny.rstudio.com/gallery/plot-interaction-zoom.html)

  * [Advanced interactions](https://shiny.rstudio.com/gallery/plot-interaction-advanced.html): This demonstrates many advanced features of interactive plots.

  * [Excluding points](https://shiny.rstudio.com/gallery/plot-interaction-exclude.html) (as depicted in the screen capture above)

For more information, see the Interactive Plots [articles](https://shiny.rstudio.com/articles/#interactive-plots) in the Shiny Dev Center, and the demo apps in the [gallery](https://shiny.rstudio.com/gallery/#interactive-plots).

## Switch from RJSONIO to jsonlite

Shiny uses the JSON format to send data between the server (running R) and the client web browser (running JavaScript).

In previous versions of Shiny, the data was serialized to/from JSON using the [RJSONIO](http://cran.r-project.org/web/packages/RJSONIO/) package. However, as of 0.12.0, Shiny switched from RJSONIO to [jsonlite](http://cran.r-project.org/web/packages/jsonlite/). The reasons for this are that jsonlite has better-defined conversion behavior, and it has better performance because much of it is now implemented in C.

For the vast majority of users, this will have no impact on existing Shiny apps.

The [htmlwidgets](http://www.htmlwidgets.org/) package has also switched to jsonlite, and any Shiny apps that use htmlwidgets also require an upgrade to that package.

## A note about Data Tables

The version we just released to CRAN is actually 0.12.1; the previous version, 0.12.0, was released three weeks ago and deprecated Shiny's [`dataTableOutput` and `renderDataTable`](https://shiny.rstudio.com/articles/datatables.html) functions and instructed you to migrate to the nascent [DT](http://rstudio.github.io/DT/) package instead. (We'll talk more about DT in a future blog post.)

User feedback has indicated this transition was too sudden and abrupt, so we've undeprecated these functions in 0.12.1. We'll continue to support these functions until DT has had more time to mature.

