---
description: 'isoband: An R package to generate contour lines and polygons.'
github: r-lib/isoband
image: logo.png
languages:
- C++
latest_release: '2025-12-05T12:51:46+00:00'
people:
- Thomas Lin Pedersen
- Hadley Wickham
- Jeroen Janssens
title: isoband
website: http://isoband.r-lib.org/

external:
  contributors:
  - clauswilke
  - thomasp85
  - hadley
  - jamarav
  - jimhester
  - eliocamp
  - jeroenjanssens
  - MichaelChirico
  description: 'isoband: An R package to generate contour lines and polygons.'
  first_commit: '2018-12-29T06:05:34+00:00'
  forks: 16
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.029225+00:00'
  latest_release: '2025-12-05T12:51:46+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Hadley Wickham
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/isoband
  stars: 132
  title: isoband
  website: http://isoband.r-lib.org/
---

The isoband package transforms gridded elevation data into publication-quality contour visualizations through its efficient generation of isolines and isobands. Whether you're mapping topographic features, visualizing temperature gradients, or exploring any continuous spatial data, isoband handles the computational complexity of contour generation while providing seamless integration with R's visualization ecosystem. The package's core functions, `isolines()` and `isobands()`, process regularly spaced grid data and return coordinate vectors that work directly with both base graphics and ggplot2 workflows.

Built with performance in mind, isoband excels at processing large datasets without degradation, making it ideal for production environments and exploratory analysis alike. Its flexible output format can be used directly with grid graphics or converted to spatial features using `iso_to_sfg()`, providing data scientists and developers with multiple pathways for creating professional contour maps. Originally developed by Claus Wilke and donated to r-lib in 2022, the package continues to serve as a foundational tool for spatial data visualization in R.
