---
description: Version, share, deploy, and monitor models
github: rstudio/vetiver-r
image: logo.png
languages:
- R
latest_release: '2025-12-13T20:36:56+00:00'
people:
- Julia Silge
- Barret Schloerke
- Daniel Falbel
- Emil Hvitfeldt
- Tomasz Kalinowski
title: vetiver-r
website: https://rstudio.github.io/vetiver-r/

external:
  contributors:
  - juliasilge
  - schloerke
  - aminadibi
  - be-marc
  - mfansler
  - csgillespie
  - dfalbel
  - EmilHvitfeldt
  - galen-ft
  - JosiahParry
  - DyfanJones
  - t-kalinowski
  - olivroy
  description: Version, share, deploy, and monitor models
  first_commit: '2021-07-09T03:41:56+00:00'
  forks: 30
  languages:
  - R
  last_updated: '2026-02-13T14:17:05.231557+00:00'
  latest_release: '2025-12-13T20:36:56+00:00'
  license: NOASSERTION
  people:
  - Julia Silge
  - Barret Schloerke
  - Daniel Falbel
  - Emil Hvitfeldt
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: rstudio/vetiver-r
  stars: 197
  title: vetiver-r
  website: https://rstudio.github.io/vetiver-r/
---

Vetiver provides fluent tooling to version, share, deploy, and monitor trained machine learning models in R. Named after the "oil of tranquility" used as a stabilizing ingredient in perfumery, vetiver brings stability and structure to the model deployment lifecycle. The package handles recording and validating model input data prototypes, creating production-ready REST APIs with Plumber, and making predictions from remote endpoints—transforming models from experimental artifacts into reliable, versioned services.

Vetiver works seamlessly with popular R modeling frameworks including tidymodels, caret, mlr3, XGBoost, ranger, keras, and base R functions like lm() and glm(). Its extensible design uses generics that support many model types, allowing data scientists to adopt a consistent MLOps workflow regardless of their modeling approach. By integrating with the pins package for model storage and versioning across local folders, Posit Connect, Amazon S3, and other backends, vetiver enables teams to collaborate on models and maintain reproducible deployment pipelines from development through production monitoring.
