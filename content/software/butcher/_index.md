---
description: Reduce the size of model objects saved to disk
github: tidymodels/butcher
image: logo.png
languages:
- R
latest_release: '2025-12-09T11:27:57+00:00'
people:
- Davis Vaughan
- Julia Silge
- Simon Couch
- Max Kuhn
- Hannah Frick
- Emil Hvitfeldt
- Jeroen Janssens
title: butcher
website: https://butcher.tidymodels.org/

external:
  contributors:
  - DavisVaughan
  - jyuu
  - juliasilge
  - simonpcouch
  - topepo
  - hfrick
  - ashbythorpe
  - EmilHvitfeldt
  - era127
  - olivroy
  - cregouby
  - pbulsink
  - jeroenjanssens
  - galen-ft
  - dpprdan
  - AshesITR
  - abichat
  description: Reduce the size of model objects saved to disk
  first_commit: '2019-06-06T19:45:18+00:00'
  forks: 16
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.326825+00:00'
  latest_release: '2025-12-09T11:27:57+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Julia Silge
  - Simon Couch
  - Max Kuhn
  - Hannah Frick
  - Emil Hvitfeldt
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/butcher
  stars: 137
  title: butcher
  website: https://butcher.tidymodels.org/
---

Fitted model objects in R often consume far more memory than necessary. The culprit? Unnecessary components like training environments, control parameters, and original data that persist after model fitting but aren't needed for predictions. This bloat becomes a significant problem when saving models to disk, deploying them to production systems, or managing multiple models in memory. Butcher solves this problem by selectively removing these unnecessary components while preserving full prediction capabilities, often reducing model size by orders of magnitude.

The package provides a suite of specialized functions to strip away different components of model objects: axe_call() removes the call object, axe_env() clears captured environments, axe_data() removes training data, and more. The primary butcher() function executes all these operations at once, making it easy to dramatically reduce model size with a single command. Whether you're deploying models to production, building model repositories, or simply trying to save disk space, butcher helps you keep only what you need without sacrificing functionality.
