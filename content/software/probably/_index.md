---
description: Tools for post-processing class probability estimates
github: tidymodels/probably
image: logo.png
languages:
- R
latest_release: '2025-10-16T12:05:16+00:00'
people:
- Davis Vaughan
- Max Kuhn
- Emil Hvitfeldt
- Edgar Ruiz
- Julia Silge
- Hannah Frick
- Simon Couch
- Gábor Csárdi
- Jeroen Janssens
title: probably
website: https://probably.tidymodels.org/

external:
  contributors:
  - DavisVaughan
  - topepo
  - EmilHvitfeldt
  - edgararuiz
  - juliasilge
  - hfrick
  - jrwinget
  - simonpcouch
  - gaborcsardi
  - jeroenjanssens
  description: Tools for post-processing class probability estimates
  first_commit: '2018-09-11T19:02:58+00:00'
  forks: 17
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.262573+00:00'
  latest_release: '2025-10-16T12:05:16+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Max Kuhn
  - Emil Hvitfeldt
  - Edgar Ruiz
  - Julia Silge
  - Hannah Frick
  - Simon Couch
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/probably
  stars: 120
  title: probably
  website: https://probably.tidymodels.org/
---

The probably package provides essential tools for post-processing class probability estimates from classification models within the tidymodels ecosystem. Rather than blindly converting model probabilities into discrete predictions, probably helps you investigate optimal probability thresholds, calibrate model outputs to ensure predicted probabilities align with observed outcomes, and make more informed decisions about when to act on predictions versus when to acknowledge uncertainty. This systematic approach to threshold optimization enables data scientists to tune models for domain-specific performance metrics beyond standard accuracy, such as optimizing for precision, recall, or business-specific cost functions.

A standout feature of probably is its support for equivocal zones, which introduce an explicit "uncertain" category for predictions where probability estimates fall below a confidence threshold. By introducing the specialized class_pred class, the package allows practitioners to withhold predictions in ambiguous cases rather than forcing arbitrary classifications on borderline examples. This capability is particularly valuable in high-stakes applications like medical diagnosis or fraud detection, where acknowledging uncertainty and deferring to human judgment can be more responsible than making low-confidence automated decisions.
