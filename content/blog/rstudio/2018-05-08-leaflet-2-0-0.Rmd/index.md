---
title: leaflet 2.0.0
people:
  - Barret Schloerke
date: '2018-05-10'
slug: leaflet-2-0-0
categories:
- Packages
tags:
- leaflet
- data visualization
- Packages
- Packages
editor_options:
  chunk_output_type: console
blogcategories:
- Products and Technology
ported_from: rstudio
port_status: in-progress
---

[leaflet](http://rstudio.github.io/leaflet/) 2.0.0 is now on CRAN!

The leaflet R package wraps the [Leaflet.js](https://leafletjs.com/) JavaScript library, and this release of the R package marks a major upgrade from the outdated Leaflet.js 0.7.x to the current Leaflet.js 1.x (specifically, 1.3.1).

Leaflet.js 1.x includes some non-backward-compatible API changes versus 0.7.x. If you’re using only R code to create your Leaflet maps, these changes should not affect you. If you are using custom JavaScript, some changes may be required to your code. Please see the Leaflet.js [reference documentation](http://leafletjs.com/reference-1.3.0.html) and [changelog](https://github.com/Leaflet/Leaflet/blob/master/CHANGELOG.md).

Big thanks to [\@timelyportfolio](https://twitter.com/timelyportfolio) and [Bhaskar Karambelkar](https://www.karambelkar.info/about/) for their significant contributions to this release!

## leaflet.extras and leaflet.esri

Two additional packages by Bhaskar, leaflet.extras and leaflet.esri, have been updated on CRAN to utilize the latest Leaflet.js library bindings. leaflet.extras extends the Leaflet R package using various Leaflet.js plugins, offering features like heatmaps, additional marker icons, and drawing tools. leaflet.esri provides access to ArcGIS services, based on the [ESRI leaflet plugin](https://esri.github.io/esri-leaflet/).

```r, eval = FALSE
library(leaflet)
library(leaflet.extras)

leaflet(quakes) %>%
  addTiles() %>%
  addHeatmap(lng = ~long, lat = ~lat, radius = 8)
```

<!-- content of http://rpubs.com/barret/leaflet-2-0-0-quakes of the above code -->
<iframe src="https://rstudio-pubs-static.s3.amazonaws.com/388042_d0a5b2ee3b2d44858e9cfc55edb109bf.html" width="100%" height="400px" frameborder=0 style="border=0;"></iframe>

## Full changelog

### Breaking Changes

* Update to latest Leaflet.js 1.x (v1.3.1). Please see the Leaflet.js [reference documentation](http://leafletjs.com/reference-1.3.0.html) and [change log](https://github.com/Leaflet/Leaflet/blob/master/CHANGELOG.md).
* Previously, labels were implemented using the 3rd party extension [Leaflet.label](https://github.com/Leaflet/Leaflet.labelExtension). Leaflet.js 1.x now provides this functionality naively. There are some minor differences to note:
  - If you are using custom JavaScript to create labels, you’ll need to change references to `L.Label` to `L.Tooltip`.
  - Tooltips are now displayed with default Leaflet.js styling.
  - In custom javascript extensions, change all  `*.bindLabel()` to `*.bindTooltip()`.
* All Leaflet.js plugins updated to versions compatible with Leaflet.js 1.x.

### Known Issues

* The default CSS z-index of the Leaflet map has changed; for some Shiny applications, the map now covers elements that are intended to be displayed on top of the map. This issue has been fixed on GitHub (`devtools::install_github("rstudio/leaflet")`). For now, you can work around this in the CRAN version by including this line in your application UI:

```r
tags$style(".leaflet-map-pane { z-index: auto; }")
```
### Features

* Added more providers for `addProviderTiles()`: OpenStreetMap.CH, OpenInfraMap, OpenInfraMap.Power, OpenInfraMap.Telecom, OpenInfraMap.Petroleum, OpenInfraMap.Water, OpenPtMap, OpenRailwayMap, OpenFireMap, SafeCast.
* Add `groupOptions` function. Currently the only option is letting you specify zoom levels at which a group should be visible.
* Added support for drag events.
* Added `method` argument to `addRasterImage()` to enable nearest neighbor interpolation when projecting categorical rasters.
* Added an `'auto'` method for `addRasterImage()`. Projected factor results are coerced into factors.
* Added `data` parameter to remaining `addXXX()` methods, including addLegend.
* Added `preferCanvas` argument to `leafletOptions()`.
### Bug Fixes and Improvements
* Relative protocols are used where possible when adding tiles. In RStudio 1.1.x on linux and windows, a known issue of 'https://' routes fail to load, but works within browsers (rstudio/rstudio#2661).
* `L.multiPolyline` was absorbed into `L.polyline`, which also accepts an [array of polyline information](http://leafletjs.com/reference-1.3.0.html#polyline).
* Fixed bug where icons were anchored to the top-center by default, not center-center.
* Fixed bug where markers would not appear in self contained knitr files.
* `L.Label` is now `L.tooltip` in Leaflet.js. `labelOptions()` now translates old options `clickable` to `interactive` and `noHide` to `permanent`.
* Fix a bug where the default `addTiles()` would not work with .html files served directly from the filesystem.
* Fix bug with accessing columns in formulas when the data source is a Crosstalk SharedData object wrapping a spatial data frame or sf object.
* Fix strange wrapping behavior for legend, especially common for Chrome when browser zoom level is not 100%.
* Fix incorrect opacity on NA entry in legend.
* Ensure type safety of `.indexOf(stamp)`.
* `validateCoords()` warns on invalid polygon data.

