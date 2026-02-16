---
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
- Mine Çetinkaya-Rundel
title: themis
website: https://themis.tidymodels.org/

external:
  contributors:
  - EmilHvitfeldt
  - RobertGregg
  - topepo
  - juliasilge
  - hfrick
  - rpln
  - jxu
  - bebru
  - mine-cetinkaya-rundel
  - PursuitOfDataScience
  description: Extra recipes steps for dealing with unbalanced data
  first_commit: '2019-10-12T18:46:35+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.406628+00:00'
  latest_release: '2025-01-22T23:40:45+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Hannah Frick
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: tidymodels/themis
  stars: 142
  title: themis
  website: https://themis.tidymodels.org/
---

Named after the ancient Greek goddess of balance, themis is an R package that extends the recipes framework with specialized preprocessing tools for handling class imbalance in datasets. When working with real-world data, it's common to encounter situations where one class significantly outnumbers others—such as fraud detection, rare disease diagnosis, or customer churn prediction. This imbalance can lead to models that perform poorly on minority classes and produce biased predictions.

themis integrates seamlessly with the tidymodels ecosystem to address this challenge through a comprehensive suite of upsampling and downsampling techniques. The package provides methods ranging from simple random oversampling to sophisticated algorithms like SMOTE (Synthetic Minority Over-sampling Technique), ADASYN, and NearMiss, all accessible as recipe steps. By allowing you to adjust class ratios directly within your preprocessing pipeline, themis helps you build more balanced models that achieve better performance across all classes, improving both model fairness and predictive accuracy where it matters most.
