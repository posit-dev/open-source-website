
<!-- README.md is generated from README.Rmd. Please edit that file -->

# discrim <a href="https://discrim.tidymodels.org/"><img src="man/figures/logo.png" align="right" height="138" alt="discrim website" /></a>

<!-- badges: start -->

[![CRAN
status](https://www.r-pkg.org/badges/version/discrim)](https://cran.r-project.org/package=discrim)
[![Codecov test
coverage](https://codecov.io/gh/tidymodels/discrim/branch/main/graph/badge.svg)](https://app.codecov.io/gh/tidymodels/discrim?branch=main)
[![R-CMD-check](https://github.com/tidymodels/discrim/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/tidymodels/discrim/actions/workflows/R-CMD-check.yaml)
[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html)
[![Codecov test
coverage](https://codecov.io/gh/tidymodels/discrim/graph/badge.svg)](https://app.codecov.io/gh/tidymodels/discrim)
<!-- badges: end -->

`discrim` contains simple bindings to enable the `parsnip` package to
fit various discriminant analysis models, such as

- Linear discriminant analysis (LDA, simple and regularized)
- Quadratic discriminant analysis (QDA, simple and regularized)
- Regularized discriminant analysis (RDA, via [Friedman
  (1989)](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C7&q=%22Regularized+Discriminant+Analysis%22&btnG=))
- Flexible discriminant analysis (FDA) using MARS features
- Naive Bayes models

## Installation

You can install the released version of discrim from
[CRAN](https://CRAN.R-project.org) with:

``` r
install.packages("discrim")
```

And the development version from [GitHub](https://github.com/) with:

``` r
# install.packages("pak")
pak::pak("tidymodels/discrim")
```

## Available Engines

The discrim package provides engines for the models in the following
table.

| model               | engine        | mode           |
|:--------------------|:--------------|:---------------|
| discrim_flexible    | earth         | classification |
| discrim_linear      | MASS          | classification |
| discrim_linear      | mda           | classification |
| discrim_linear      | sda           | classification |
| discrim_linear      | sparsediscrim | classification |
| discrim_quad        | MASS          | classification |
| discrim_quad        | sparsediscrim | classification |
| discrim_regularized | klaR          | classification |
| naive_Bayes         | klaR          | classification |
| naive_Bayes         | naivebayes    | classification |

## Example

Here is a simple model using a simulated two-class data set contained in
the package:

``` r
library(discrim)

parabolic_grid <-
  expand.grid(X1 = seq(-5, 5, length = 100),
              X2 = seq(-5, 5, length = 100))

fda_mod <-
  discrim_flexible(num_terms = 3) |>
  # increase `num_terms` to find smoother boundaries
  set_engine("earth") |>
  fit(class ~ ., data = parabolic)

parabolic_grid$fda <-
  predict(fda_mod, parabolic_grid, type = "prob")$.pred_Class1

library(ggplot2)
ggplot(parabolic, aes(x = X1, y = X2)) +
  geom_point(aes(col = class), alpha = .5) +
  geom_contour(data = parabolic_grid, aes(z = fda), col = "black", breaks = .5) +
  theme_bw() +
  theme(legend.position = "top") +
  coord_equal()
```

<img src="man/figures/README-example-1.png" alt="Scatter chart. X1 along the x-axis, X2 along the y-axis. points are scattered, with a trend between X1 and X2. Most of the middle points are colored and labeled Class2, with the remaining points labeled Class1. Two connected straight lines, doing its best to separate the two classes." width="100%" />

## Contributing

This project is released with a [Contributor Code of
Conduct](https://contributor-covenant.org/version/2/1/CODE_OF_CONDUCT.html).
By contributing to this project, you agree to abide by its terms.

- For questions and discussions about tidymodels packages, modeling, and
  machine learning, please [post on RStudio
  Community](https://forum.posit.co/new-topic?category_id=15&tags=tidymodels,question).

- If you think you have encountered a bug, please [submit an
  issue](https://github.com/tidymodels/discrim/issues).

- Either way, learn how to create and share a
  [reprex](https://reprex.tidyverse.org/articles/articles/learn-reprex.html)
  (a minimal, reproducible example), to clearly communicate about your
  code.

- Check out further details on [contributing guidelines for tidymodels
  packages](https://www.tidymodels.org/contribute/) and [how to get
  help](https://www.tidymodels.org/help/).
