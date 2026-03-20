---
color: '#94CC28'
description: Local Interpretable Model-Agnostic Explanations (R port of original Python
  package)
github: tidymodels/lime
image: logo.png
languages:
- R
latest_release: '2025-12-10T00:23:55+00:00'
people:
- Thomas Lin Pedersen
- Emil Hvitfeldt
- Jeroen Ooms
title: lime
website: https://lime.data-imaginist.com/

external:  # updated automatically, do not edit
  description: Local Interpretable Model-Agnostic Explanations (R port of original
    Python package)
  first_commit: '2017-03-17T10:40:29+00:00'
  forks: 109
  languages:
  - R
  last_updated: '2026-03-20T10:27:44.468025+00:00'
  latest_release: '2025-12-10T00:23:55+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Emil Hvitfeldt
  - Jeroen Ooms
  readme_image: man/figures/logo.png
  repo: tidymodels/lime
  stars: 492
  title: lime
  website: https://lime.data-imaginist.com/
---

The lime package provides model-agnostic explanations for black box machine learning classifiers by identifying which features in the input data drove individual predictions. It works with any classifier and supports tabular data, images, and text.

The package implements the Local Interpretable Model-agnostic Explanations (LIME) methodology in an R-native API. It integrates with popular ML frameworks like caret, parsnip, and mlr out of the box, and can be extended to support custom models. For each prediction, lime fits local surrogate models to determine which features were most influential, with built-in visualization functions and an interactive Shiny interface for exploring text model explanations.
