---
title: Spatial manipulation with sf
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-10-01'
description: Work with geospatial vector data (points, lines, and polygons) using the sf package.
download_url: sf.pdf
people:
- Ryan Garnett
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

The sf package provides tools for working with simple features — geospatial vectors including
points, lines, and polygons. This cheat sheet covers spatial predicates, geometric operations,
measurements, geometry creation, and miscellaneous utilities for reading and transforming spatial data.

## What's covered
- Geometric confirmation – spatial predicates (`st_contains`, `st_intersects`, `st_within`, `st_overlaps`, etc.)
- Geometric operations – `st_buffer`, `st_centroid`, `st_convex_hull`, `st_union`, `st_simplify`, `st_difference`
- Geometry creation – `st_point`, `st_polygon`, `st_linestring`, `st_multipolygon`, `st_triangulate`, `st_voronoi`
- Geometric measurement – `st_area`, `st_distance`, `st_length`
- Misc operations – `st_as_sf`, `st_cast`, `st_join`, `st_transform`, `st_read`, `st_nearest_feature`
