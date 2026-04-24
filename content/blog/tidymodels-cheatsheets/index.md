---
title: "tidymodels Cheatsheets"
date: 2026-04-24
people:
  - Edgar Ruiz
description: >
  Two new cheatsheets for tidymodels are now available: one for creating models
  with parsnip, and one for preprocessing data with recipes.
image: "tidymodels-cheatsheets.png"
image-alt: ""
topics:
  - Machine Learning
software:
  - tidymodels
languages:
  - R
resources:
  - cheatsheets
tags:
  -
source: tidyverse
nohero: false
hidesubscription: false
---



Until recently, [tidymodels](https://www.tidymodels.org/) had not had a cheatsheet in its almost 8-year history. The first one, released earlier this year, focuses on [data preprocessing using `recipes`](/resources/cheatsheets/ml-preprocessing-data/). Today, we are excited to announce a second cheatsheet, this one focusing on [modeling using the `parsnip` package](/resources/cheatsheets/ml-create-models/).

In this post we'll review the content and composition of the new cheatsheets, starting with the newest one.

## Create Models with **parsnip**

The cheatsheet is organized into three main parts: an introduction to parsnip's basics, a catalog of all models available through the package, and an overview of operations for fitting and working with models.

### Basics

This section introduces the three building blocks of every parsnip model specification. The **model type** is the function that defines what kind of model to use, such as `rand_forest()` or `linear_reg()`. The **mode** determines how the model will be used, either `"regression"` or `"classification"`. Finally, the **engine** is the package or system that will execute the training, set via `set_engine()`.

### Model catalog

The largest section of the cheatsheet catalogs all models available through parsnip, grouped by use case:

- **Classification only:** `logistic_reg()`, `multinom_reg()`, `naive_Bayes()`, `ordinal_reg()`
- **Regression only:** `linear_reg()`, `poisson_reg()`
- **General use** (both modes): `decision_tree()`, `nearest_neighbor()`, `mlp()`, `mars()`
- **Discriminant analysis:** `discrim_linear()`, `discrim_quad()`, `discrim_flexible()`, `discrim_regularized()`
- **Ensemble methods:** `rand_forest()`, `boost_tree()`, `bag_tree()`, `bart()`
- **Support Vector Machines:** `svm_linear()`, `svm_poly()`, `svm_rbf()`
- **Feature rules:** `rule_fit()`, `C5_rules()`, `cubist_rules()`
- **Survival models:** `proportional_hazards()`, `survival_reg()`

One design choice in particular makes this section much easier to navigate: **pills**. Each model's compatible engines and supported modes are shown as small, visually distinct tags, so you can see at a glance which mode a given engine supports, without having to read through the description text. Each mode is encoded in the pill with a number: Classification (1), Regression (2), Censored Regression (3), and Quantile Regression (4). A legend mapping each number to its mode is available at the top of page one.

And true to the R cheatsheet tradition, individual models or groups of related models are paired with **small, charming illustrations**, a staple of the format that gives you a visual anchor to help you find a model family again later. Each illustration is carefully thought out to be as representative and memorable as possible, making them genuinely useful rather than purely decorative. Handy when you have a vague memory of "that tree-based ensemble that used Bayesian analysis" and need to scan quickly.

### Operations

The last section covers the practical workflow of fitting and using a model:

- Methods for training and generating predictions, such as `fit()` and `predict()`
- Tidiers for extracting results in a tidy format, such as `tidy()`, `glance()`, and `augment()`
- Extract helpers for pulling engine-specific objects out of a fit, such as `extract_fit_engine()` and `extract_spec_parsnip()`

Each function is paired with a **quick runnable example**, so you can see exactly what the call looks like in practice. Notably, the examples build on each other, starting from the two lines of code right below the section title, making it easy to follow the full workflow from model specification to results.

## Preprocessing Data with **recipes**

After a quick Basics section covering the core workflow, the vast majority of the cheatsheet is dedicated to `step_*()` functions, the building blocks of any recipe. It finishes with an overview of role and type variable management.

### Step catalog

The step functions are listed with their arguments and a short description. The steps are organized into groups based on what they do:

- **Filters:** steps for removing variables that are sparse, zero-variance, linearly dependent, highly correlated, or missing too many values
- **In-place Transformations:** basis functions (splines, polynomials), discretization, and normalization steps
- **Imputation:** a range of `step_impute_*()` strategies, from mean and median substitution to model-based approaches using bagged trees or k-nearest neighbors
- **Encodings:** type converters (e.g. factor to string, numeric to factor), value converters, and other factor-handling steps
- **Dummy Variables:** one-hot and binary encoding, text pattern matching, and conversion helpers
- **Multivariate Transformations:** signal extraction (PCA, ICA, PLS, and friends) and centroid-based distance measures
- **Date & Time:** steps for converting date and datetime columns into usable numeric or factor features
- **Row operations:** sampling, shuffling, slicing, and removing rows with missing values
- **Other:** interaction terms, renaming, rolling window statistics, geographic distances, and ratios

As with the parsnip cheatsheet, each group of steps is paired with **small, carefully thought out illustrations** to help you visually locate a step family when scanning.

### Role & type

The last section focuses on the selection and management of variable roles and types within the recipe. The selection side covers ways to target variables by their role (outcome, predictor, or any custom role) as well as by their type (numeric, factor, logical, and so on), including a handy set of convenience selectors for the most common combinations. The management side covers functions for adding, updating, and removing roles, showing you how to gain fine-grained control over how each variable participates in the recipe.

