---
title: 'Leaflet: Interactive web maps with R'
description: "Create interactive web maps in R with leaflet: markers, polygons, popups, GeoJSON support, and seamless Shiny integration."
auto-description: true
people:
  - Yihui Xie
date: '2015-06-24'
categories:
  - Visualization
  - Interactive Apps
tags:
  - Htmlwidgets
  - Spatial
  - Packages
  - RStudio
slug: leaflet-interactive-web-maps-with-r
blogcategories:
  - Products and Technology
ported_from: rstudio
port_status: in-progress
software: ["leaflet"]
languages: ["R"]
ported_categories:
  - Packages
---


We are excited to announce that a new package **leaflet** has been released on CRAN. The R package **leaflet** is an interface to the JavaScript library [Leaflet](http://leafletjs.com/) to create interactive web maps. It was developed on top of the **[htmlwidgets](http://htmlwidgets.org)** framework, which means the maps can be rendered in R Markdown (v2) documents, Shiny apps, and RStudio IDE / the R console. Please see <http://rstudio.github.io/leaflet> for the full documentation. To install the package, run

```r
install.packages('leaflet')
```

We quietly introduced this package in December when we [announced htmlwidgets](https://blog.rstudio.com/2014/12/18/htmlwidgets-javascript-data-visualization-for-r/), but in the months since then we've added a lot of new features and launched a new set of [documentation](http://rstudio.github.io/leaflet). If you haven't looked at leaflet lately, now is a great time to get reacquainted!

## The Map Widget

The basic usage of this package is that you create a map widget using the `leaflet()` function, and add layers to the map using the layer functions such as `addTiles()`, `addMarkers()`, and so on. Adding layers can be done through the pipe operator `%>%` from **magrittr** (you are not required to use `%>%`, though):

```r
library(leaflet)

m <- leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852,
    popup="The birthplace of R")
m  # Print the map
```

![leaflet-basic](https://rstudioblog.files.wordpress.com/2015/06/leaflet-basic.png)

There are a variety of layers that you can add to a map widget, including:

  * Map tiles

  * Markers / Circle Markers

  * Polygons / Rectangles

  * Lines

  * Popups

  * GeoJSON / TopoJSON

  * Raster Images

  * Color Legends

  * Layer Groups and Layer Control

There are a sets of methods to manipulate the attributes of a map, such as `setView()` and `fitBounds()`, etc. You can find the details from the help page `?setView`.

<!-- more -->

The `leaflet()` function and all layer functions have a `data` argument that can take several types of spatial data objects, including matrices and data frames with latitude and longitude columns, spatial objects from the **sp** package (e.g. `SpatialPoints` and `SpatialPointsDataFrame`, etc), and the data frame returned from `maps::map()`. When you have got a data object in `leaflet()` or layer functions, you may use the formula interface to pass values of variables to function arguments.

```r
m <- leaflet(df) %>% addTiles()
m %>% addCircleMarkers(radius = ~size, color = ~color)
# this is more compact than radius = df$size, color = df$color
```

## Basemaps

You can add basemaps to a map widget using map tiles. The default tiles provided by `addTiles()` are OpenStreetMap tiles, and you can easily add third-party tiles via `addProviderTiles()`. WMS (Web Map Service) tiles can be added via `addWMSTiles()`. You may use more than one tile layer on a map, too.

## Markers and Popups

Icon markers and circle markers can be placed at the locations specified by latitudes/longitudes on a map via `addMarkers()` and `addCircleMarkers()`, respectively. You can change the default appearance of icon markers (dropped pins) and use custom icon images, and you can also customize the appearance of circle markers (radius, color, and so on). When there are a large number of markers on a map, you may cluster them into groups (each group containing multiple markers close to each other), and see individual markers as you zoom into the map. When you add a marker to a map, you can also bind a popup to it through the `popup` argument, so users can see more information after they click on the marker. It is possible to add popups separately without markers as well via `addPopups()`.

## Lines and Shapes

Polygons, polylines, circles, and rectangles can be added to the map through `addPolygons()`, `addPolylines()`, `addCircles()`, and `addRectangles()`. For example, you can create a choropleth map by adding polygons with different colors.

## GeoJSON / TopoJSON

When your data is in the GeoJSON or TopoJSON format, you can add it to the map using `addGeoJSON()` and `addTopoJSON()`, respectively. The features in the JSON data can be styled via either the styles specified inside the data, or the arguments of the functions `addGeoJSON()`/`addTopoJSON()`.

## Raster Images

Two-dimensional `RasterLayer` objects (from the [**raster** package](http://cran.r-project.org/package=raster)) can be turned into images and added to Leaflet maps using the `addRasterImage()` function. You can color the image through the colors argument that accepts a variety of color specifications.

## Shiny Integration

Like most Shiny output widgets, you just create a leaflet output element in the UI using `leafletOutput()`, and render the widget on the server side using `renderLeaflet()`, with a leaflet widget object passed to `renderLeaflet()`.

After a widget is rendered in Shiny, you may modify it using the `leafletProxy()` object. All you need to do is replace `leaflet()` with `leafletProxy()`. For example, suppose the output ID of the map is `mymap`, and you have two numeric inputs `x` and `y` (specifying lng and lat) in the app, then you can add new markers to the map via:

```r
observe({
  leafletProxy("mymap") %>% addMarkers(input$x, input$y)
})
```

If you added layers with layer ID's to a map, you will be able to remove certain layers according to the layer ID's (e.g. `removeMarker()`). You can also clear entire layers (e.g. `clearMarkers()`).

When interacting with a map or its layers, you can obtain some information about the interaction from the Shiny input object. For example, `input$mymap_shape_click` will be a list of the form `list(lat = lat, lng = lng, id = layerId)` after you click on a shape object (e.g. a marker or a circle) on the map.

## Color Palettes and Legends

We have provided four types of color palettes in this package: `colorNumeric()`, `colorBin()`, `colorQuantile()`, and `colorFactor()`. These palette functions return functions that can be applied to numeric or factor values to generate colors. If you have used one of these color palettes, you may also use `addLegend()` to add a color legend to the map.

## Layer Groups and Layer Control

Normally a layer function has an argument called group, which can be used to assign multiple layer elements into a group. Later you may use `addLayersControl()` to add a layer control to the map to show/hide groups.

We hope you will enjoy using this package. Please let us know if you have any comments or questions when the R package documentation or the website <http://rstudio.github.io/leaflet> is not clear enough. You are welcome to [file bug reports / feature requests](https://github.com/rstudio/leaflet/issues) to the Github repository or ask questions in the [shiny-discuss](https://groups.google.com/forum/#!forum/shiny-discuss) mailing list.

