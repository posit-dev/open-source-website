---
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

external:
  contributors:
  - thomasp85
  - EmilHvitfeldt
  - pommedeterresautee
  - jeroen
  - nielsenmarkus11
  - ChrisMuir
  - christophM
  - jonmcalder
  - ledgerW
  - batpigandme
  - martinju
  - mdancho84
  - maelle
  - pkopper
  - samleegithub
  - millerjoey
  description: Local Interpretable Model-Agnostic Explanations (R port of original
    Python package)
  first_commit: '2017-03-17T10:40:29+00:00'
  forks: 109
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.049131+00:00'
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

LIME (Local Interpretable Model-agnostic Explanations) transforms black-box machine learning models into interpretable predictions by explaining why specific outcomes occurred. Rather than treating complex models as inscrutable systems, LIME identifies the small set of features in your data that drove each individual prediction, making it invaluable for model validation, debugging, and building stakeholder trust. The package works seamlessly across popular modeling frameworks like caret, parsnip, and mlr, ensuring you can explain predictions regardless of your modeling approach.

Built with an idiomatic R implementation, LIME handles diverse data types including tabular data with feature-level explanations, images with visual highlighting of decision-influencing regions, and text with word-level importance indicators. The package delivers explanations in structured tabular formats containing feature weights, prediction probabilities, and model performance metrics, making complex model behavior accessible to both technical and non-technical audiences. Whether you're ensuring compliance with interpretability requirements or identifying potentially problematic feature relationships, LIME provides the transparency needed for responsible machine learning in production environments.
