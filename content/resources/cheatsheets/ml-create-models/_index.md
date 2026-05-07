---
title: Create models with parsnip
image: page-1.png
resource_type: cheatsheet
date: '2026-04-09'
description: Quick reference guide for create models with parsnip.
download_url: ml-create-models.pdf
software:
- parsnip
languages:
- R
people:
- Edgar Ruiz
thumbnails:
- page-1.png
- page-2.png
---

## Basics

`parsnip` provides a tidy, unified interface to a range of models from other packages. It helps avoid having to remember how to properly call the modeling functions of those external packages.

A `parsnip` specification is made up of 3 main components:

1.  The type of model to be used, such as Random Forest (`rand_forest()`) or linear regression (`linear_reg()`)

2.  How will the model be used, or mode. The two most common are "regression" and "classification".

3.  The computational engine, or program that will actually execute the training. It could be an external R package, such as ranger, or even an engine outside of R, such as Stan or Apache Spark.

```r
library(tidymodels)

rand_forest(mtry = 10, trees = 2000) |> # Define type of model
  set_engine("ranger", importance = "impurity") |> # Select an engine
  set_mode("regression") # Set the mode
```

-   `set_engine(object, engine, ...)` - Specifies which package or system will be used to fit the model, along with any arguments specific to that software.

-   `set_args(object, ...)` - Modifies the arguments of a model specification.

-   `set_mode(object, mode, …)` - Changes the model's mode.

-   `show_engines(x)` - The possible engines for a model can depend on what packages are loaded. Some parsnip extension add engines to existing models.

```r
show_engines("linear_reg")
```

## Legends

### Mode Support Numbers

-   **1** - Classification
-   **2** - Regression
-   **3** - Censored Regression
-   **4** - Quantile Regression

### Engine Tags

Engine tags show the engine name and mode support numbers. For example, <span class="pill" style="text-transform: none">h2o 1, 2</span> means engine `h2o` supports classification (1) and regression (2).

## Classification Only

-   `logistic_reg(mode = "classification", engine = "glm", penalty, mixture)` - Generalized linear model for binary outcomes. A linear combination of the predictors is used to model the log odds of an event.

    <span class="pill" style="text-transform: none">brulee 1</span> <span class="pill" style="text-transform: none">gee 1</span> <span class="pill" style="text-transform: none">glm 1</span> <span class="pill" style="text-transform: none">glmer 1</span> <span class="pill" style="text-transform: none">glmnet 1</span> <span class="pill" style="text-transform: none">h2o 1</span> <span class="pill" style="text-transform: none">keras 1</span> <span class="pill" style="text-transform: none">LiblineaR 1</span> <span class="pill" style="text-transform: none">spark 1</span> <span class="pill" style="text-transform: none">stan 1</span> <span class="pill" style="text-transform: none">stan_glmer 1</span>

-   `multinom_reg(mode = "classification", engine = "nnet", penalty, mixture)` - Uses linear predictors to predict multiclass data using the multinomial distribution.

    <span class="pill" style="text-transform: none">brulee 1</span> <span class="pill" style="text-transform: none">glmnet 1</span> <span class="pill" style="text-transform: none">h2o 1</span> <span class="pill" style="text-transform: none">keras 1</span> <span class="pill" style="text-transform: none">nnet 1</span> <span class="pill" style="text-transform: none">spark 1</span>

-   `naive_Bayes(mode = "classification", smoothness, Laplace, engine = "klaR")` - Uses Bayes' theorem to compute the probability of each class, given the predictor values.

    <span class="pill" style="text-transform: none">h2o 1</span> <span class="pill" style="text-transform: none">klaR 1</span> <span class="pill" style="text-transform: none">naivebayes 1</span>

-   `null_model(mode = "classification", engine = "parsnip")` - Fit a single mean or largest class model. This is the user-facing function for the null_model() specification.

    <span class="pill" style="text-transform: none">parsnip 1</span>

-   `ordinal_reg(mode = "classification", ordinal_link, odds_link, penalty, mixture, engine = "polr")` - Defines a generalized linear model that predicts an ordinal outcome.

    <span class="pill" style="text-transform: none">rpartScore 1</span> <span class="pill" style="text-transform: none">polr 1</span> <span class="pill" style="text-transform: none">vgam 1</span> <span class="pill" style="text-transform: none">vglm 1</span>

## Regression Only

-   `linear_reg(mode = "regression", engine = "lm", penalty, mixture)` - Defines a model that can predict numeric values from predictors using a linear function.

    <span class="pill" style="text-transform: none">brulee 2</span> <span class="pill" style="text-transform: none">gee 2</span> <span class="pill" style="text-transform: none">glm 2</span> <span class="pill" style="text-transform: none">glmer 2</span> <span class="pill" style="text-transform: none">glmnet 2</span> <span class="pill" style="text-transform: none">gls 2</span> <span class="pill" style="text-transform: none">h2o 2</span> <span class="pill" style="text-transform: none">keras 2</span> <span class="pill" style="text-transform: none">lm 2</span> <span class="pill" style="text-transform: none">lme 2</span> <span class="pill" style="text-transform: none">quantreg 2</span> <span class="pill" style="text-transform: none">spark 2</span> <span class="pill" style="text-transform: none">stan 2</span> <span class="pill" style="text-transform: none">stan_glmer 2</span>

-   `poisson_reg(mode = "regression", penalty, mixture, engine = "glm")` - Defines a generalized linear model for count data that follow a Poisson distribution.

    <span class="pill" style="text-transform: none">gee 2</span> <span class="pill" style="text-transform: none">glm 2</span> <span class="pill" style="text-transform: none">glmer 2</span> <span class="pill" style="text-transform: none">glmnet 2</span> <span class="pill" style="text-transform: none">h2o 2</span> <span class="pill" style="text-transform: none">hurdle 2</span> <span class="pill" style="text-transform: none">stan 2</span> <span class="pill" style="text-transform: none">stan_glmer 2</span> <span class="pill" style="text-transform: none">zeroinfl 2</span>

## General Use

-   `decision_tree(mode, engine = "rpart", cost_complexity, tree_depth, min_n)` - A set of if/then statements creates a tree-based structure.

    <span class="pill" style="text-transform: none">partykit 1, 2, 3</span> <span class="pill" style="text-transform: none">rpart 1, 2, 3</span> <span class="pill" style="text-transform: none">spark 1, 2</span> <span class="pill" style="text-transform: none">C5.0 1</span>

-   `mars(mode, engine = "earth", num_terms, prod_degree, prune_method)` - Uses artificial features for some predictors. These features resemble hinge functions and the result is a model that is a segmented regression in small dimensions.

    <span class="pill" style="text-transform: none">earth 1, 2</span>

-   `mlp(mode, engine = "nnet", hidden_units, penalty, dropout, epochs, activation, learn_rate)` - Defines a multilayer perceptron model (a.k.a. a single layer, feed-forward neural network).

    <span class="pill" style="text-transform: none">nnet 1, 2</span> <span class="pill" style="text-transform: none">brulee 1, 2</span> <span class="pill" style="text-transform: none">brulee_two_layer 1, 2</span> <span class="pill" style="text-transform: none">keras 1, 2</span> <span class="pill" style="text-transform: none">grnn 1, 2</span>

-   `gen_additive_mod(mode, select_features, adjust_deg_free, engine = "mgcv")` - Uses smoothed functions of numeric predictors in a generalized linear model.

    <span class="pill" style="text-transform: none">mgcv 1, 2</span>

-   `nearest_neighbor(mode, engine = "kknn", neighbors, weight_func, dist_power)` - Uses the K most similar data points from the training set to predict new samples.

    <span class="pill" style="text-transform: none">kknn 1, 2</span>

-   `pls(mode, predictor_prop, num_comp, engine = "mixOmics")` - Uses latent variables to model the data. Similar to a supervised version of PCA.

    <span class="pill" style="text-transform: none">mixOmics 1, 2</span>

## Discriminant

-   `discrim_flexible(mode = "classification", num_terms, prod_degree, prune_method, engine = "earth")` - Fits a discriminant analysis model that uses nonlinear features created using MARS.

    <span class="pill" style="text-transform: none">earth 1</span>

-   `discrim_regularized(mode = "classification", frac_common_cov, frac_identity, engine = "klaR")` - Estimates a multivariate distribution for the predictors separately for the data in each class. The model's structure can be LDA, QDA, or a combination. Each probability class is computed using Bayes's theorem, given the predictor values.

    <span class="pill" style="text-transform: none">klaR 1</span>

Estimates a multivariate distribution for the predictors separately for the data in each class using a method described below. Each class' probability is computed using Bayes' theorem, given the predictor values.

-   `discrim_linear(mode = "classification", regularization_method, engine = "MASS", penalty)` - Uses Gaussian with a common covariance matrix to perform the estimate.

    <span class="pill" style="text-transform: none">MASS 1</span> <span class="pill" style="text-transform: none">mda 1</span> <span class="pill" style="text-transform: none">sda 1</span> <span class="pill" style="text-transform: none">sparsediscrim 1</span>

-   `discrim_quad(mode = "classification", regularization_method, engine = "MASS")` - Uses Gaussian with separate covariance matrices to perform the estimate.

    <span class="pill" style="text-transform: none">MASS 1</span> <span class="pill" style="text-transform: none">sparsediscrim 1</span>

## Support Vector Machine

**Classification:** Maximizes the width of the margin between classes using a method described below.

**Regression:** Optimizes a robust loss function only affected by very large model residuals and uses an additional method described below.

-   `svm_linear(mode, cost, engine = "LiblineaR", margin)` - Classification: A linear class boundary. Regression: Uses a linear fit.

    <span class="pill" style="text-transform: none">kernlab 1, 2</span> <span class="pill" style="text-transform: none">LiblineaR 1, 2</span>

-   `svm_poly(mode, cost, engine = "kernlab", degree, scale_factor)` - Classification: A polynomial class boundary. Regression: Uses polynomial functions of the predictors.

    <span class="pill" style="text-transform: none">kernlab 1, 2</span>

-   `svm_rbf(mode, cost, engine = "kernlab", rbf_sigma)` - Classification: A nonlinear class boundary. Regression: Uses nonlinear functions of the predictors.

    <span class="pill" style="text-transform: none">kernlab 1, 2</span>

## Feature Rules

-   `rule_fit(mode, mtry, trees, min_n, tree_depth, learn_rate, loss_reduction, sample_size, stop_iter, penalty, engine = "xrf")` - Derives simple feature rules from a tree ensemble and uses them as features in a regularized model.

    <span class="pill" style="text-transform: none">xrf 1, 2</span> <span class="pill" style="text-transform: none">h2o 1</span>

-   `C5_rules(mode = "classification", trees, min_n, engine = "C5.0")` - Derives feature rules from a tree for prediction. A single tree or boosted ensemble can be used.

    <span class="pill" style="text-transform: none">C5.0 1</span>

-   `cubist_rules(mode = "regression", committees, neighbors, max_rules, engine = "Cubist")` - Derives simple feature rules from a tree ensemble and creates regression models within each rule.

    <span class="pill" style="text-transform: none">Cubist 2</span>

## Ensemble

*"E Pluribus Unum"*

-   `bag_mars(mode, num_terms, prod_degree, prune_method, engine = "earth")` - Ensemble of generalized linear models that use artificial features for some predictors. These features resemble hinge functions and the result is a model that is a segmented regression in small dimensions.

    <span class="pill" style="text-transform: none">earth 1, 2</span>

-   `bag_mlp(mode, hidden_units, penalty, epochs, engine = "nnet")` - An ensemble of single layer, feed-forward neural networks.

    <span class="pill" style="text-transform: none">nnet 1, 2</span>

-   `bag_tree(mode, cost_complexity = 0, tree_depth, min_n = 2, class_cost, engine = "rpart")` - Ensemble of decision trees.

    <span class="pill" style="text-transform: none">C5.0 1</span> <span class="pill" style="text-transform: none">rpart 1, 2, 3</span>

-   `bart(mode, engine = "dbarts", trees, prior_terminal_node_coef, prior_terminal_node_expo, prior_outcome_range)` - Tree ensemble model that uses Bayesian analysis to assemble the ensemble.

    <span class="pill" style="text-transform: none">dbarts 1, 2</span>

-   `boost_tree(mode, engine = "xgboost", mtry, trees, min_n, tree_depth, learn_rate, loss_reduction, sample_size, stop_iter)` - Creates a series of decision trees forming an ensemble. Each tree depends on the results of previous trees. All trees in the ensemble are combined to produce a final prediction.

    <span class="pill" style="text-transform: none">C5.0 1</span> <span class="pill" style="text-transform: none">catboost 1, 2</span> <span class="pill" style="text-transform: none">h2o 1, 2</span> <span class="pill" style="text-transform: none">lightgbm 1, 2</span> <span class="pill" style="text-transform: none">mboost 3</span> <span class="pill" style="text-transform: none">spark 1, 2</span> <span class="pill" style="text-transform: none">xgboost 1, 2, 4</span>

-   `rand_forest(mode, engine = "ranger", mtry, trees, min_n)` - Creates a large number of decision trees, each independent of the others. The final prediction uses all predictions from the individual trees and combines them.

    <span class="pill" style="text-transform: none">aorsf 1, 2, 3</span> <span class="pill" style="text-transform: none">grf 1, 2, 4</span> <span class="pill" style="text-transform: none">h2o 1, 2</span> <span class="pill" style="text-transform: none">partykit 1, 2, 3</span> <span class="pill" style="text-transform: none">randomForest 1, 2</span> <span class="pill" style="text-transform: none">ranger 1, 2</span> <span class="pill" style="text-transform: none">spark 1, 2</span>

## Survival

-   `proportional_hazards(mode = "censored regression", engine = "survival", penalty, mixture)` - Defines a model for the hazard function as a multiplicative function of covariates times a baseline hazard.

    <span class="pill" style="text-transform: none">glmnet 3</span> <span class="pill" style="text-transform: none">survival 3</span>

-   `survival_reg(mode = "censored regression", engine = "survival", dist)` - Defines a parametric survival model.

    <span class="pill" style="text-transform: none">flexsurv 3</span> <span class="pill" style="text-transform: none">flexsurvspline 3</span> <span class="pill" style="text-transform: none">survival 3</span>

## Operations

```r
library(tidymodels)

lm_spec <- linear_reg() |>
  set_engine("lm")

lm_spec
```

### Methods

-   `fit(object, ...)` - Estimates parameters for a given model from a set of data.

    ```r
    lm_fit <- fit(lm_spec, mpg ~ ., data = mtcars)

    lm_fit
    ```

-   `predict(object, ...)`

    ```r
    predict(lm_fit, mtcars)
    ```

-   `autoplot(object, ...)` - Uses ggplot2 to draw a particular plot for an object of a particular class.

-   `update(object, ...)` - Updates and (by default) re-fits a model. It does this by extracting the call stored in the object, updating the call and evaluating that call.

### Tidiers

-   `augment(x, ...)` - Augment data with model results.

    ```r
    augment(lm_fit, mtcars)
    ```

-   `glance(x, ...)` - Construct a single row summary "glance" of a model fit.

    ```r
    glance(lm_fit)
    ```

-   `tidy(x, ...)` - Turn an object into a tidy tibble.

    ```r
    tidy(lm_fit)
    ```

### General

-   `repair_call(x, data)` - When the user passes a formula to fit() and the underlying model function uses a formula, the call object produced by fit() may not be usable by other functions.

-   `control_parsnip(verbosity = 1L, catch = FALSE)` - Pass options to the fit.model_spec() function to control its output and computations.

    ```r
    control_parsnip(verbosity = 2)
    ```

-   `show_engines(x)` - The possible engines for a model can depend on what packages are loaded. Some parsnip extension add engines to existing models.

    ```r
    show_engines("linear_reg")
    ```

-   `translate(x, ...)` - Translates a model specification into a code object that is specific to a particular engine (e.g. R package). It translates generic parameters to their counterparts.

    ```r
    translate(lm_spec)
    ```

-   `multi_predict(object, ...)` - For some models, predictions can be made on sub-models in the model object.

### Extract

-   `extract_spec_parsnip(x, ...)` - Returns a parsnip model specification.

    ```r
    extract_spec_parsnip(lm_fit)
    ```

-   `extract_fit_engine(x, ...)` - Returns the engine specific fit embedded within a parsnip model fit. For example, when using linear_reg() with the "lm" engine, this returns the underlying lm object.

    ```r
    extract_fit_engine(lm_fit)
    ```

-   `extract_parameter_dials(x, parameter, ...)` - Returns a single dials parameter object.

-   `extract_parameter_set_dials(x, ...)` - Returns a set of dials parameter objects.

-   `extract_fit_time(x, summarize = TRUE, ...)` - Returns a tibble with fit times. The fit times correspond to the time for the parsnip engine to fit and do not include other portions of the elapsed time in fit.model_spec().
