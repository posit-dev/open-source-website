
# shinymodels

<!-- badges: start -->

[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
[![CRAN
status](https://www.r-pkg.org/badges/version/shinymodels)](https://CRAN.R-project.org/package=shinymodels)
[![Codecov test
coverage](https://codecov.io/gh/tidymodels/shinymodels/branch/main/graph/badge.svg)](https://app.codecov.io/gh/tidymodels/shinymodels?branch=main)
[![R-CMD-check](https://github.com/tidymodels/shinymodels/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/tidymodels/shinymodels/actions/workflows/R-CMD-check.yaml)
[![R-CMD-check-no-suggests](https://github.com/tidymodels/shinymodels/actions/workflows/R-CMD-check-no-suggests.yaml/badge.svg)](https://github.com/tidymodels/shinymodels/actions/workflows/R-CMD-check-no-suggests.yaml)
<!-- badges: end -->

The goal of shinymodels is to launch a Shiny app given tidymodels’
tuning or resampling results, to make it easier to explore the modeling
results.

## Installation

You can install the released version of shinymodels from
[CRAN](https://CRAN.R-project.org) with:

``` r
install.packages("shinymodels") 
```

And the development version from [GitHub](https://github.com/) with:

``` r
# install.packages("pak")
pak::pak("tidymodels/shinymodels")
```

## Example

Start by tuning or fitting to resampling folds, using tune functions
like `fit_resamples()` or `tune_bayes()`.

As an example, we will simulate a simple relationship:

``` r
library(shinymodels)
library(tidymodels)
tidymodels_prefer()

set.seed(1)
n <- 100
simulated <-
  data.frame(x1 = runif(n, min = -1), x2 = runif(n)) %>% 
  mutate(y = 3 - 5 * x1 + 15 * x1^2 +  + 10 * x2 + rnorm(n, sd = 5))
```

Let’s resample a linear regression model that is missing an important
nonlinear term (i.e., `poly(x1, 2)`):

``` r
set.seed(2)
folds <- vfold_cv(simulated)

reg_res <-
  linear_reg() %>%
  fit_resamples(y ~ .,
                resamples = folds,
                control = control_resamples(save_pred = TRUE))
```

To interactively assess the model fit, we can use the `explore()`
function:

``` r
explore(reg_res)
```

Use the Shiny app to explore the model results and detect any outliers
or problematic observations. In the image below, the observed and
predicted values are visualized, with one sample selected and
highlighted. The residuals are also plotted against `x1` and the
quadratic pattern shows that a nonlinear term should be added.

![screenshot of shiny app. Options are shown in a column to the left. In
the main area 3 tabs are shown; Observed vs. Predicted, Residuals
vs. Predicted, and Residals vs. A numeric
predictor.](man/figures/example.png)

The `explore()` function can be used with objects produced by
`fit_resamples()`, `last_fit()`, or any of the `tune_*()` functions.

## Contributing

This project is released with a [Contributor Code of
Conduct](https://contributor-covenant.org/version/2/0/CODE_OF_CONDUCT.html).
By contributing to this project, you agree to abide by its terms.

- For questions and discussions about tidymodels packages, modeling, and
  machine learning, please [post on RStudio
  Community](https://community.rstudio.com/new-topic?category_id=15&tags=tidymodels,question).

- If you think you have encountered a bug, please [submit an
  issue](https://github.com/tidymodels/shinymodels/issues).

- Either way, learn how to create and share a
  [reprex](https://reprex.tidyverse.org/articles/articles/learn-reprex.html)
  (a minimal, reproducible example), to clearly communicate about your
  code.

- Check out further details on [contributing guidelines for tidymodels
  packages](https://www.tidymodels.org/contribute/) and [how to get
  help](https://www.tidymodels.org/help/).
