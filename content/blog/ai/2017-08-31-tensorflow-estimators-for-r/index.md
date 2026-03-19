---
title: "TensorFlow Estimators"
description: |
  The tfestimators package is an R interface to TensorFlow Estimators, a high-level API that provides implementations of many different model types including linear models and deep neural networks.
date: 2017-08-31
categories:
  - Packages/Releases
author:
  - name: Yuan Tang
    url: https://orcid.org/0000-0001-5243-233X
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com
people:
  - Yuan Tang
image: thumbnail.png
ported_from: ai
port_status: in-progress
software: ["tfestimators", "tensorflow"]
languages: ["R"]
---



The [tfestimators package](https://tensorflow.rstudio.com/tfestimators) is an R interface to TensorFlow Estimators, a high-level API that provides implementations of many different model types including linear models and deep neural networks.

More models are coming soon such as state saving recurrent neural networks, dynamic recurrent neural networks, support vector machines, random forest, KMeans clustering, etc. TensorFlow estimators also provides a flexible framework for defining arbitrary new model types as custom estimators.

The framework balances the competing demands for flexibility and simplicity by offering APIs at different levels of abstraction, making common model architectures available out of the box, while providing a library of utilities designed to speed up experimentation with model architectures.

These abstractions guide developers to write models in ways conducive to productionization as well as making it possible to write downstream infrastructure for distributed training or parameter tuning independent of the model implementation.

To make out of the box models flexible and usable across a wide range of problems, **tfestimators** provides canned Estimators that are are parameterized not only over traditional hyperparameters, but also using feature columns, a declarative specification describing how to interpret input data.

For more details on the architecture and design of TensorFlow Estimators, please check out the [KDD'17](http://www.kdd.org/kdd2017/) paper: [TensorFlow Estimators: Managing Simplicity vs. Flexibility in High-Level Machine Learning Frameworks](http://terrytangyuan.github.io/data/papers/tf-estimators-kdd-paper.pdf).

## Quick Start

### Installation

To use **tfestimators**, you need to install both the **tfestimators** R package as well as [TensorFlow](https://rstudio.github.io/tensorflow/) itself.

First, install the tfestimators R package as follows:

``` r
devtools::install_github("rstudio/tfestimators")
```

Then, use the `install_tensorflow()` function to install TensorFlow (note that the current tfestimators package requires version 1.3.0 of TensorFlow so even if you already have TensorFlow installed you should update if you are running a previous version):

``` r
library(tfestimators)
install_tensorflow()
```

This will provide you with a default installation of TensorFlow suitable for getting started. See the [article on installation](https://tensorflow.rstudio.com/installation.html) to learn about more advanced options, including installing a version of TensorFlow that takes advantage of NVIDIA GPUs if you have the correct CUDA libraries installed.

### Linear Regression

Let's create a simple linear regression model with the [mtcars dataset](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html) to demonstrate the use of estimators. We'll illustrate how **input functions** can be constructed and used to feed data to an estimator, how **feature columns** can be used to specify a set of transformations to apply to input data, and how these pieces come together in the Estimator interface.

#### Input Function

Estimators can receive data through input functions. Input functions take an arbitrary data source (in-memory data sets, streaming data, custom data format, and so on) and generate Tensors that can be supplied to TensorFlow models. The **tfestimators** package includes an `input_fn()` function that can create TensorFlow input functions from common R data sources (e.g. data frames and matrices). It's also possible to write a fully custom input function.

Here, we define a helper function that will return an input function for a subset of our `mtcars` data set.

``` r
library(tfestimators)

# return an input_fn for a given subset of data
mtcars_input_fn <- function(data) {
  input_fn(data, 
           features = c("disp", "cyl"), 
           response = "mpg")
}
```

#### Feature Columns

Next, we define the feature columns for our model. Feature columns are used to specify how Tensors received from the input function should be combined and transformed before entering the model training, evaluation, and prediction steps. A feature column can be a plain mapping to some input column (e.g. `column_numeric()` for a column of numerical data), or a transformation of other feature columns (e.g. `column_crossed()` to define a new column as the cross of two other feature columns).

Here, we create a list of feature columns containing two numeric variables - `disp` and `cyl`:

``` r
cols <- feature_columns(
  column_numeric("disp"),
  column_numeric("cyl")
)
```

You can also define multiple feature columns at once:

``` r
cols <- feature_columns( 
  column_numeric("disp", "cyl")
)
```

By using the family of feature column functions we can define various transformations on the data before using it for modeling.

#### Estimator

Next, we create the estimator by calling the `linear_regressor()` function and passing it a set of feature columns:

``` r
model <- linear_regressor(feature_columns = cols)
```

#### Training

We're now ready to train our model, using the `train()` function. We'll partition the `mtcars` data set into separate training and validation data sets, and feed the training data set into `train()`. We'll hold 20% of the data aside for validation.

``` r
indices <- sample(1:nrow(mtcars), size = 0.80 * nrow(mtcars))
train <- mtcars[indices, ]
test  <- mtcars[-indices, ]

# train the model
model %>% train(mtcars_input_fn(train))
```

#### Evaluation

We can evaluate the model's accuracy using the `evaluate()` function, using our 'test' data set for validation.

``` r
model %>% evaluate(mtcars_input_fn(test))
```

#### Prediction

After we've finished training out model, we can use it to generate predictions from new data.

``` r
new_obs <- mtcars[1:3, ]
model %>% predict(mtcars_input_fn(new_obs))
```

## Learning More

After you've become familiar with these concepts, these articles cover the basics of using TensorFlow Estimators and the main components in more detail:

- [Estimator Basics](https://tensorflow.rstudio.com/tfestimators/articles/estimator_basics.html)
- [Input Functions](https://tensorflow.rstudio.com/tfestimators/articles/input_functions.html)
- [Feature Columns](https://tensorflow.rstudio.com/tfestimators/articles/feature_columns.html)

These articles describe more advanced topics/usage:

- [Run Hooks](https://tensorflow.rstudio.com/tfestimators/articles/run_hooks.html)
- [Custom Estimators](https://tensorflow.rstudio.com/tfestimators/articles/creating_estimators.html)
- [TensorFlow Layers](https://tensorflow.rstudio.com/tfestimators/articles/layers.html)
- [TensorBoard Visualization](https://tensorflow.rstudio.com/tfestimators/articles/tensorboard.html)
- [Parsing Utilities](https://tensorflow.rstudio.com/tfestimators/articles/parsing_spec.html)

One of the best ways to learn is from reviewing and experimenting with examples. See the [Examples](https://tensorflow.rstudio.com/tfestimators/articles/examples/index.html) page for a variety of examples to help you get started.
