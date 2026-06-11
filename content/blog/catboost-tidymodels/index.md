---
title: CatBoost support in tidymodels
date: 2026-06-15T00:00:00.000Z
people:
  - Emil Hvitfeldt
description: >
  CatBoost is now available as a supported engine in tidymodels. This post shows
  how to train, tune, and use CatBoost models through the familiar parsnip
  interface.
image: featured.png
image-alt: >-
  The CatBoost logo and the tidymodels hex side by side on a gradient
  background.
topics:
  - Machine Learning
software:
  - tidymodels
  - parsnip
  - bonsai
languages:
  - R
hidesubscription: false
---


[CatBoost](https://catboost.ai/) is a very popular and high-quality gradient boosting library.
With the latest releases of [bonsai](https://bonsai.tidymodels.org/) and [parsnip](https://parsnip.tidymodels.org/),
you can now train CatBoost models from R using the same tidymodels interface you already use for xgboost, LightGBM, and the rest of the `boost_tree()` family.

## Installing CatBoost

The one wrinkle is installation.
The CatBoost R package is not on CRAN,
so you can't reach for `install.packages("catboost")` directly.

Grab the URL for your platform from the [CatBoost R installation guide](https://catboost.ai/docs/en/installation/r-installation-binary-installation) and install it with the remotes package.
For example, on an Apple Silicon or Intel Mac:

``` r
install.packages("remotes")
remotes::install_url(
  "https://github.com/catboost/catboost/releases/download/v1.2.10/catboost-R-darwin-universal2-1.2.10.tgz",
  INSTALL_opts = c("--no-multiarch", "--no-test-load", "--no-staged-install")
)
```

Swap in the release version, operating system, and architecture that match your setup.
The guide lists the full URL pattern and the binaries available for each release.

Once CatBoost itself is installed,
the tidymodels packages is just the usual packages:

``` r
# install.packages("pak")
pak::pak(c("tidymodels", "bonsai"))
```

You'll need **bonsai 0.4.1** (or later) and **parsnip 1.4.0** (or later),
which is where the CatBoost engine landed and got polished.

## Fitting a CatBoost model

CatBoost is supported as an engine for `boost_tree()`.
Loading bonsai registers the engine,
and from there it behaves like any other parsnip model spec:

``` r
library(tidymodels)
```

    ── Attaching packages ────────────────────────────────────── tidymodels 1.4.1 ──

    ✔ broom        1.0.12.9000     ✔ recipes      1.3.2      
    ✔ dials        1.4.3           ✔ rsample      1.3.2      
    ✔ dplyr        1.2.1           ✔ tailor       0.1.0      
    ✔ ggplot2      4.0.3           ✔ tidyr        1.3.2      
    ✔ infer        1.1.0           ✔ tune         2.1.0.9000 
    ✔ modeldata    1.5.1           ✔ workflows    1.3.0      
    ✔ parsnip      1.6.0           ✔ workflowsets 1.1.1      
    ✔ purrr        1.2.2           ✔ yardstick    1.4.0      

    ── Conflicts ───────────────────────────────────────── tidymodels_conflicts() ──
    ✖ purrr::discard() masks scales::discard()
    ✖ dplyr::filter()  masks stats::filter()
    ✖ dplyr::lag()     masks stats::lag()
    ✖ recipes::step()  masks stats::step()

``` r
library(bonsai)

cat_spec <-
  boost_tree(trees = 500, learn_rate = 0.05) |>
  set_engine("catboost") |>
  set_mode("regression")

cat_fit <- fit(cat_spec, mpg ~ ., data = mtcars)
cat_fit
```

    parsnip model object

    CatBoost model (500 trees)
    Loss function: RMSE
    Fit to 10 feature(s)

## Tuning

The CatBoost engine supports the standard `boost_tree()` tuning parameters,
and the recent releases made tuning both faster and more correct.

A typical tuning setup looks like this:

``` r
cat_spec <-
  boost_tree(trees = tune(), learn_rate = tune()) |>
  set_engine("catboost") |>
  set_mode("regression")

cat_wf <- workflow(mpg ~ ., cat_spec)

set.seed(123)
folds <- vfold_cv(mtcars, v = 5)

tune_res <- tune_grid(cat_wf, resamples = folds, grid = 20)

show_best(tune_res, metric = "rmse")
```

    # A tibble: 5 × 8
      trees learn_rate .metric .estimator  mean     n std_err .config         
      <int>      <dbl> <chr>   <chr>      <dbl> <int>   <dbl> <chr>           
    1  1473     0.0379 rmse    standard    2.76     5   0.419 pre0_mod15_post0
    2   527     0.0513 rmse    standard    2.81     5   0.443 pre0_mod06_post0
    3  1053     0.0941 rmse    standard    2.83     5   0.447 pre0_mod11_post0
    4   211     0.127  rmse    standard    2.84     5   0.400 pre0_mod03_post0
    5   632     0.234  rmse    standard    2.86     5   0.480 pre0_mod07_post0

Thanks to the [submodel trick](https://parsnip.tidymodels.org/articles/Submodels.html)
tuning `trees` doesn't require refitting the model from scratch at every candidate value.

## Wrapping up

CatBoost is a great addition to the gradient boosting options available in tidymodels,
especially if you work with categorical features or want a strong out-of-the-box model.

For the full details, see the [bonsai changelog](https://bonsai.tidymodels.org/news/index.html) and the [parsnip 1.4.0 release notes](https://parsnip.tidymodels.org/news/index.html#parsnip-140).
