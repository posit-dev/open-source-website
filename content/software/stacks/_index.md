---
description: An R package for tidy stacked ensemble modeling
github: tidymodels/stacks
image: logo.png
color: "#783F23"
languages:
- R
latest_release: '2025-05-27T19:55:03+00:00'
people:
- Simon Couch
- Max Kuhn
- Emil Hvitfeldt
- Hannah Frick
- Gábor Csárdi
title: stacks
website: https://stacks.tidymodels.org

external:  # updated automatically, do not edit
  description: An R package for tidy stacked ensemble modeling
  first_commit: '2020-06-12T20:51:21+00:00'
  forks: 29
  languages:
  - R
  last_updated: '2026-03-05T16:23:26.553733+00:00'
  latest_release: '2025-05-27T19:55:03+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Max Kuhn
  - Emil Hvitfeldt
  - Hannah Frick
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: tidymodels/stacks
  stars: 302
  title: stacks
  website: https://stacks.tidymodels.org
---

stacks is an R package for model stacking that integrates with the tidymodels ecosystem. It creates ensemble models by combining predictions from multiple trained models (called members) into a single meta-model that leverages the strengths of each individual model.

The package uses regularized linear regression to determine stacking coefficients, automatically selecting which candidate models contribute to the final ensemble by zeroing out low-performing members. It works with any model type from parsnip, any resampling scheme from rsample, and any error metric from yardstick, making it flexible across different modeling scenarios. The workflow involves adding candidate models to a data stack, blending their predictions through metalearning, and fitting the final ensemble on the full training set.
