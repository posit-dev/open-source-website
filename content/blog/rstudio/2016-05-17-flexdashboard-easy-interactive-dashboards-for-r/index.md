---
title: 'flexdashboard: Easy interactive dashboards for R'
people:
  - RStudio Team
date: '2016-05-17'
categories:
  - Publishing
  - Interactive Apps
slug: flexdashboard-easy-interactive-dashboards-for-r
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - R Markdown
  - Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Packages
  - R Markdown
  - Shiny
---


Today we're excited to announce [flexdashboard](https://rmarkdown.rstudio.com/flexdashboard/), a new package that enables you to easily create flexible, attractive, interactive dashboards with R. Authoring and customization of dashboards is done using [R Markdown](http://rmarkdown.rstudio.com) and you can optionally include [Shiny](https://shiny.rstudio.com) components for additional interactivity.

![neighborhood-diversity-flexdashboard](https://rstudioblog.files.wordpress.com/2016/05/neighborhood-diversity-flexdashboard.png)

Highlights of the [flexdashboard](https://rmarkdown.rstudio.com/flexdashboard/) package include:

  * Support for a wide variety of components including interactive [htmlwidgets](http://www.htmlwidgets.org/); base, lattice, and grid graphics; tabular data; gauges; and value boxes.

  * Flexible and easy to specify row and column-based [layouts](https://rmarkdown.rstudio.com/flexdashboard/layouts.html). Components are intelligently re-sized to fill the browser and adapted for display on mobile devices.

  * Extensive support for text annotations to include assumptions, contextual narrative, and analysis within dashboards.

  * [Storyboard](https://rmarkdown.rstudio.com/flexdashboard/using.html#storyboards) layouts for presenting sequences of visualizations and related commentary.

  * By default dashboards are standard HTML documents that can be deployed on any web server or even attached to an email message. You can optionally add [Shiny](https://shiny.rstudio.com/) components for additional interactivity and then [deploy](https://shiny.rstudio.com/deploy/) on Shiny Server or shinyapps.io.

### Getting Started

The flexdashboard package is available on CRAN; you can install it as follows:

````
install.packages("flexdashboard", type = "source")
````

To author a flexdashboard you create an [R Markdown](https://rmarkdown.rstudio.com/) document with the `flexdashboard::flex_dashboard` output format. You can do this from within RStudio using the **New R Markdown** dialog:

![](https://rmarkdown.rstudio.com/flexdashboard/images/NewRMarkdown.png)

Dashboards are simple R Markdown documents where each level 3 header (`###`) defines a section of the dashboard. For example, here's a simple dashboard layout with 3 charts arranged top to bottom:

````
---
title: "My Dashboard"
output: flexdashboard::flex_dashboard
---

### Chart 1

```r

```

### Chart 2

```r

```

### Chart 3

```r

```
````

You can use level 2 headers (`-----------`) to introduce rows and columns into your dashboard and section attributes to control their relative size:

````
---
title: "My Dashboard"
output: flexdashboard::flex_dashboard
---

Column {data-width=600}
-------------------------------------

### Chart 1

```r

```

Column {data-width=400}
-------------------------------------

### Chart 2

```r

```

### Chart 3

```r

```
````

### Learning More

The [flexdashboard website](https://rmarkdown.rstudio.com/flexdashboard/) includes extensive documentation on building your own dashboards, including:

  * A [user guide](https://rmarkdown.rstudio.com/flexdashboard/using.html) for all of the features and options of flexdashboard, including layout orientations (row vs. column based), chart sizing, the various supported components, theming, and creating dashboards with multiple pages.

  * Details on using [Shiny](https://rmarkdown.rstudio.com/flexdashboard/shiny.html) to create dashboards that enable viewers to change underlying parameters and see the results immediately, or that update themselves incrementally as their underlying data changes.

  * A variety of [sample layouts](https://rmarkdown.rstudio.com/flexdashboard/layouts.html) which you can use as a starting point for your own dashboards.

  * Many [examples](https://rmarkdown.rstudio.com/flexdashboard/examples.html) of flexdashboard in action (including links to source code if you want to dig into how each example was created).

The examples below illustrate the use of flexdashboard with various packages and layouts (click the thumbnail to view a running version of each dashboard):

[![htmlwidgets-d3heatmap](https://rstudioblog.files.wordpress.com/2016/05/htmlwidgets-d3heatmap.png)](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-d3heatmap/)

<p class="caption">d3heatmap: NBA scoring</p>

[![ggplotly: ggplot2 geoms](https://rstudioblog.files.wordpress.com/2016/05/plotly.png)](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-ggplotly-geoms/)

<p class="caption">ggplotly: ggplot2 geoms</p>

[![Shiny: biclust example](https://rstudioblog.files.wordpress.com/2016/05/shiny-biclust.png)](https://jjallaire.shinyapps.io/shiny-biclust/)

<p class="caption">Shiny: biclust example</p>

[![dygraphs: Linked time series](https://rstudioblog.files.wordpress.com/2016/05/dygraphs.png)](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-dygraphs/)

<p class="caption">dygraphs: linked time series</p>

[![highcharter: sales report](https://rstudioblog.files.wordpress.com/2016/05/htmlwidgets-highcharter.png)](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-highcharter/)

<p class="caption">highcharter: sales report</p>

[![Storyboard: htmlwidgets showcase](https://rstudioblog.files.wordpress.com/2016/05/htmlwidgets-showcase-storyboard.png)](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-showcase-storyboard/)

<p class="caption">Storyboard: htmlwidgets showcase</p>

[![rbokeh: iris dataset](https://rstudioblog.files.wordpress.com/2016/05/htmlwidgets-rbokeh-iris.png)](https://beta.rstudioconnect.com/jjallaire/htmlwidgets-rbokeh-iris/)

<p class="caption">rbokeh: iris dataset</p>

[![Shiny: diamonds explorer](https://rstudioblog.files.wordpress.com/2016/05/shiny-diamonds-explorer.png)](https://jjallaire.shinyapps.io/shiny-ggplot2-diamonds/)

<p class="caption">Shiny: diamonds explorer</p>

### Try It Out

The [flexdashboard](https://rmarkdown.rstudio.com/flexdashboard/) package provides a simple yet powerful framework for creating dashboards from R. If you know R Markdown you already know enough to begin creating dashboards right now! We hope you'll try it out and [let us know](https://github.com/rstudio/flexdashboard/issues) how it's working and what else we can do to make it better.

