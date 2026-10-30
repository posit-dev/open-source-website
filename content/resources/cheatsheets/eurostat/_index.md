---
title: Access Eurostat data with eurostat
image: page-1.png
resource_type: cheatsheet
by: community
date: '2017-03-01'
description: Search, download, label, and visualize data from the Eurostat Open Data portal using R.
download_url: eurostat.pdf
people:
- Przemysław Biecek
- Markus Kainu
thumbnails:
- page-1.png
languages:
- R
---

The eurostat package provides a complete R interface to the Eurostat Open Data portal. Key functions allow users to find table codes, download tables as tibbles, add human-readable labels, and produce plots and choroplethmaps of the retrieved data.

## What's covered
- Find the table code – `search_eurostat()` to scan the Eurostat directory
- Download the table – `get_eurostat()` with time format, filters, and caching
- Add labels – `label_eurostat()` to replace codes with descriptions
- eurostat and plots – combining with ggplot2 and dplyr for time-series plots
- eurostat and maps – `get_eurostat_geospatial()` with sf and `ggplot2::geom_sf()`
