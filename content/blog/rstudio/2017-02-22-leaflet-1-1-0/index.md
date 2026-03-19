---
title: leaflet 1.1.0
people:
  - Joe Cheng
date: '2017-02-22'
categories:
- Packages
slug: leaflet-1-1-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["leaflet"]
languages: ["R"]
---


Leaflet 1.1.0 is now available on CRAN! The [Leaflet package](https://rstudio.github.io/leaflet/) is a tidy wrapper for the [Leaflet.js](http://leafletjs.com/) mapping library, and makes it incredibly easy to generate interactive maps based on spatial data you have in R.

[![leaflet-choro](https://rstudioblog.files.wordpress.com/2017/02/leaflet-choro.png)](http://rstudio.github.io/leaflet/choropleths.html)

This release was nearly a year in the making, and includes many important new features.

  * Easily add textual [labels](http://rstudio.github.io/leaflet/popups.html#labels) on markers, polygons, etc., either on hover or statically

  * [Highlight](http://rstudio.github.io/leaflet/shapes.html#highlighting-shapes) polygons, lines, circles, and rectangles on hover

  * Markers can now be [configured](http://rstudio.github.io/leaflet/markers.html#awesome-icons) with a variety of colors and icons, via integration with [Leaflet.awesome-markers](https://github.com/lvoogdt/Leaflet.awesome-markers)

  * Built-in support for many types of objects from `[sf](https://cran.r-project.org/web/packages/sf/index.html)`, a new way of representing spatial data in R (all basic `sf`/`sfc`/`sfg` types except `MULTIPOINT` and `GEOMETRYCOLLECTION` are directly supported)

  * Projections other than Web Mercator are [now supported](http://rstudio.github.io/leaflet/projections.html) via [Proj4Leaflet](https://github.com/kartena/Proj4Leaflet)

  * Color palette functions now natively support [viridis](https://bids.github.io/colormap/) palettes; use `"viridis"`, `"magma"`, `"inferno"`, or `"plasma"` as the palette argument

  * Discrete color palette functions (`colorBin`, `colorQuantile`, and `colorFactor`) work much better with [color brewer](http://colorbrewer2.org/) palettes

  * Integration with [several Leaflet.js utility plugins](http://rstudio.github.io/leaflet/morefeatures.html)

  * Data with `NA` points or zero rows no longer causes errors

  * Support for linked brushing and filtering, via [Crosstalk](https://rstudio.github.io/crosstalk/) (more about this to come in another blog post)

Many thanks to [@bhaskarvk](https://github.com/bhaskarvk) who contributed much of the code for this release.

Going forward, our intention is to prevent any more Leaflet.js plugins from accreting in the core leaflet package. Instead, we have made it possible to write 3rd party R packages that extend leaflet (though the process to do this is not documented yet). In the meantime, Bhaskar has started developing his own [leaflet.extras](https://github.com/bhaskarvk/leaflet.extras) package; it already supports several plugins, for everything from animated markers to heatmaps.

