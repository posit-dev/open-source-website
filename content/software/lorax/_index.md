---
description: R functions and methods to extract elements of tree- and     rule-based
  models.
github: tidymodels/lorax
image: logo.png
color: "#D2934A"
languages:
- R
people:
- Max Kuhn
title: lorax
topics:
- Machine Learning
website: http://lorax.tidymodels.org/

external:  # updated automatically, do not edit
  description: R functions and methods to extract elements of tree- and     rule-based
    models.
  first_commit: '2026-03-14T15:01:44+00:00'
  forks: 1
  languages:
  - R
  last_updated: '2026-09-18T14:24:40.933478+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  readme_image: man/figures/logo.png
  repo: tidymodels/lorax
  stars: 8
  title: lorax
  website: http://lorax.tidymodels.org/
---

lorax extracts decision rules from tree- and rule-based models fitted in R. Rules are expressed as logical predicates that identify paths to terminal nodes, making model behavior more transparent and interpretable.

The package provides a consistent interface across many tree-based implementations, with accessors for the predictors a model actually uses and its variable importance scores, plus conversion methods to partykit party objects so that individual trees can be plotted and analyzed with partykit's tools.
