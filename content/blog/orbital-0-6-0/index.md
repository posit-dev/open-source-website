---
title: orbital 0.6.0
date: '2026-08-28'
people:
  - Emil Hvitfeldt
description: |
  orbital 0.6.0 is on CRAN, with support for many more models.
image: featured.jpg
image-alt: >-
  Earth seen from orbit, cloud-covered ocean curving away to a thin blue
  horizon, with a satellite in the upper right.
photo:
  url: https://unsplash.com/photos/view-of-earth-and-satellite-yZygONrUBe8
  author: NASA
source: tidyverse
software:
  - orbital
  - tidypredict
  - tidymodels
languages:
  - R
topics:
  - Machine Learning
  - MLOps and Admin
tags:
  - tidymodels
format:
  hugo-md:
    echo: true
---


We're happy to announce the release of [orbital](https://orbital.tidymodels.org/) 0.6.0.
orbital turns a fitted tidymodels workflow into the set of equations that produce its predictions,
so you can run those predictions in a database instead of moving the data to R.
It uses [tidypredict](https://tidypredict.tidymodels.org/) under the hood to translate fitted models.
This post also covers the release of tidypredict 1.2.0.

This post is about the R package.
There is also a [Python version of orbital](https://posit-dev.github.io/orbital/) that works on scikit-learn pipelines.

You can install both from CRAN with:

``` r
install.packages(c("orbital", "tidypredict"))
```

This post covers the highlights of these releases.
You can see the full list of changes in the [orbital release notes](https://orbital.tidymodels.org/news/index.html) and the [tidypredict release notes](https://tidypredict.tidymodels.org/news/index.html).

## A lot more models

Previously orbital and tidypredict supported a handful of useful models.
This included linear models, decision trees, random forests, and boosted trees models.
This release adds discriminant analysis, naive Bayes, neural networks, support vector machines, partial least squares,
and several more rule and ensemble methods.
This fills in the gaps of most of the known models that can be made to work with orbital.

Newly supported for regression:

- `bart(engine = "dbarts")`
- `boost_tree(engine = "h2o_gbm")`
- `linear_reg(engine = "glm")`
- `mlp(engine = "nnet")`
- `null_model()`
- `pls(engine = "mixOmics")`
- `rand_forest(engine = "aorsf")`
- `rand_forest(engine = "partykit")`
- `rule_fit(engine = "h2o")`
- `svm_linear(engine = "kernlab")`
- `svm_linear(engine = "LiblineaR")`

Newly supported for classification:

- `bag_tree(engine = "rpart")` and `bag_tree(engine = "C5.0")`
- `boost_tree(engine = "C5.0")`
- `boost_tree(engine = "h2o_gbm")`
- `C5_rules(engine = "C5.0")`
- `decision_tree(engine = "C5.0")`
- `discrim_linear(engine = "MASS")`, `discrim_quad(engine = "MASS")`
- `discrim_linear()` with the `"mda"`, `"sda"`, and `"sparsediscrim"` engines
- `logistic_reg(engine = "LiblineaR")`
- `mlp(engine = "nnet")`
- `multinom_reg(engine = "nnet")`
- `naive_Bayes(engine = "klaR")` and `naive_Bayes(engine = "naivebayes")`
- `null_model()`
- `pls(engine = "mixOmics")`
- `rule_fit(engine = "h2o")`
- `rule_fit(engine = "xrf")`
- `svm_linear(engine = "kernlab")`
- `svm_linear(engine = "LiblineaR")`

One thing worth noting here is that you need a running H2O cluster to build the orbital object.
Prediction and SQL generation from the orbital object stays dependency free.

Here is a linear discriminant analysis model,
which was not supported before this release,
fit on the penguins data and then run in DuckDB.

``` r
library(tidymodels)
library(discrim)
library(orbital)
library(duckdb)

data(penguins, package = "modeldata")
penguins <- tidyr::drop_na(penguins)

rec_spec <- recipe(species ~ ., data = penguins) |>
  step_dummy(all_nominal_predictors()) |>
  step_normalize(all_numeric_predictors())

mod_spec <- discrim_linear(engine = "MASS")

wf_spec <- workflow(rec_spec, mod_spec) |>
  fit(penguins)

orb <- orbital(wf_spec, type = c("class", "prob"))

con <- DBI::dbConnect(duckdb::duckdb())
penguins_db <- dplyr::copy_to(con, penguins, "penguins")

predict(orb, penguins_db)
```

    # A query:  ?? x 4
    # Database: DuckDB 1.5.5 [root@Darwin 25.6.0:R 4.6.1/:memory:]
       .pred_class .pred_Adelie .pred_Chinstrap .pred_Gentoo
       <chr>              <dbl>           <dbl>        <dbl>
     1 Adelie             1.000        6.43e- 9     4.64e-25
     2 Adelie             1.000        5.25e- 6     8.81e-16
     3 Adelie             1.000        1.97e- 4     2.61e-17
     4 Adelie             1.000        2.99e- 8     1.93e-23
     5 Adelie             1.000        8.34e- 9     4.42e-29
     6 Adelie             1.000        1.60e- 6     4.14e-20
     7 Adelie             1.000        6.03e-10     1.45e-18
     8 Adelie             0.999        6.47e- 4     4.16e-20
     9 Adelie             1.000        9.56e-10     1.97e-30
    10 Adelie             1.000        6.73e-14     9.13e-27
    # ℹ more rows

We have documented the [list of supported models](https://orbital.tidymodels.org/articles/supported-models.html).
If there is a model you need that is still missing,
[let us know](https://github.com/tidymodels/tidypredict/issues) so we can prioritize it.

## When a model has no probability

While we added these new methods we ran into a problem we didn't have before.
For many classification models you get both predicted probabilities and hard class predictions.
This release has added models where that is not the case.
A number of newly added models only produce hard class predictions.

Instead of trying to invent class probabilities,
we produce an informative error for the affected models.

``` r
c5_wf <- workflow(
  species ~ .,
  decision_tree(mode = "classification", engine = "C5.0")
) |>
  fit(penguins)

orbital(c5_wf, type = "prob")
```

    Error in `orbital()`:
    ! "prob" predictions are not available for this model.
    ℹ It predicts a class directly, with no probability behind it.
    ℹ Use `type = "class"` instead.

## tidypredict is now a toolkit, not just a function

We have talked a lot about orbital so far.
This is because we think that it is the ideal interface compared to tidypredict,
if your goal is to generate SQL expressions for a fitted model or workflow.

orbital and tidypredict work together to generate the expression that you need.
We have expanded tidypredict with a number of generics,
which are all developer focused.
With the goal that packages other than orbital can benefit from the work we have done.
Three of them describe what a model's fitted expressions compute:

- `tidypredict_output_type()` returns `"numeric"`, `"prob"`, `"decision"`, or `"class"`
- `tidypredict_outcome_levels()` returns the outcome levels in model order
- `tidypredict_normalized()` reports whether per-level probabilities already sum to one

Below we see two of the generics in action.

``` r
library(tidypredict)

svm_fit <- svm_linear(mode = "classification", engine = "LiblineaR") |>
  fit(sex ~ bill_length_mm + body_mass_g, data = penguins)

tidypredict_output_type(svm_fit$fit)
```

    [1] "decision"

``` r
tidypredict_outcome_levels(svm_fit$fit)
```

    [1] "female" "male"  

The other five expose the per-tree pieces that `tidypredict_fit()` assembles,
so a package generating its own code can split an ensemble apart and put it back together:

- `tidypredict_trees()` returns per-tree expressions
- `tidypredict_n_trees()` returns the number of trees
- `tidypredict_combine_trees()` turns per-tree expressions back into a prediction
- `tidypredict_class_trees()` returns per-tree expressions for each outcome level
- `tidypredict_class_exprs()` returns one finished expression per outcome level

``` r
rf <- rand_forest(mode = "regression", trees = 5, engine = "ranger") |>
  fit(body_mass_g ~ bill_length_mm + flipper_length_mm, data = penguins)

tidypredict_n_trees(rf$fit)
```

    [1] 5

``` r
tidypredict_combine_trees(rf$fit, rlang::syms(paste0("tree_", 1:5)))
```

    (tree_1 + tree_2 + tree_3 + tree_4 + tree_5)/5

A lot of this logic was hardcoded inside orbital on a model by model basis,
it is now formalized in such a way that you can easily use just the bits you need.

## Acknowledgements

Many thanks to all the people who contributed to orbital and tidypredict since the last release!

[@EmilHvitfeldt](https://github.com/EmilHvitfeldt), [@jannikbx](https://github.com/jannikbx), and [@RAMitchell](https://github.com/RAMitchell).
