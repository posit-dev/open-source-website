---
title: ggvis 0.4
people:
  - Winston Chang
date: '2014-10-13'
slug: ggvis-0-4
ported_from: rstudio
port_status: in-progress
languages: ["R"]
categories:
  - Visualization
  - Interactive Apps
tags:
  - RStudio
---


ggvis 0.4 is now available on CRAN. You can install it with:

```r
install.packages("ggvis")
```

The major features of this release are:

  * Boxplots, with `layer_boxplots()`

```r
chickwts %>% ggvis(~feed, ~weight) %>% layer_boxplots()
```

![ggvis box plot](https://rstudioblog.files.wordpress.com/2014/10/ggvis-0-4-boxplot.png)

  * Better stability when errors occur.

  * Better handling of empty data and malformed data.

  * More consistent handling of data in compute pipeline functions.

Because of these changes, interactive graphics with dynamic data sources will work more reliably.

Additionally, there are many small improvements and bug fixes under the hood. You can see the full change log [here](https://github.com/rstudio/ggvis/releases/tag/v0.4).

