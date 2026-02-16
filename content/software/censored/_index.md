---
description: Parsnip wrappers for survival models
github: tidymodels/censored
image: logo.png
languages:
- R
latest_release: '2025-02-14T20:49:56+00:00'
people:
- Hannah Frick
- Emil Hvitfeldt
- Max Kuhn
- Davis Vaughan
- Simon Couch
- Gábor Csárdi
- Jeroen Janssens
- Julia Silge
title: censored
website: https://censored.tidymodels.org/

external:
  contributors:
  - hfrick
  - EmilHvitfeldt
  - topepo
  - DavisVaughan
  - simonpcouch
  - bcjaeger
  - gaborcsardi
  - jeroenjanssens
  - juliasilge
  - mattwarkentin
  description: Parsnip wrappers for survival models
  first_commit: '2020-07-31T04:58:54+00:00'
  forks: 15
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.626432+00:00'
  latest_release: '2025-02-14T20:49:56+00:00'
  license: NOASSERTION
  people:
  - Hannah Frick
  - Emil Hvitfeldt
  - Max Kuhn
  - Davis Vaughan
  - Simon Couch
  - Gábor Csárdi
  - Jeroen Janssens
  - Julia Silge
  readme_image: man/figures/logo.png
  repo: tidymodels/censored
  stars: 122
  title: censored
  website: https://censored.tidymodels.org/
---

censored is a parsnip extension package that brings the power of the tidymodels ecosystem to survival analysis and censored regression modeling. It provides a unified, consistent interface for working with time-to-event data, enabling data scientists to fit and evaluate survival models using the same intuitive workflow they rely on for other machine learning tasks. With support for multiple prediction types including survival probabilities, hazard rates, time-to-event estimates, and quantiles, censored makes it easy to extract the specific insights you need from your survival models without wrestling with inconsistent APIs across different modeling packages.

What makes censored particularly valuable is its comprehensive support for 11 different model configurations spanning tree-based methods, proportional hazards models, and parametric survival regression. Whether you need random forests via partykit or aorsf, boosted trees with mboost, proportional hazards models through survival or glmnet, or flexible parametric models using flexsurv, censored provides seamless access to specialized survival modeling techniques while maintaining the familiar tidymodels syntax. This unified approach streamlines the entire modeling process from data preprocessing through model comparison, letting you focus on finding the best solution for your survival analysis challenges rather than learning multiple package-specific interfaces.
