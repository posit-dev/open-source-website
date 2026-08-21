---
title: Machine learning with tidymodels
image: page-1.png
resource_type: cheatsheet
date: '2026-08-03'
description: A map of the tidymodels packages, grouped by where each one fits in the
  machine learning workflow.
download_url: ml-tidymodels.pdf
software:
- tidymodels
languages:
- R
people:
- Edgar Ruiz
thumbnails:
- page-1.png
- page-2.png
---

## Intro

`tidymodels` is a collection of R packages for modeling and machine learning that share a common design and grammar. Unlike most cheatsheets, which cover the functions of a single package, this cheatsheet maps the packages themselves, grouping each by where it fits in the machine learning workflow.

The workflow runs from **Resampling** to **Pre-processing**, **Modeling**, **Post-processing**, and **Measuring**. **Orchestrating** spans pre-processing through post-processing, feeds into **Tuning**, and leads to **Deploy**.

## Resampling

Split and resample data for honest evaluation.

-   [rsample](https://rsample.tidymodels.org) - Create and manage resampling sets such as cross-validation, bootstraps, and validation splits.

-   [spatialsample](https://spatialsample.tidymodels.org) - Resample spatial data while respecting geographic structure.

## Pre-processing

Prepare data for modeling.

-   [recipes](https://recipes.tidymodels.org) - The preprocessing framework for building pipeable feature-engineering steps.

-   [embed](https://embed.tidymodels.org) - Recipe steps that encode categorical predictors via target, likelihood, and entity embeddings.

-   [textrecipes](https://textrecipes.tidymodels.org) - Recipe steps that turn text into model-ready features.

-   [themis](https://themis.tidymodels.org) - Recipe steps to rebalance class-imbalanced data with up-sampling, down-sampling, and SMOTE.

-   [filtro](https://filtro.tidymodels.org) - Filter-based supervised feature selection.

## Modeling

Define and fit models through one consistent interface.

### Classification & regression

-   [parsnip](https://parsnip.tidymodels.org) - The core tidy interface every model plugs into, across many engines.

-   [bonsai](https://bonsai.tidymodels.org) - Tree-based engines such as LightGBM and partykit.

-   [baguette](https://baguette.tidymodels.org) - Bagged ensembles of trees and MARS.

-   [rules](https://rules.tidymodels.org) - Rule-based models such as Cubist, C5.0, and RuleFit.

-   [discrim](https://discrim.tidymodels.org) - Discriminant analysis and naive Bayes models.

### Specialized problems

-   [poissonreg](https://poissonreg.tidymodels.org) - Poisson and count-data regression.

-   [censored](https://censored.tidymodels.org) - Survival models for time-to-event outcomes.

-   [multilevelmod](https://multilevelmod.tidymodels.org) - Mixed-effects and hierarchical models.

-   [tidyclust](https://tidyclust.tidymodels.org) - Clustering models under a tidy interface.

-   [plsmod](https://plsmod.tidymodels.org) - Partial least squares and other projection models.

-   [tabby](https://tabby.tidymodels.org) - Tabular deep-learning models; runs with brulee and tabpfn.

-   [agua](https://agua.tidymodels.org) - Interface to h2o models and AutoML.

## Post-processing

Adjust predictions.

-   [probably](https://probably.tidymodels.org) - Tune classification thresholds and handle equivocal zones.

-   [tailor](https://tailor.tidymodels.org) - Post-process predictions through calibration and other sequential adjustments.

## Measuring

Measure model quality.

-   [yardstick](https://yardstick.tidymodels.org) - Measure model performance with tidy metrics.

-   [tidyposterior](https://tidyposterior.tidymodels.org) - Compare models across resamples using Bayesian methods.

## Orchestrating

Tie the pieces together.

-   [workflows](https://workflows.tidymodels.org) - Bundle preprocessing, model, and post-processing into one object.

-   [workflowsets](https://workflowsets.tidymodels.org) - Create and evaluate many workflows at once.

-   [stacks](https://stacks.tidymodels.org) - Build stacked ensembles from tuned models.

## Tuning

Optimize hyperparameters.

-   [tune](https://tune.tidymodels.org) - Run grid and iterative hyperparameter search.

-   [dials](https://dials.tidymodels.org) - Define tuning parameters and build grids. Often called for you by tune.

-   [finetune](https://finetune.tidymodels.org) - Add search strategies such as racing and simulated annealing.

-   [important](https://important.tidymodels.org) - Measure predictor importance.

## Deploy

Put models into production.

### Prepare & serve

-   [vetiver](https://vetiver.tidymodels.org) - Version, deploy, and monitor models in production.

-   [butcher](https://butcher.tidymodels.org) - Strip fitted models down to reduce object size.

-   [applicable](https://applicable.tidymodels.org) - Flag new samples that fall outside the training distribution.

### Run in a database

-   [tidypredict](https://tidypredict.tidymodels.org) - Generate SQL to score models inside a database.

-   [modeldb](https://modeldb.tidymodels.org) - Fit models directly in a database.

-   [orbital](https://orbital.tidymodels.org) - Convert workflows into portable equations that can run in-database.

## Data

Datasets used in documentation, tests, and teaching.

-   [modeldata](https://modeldata.tidymodels.org) - Over 40 example datasets bundled for modeling.

-   [modeldatatoo](https://modeldatatoo.tidymodels.org) - Over half a dozen larger datasets downloaded on demand.

## Deep learning

R packages that implement or wrap tabular deep-learning models.

-   [brulee](https://brulee.tidymodels.org) - Torch-based models, from MLPs to ResNet and SAINT.

-   [tabpfn](https://tabpfn.tidymodels.org) - A pretrained transformer that predicts tabular data with no training.

## Other

### General

-   [broom](https://broom.tidymodels.org) - Convert model objects into tidy tibbles.

-   [infer](https://infer.tidymodels.org) - Run statistical inference and hypothesis tests.

-   [corrr](https://corrr.tidymodels.org) - Explore correlations in a data frame.

### Development

-   [hardhat](https://hardhat.tidymodels.org) - Scaffold new modeling packages.

## The `tidymodels` package

The `tidymodels` package installs and loads a set of packages that are considered important during day-to-day machine learning development.

It loads the following packages from tidymodels:

-   `rsample`
-   `recipes`
-   `parsnip`
-   `yardstick`
-   `tailor`
-   `tune`
-   `dials`
-   `workflows`
-   `workflowsets`
-   `broom`
-   `infer`
-   `modeldata`

It also loads the following packages from the tidyverse:

-   `dplyr`
-   `ggplot2`
-   `purrr`
-   `tidyr`

## Example

A complete workflow: split, engineer features, tune, finalize, and deploy.

```r
library(tidymodels)

# Split data and make CV folds
set.seed(857)

splits <- ames |>
  initial_split(prop = 0.8)
train <- training(splits)
folds <- train |>
  vfold_cv(v = 5)

# Feature engineering in a recipe
rec <- recipe(
  Sale_Price ~ Gr_Liv_Area + Year_Built + Bldg_Type,
  data = train
) |>
  step_log(Gr_Liv_Area, base = 10) |>
  step_dummy(all_nominal_predictors()) |>
  step_normalize(all_numeric_predictors())

# Model with parameters to tune
mod <- decision_tree(
  cost_complexity = tune(),
  tree_depth = tune()
) |>
  set_engine("rpart") |>
  set_mode("regression")

# Bundle into a workflow
wf <- workflow() |>
  add_recipe(rec) |>
  add_model(mod)

# Tune over the folds
res <- wf |>
  tune_grid(
    resamples = folds,
    grid = 10
  )

# Finalize best, refit, test once
best <- res |>
  select_best(metric = "rmse")
final <- wf |>
  finalize_workflow(best) |>
  last_fit(splits)

collect_metrics(final)

# Deploy the fitted workflow
library(vetiver)
library(pins)

v <- final |>
  extract_workflow() |>
  vetiver_model("ames_tree")

board <- board_temp()
vetiver_pin_write(board, v)
```
