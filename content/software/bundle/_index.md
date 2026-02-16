---
description: Prepare objects for serialization with a consistent interface
github: rstudio/bundle
image: diagram_04.png
languages:
- R
latest_release: '2025-12-10T20:15:43+00:00'
people:
- Simon Couch
- Julia Silge
- Emil Hvitfeldt
- Daniel Falbel
title: bundle
website: https://rstudio.github.io/bundle/

external:
  contributors:
  - simonpcouch
  - juliasilge
  - qiushiyan
  - EmilHvitfeldt
  - dfalbel
  - MichaelChirico
  - olivroy
  description: Prepare objects for serialization with a consistent interface
  first_commit: '2022-06-23T19:15:20+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-02-13T14:17:05.661220+00:00'
  latest_release: '2025-12-10T20:15:43+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Julia Silge
  - Emil Hvitfeldt
  - Daniel Falbel
  readme_image: man/figures/diagram_04.png
  repo: rstudio/bundle
  stars: 31
  title: bundle
  website: https://rstudio.github.io/bundle/
---

Deploying machine learning models to production environments can be surprisingly challenging when models maintain references to external information like server connections or internal package functions. While standard R serialization methods such as `save()` or `saveRDS()` work well for simple objects, they often fail to capture these critical references, leading to broken predictions when models are reloaded in different computational environments. The bundle package solves this problem by providing a unified interface to prepare model objects for safe transfer between R sessions, ensuring that all necessary context travels with the model.

Bundle offers a straightforward two-function workflow: `bundle()` prepares your trained model by encapsulating external references into a portable object, while `unbundle()` restores the model with full functionality in a new R session. This consistent interface works across different model types and frameworks, making it invaluable for data scientists and ML engineers who need to train models in development environments and deploy them to production servers. Whether you're working with tidymodels, XGBoost, or other modeling frameworks, bundle ensures your models remain fully functional across different computational contexts, eliminating a common source of deployment failures.
