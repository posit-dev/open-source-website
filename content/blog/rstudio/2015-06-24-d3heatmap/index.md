---
title: 'd3heatmap: Interactive heat maps'
description: "d3heatmap creates interactive heat maps with D3.js: zoom by dragging, highlight rows/columns on click, hover to see values."
auto-description: true
people:
  - Joe Cheng
date: '2015-06-24'
categories:
  - Visualization
  - Interactive Apps
tags:
  - D3
  - Htmlwidgets
  - Packages
  - RStudio
slug: d3heatmap
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
languages: ["R"]
ported_categories:
  - Packages
---


We're pleased to announce **[d3heatmap](https://github.com/rstudio/d3heatmap)**, our new package for generating interactive heat maps using [d3.js](http://d3js.org/) and [htmlwidgets](http://www.htmlwidgets.org/). [Tal Galili](http://www.r-statistics.com/), author of [dendextend](http://cran.r-project.org/package=dendextend), collaborated with us on this package.

d3heatmap is designed to have a familiar feature set and API for anyone who has used [heatmap](http://www.rdocumentation.org/packages/stats/functions/heatmap) or [heatmap.2](http://www.rdocumentation.org/packages/gplots/functions/heatmap.2) to create static heatmaps. You can specify dendrogram, clustering, and scaling options in the same way.

d3heatmap includes the following features:

  * Shows the row/column/value under the mouse cursor

  * Click row/column labels to highlight

  * Drag a rectangle over the image to zoom in

  * Works from the R console, in RStudio, with [R Markdown](https://rmarkdown.rstudio.com/), and with [Shiny](https://shiny.rstudio.com/)

## Installation

```r
install.packages("d3heatmap")
```

## Examples

Here's a very simple example (source: [flowingdata](http://flowingdata.com/2010/01/21/how-to-make-a-heatmap-a-quick-and-easy-solution/)):

```r
library(d3heatmap)
url <- "http://datasets.flowingdata.com/ppg2008.csv"
nba_players <- read.csv(url, row.names = 1)
d3heatmap(nba_players, scale = "column")
```

[![d3heatmap](https://rstudioblog.files.wordpress.com/2015/06/screen-shot-2015-06-24-at-1-50-07-pm.png)](http://rpubs.com/jcheng/nba1)

You can easily customize the colors using the `colors` parameter. This can take an [RColorBrewer](http://cran.r-project.org/package=RColorBrewer) palette name, a vector of colors, or a function that takes (potentially scaled) data points as input and returns colors.

<!-- more -->

Let's modify the previous example by using the `"Blues"` colorbrewer palette, and dropping the clustering and dendrograms:

```r
d3heatmap(nba_players, scale = "column", dendrogram = "none",
    color = "Blues")
```

[![d3heatmap](https://rstudioblog.files.wordpress.com/2015/06/screen-shot-2015-06-24-at-1-39-15-pm.png)](http://rpubs.com/jcheng/nba2)

If you want to use discrete colors instead of continuous, you can use the `col_*` functions from the [scales](http://cran.r-project.org/package=scales) package.

```r
d3heatmap(nba_players, scale = "column", dendrogram = "none",
    color = scales::col_quantile("Blues", NULL, 5))
```

[![d3heatmap](https://rstudioblog.files.wordpress.com/2015/06/screen-shot-2015-06-24-at-1-40-21-pm.png)](http://rpubs.com/jcheng/nba3)Thanks to integration with the dendextend package, you can customize dendrograms with cluster colors:

```r
d3heatmap(nba_players, colors = "Blues", scale = "col",
    dendrogram = "row", k_row = 3)
```

[![d3heatmap](https://rstudioblog.files.wordpress.com/2015/06/screen-shot-2015-06-24-at-1-57-20-pm.png)](http://rpubs.com/jcheng/nba4)For issue reports or feature requests, please see our [GitHub repo](https://github.com/rstudio/d3heatmap).

