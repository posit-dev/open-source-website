---
title: Google Earth Engine with rgee
image: page-1.png
resource_type: cheatsheet
by: community
date: '2024-05-01'
description: Analyze and visualize Earth Engine spatial datasets from R using rgee's interface to the Google Earth Engine API.
download_url: rgee.pdf
people:
- Antony Barja
- Cesar Aybar
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

The rgee package provides an R interface to Google Earth Engine (GEE), allowing spatial data analysis on GEE's cloud platform using familiar R syntax and the pipe operator. It supports the full Earth Engine class hierarchy—images, image collections, features, feature collections, and geometries—along with data import/export, visualization, and GEE asset management.

## What's covered
- Mission and installation – setup for Windows, macOS, Linux, and Docker with `ee_install()`
- Basic classes – `ee$Number`, `ee$String`, `ee$Date`, `ee$Array`, `ee$Dictionary`, `ee$List`
- Geometric types – `ee$Geometry$Point`, `Polygon`, `MultiLineString`, `MultiGeometry`, and sf equivalents
- Geometric operations – `$buffer()`, `$intersection()`, `$union()`, `$difference()`, `$symmetricdifference()`
- Data catalog – `ee_utils_dataset_display()` for searching Earth Engine datasets
- Visualization – `Map$addLayer()`, `Map$addLegend()`, `ee_print()` for metadata display
- Image and ImageCollection I/O – `ee_as_raster()`, `ee_as_stars()`, `ee_image_to_drive()`, `raster_as_ee()`
- GEE Asset Manager – `ee_manage_create()`, `ee_manage_delete()`, `ee_manage_copy()`, and related functions
- Custom animations – `ee_utils_gif_creator()`, `ee_utils_gif_annotate()`, `ee_utils_gif_save()`
