---
description: parsnip extension for rule-based models
github: tidymodels/rules
image: logo.png
languages:
- R
latest_release: '2023-03-08T23:13:46+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Simon Couch
- Julia Silge
- Hannah Frick
- Gábor Csárdi
- Jeroen Janssens
title: rules
website: https://rules.tidymodels.org

external:
  contributors:
  - topepo
  - EmilHvitfeldt
  - simonpcouch
  - juliasilge
  - hfrick
  - aluxh
  - FvD
  - gaborcsardi
  - jaredlander
  - jeroenjanssens
  description: parsnip extension for rule-based models
  first_commit: '2019-10-27T20:58:03+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.422278+00:00'
  latest_release: '2023-03-08T23:13:46+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Simon Couch
  - Julia Silge
  - Hannah Frick
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/rules
  stars: 42
  title: rules
  website: https://rules.tidymodels.org
---

The rules package brings rule-based modeling to the tidymodels ecosystem by extending parsnip with specialized model definitions for interpretable, transparent prediction approaches. Rule-based models offer a unique combination of predictive power and explainability, making them particularly valuable when model interpretability is as important as accuracy. By generating human-readable if-then rules, these models help data scientists understand and communicate the logic behind predictions in a way that traditional black-box algorithms cannot.

Rules supports three distinct modeling paradigms through a unified interface: Cubist models for rule sets with embedded linear models and ensemble methods, C5.0 for classification rule sets derived from decision trees, and RuleFit for extracting rules from tree ensembles and incorporating them into regularized regression. This integration allows you to leverage the full power of tidymodels workflows, including preprocessing pipelines, hyperparameter tuning, and model comparison, while working with interpretable rule-based algorithms that provide clear insights into your data's underlying patterns.
