---
title: Add silhouettes with rphylopic
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-09-01'
description: Add organism silhouette images from PhyloPic to ggplot2 or base R plots using the rphylopic package.
download_url: rphylopic.pdf
people:
- Gabriela Palomo-Munoz
thumbnails:
- page-1.png
languages:
- R
---

The rphylopic package allows R users to search PhyloPic's database of freely available organism silhouettes and embed them in ggplot2 or base R graphics as backgrounds, scatter plot points, or leaflet map icons. Silhouettes are identified by a UUID and retrieved with `image_data()`.

## What's covered
- Install rphylopic – CRAN and GitHub development versions
- Find silhouettes – `name_search()` by common name, `name_get()`, `name_images()`, `name_taxonomy()`, `ubio_get()`
- Plot silhouette behind a plot – `add_phylopic()` for ggplot2 and `add_phylopic_base()` for base R
- Plot silhouette anywhere in a plot – `x`, `y`, `ysize`, `alpha` positioning arguments
- Plot silhouettes as scatter points – iterating `add_phylopic()` over data rows
- Save PNG to disk – `save_png()` for offline use and custom icons
- Use silhouettes as leaflet icons – `makeIcon()` with a saved PNG path
