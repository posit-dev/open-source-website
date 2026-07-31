---
title: lorax
description: Extract decision rules and characteristics from tree- and rule-based models
github: tidymodels/lorax
image: logo.png
languages:
- R
people:
- Max Kuhn
topics:
- Machine Learning
website: https://lorax.tidymodels.org
---

lorax extracts decision rules from tree- and rule-based models fitted in R. Rules are expressed as logical predicates that identify paths to terminal nodes, making model behavior more transparent and interpretable.

The package provides a consistent interface across many tree-based implementations, with accessors for the predictors a model actually uses and its variable importance scores, plus conversion methods to partykit party objects so that individual trees can be plotted and analyzed with partykit's tools.
