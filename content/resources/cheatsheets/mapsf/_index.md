---
title: Thematic maps with mapsf
image: page-1.png
resource_type: cheatsheet
by: community
date: '2021-11-01'
description: Create and export thematic maps from sf objects using choropleth, proportional symbol, and other map types.
download_url: mapsf.pdf
people:
- Ronan Ysebaert
thumbnails:
- page-1.png
languages:
- R
---

The mapsf package creates thematic maps from `sf` objects in R. It supports choropleth, typology, proportional symbol, graduated symbol, and combined map types, alongside flexible layout tools for titles, north arrows, scale bars, insets, and annotations. Maps can be exported to PNG or SVG with `mf_export()`.

## What's covered
- Base map – `mf_map()` and `mf_get_mtq()` for loading sample data and rendering base layers
- Symbology – choropleth, typology, proportional symbols, graduated symbols, combined types (`prop_choro`, `prop_typo`, `symb_choro`)
- Legends – automatic default legends and `mf_legend()` customization
- Colors – `mf_get_pal()` for asymmetric diverging palettes using `hcl.colors()`
- Map layout – `mf_theme()`, `mf_title()`, `mf_arrow()`, `mf_scale()`, `mf_label()`, `mf_annotation()`, `mf_credits()`, insets
- Export maps – `mf_export()` for PNG and SVG with theme, expanded bounding box, or area-centered output
