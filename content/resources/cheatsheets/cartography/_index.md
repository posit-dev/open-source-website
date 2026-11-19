---
title: Thematic maps with cartography
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-08-01'
description: Create thematic maps from sf and sp spatial objects with choropleth, symbol, typology, and basemap layers.
download_url: cartography.pdf
people:
- Timothée Giraud
thumbnails:
- page-1.png
languages:
- R
---

cartography works alongside the sf and sp packages to produce thematic maps in R. It offers layer functions for representing quantitative and qualitative spatial data, spatial transformation utilities, and tools for composing full map layouts with north arrows, scale bars, and legends.

## What's covered
- Choropleth layer – `choroLayer()` with classification methods
- Typology layer – `typoLayer()`
- Proportional symbols layer – `propSymbolsLayer()`
- Colorized proportional symbols (relative) – `propSymbolsChoroLayer()`
- Colorized proportional symbols (qualitative) – `propSymbolsTypoLayer()`
- Double proportional symbols – `propTrianglesLayer()`
- OpenStreetMap basemap – `getTiles()`, `tilesLayer()`
- Polygons to grid transformation – `getGridLayer()`
- Points to links transformation – `getLinkLayer()`
- Polygons to borders – `getBorders()`
- Polygons to pencil lines – `getPencilLayer()`
- Map layout – `layoutLayer()`, `north()`, `barscale()`
- Figure dimensions – `getFigDim()`
