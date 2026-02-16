---
description: Tools for tidy parameter tuning
github: tidymodels/tune
image: logo.png
languages:
- R
latest_release: '2025-10-17T15:54:07+00:00'
people:
- Max Kuhn
- Simon Couch
- Hannah Frick
- Davis Vaughan
- Julia Silge
- Emil Hvitfeldt
- Edgar Ruiz
- Lionel Henry
- Jeroen Janssens
- Gábor Csárdi
title: tune
website: https://tune.tidymodels.org

external:
  contributors:
  - topepo
  - simonpcouch
  - hfrick
  - DavisVaughan
  - juliasilge
  - EmilHvitfeldt
  - rorynolan
  - qiushiyan
  - stevenpawley
  - edgararuiz
  - dcossyleon
  - BrennanAntone
  - cheryldietrich
  - tjburch
  - monicagerber
  - martaalcalde
  - thegargiulian
  - lionel-
  - kelseygonzalez
  - Joscelinrocha
  - cimentadaj
  - jonthegeek
  - jeroenjanssens
  - gaborcsardi
  - franzbischoff
  - dmalkr
  description: Tools for tidy parameter tuning
  first_commit: '2019-08-09T20:49:40+00:00'
  forks: 47
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.358568+00:00'
  latest_release: '2025-10-17T15:54:07+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Simon Couch
  - Hannah Frick
  - Davis Vaughan
  - Julia Silge
  - Emil Hvitfeldt
  - Edgar Ruiz
  - Lionel Henry
  - Jeroen Janssens
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: tidymodels/tune
  stars: 320
  title: tune
  website: https://tune.tidymodels.org
---

Finding the right hyperparameters for your machine learning models can be a time-consuming and complex process. The tune package streamlines hyperparameter optimization for tidymodels workflows, providing a comprehensive toolkit for both traditional grid search and modern optimization techniques. Whether you're fine-tuning a random forest, calibrating an SVM, or optimizing preprocessing recipe parameters, tune integrates seamlessly with parsnip models, recipes, and dials parameter specifications to help you discover the best settings for your models.

Built with the tidymodels philosophy of composable and consistent interfaces, tune offers multiple search strategies including basic grid search, iterative Bayesian optimization, and racing methods that efficiently eliminate poor parameter combinations early. The package supports parallel processing to speed up computation, works naturally with cross-validation and other resampling methods, and returns results in tidy data formats that make it easy to visualize and compare model performance across different parameter configurations. For data scientists building production-ready models, tune provides the essential infrastructure to systematically explore hyperparameter spaces and extract maximum predictive performance from your modeling workflows.