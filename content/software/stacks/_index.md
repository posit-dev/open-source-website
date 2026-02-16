---
description: An R package for tidy stacked ensemble modeling
github: tidymodels/stacks
image: logo.png
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

external:
  contributors:
  - simonpcouch
  - topepo
  - EmilHvitfeldt
  - hfrick
  - gaborcsardi
  - Joscelinrocha
  - asmae-toumi
  - osorensen
  description: An R package for tidy stacked ensemble modeling
  first_commit: '2020-06-12T20:51:21+00:00'
  forks: 29
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.579165+00:00'
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

stacks is an R package that implements model stacking, a powerful ensemble method that combines predictions from multiple models to create a single, superior predictive model. By systematically blending diverse modeling approaches—from random forests to neural networks—stacks captures complementary strengths across different algorithms, often achieving better predictive performance than any individual model alone. The package uses regularized linear regression to automatically determine optimal weights for each candidate model, intelligently excluding redundant contributors while retaining those that genuinely improve predictions.

Built as a natural extension of the tidymodels ecosystem, stacks integrates seamlessly with familiar tools like recipes, workflows, and tune. It supports any model available in parsnip, works with any resampling scheme from rsample, and can optimize for any metric from yardstick or custom performance measures. Whether you're working on classification or regression problems, stacks provides a tidy, principled workflow for creating interpretable and efficient ensemble models that leverage the full breadth of your modeling toolkit.
