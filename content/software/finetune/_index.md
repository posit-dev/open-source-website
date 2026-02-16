---
description: Additional functions for model tuning
github: tidymodels/finetune
image: logo.png
languages:
- R
latest_release: '2025-05-20T21:08:32+00:00'
people:
- Max Kuhn
- Simon Couch
- Hannah Frick
- Emil Hvitfeldt
- Julia Silge
- Gábor Csárdi
- Jeroen Janssens
title: finetune
website: https://finetune.tidymodels.org/

external:
  contributors:
  - topepo
  - simonpcouch
  - hfrick
  - EmilHvitfeldt
  - juliasilge
  - SokolovAnatoliy
  - FvD
  - gaborcsardi
  - jeroenjanssens
  - krlmlr
  - mfansler
  - qiushiyan
  description: Additional functions for model tuning
  first_commit: '2020-07-04T20:12:07+00:00'
  forks: 11
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.610867+00:00'
  latest_release: '2025-05-20T21:08:32+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Simon Couch
  - Hannah Frick
  - Emil Hvitfeldt
  - Julia Silge
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/finetune
  stars: 63
  title: finetune
  website: https://finetune.tidymodels.org/
---

The finetune package brings advanced hyperparameter optimization methods to the tidymodels ecosystem, making it easier to find optimal model configurations without exhaustive computational overhead. Built as an extension to the tune package, finetune provides sophisticated search algorithms including simulated annealing and racing methods that intelligently explore the parameter space. These techniques are particularly valuable when working with complex models or large datasets where traditional grid search becomes prohibitively expensive.

At its core, finetune offers three powerful approaches to model tuning. Simulated annealing uses a probabilistic strategy that occasionally accepts worse solutions to escape local optima, helping you discover better hyperparameter combinations across rugged optimization landscapes. Racing methods take a different approach by evaluating all candidate parameters on small resamples first, then statistically eliminating poor performers early in the process. Whether you choose ANOVA-based racing or win/loss tournament-style racing, you can dramatically reduce tuning time while maintaining the quality of your final model selection.
