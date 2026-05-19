---
color: '#242C3C'
description: Extra recipes steps for dealing with unbalanced data
github: tidymodels/themis
image: logo.png
languages:
- R
latest_release: '2025-01-22T23:40:45+00:00'
people:
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Hannah Frick
- Jeroen Janssens
- Mine Çetinkaya-Rundel
title: themis
topics:
- Data Wrangling
- Machine Learning
website: https://themis.tidymodels.org/

external:  # updated automatically, do not edit
  description: Extra recipes steps for dealing with unbalanced data
  first_commit: '2019-10-12T18:46:35+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-05-19T11:51:32.141249+00:00'
  latest_release: '2025-01-22T23:40:45+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Hannah Frick
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: tidymodels/themis
  stars: 143
  title: themis
  website: https://themis.tidymodels.org/
---

themis provides preprocessing steps for the recipes package that handle imbalanced classification data. It implements multiple over-sampling and under-sampling algorithms to balance class distributions before model training.

The package includes several sampling techniques like SMOTE, ADASYN, and Tomek links that address class imbalance through synthetic data generation or selective sampling. These methods integrate directly into recipes workflows and support multi-class problems with tunable sampling ratios. themis solves the common problem where machine learning models perform poorly on minority classes due to unbalanced training data.
