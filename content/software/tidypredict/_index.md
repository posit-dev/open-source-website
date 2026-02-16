---
description: Run predictions inside the database
github: tidymodels/tidypredict
image: logo.png
languages:
- R
latest_release: '2025-12-12T20:10:58+00:00'
people:
- Edgar Ruiz
- Emil Hvitfeldt
- Max Kuhn
- Simon Couch
- Julia Silge
- Hannah Frick
- Davis Vaughan
- Jeroen Janssens
title: tidypredict
website: https://tidypredict.tidymodels.org

external:
  contributors:
  - edgararuiz
  - EmilHvitfeldt
  - edgararuiz-zz
  - topepo
  - Athospd
  - simonpcouch
  - JiaxiangBU
  - juliasilge
  - ThenoobMario
  - hfrick
  - saadaslam
  - tslumley
  - wibeasley
  - bfgray3
  - dpprdan
  - DavisVaughan
  - jeroenjanssens
  - washcycle
  - SimonCoulombe
  description: Run predictions inside the database
  first_commit: '2017-12-18T00:26:43+00:00'
  forks: 33
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.150548+00:00'
  latest_release: '2025-12-12T20:10:58+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  - Emil Hvitfeldt
  - Max Kuhn
  - Simon Couch
  - Julia Silge
  - Hannah Frick
  - Davis Vaughan
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/tidypredict
  stars: 262
  title: tidypredict
  website: https://tidypredict.tidymodels.org
---

tidypredict enables you to run predictions from R models directly inside databases, eliminating the need to pull data into R for scoring. By parsing trained models and translating them into SQL statements, tidypredict allows you to leverage your database's computational power for predictions at scale. It works seamlessly with dplyr's database interface, supporting multiple backends including MS SQL, PostgreSQL, and others, making it an essential tool for production machine learning workflows where data movement is costly or impractical.

The package supports a wide range of popular modeling frameworks including linear and generalized linear models, random forests via randomForest and ranger, XGBoost, LightGBM, MARS, Cubist, and partykit trees. What makes tidypredict particularly valuable is its parsed model specification format, which provides a lightweight alternative to saving entire model objects or using PMML. This approach is ideal for deploying models in Shiny applications or sharing model logic across systems without the overhead of large serialized objects, while maintaining full compatibility with the tidymodels ecosystem and parsnip interface.