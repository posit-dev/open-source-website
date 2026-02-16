---
description: Parsnip wrappers for mixed-level and hierarchical models
github: tidymodels/multilevelmod
image: logo.png
languages:
- R
latest_release: '2022-06-17T12:13:05+00:00'
people:
- Hannah Frick
- Max Kuhn
- Emil Hvitfeldt
- Julia Silge
- Jeroen Janssens
title: multilevelmod
website: https://multilevelmod.tidymodels.org/

external:
  contributors:
  - hfrick
  - topepo
  - EmilHvitfeldt
  - juliasilge
  - shah-in-boots
  - jeroenjanssens
  - a-difabio
  description: Parsnip wrappers for mixed-level and hierarchical models
  first_commit: '2020-04-23T22:54:06+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.500841+00:00'
  latest_release: '2022-06-17T12:13:05+00:00'
  license: NOASSERTION
  people:
  - Hannah Frick
  - Max Kuhn
  - Emil Hvitfeldt
  - Julia Silge
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/multilevelmod
  stars: 73
  title: multilevelmod
  website: https://multilevelmod.tidymodels.org/
---

multilevelmod brings the power of mixed-effects and hierarchical models into the tidymodels ecosystem by providing parsnip wrappers for multi-level modeling. When your data has nested or grouped structures—such as repeated measurements on subjects, students within schools, or observations within geographic regions—multilevelmod lets you model these hierarchical relationships using the familiar and consistent parsnip interface. This integration allows data scientists to incorporate random effects and hierarchical structures into their tidymodels workflows without leaving the framework they already know.

The package supports a wide range of computational backends across three primary model types: linear regression, logistic regression, and Poisson regression. You can choose from frequentist engines like lmer, glmer, and gee, or Bayesian approaches using stan_glmer, giving you the flexibility to select the right tool for your modeling needs. Whether you're analyzing longitudinal data, conducting meta-analyses, or working with any dataset where observations are naturally grouped, multilevelmod provides a unified interface that makes multi-level modeling more accessible and integrates seamlessly with the broader tidymodels toolkit for preprocessing, resampling, and model evaluation.
