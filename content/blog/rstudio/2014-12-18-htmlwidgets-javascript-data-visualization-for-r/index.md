---
title: 'htmlwidgets: JavaScript data visualization for R'
description: "Introducing htmlwidgets: bring JavaScript visualization libraries to R. Works in console, R Markdown, and Shiny."
auto-description: true
people:
  - RStudio Team
date: '2014-12-18'
categories:
  - Interactive Apps
slug: htmlwidgets-javascript-data-visualization-for-r
blogcategories:
  - Products and Technology
  - Company News and Events
  - Open Source
tags:
  - Packages
  - Shiny
  - RStudio
  - News
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - News
  - Packages
  - Shiny
---


Today we're excited to announce [htmlwidgets](http://www.htmlwidgets.org), a new framework that brings the best of JavaScript data visualization libraries to R. There are already several packages that take advantage of the framework ([leaflet](http://www.htmlwidgets.org/showcase_leaflet.html), [dygraphs](http://www.htmlwidgets.org/showcase_dygraphs.html), [networkD3](http://www.htmlwidgets.org/showcase_networkD3.html), [DataTables](http://www.htmlwidgets.org/showcase_datatables.html), and [rthreejs](http://www.htmlwidgets.org/showcase_threejs.html)) with hopefully many more to come.

An **htmlwidget** works just like an R plot except it produces an interactive web visualization. A line or two of R code is all it takes to produce a D3 graphic or Leaflet map. Widgets can be used at the R console as well as embedded in [R Markdown](http://rmarkdown.rstudio.com) reports and [Shiny](https://shiny.rstudio.com) web applications. Here's an example of using leaflet directly from the R console:

![rconsole.2x](https://rstudioblog.files.wordpress.com/2014/12/rconsole-2x.png)

When printed at the console the leaflet widget displays in the RStudio Viewer pane. All of the tools typically available for plots are also available for widgets, including history, zooming, and export to file/clipboard (note that when not running within RStudio widgets will display in an external web browser).

Here's the same widget in an R Markdown report. Widgets automatically print as HTML within R Markdown documents and even respect the default knitr figure width and height.

![rmarkdown.2x](https://rstudioblog.files.wordpress.com/2014/12/rmarkdown-2x.png)

Widgets also provide Shiny output bindings so can be easily used within web applications. Here's the same widget in a Shiny application:

![shiny.2x](https://rstudioblog.files.wordpress.com/2014/12/shiny-2x.jpg)

### **Bringing JavaScript to R**

The **htmlwidgets** framework is a collaboration between Ramnath Vaidyanathan (rCharts), Kenton Russell (Timely Portfolio), and RStudio. We've all spent countless hours creating bindings between R and the web and were motivated to create a framework that made this as easy as possible for all R developers.

There are a plethora of libraries available that create attractive and fully interactive data visualizations for the web. However, the programming interface to these libraries is JavaScript, which places them outside the reach of nearly all statisticians and analysts. **htmlwidgets** makes it extremely straightforward to create an R interface for any JavaScript library.

Here are a few widget libraries that have been built so far:

  * [leaflet](http://www.htmlwidgets.org/showcase_leaflet.html), a library for creating dynamic maps that support panning and zooming, with various annotations like markers, polygons, and popups.

  * [dygraphs](http://www.htmlwidgets.org/showcase_dygraphs.html), which provides rich facilities for charting time-series data and includes support for many interactive features including series/point highlighting, zooming, and panning.

  * [networkD3](http://www.htmlwidgets.org/showcase_networkD3.html), a library for creating D3 network graphs including force directed networks, Sankey diagrams, and Reingold-Tilford tree networks.

  * [DataTables](http://www.htmlwidgets.org/showcase_datatables.html), which displays R matrices or data frames as interactive HTML tables that support filtering, pagination, and sorting.

  * [rthreejs](http://www.htmlwidgets.org/showcase_threejs.html), which features 3D scatterplots and globes based on WebGL.

All of these libraries combine visualization with direct interactivity, enabling users to explore data dynamically. For example, time-series visualizations created with dygraphs allow dynamic panning and zooming:

[![NewHavenTemps](https://rstudioblog.files.wordpress.com/2014/12/newhaventemps.png)](http://rstudio.github.io/dygraphs/gallery-range-selector.html)

### **Learning More**

To learn more about the framework and see a showcase of the available widgets in action check out the [htmlwidgets web site](http://www.htmlwidgets.org). To learn more about building your own widgets, install the **htmlwidgets** package from CRAN and check out the [developer documentation](http://www.htmlwidgets.org/develop_intro.html).

