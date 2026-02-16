---
description: Tools for ggplot2 scales
github: r-lib/scales
image: logo.png
languages:
- R
latest_release: '2025-04-23T14:42:43+00:00'
people:
- Hadley Wickham
- Thomas Lin Pedersen
- Teun Van den Brand
- Winston Chang
- Joe Cheng
- Max Kuhn
- Charlotte Wickham
- Barret Schloerke
title: scales
website: https://scales.r-lib.org

external:
  contributors:
  - hadley
  - thomasp85
  - teunbrand
  - dpseidel
  - wch
  - karawoo
  - BrianDiggs
  - jcheng5
  - dougmitarotonda
  - clauswilke
  - larmarange
  - zeehio
  - batpigandme
  - jiho
  - jimhester
  - aaronwolen
  - jrnold
  - davidchall
  - yutannihilation
  - dvmlls
  - ThierryO
  - zamorarr
  - mikmart
  - mjskay
  - billdenney
  - lepennec
  - hmalmedal
  - Moohan
  - johanneskoch94
  - kellijohnson-NOAA
  - kohske
  - LluisRamon
  - topepo
  - sflippl
  - stragu
  - stephLH
  - foo-bar-baz-qux
  - wibeasley
  - yihui
  - seaaan
  - EricMarcon
  - nacnudus
  - d-morrison
  - dmi3kno
  - colindouglas
  - cwickham
  - pearsonca
  - bwiernik
  - bhogan-mitre
  - schloerke
  - agila5
  - AndreaCirilloAC
  - ndevln
  - Aehmlo
  description: Tools for ggplot2 scales
  first_commit: '2010-11-08T00:44:23+00:00'
  forks: 117
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.456089+00:00'
  latest_release: '2025-04-23T14:42:43+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Thomas Lin Pedersen
  - Teun Van den Brand
  - Winston Chang
  - Joe Cheng
  - Max Kuhn
  - Charlotte Wickham
  - Barret Schloerke
  readme_image: man/figures/logo.png
  repo: r-lib/scales
  stars: 444
  title: scales
  website: https://scales.r-lib.org
---

Scales provides the internal scaling infrastructure that powers ggplot2, making it easier to convert data values into visual properties like position, color, and size. One of the most challenging aspects of creating effective data visualizations is scaling—transforming raw data into perceptual properties—and its inverse, creating readable guides like legends and axes that help viewers interpret the graph. The scales package tackles both of these problems head-on, giving you precise control over how your data is displayed.

With scales, you can customize every aspect of how your plots communicate information. Use break functions to control where tick marks appear on axes, label functions to format dates, numbers, and currency in readable ways, and transformation functions to apply custom mathematical transformations like logarithmic or square root scales. The package also provides access to carefully designed color palettes from systems like Viridis and ColorBrewer that work in any plotting system, not just ggplot2. Whether you need to display thousands of data points with abbreviated labels, format dates in a specific style, or apply a custom transformation repeatedly across multiple visualizations, scales gives you the tools to make your graphics both beautiful and informative.
