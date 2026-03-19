---
title: svglite 1.0.0
people:
  - Hadley Wickham
date: '2015-12-10'
categories:
- Packages
slug: svglite-1-0-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["svglite"]
languages: ["R"]
---


I'm pleased to announced a new package for producing [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)s from R: [svglite](http://github.com/hadley/svglite). This package is a fork of [Matthieu Decorde](https://github.com/mdecorde) RSvgDevice and wouldn't be possible without his hard work. I'd also like to thank [David Gohel](https://github.com/davidgohel) who wrote the gdtools package: it solves all the hardest problems associated with making good SVGs from R.

Today, most browsers have good support for SVG and it is a great way of displaying vector graphics on the web. Unfortunately, R's built-in `svg()` device is focussed on high quality rendering, not size or speed. It renders text as individual polygons: this ensures a graphic will look exactly the same regardless of what fonts you have installed, but makes output considerably larger (and harder to edit in other tools). svglite produces hand-optimised SVG that is as small as possible.

## Features

svglite is a complete graphics device: that means you can give it any graphic and it will look the same as the equivalent `.pdf` or `.png`. Please [file an issue](https://github.com/hadley/svglite/issues) if you discover a plot that doesn't look right.

## Use

In an interactive session, you use it like any other R graphics device:

```r
svglite::svglite("myfile.svg")
plot(runif(10), runif(10))
dev.off()
```

If you want to use it in knitr, just set your chunk options as follows:

    ```r setup, include = FALSE
    library(svglite)
    knitr::opts_chunk$set(
      dev = "svglite",
      fig.ext = ".svg"
    )

(Thanks to Bob Rudis for [the tip](https://twitter.com/hrbrmstr/status/662708164597563392))

There are also a few helper functions:

  * `htmlSVG()` makes it easy to preview the SVG in RStudio.

  * `editSVG()` opens the SVG file in your default SVG editor.

  * `xmlSVG()` returns the SVG as an [xml2](http://github.com/hadley/xml2) object.

