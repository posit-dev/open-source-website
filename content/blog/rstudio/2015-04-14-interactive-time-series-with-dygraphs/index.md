---
title: Interactive time series with dygraphs
people:
  - RStudio Team
date: '2015-04-14'
slug: interactive-time-series-with-dygraphs
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
categories:
  - Interactive Apps
ported_categories:
  - Packages
  - Shiny
---


The [dygraphs package](http://rstudio.github.io/dygraphs/) is an R interface to the dygraphs JavaScript charting library. It provides rich facilities for charting time-series data in R, including:

  * Automatically plots [xts](http://cran.rstudio.com/web/packages/xts/index.html) time-series objects (or objects convertible to xts).

  * Rich interactive features including [zoom/pan](http://rstudio.github.io/dygraphs/gallery-range-selector.html) and series/point [highlighting](http://rstudio.github.io/dygraphs/gallery-series-highlighting.html).

  * Highly configurable axis and series display (including optional 2nd Y-axis).

  * Display [upper/lower bars](http://rstudio.github.io/dygraphs/gallery-upper-lower-bars.html) (e.g. prediction intervals) around series.

  * Various graph overlays including [shaded regions](http://rstudio.github.io/dygraphs/gallery-shaded-regions.html), [event lines](http://rstudio.github.io/dygraphs/gallery-event-lines.html), and [annotations](http://rstudio.github.io/dygraphs/gallery-annotations.html).

  * Use at the R console just like conventional R plots (via RStudio Viewer).

  * Embeddable within [R Markdown](http://rstudio.github.io/dygraphs/r-markdown.html) documents and [Shiny](http://rstudio.github.io/dygraphs/shiny.html) web applications.

The dygraphs package is available on CRAN now and can be installed with:

```r
install.packages("dygraphs")
```

### Examples

Here are some examples of interactive time series visualizations you can create with only a line or two of R code (the screenshots are static, click them to see the interactive version).

#### Panning and Zooming

This code adds a range selector that's can be used to pan and zoom around the series data:

```r
dygraph(nhtemp, main = "New Haven Temperatures") %>%
  dyRangeSelector()
```

[![Screen Shot 2015-04-09 at 1.01.35 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-09-at-1-01-35-pm.png)](http://rstudio.github.io/dygraphs/gallery-range-selector.html)

#### Point Highlighting

When you hover over the time-series the values of all points at the location of the mouse are shown in the legend:

```r
lungDeaths <- cbind(ldeaths, mdeaths, fdeaths)
dygraph(lungDeaths, main = "Deaths from Lung Disease (UK)") %>%
  dyOptions(colors = RColorBrewer::brewer.pal(3, "Set2"))
```

[![Screen Shot 2015-04-09 at 12.53.54 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-09-at-12-53-54-pm.png)](http://rstudio.github.io/dygraphs/gallery-series-options.html)

#### Shading and Annotations

There are a wide variety of tools available to annotate time series. Here we demonstrate creating shaded regions:

```r
dygraph(nhtemp, main="New Haven Temperatures") %>%
  dySeries(label="Temp (F)", color="black") %>%
  dyShading(from="1920-1-1", to="1930-1-1", color="#FFE6E6") %>%
  dyShading(from="1940-1-1", to="1950-1-1", color="#CCEBD6")
```

[![Screen Shot 2015-04-09 at 1.11.31 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-09-at-1-11-31-pm1.png)](http://rstudio.github.io/dygraphs/gallery-shaded-regions.html)

You can find additional examples and documentation on the [dygraphs for R](http://rstudio.github.io/dygraphs/) website.

### Bringing JavaScript to R

One of the reasons we are excited about dygraphs is that it takes a mature and feature rich visualization library formerly only accessible to web developers and makes it available to all R users.

This is part of a larger trend enabled by the [htmlwidgets](http://www.htmlwidgets.org) package, and we expect that more and more libraries like dygraphs will emerge over the coming months to bring the best of JavaScript data visualization to R.

