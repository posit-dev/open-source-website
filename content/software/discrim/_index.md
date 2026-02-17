---
description: Wrappers for discriminant analysis and naive Bayes models for use with
  the parsnip package
github: tidymodels/discrim
image: logo.png
languages:
- R
latest_release: '2025-12-01T23:23:30+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Julia Silge
- Hannah Frick
- Gábor Csárdi
- Jeroen Janssens
- Simon Couch
title: discrim
website: https://discrim.tidymodels.org

external:
  description: Wrappers for discriminant analysis and naive Bayes models for use with
    the parsnip package
  first_commit: '2019-10-08T02:11:36+00:00'
  forks: 4
  languages:
  - R
  last_updated: '2026-02-17T11:30:13.790251+00:00'
  latest_release: '2025-12-01T23:23:30+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Julia Silge
  - Hannah Frick
  - Gábor Csárdi
  - Jeroen Janssens
  - Simon Couch
  readme_image: man/figures/logo.png
  repo: tidymodels/discrim
  stars: 31
  title: discrim
  website: https://discrim.tidymodels.org
---

The discrim package provides bindings that enable the parsnip package (part of tidymodels) to fit discriminant analysis and naive Bayes classification models. It supports linear discriminant analysis (LDA), quadratic discriminant analysis (QDA), regularized discriminant analysis (RDA), flexible discriminant analysis (FDA), and naive Bayes models.

The package integrates multiple computational engines (MASS, mda, klaR, sparsediscrim, earth, naivebayes) into a consistent parsnip interface, allowing you to fit different variants of discriminant analysis models using tidymodels workflows. It includes support for regularized versions of LDA and QDA for high-dimensional data, and flexible discriminant analysis that uses MARS features to find nonlinear decision boundaries. All models work seamlessly with tidymodels tools for cross-validation, hyperparameter tuning, and model evaluation.
