
<!-- README.md is generated from README.Rmd. Please edit that file -->

# sparkxgb

<!-- badges: start -->

[![R-CMD-check](https://github.com/rstudio/sparkxgb/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/rstudio/sparkxgb/actions/workflows/R-CMD-check.yaml)
[![Spark
Tests](https://github.com/rstudio/sparkxgb/actions/workflows/Tests.yaml/badge.svg)](https://github.com/rstudio/sparkxgb/actions/workflows/Tests.yaml)
[![Codecov test
coverage](https://codecov.io/gh/rstudio/sparkxgb/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rstudio/sparkxgb?branch=main)
[![CRAN
status](https://www.r-pkg.org/badges/version/sparkxgb)](https://CRAN.R-project.org/package=sparkxgb)
<!-- badges: end -->

## Overview

**sparkxgb** is a [sparklyr](https://spark.posit.co/) extension that
provides an interface to [XGBoost](https://github.com/dmlc/xgboost) on
Spark.

## Installation

``` r
install.packages("sparkxgb")
```

### Development version

You can install the development version of `sparkxgb` with:

``` r
# install.packages("pak")
pak::pak("rstudio/sparkxgb")
```

## Example

**sparkxgb** supports the familiar formula interface for specifying
models:

``` r
library(sparkxgb)
library(sparklyr)
library(dplyr)

sc <- spark_connect(master = "local")
iris_tbl <- sdf_copy_to(sc, iris)

xgb_model <- xgboost_classifier(
  iris_tbl,
  Species ~ .,
  num_class = 3,
  num_round = 50,
  max_depth = 4
)

xgb_model %>%
  ml_predict(iris_tbl) %>%
  select(Species, predicted_label, starts_with("probability_")) %>%
  glimpse()
#> Rows: ??
#> Columns: 5
#> Database: spark_connection
#> $ Species                <chr> "setosa", "setosa", "setosa", "setosa", "setosa…
#> $ predicted_label        <chr> "setosa", "setosa", "setosa", "setosa", "setosa…
#> $ probability_setosa     <dbl> 0.9971547, 0.9948581, 0.9968392, 0.9968392, 0.9…
#> $ probability_versicolor <dbl> 0.002097376, 0.003301427, 0.002284616, 0.002284…
#> $ probability_virginica  <dbl> 0.0007479066, 0.0018403779, 0.0008762418, 0.000…
```

It also provides a Pipelines API, which means you can use a
`xgboost_classifier` or `xgboost_regressor` in a pipeline as any
`Estimator`, and do things like hyperparameter tuning:

``` r
pipeline <- ml_pipeline(sc) %>%
  ft_r_formula(Species ~ .) %>%
  xgboost_classifier(num_class = 3)

param_grid <- list(
  xgboost = list(
    max_depth = c(1, 5),
    num_round = c(10, 50)
  )
)

cv <- ml_cross_validator(
  sc,
  estimator = pipeline,
  evaluator = ml_multiclass_classification_evaluator(
    sc,
    label_col = "label",
    raw_prediction_col = "rawPrediction"
  ),
  estimator_param_maps = param_grid
)

cv_model <- cv %>%
  ml_fit(iris_tbl)

summary(cv_model)
#> Summary for CrossValidatorModel 
#>             <cross_validator__13c346ec_bc09_4b8a_952d_92f9711299d7> 
#> 
#> Tuned Pipeline
#>   with metric f1
#>   over 4 hyperparameter sets 
#>   via 3-fold cross validation
#> 
#> Estimator: Pipeline
#>            <pipeline__bf0a05c1_6f0e_4875_ac1a_c77fbd6635f3> 
#> Evaluator: MulticlassClassificationEvaluator
#>            <multiclass_classification_evaluator__387ea4db_61da_45cb_813e_8c6f63811fff> 
#> 
#> Results Summary: 
#>          f1 max_depth_1 num_round_1
#> 1 0.9134404           1          10
#> 2 0.8993533           5          10
#> 3 0.9064859           1          50
#> 4 0.9064859           5          50

spark_disconnect(sc)
```
