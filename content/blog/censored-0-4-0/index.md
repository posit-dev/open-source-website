---
title: censored 0.4.0
date: 2026-11-20T00:00:00.000Z
people:
  - Hannah Frick
description: >
  censored 0.4.0 is on CRAN! It brings two new random forest engines, a null
  model for censored regression, and faster tuning for boosted trees.
image: featured.jpg
image-alt: >
  Motion-blurred photo of trees in autumn, with bright red and orange foliage
  against a pale sky.
topics:
  - Machine Learning
software:
  - censored
  - tidymodels
  - parsnip
languages:
  - R
source: tidyverse
hidesubscription: false
photo:
  url: >-
    https://unsplash.com/photos/a-blurry-photo-of-a-tree-with-red-leaves-P6uuIfdoeKo
  author: Christian Wright
---


## Intro

We're tickled pink to announce the release of [censored](https://censored.tidymodels.org/) 0.4.0. censored is a parsnip extension package for time-to-event aka survival models.

You can install it from CRAN with:

``` r
install.packages("censored")
```

This blog post will introduce two new random forest engines, a null model as a baseline, faster tuning for boosted trees, and fixes that change model results.

You can see a full list of changes in the [release notes](https://github.com/tidymodels/censored/releases/tag/v0.4.0).

## Two new engines for random forests

`rand_forest()` for censored regression now has two more engines: `"ranger"` and `"randomForestSRC"`. These join `"partykit"` and `"aorsf"`. Both are popular, fast implementations of random survival forests. Both new engines support predicts of `type = "time"` for survival time and `type = "survival"` for probability of survival.

``` r
lung <- na.omit(survival::lung)
lung_pred <- lung[1:3, ]

set.seed(1)
rf_ranger <- rand_forest(trees = 500) |>
  set_engine("ranger") |>
  set_mode("censored regression") |>
  fit(Surv(time, status) ~ ., data = lung)

predict(rf_ranger, lung_pred, type = "time")
#> # A tibble: 3 × 1
#>   .pred_time
#>        <dbl>
#> 1        455
#> 2        210
#> 3        643
```

To use randomForestSRC instead of ranger, simply switch out the engine.

As usual for censored, predictions of survival probability at various `eval_time` points are returned as nested tibbles, keeping to the tidymodels principle of one row per observation.

``` r
set.seed(1)
rf_rfsrc <- rand_forest(trees = 500) |>
  set_engine("randomForestSRC") |>
  set_mode("censored regression") |>
  fit(Surv(time, status) ~ ., data = lung)

pred_rfsrc <- predict(
  rf_rfsrc,
  lung_pred,
  type = "survival",
  eval_time = c(100, 500)
)
pred_rfsrc
#> # A tibble: 3 × 1
#>   .pred           
#>   <list>          
#> 1 <tibble [2 × 2]>
#> 2 <tibble [2 × 2]>
#> 3 <tibble [2 × 2]>
pred_rfsrc$.pred[[1]]
#> # A tibble: 2 × 2
#>   .eval_time .pred_survival
#>        <dbl>          <dbl>
#> 1        100          0.911
#> 2        500          0.315
```

### Coming from randomForestSRC?

parsnip's, and therefore censored's, raison d'être is to provide an interface to various models that makes switching between them as easy as in the example above. Sometimes that means that working with an engine via censored is a little different than working with the engine package directly. So if you are used to working with `randomForestSRC::rfsrc()` directly, here are some noteworthy differences.

randomForestSRC requires you to specify the response in the model formula via a call to `Surv()` and for a survival forest, the status variable has to be coded 0/1, otherwise a competing risks forest is being fitted:

``` r
set.seed(1)
rfsrc_direct <- randomForestSRC::rfsrc(Surv(time, status) ~ ., data = lung)
rfsrc_direct$family
#> [1] "surv-CR"
```

Since a 1/2 encoding of the status is not uncommon, as, e.g., in the everyone's favorite example dataset `lung`, censored evaluates the `Surv()` response first, so a 1/2 coding is handled like in every other survival model:

``` r
extract_fit_engine(rf_rfsrc)$family
#> [1] "surv"
```

In the usual tidymodels setup, you bundle a model with a recipe for preprocessing in a workflow. This works best when the response is handled outside of the recipe, i.e., you pre-make your response as a `Surv` object.

``` r
lung_surv <- lung |>
  mutate(surv = Surv(time, status), .keep = "unused")
```

Handing such a pre-made `surv` response directly to `randomForestSRC::rfsrc()` results in a regression forest, as the signal of the `Surv()` specification is missing from the model formula. Since it is such a common pattern in the tidymodels context, you can use it with censored though:

``` r
rf_spec <- rand_forest() |>
  set_engine("randomForestSRC") |>
  set_mode("censored regression")
rec <- recipe(surv ~ ., data = lung_surv)
rf_fit <- workflow(rec, rf_spec) |>
  fit(data = lung_surv)

extract_fit_engine(rf_fit)$family
#> [1] "surv"
```

## A null model for censored regression

parsnip contains a `null_model()` to help you establish a baseline for your modeling problem. It now has a `"censored regression"` mode with the `"survival"` engine. This ignores the predictors and fits a Kaplan-Meier curve via `survival::survfit()`. It supports predictions of `type = "time"` and `type = "survival"`, like the other engines in censored.

So let's see how a random forest does compared to the null model! We estimate the integrated Brier score via resampling for both models, keeping the random forest to the default values for all hyperparameters. For more on the integrated Brier score and other dynamic metrics, see also the [tidymodels.org survival articles](https://www.tidymodels.org/learn/#category=survival%20analysis).

``` r
set.seed(2)
lung_folds <- vfold_cv(lung, v = 5)

surv_metrics <- metric_set(brier_survival_integrated)
eval_times <- seq(100, 700, by = 100)

null_res <- workflow(
  Surv(time, status) ~ .,
  null_model() |>
    set_engine("survival") |>
    set_mode("censored regression")
) |>
  fit_resamples(lung_folds, metrics = surv_metrics, eval_time = eval_times)

ranger_res <- workflow(
  Surv(time, status) ~ .,
  rand_forest() |>
    set_engine("ranger") |>
    set_mode("censored regression")
) |>
  fit_resamples(lung_folds, metrics = surv_metrics, eval_time = eval_times)

bind_rows(
  collect_metrics(null_res) |> mutate(model = "Kaplan-Meier"),
  collect_metrics(ranger_res) |> mutate(model = "ranger")
) |>
  select(model, .metric, mean, n, std_err)
#> # A tibble: 2 × 5
#>   model        .metric                    mean     n std_err
#>   <chr>        <chr>                     <dbl> <int>   <dbl>
#> 1 Kaplan-Meier brier_survival_integrated 0.171     5 0.00903
#> 2 ranger       brier_survival_integrated 0.173     5 0.00516
```

On this small dataset (dropping observations with missing values for ranger only leaves 167 of them), the random forest is on par with the Kaplan-Meier but not better - exactly why we want to know how well a more complex model does compared to the baseline! If you wanted to dig deeper into this, you could assess the differences in these two models via `int_pctl()` to calculate bootstrap confidence intervals.

## mboost: tunable learning rate and `multi_predict()`

Boosted survival trees via `boost_tree()` with the `"mboost"` engine got several improvements. We've made the `learn_rate` tunable and as part of that, it now properly maps to `mboost::boost_control(nu)`. Previously it was silently ignored. I suspect that this might have been overlooked in part because the learn rate is not typically what you tune. (But now you can if you want to!) As long as it's small (mboost's default is 0.1), the number of trees is usually much more influential.

This is where the second improvement for the mboost engine comes in. It now has a `multi_predict()` method which let's you predict for multiple number of trees from a single fitted model object.

``` r
boost_fit <- boost_tree(trees = 200, learn_rate = 0.05) |>
  set_engine("mboost") |>
  set_mode("censored regression") |>
  fit(Surv(time, status) ~ ., data = lung)

multi_pred <- multi_predict(
  boost_fit,
  lung_pred,
  type = "survival",
  eval_time = c(100, 500),
  trees = c(50, 100, 200)
)
multi_pred$.pred[[1]]
#> # A tibble: 6 × 3
#>   trees .eval_time .pred_survival
#>   <int>      <dbl>          <dbl>
#> 1    50        100          0.879
#> 2    50        500          0.298
#> 3   100        100          0.887
#> 4   100        500          0.288
#> 5   200        100          0.895
#> 6   200        500          0.271
```

This submodel trick of "fit once, predict often" is nice when exploring one model but really shines when using `tune_grid()`. That uses the `multi_predict()` method automatically, making tuning over many different values for `trees` cheap(er). For each resample, it find the grid points which only differ in the number of trees, fits only the model with the largest number of trees, and predicts from it for all the smaller `trees` values, instead of fitting one model per grid point.

So let's do a small example: We are tuning over `trees` (and keeping `learn_rate` at its default), reusing `lung_folds` from the null model section.

``` r
boost_wflow <- workflow(
  Surv(time, status) ~ .,
  boost_tree(trees = tune()) |>
    set_engine("mboost") |>
    set_mode("censored regression")
)

system.time(
  boost_res <- tune_grid(
    boost_wflow,
    resamples = lung_folds,
    grid = 10,
    metrics = metric_set(concordance_survival)
  )
)
#>    user  system elapsed 
#>  32.033   0.035  32.092
```

To give you a ballpark figure, with censored 0.3.5 (and no `multi_predict()` method), the same code took about 90 seconds on my laptop. So this is roughly 3 times faster now, corresponding to fitting one model instead of ten per resample. The more values for `trees` you need to tune over, the more you will notice this speedup.

## Fixes that change your model results

We tightened tests for this release. You can read the full list of bugs we found and fixed in the [release notes](https://github.com/tidymodels/censored/releases/tag/v0.4.0). Here we want to highlight a few that change the fitted models or their predictions. If you've used these engines before, you'll want to know about them.

### Decision trees now predict survival times

For `decision_tree()` with the `"rpart"` engine, `type = "time"` predictions are now the median survival time from the Kaplan-Meier curve in each leaf. Previously, they were rpart's relative event rate, which is not a time at all! For the three patients below, censored 0.3.5 predicted 0.91, 2.29, and 0.71 "days".

``` r
tree_fit <- decision_tree() |>
  set_engine("rpart") |>
  set_mode("censored regression") |>
  fit(Surv(time, status) ~ ., data = lung)

predict(tree_fit, lung_pred, type = "time")
#> # A tibble: 3 × 1
#>   .pred_time
#>        <dbl>
#> 1        337
#> 2        197
#> 3        428
```

### Model arguments now reach the engine

In a few places, arguments were silently ignored or overridden. We've already seen the `learn_rate` for boosted trees with mboost. The other model that wasn't quite right in this regard was `bag_tree()` with the rpart engine. `tree_depth`, `min_n`, and `cost_complexity` are now passed on to the individual trees, as are other `rpart::rpart.control()` arguments set via `set_engine()`.

This has a consequence for default fits of bagged survival trees with `"rpart"`: they now use the general `bag_tree()` defaults of `cost_complexity = 0` and `min_n = 2`, i.e., fully grown, unpruned trees, which is the usual choice for bagging. Previously, they used rpart's defaults of `cp = 0.01` and `minsplit = 20`.

``` r
set.seed(3)
bag_fit <- bag_tree() |>
  set_engine("rpart") |>
  set_mode("censored regression") |>
  fit(Surv(time, status) ~ ., data = lung)

bag_engine <- extract_fit_engine(bag_fit)
bag_engine$mtrees[[1]]$btree$control[c("cp", "minsplit")]
#> $cp
#> [1] 0
#> 
#> $minsplit
#> [1] 2
```

### Case weights

`bag_tree()` with the `"rpart"` engine and `boost_tree()` with the `"mboost"` engine no longer accept case weights. For bagged trees, the underlying package ipred now errors when weights are passed. For boosted trees, mboost can do weighted fits but does not predict from those fits. So instead of finding out about this at prediction time, we have turned off case weights for this engine for now.

## Acknowledgements

A big thank you to all the people who have contributed to censored since the release of v0.3.0:

[@AKALeon](https://github.com/AKALeon), [@EmilHvitfeldt](https://github.com/EmilHvitfeldt), [@gaborcsardi](https://github.com/gaborcsardi), [@hfrick](https://github.com/hfrick), [@jeroenjanssens](https://github.com/jeroenjanssens), [@jesusherranz](https://github.com/jesusherranz), [@jkylearmstrong](https://github.com/jkylearmstrong), [@simonpcouch](https://github.com/simonpcouch), and [@topepo](https://github.com/topepo).
