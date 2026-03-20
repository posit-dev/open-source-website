---
color: '#085032'
description: A tidy unified interface to models
github: tidymodels/parsnip
image: logo.png
languages:
- R
latest_release: '2026-01-11T20:23:17+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Hannah Frick
- Julia Silge
- Simon Couch
- Davis Vaughan
- Mine Çetinkaya-Rundel
- Tomasz Kalinowski
- Edgar Ruiz
- Gábor Csárdi
title: parsnip
website: https://parsnip.tidymodels.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: A tidy unified interface to models
  first_commit: '2017-12-10T22:48:42+00:00'
  forks: 107
  languages:
  - R
  last_updated: '2026-03-20T10:27:44.572617+00:00'
  latest_release: '2026-01-11T20:23:17+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Hannah Frick
  - Julia Silge
  - Simon Couch
  - Davis Vaughan
  - Mine Çetinkaya-Rundel
  - Tomasz Kalinowski
  - Edgar Ruiz
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/parsnip
  stars: 648
  title: parsnip
  website: https://parsnip.tidymodels.org
---

parsnip provides a unified interface for defining and fitting machine learning models in R. It allows you to specify models using a consistent syntax regardless of which underlying package (engine) you use to actually fit the model.

Different R packages that implement the same algorithm often have inconsistent argument names and interfaces. parsnip solves this by standardizing model specifications and separating the model definition from the computational engine, so you can switch between implementations (like ranger, randomForest, or Spark) without rewriting your code. It harmonizes argument names across packages and model types, making it easier to experiment with different algorithms and engines.
