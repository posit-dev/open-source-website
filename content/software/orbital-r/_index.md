---
color: '#24053C'
description: Turn Tidymodels Workflows Into Series of Equations
github: tidymodels/orbital
image: logo.png
languages:
- R
latest_release: '2026-03-12T22:05:04+00:00'
people:
- Emil Hvitfeldt
- Jeroen Janssens
title: orbital-r
website: https://orbital.tidymodels.org

override:
  title: orbital-r

external:  # updated automatically, do not edit
  description: Turn Tidymodels Workflows Into Series of Equations
  first_commit: '2024-06-13T19:03:09+00:00'
  forks: 3
  languages:
  - R
  last_updated: '2026-07-21T09:46:56.488727+00:00'
  latest_release: '2026-03-12T22:05:04+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/orbital
  stars: 49
  title: orbital
  website: https://orbital.tidymodels.org
---

Orbital converts fitted tidymodels workflows into a series of equations that can be evaluated outside of R, such as in a database via SQL or in other languages. This allows trained models to be deployed in environments where R is not available.

The package supports a range of tidymodels workflows, translating both preprocessing steps from recipes and model predictions into portable equations. This makes it possible to score data at scale directly in a database, or embed the calculations in other systems, while producing predictions identical to the original tidymodels workflow.
