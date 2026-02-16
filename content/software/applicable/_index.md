---
description: Quantify extrapolation of new samples given a training set
github: tidymodels/applicable
image: logo.png
languages:
- R
latest_release: '2024-04-24T17:26:35+00:00'
people:
- Max Kuhn
- Emil Hvitfeldt
- Julia Silge
- Hannah Frick
title: applicable
website: https://applicable.tidymodels.org/

external:
  contributors:
  - marlycormar
  - topepo
  - EmilHvitfeldt
  - juliasilge
  - hfrick
  description: Quantify extrapolation of new samples given a training set
  first_commit: '2019-07-08T18:53:53+00:00'
  forks: 8
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.342803+00:00'
  latest_release: '2024-04-24T17:26:35+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Emil Hvitfeldt
  - Julia Silge
  - Hannah Frick
  readme_image: man/figures/logo.png
  repo: tidymodels/applicable
  stars: 47
  title: applicable
  website: https://applicable.tidymodels.org/
---

applicable is an R package that addresses a critical question in predictive modeling: when should you trust your model's predictions? When new data points are substantially different from your training set, their predicted values may be unreliable. The package provides methods to quantify this extrapolation risk by measuring how far new observations deviate from the original training data, helping you identify potentially suspect predictions before they lead to costly errors. This concept of an "applicability domain," borrowed from chemistry where such models are standard practice, serves as essential quality control for production models.

What makes applicable particularly valuable for data scientists is its ability to work with both binary and continuous data, providing tailored methods for different modeling scenarios. Rather than blindly trusting model outputs on unfamiliar data, you can quantify whether predictions fall within your model's learned domain or represent dangerous extrapolations. As part of the tidymodels ecosystem, applicable integrates seamlessly with your existing modeling workflows, making it straightforward to add this layer of prediction reliability assessment to any project where stakes are high and out-of-distribution predictions could have serious consequences.
