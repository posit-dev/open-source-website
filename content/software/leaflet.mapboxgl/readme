# leaflet.mapboxgl

Provides an R interface to extend the [R Leaflet](https://rstudio.github.io/leaflet/) package with the [Mapbox GL Leaflet](https://github.com/mapbox/mapbox-gl-leaflet) plugin.

## Compatibility

WebGL support is required. Most modern web browsers are supported, but IE11 may not work.

RStudio 1.1 on Windows and Linux do not support WebGL and will not work. RStudio 1.1 for Mac should work.

RStudio 1.2 will work if the rendering engine is set to Desktop OpenGL, which is the default on many systems. If your maps fail to render, you can try changing the rendering engine from the default value of "Auto-detect" to "Desktop OpenGL" by going to Tools | Global Options | General | Advanced | Rendering Engine. (Tip: If this puts your IDE into an unusable state, holding Ctrl during startup will bring up a dialog that lets you revert the Rendering Engine setting to "Auto-detect".)

## Installation

This package is not yet available on CRAN.

```r
devtools::install_github("rstudio/leaflet.mapboxgl")
```

## Usage

First, you must provide your [Mapbox access token](https://docs.mapbox.com/help/how-mapbox-works/access-tokens/#creating-and-managing-access-tokens) as a global R option. (If you are using non-Mapbox datasource, you still need to provide a value, but it can just be `NA`.)

```r
options(mapbox.accessToken = "...")
```

Then, create your Leaflet map, and call the `addMapboxGL` function.

```r
library(leaflet)
library(leaflet.mapboxgl)

leaflet(quakes) %>%
  addMapboxGL(style = "mapbox://styles/mapbox/streets-v9") %>%
  addCircleMarkers(weight = 1, fillOpacity = 0, radius = 3)
```

<img src="https://raw.githubusercontent.com/rstudio/leaflet.mapboxgl/master/sshot.png" alt="Screenshot of map" width="615" height="421"/>

## License

MIT
