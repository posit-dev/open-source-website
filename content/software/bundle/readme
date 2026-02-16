
<!-- README.md is generated from README.Rmd. Please edit that file -->

# bundle

<!-- badges: start -->

[![R-CMD-check](https://github.com/rstudio/bundle/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/rstudio/bundle/actions/workflows/R-CMD-check.yaml)
[![CRAN
status](https://www.r-pkg.org/badges/version/bundle)](https://CRAN.R-project.org/package=bundle)
[![Lifecycle:
stable](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://lifecycle.r-lib.org/articles/stages.html#stable)
[![Codecov test
coverage](https://codecov.io/gh/rstudio/bundle/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rstudio/bundle?branch=main)
<!-- badges: end -->

Typically, models in R exist in memory and can be saved as `.rds` files.
However, some models store information in locations that cannot be saved
using `save()` or `saveRDS()` directly. The goal of bundle is to provide
a common interface to capture this information, situate it within a
portable object, and restore it for use in new settings.

## Installation

You can install the released version of bundle from
[CRAN](https://CRAN.R-project.org) with:

``` r
install.packages("bundle")
```

And the development version from [GitHub](https://github.com/) with:

``` r
# install.packages("pak")
pak::pak("rstudio/bundle")
```

## Overview

We often imagine a trained model as a somewhat “standalone” R
object—given some new data, the R object can generate predictions on its
own. In reality, some types of model objects also make use of
*references* to generate predictions. A reference is a piece of
information that a model object refers to that isn’t part of the object
itself; this could be anything from a connection with a server to an
internal function in the package used to train the model. When we call
`predict()`, model objects know where to look to retrieve that data, but
saving model objects can sometimes disrupt those references. Thus, if we
want to train a model, save it, re-load it into memory in a production
setting, and generate predictions with it, we may run into issues
because those references do not exist in the new computational
environment.

We need some way to preserve access to those references. The bundle
package provides a consistent interface for *bundling* model objects
with their references so that they can be safely saved and re-loaded in
production:

<img src="man/figures/diagram_04.png" alt="A diagram showing a rectangle, labeled model object, and another rectangle, labeled predictions. The two are connected by an arrow from model object to predictions, with the label 'predict'. There are two boxes labeled reference, connected to the arrow labeled predict with dotted arrows, to show that, most of the time, we don't need to think about including them in our workflow. There are two boxes, labeled R Session number one, and R session number two. In focus is the arrow from the model object, in R Session number one, to a model object in R session number two. This arrow connecting the model object in R session one and the model object in R session two is connected by a verb called bundle. The bundle function outputs an object called a bundle." width="100%" />

For more on this diagram, see the [main bundle
vignette](https://rstudio.github.io/bundle/articles/bundle.html).

When you’re ready to save your model, `bundle()` it first. Once you’ve
loaded it in a new setting, `unbundle()` it!

## Example

The bundle package prepares model objects so that they can be
effectively saved and re-loaded for use in new R sessions. To
demonstrate using bundle, we will train a boosted tree model using
[XGBoost](https://xgboost.readthedocs.io/), bundle it, and then pass the
bundle into another R session to generate predictions on new data.

First, load needed packages:

``` r
library(bundle)
library(parsnip)
library(callr)
library(waldo)
```

Fit the boosted tree model:

``` r
# fit an boosted tree with xgboost via parsnip
mod <-
  boost_tree(trees = 5, mtry = 3) |>
  set_mode("regression") |>
  set_engine("xgboost") |>
  fit(mpg ~ ., data = mtcars[1:25, ])

mod
#> parsnip model object
#> 
#> ##### xgb.Booster
#> call:
#>   xgboost::xgb.train(params = list(eta = 0.3, max_depth = 6, gamma = 0, 
#>     colsample_bytree = 1, colsample_bynode = 0.3, min_child_weight = 1, 
#>     subsample = 1, nthread = 1, objective = "reg:squarederror"), 
#>     data = x$data, nrounds = 5, evals = x$watchlist, verbose = 0)
#> # of features: 10 
#> # of rounds:  5 
#> callbacks:
#>    evaluation_log 
#> evaluation_log:
#>   iter training_rmse
#>  <int>         <num>
#>      1      4.655552
#>      2      3.648086
#>      3      2.877980
#>      4      2.302021
#>      5      1.850090
```

Note that simply saving and loading the model results in changes to the
fitted model:

``` r
temp_file <- tempfile()
saveRDS(mod, temp_file)
mod2 <- readRDS(temp_file)

compare(mod, mod2, ignore_formula_env = TRUE)
#> `old$fit$ptr` is <pointer: 0x11a0cf990>
#> `new$fit$ptr` is <pointer: 0x10bed38a0>
```

Saving and reloading `mod2` didn’t preserve XGBoost’s reference to its
`pointer`, which may result in failures later in the modeling process.

We thus need to prepare the fitted model to be saved before passing it
to another R session. We can do so by bundling it:

``` r
# bundle the model
bundled_mod <-
  bundle(mod)

bundled_mod
#> bundled model_fit object.
```

Passing the model to another R session and generating predictions on new
data:

``` r
# load the model in a fresh R session and predict on new data
r(
  func = function(bundled_mod) {
    library(bundle)
    library(parsnip)

    unbundled_mod <-
      unbundle(bundled_mod)

    predict(unbundled_mod, new_data = mtcars[26:32, ])
  },
  args = list(
    bundled_mod = bundled_mod
  )
)
#> # A tibble: 7 × 1
#>   .pred
#>   <dbl>
#> 1  28.6
#> 2  25.8
#> 3  25.8
#> 4  16.7
#> 5  20.2
#> 6  15.3
#> 7  21.2
```

For a more in-depth demonstration of the package, see the [main
vignette](https://rstudio.github.io/bundle/articles/bundle.html) with
`vignette("bundle")`.

## Contributing

This project is released with a [Contributor Code of
Conduct](https://contributor-covenant.org/version/2/0/CODE_OF_CONDUCT.html).
By contributing to this project, you agree to abide by its terms.

- For questions and discussions about our packages, modeling, and
  machine learning, please [post on RStudio
  Community](https://forum.posit.co/new-topic?category_id=15&tags=question).

- If you think you have encountered a bug, please [submit an
  issue](https://github.com/rstudio/bundle/issues).

- Either way, learn how to create and share a
  [reprex](https://reprex.tidyverse.org/articles/articles/learn-reprex.html)
  (a minimal, reproducible example), to clearly communicate about your
  code.
