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
  contributors:
  - topepo
  - EmilHvitfeldt
  - juliasilge
  - hfrick
  - gaborcsardi
  - jeroenjanssens
  - simonpcouch
  description: Wrappers for discriminant analysis and naive Bayes models for use with
    the parsnip package
  first_commit: '2019-10-08T02:11:36+00:00'
  forks: 4
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.389845+00:00'
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

discrim is a specialized R package that brings discriminant analysis and naive Bayes classification methods into the tidymodels ecosystem. It provides a unified interface for fitting various classification models including linear discriminant analysis, quadratic discriminant analysis, regularized discriminant analysis, flexible discriminant analysis, and naive Bayes classifiers. By wrapping functionality from multiple underlying packages like MASS, mda, klaR, and naivebayes, discrim allows you to apply these classical statistical learning techniques using consistent tidymodels syntax and workflows.

What makes discrim valuable for data scientists is its ability to simplify complex classification tasks through a standardized approach. Instead of learning different function signatures and data structures for each discriminant analysis package, you can leverage the familiar parsnip interface to fit, tune, and evaluate models. The package supports both standard and regularized variants of discriminant analysis, making it particularly useful for high-dimensional classification problems where feature selection and regularization are important. Whether you're working with well-separated classes that benefit from linear boundaries or complex decision surfaces requiring flexible discriminant analysis, discrim provides the tools you need within a cohesive modeling framework.
