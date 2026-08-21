---
title: 'cuda.ml 0.4.0: GPU-accelerated machine learning from R'
date: 2026-08-21T00:00:00.000Z
people:
  - Tomasz Kalinowski
description: >
  cuda.ml 0.4.0 simplifies installation, expands tidymodels integration and
  tree-ensemble inference, and adds portable persistence for supported fitted
  models.
image: featured-alt.png
image-alt: >-
  An aerial-style view of broad salt ponds in pink, coral, orange, turquoise,
  and deep blue, divided by narrow roads.
topics:
  - Machine Learning
  - MLOps and Admin
software:
  - cuda.ml
  - parsnip
  - tidymodels
languages:
  - R
source: ai
hidesubscription: false
---


[cuda.ml](https://mlverse.github.io/cuda.ml/) is an R package for
running common data science and machine-learning operations on NVIDIA
GPUs. It provides high-level interfaces for fitting regression and
classification models, finding nearest neighbors, clustering
observations, reducing dimensions, and running predictions from tree
ensembles. You can use its direct R functions or work through parsnip
and tidymodels.

cuda.ml is for data scientists who work primarily in R and want to use a
GPU without moving their modeling workflow to Python or learning
low-level GPU APIs. Version 0.4.0 is a substantial update to the
package. It makes installation much simpler, expands tidymodels support,
adds more ways to run tree-ensemble models, and makes it straightforward
to save and restore supported fitted models.

## Install from CRAN

For most users, setup is two commands:

``` r
install.packages("cuda.ml")
cuda.ml::cuda_ml_install()
```

The package from CRAN is a regular, portable R package.
`cuda_ml_install()` downloads and verifies the matching compiled backend
and GPU libraries, then keeps them in a cache for later R sessions. On a
supported system, you do not need to compile cuda.ml from source,
configure a Python environment, or assemble the GPU libraries yourself.

The result is a familiar R package workflow: install the package,
prepare its supporting libraries once, and start an analysis. The extra
installation call is explicit because the GPU libraries are much larger
than the R package. Repeated calls reuse the completed cache, and
loading cuda.ml itself is quiet and does not initialize CUDA.

Prebuilt support is available for Linux x86_64 with glibc 2.28 or newer.
GPU operations require a supported NVIDIA GPU and driver 580 or newer.
On Windows, install and run R inside a compatible WSL2 Linux
distribution. See the [installation guide](https://mlverse.github.io/cuda.ml/articles/install-manage.html) for the complete system requirements and source-build options.

## Use familiar modeling interfaces

cuda.ml registers parsnip engines for linear, logistic, and multinomial
regression, random forests, nearest neighbors, and radial, polynomial,
and linear support-vector machines. For example, this fits a
random-forest classifier on the GPU using the standard parsnip
interface:

``` r
library(cuda.ml)
library(parsnip)

forest_spec <- rand_forest() |>
  set_mode("classification") |>
  set_engine("cuda.ml")

forest_fit <- forest_spec |>
  fit(class ~ ., data = modeldata::hpc_data)
predict(forest_fit, modeldata::hpc_data[1:5, ], type = "prob")
```

``` text
# A tibble: 5 × 4
  .pred_VF .pred_F .pred_M  .pred_L
     <dbl>   <dbl>   <dbl>    <dbl>
1    0.309  0.597  0.0666  0.0275
2    0.899  0.0838 0.0138  0.00335
3    0.965  0.0261 0.00850 0.000883
4    0.973  0.0228 0.00416 0.000352
5    0.966  0.0298 0.00416 0.000352
```

`set_engine("cuda.ml")` selects the GPU-backed cuda.ml engine; the rest
is a standard parsnip workflow. Recipes can learn preprocessing on the
training data and carry it into resampling and prediction.

## Work directly with cuda.ml

cuda.ml also provides a direct R interface. This is useful when you
prefer a function-oriented workflow or want to use the package on its
own.

``` r
library(cuda.ml)
library(ggplot2)

clusters <- cuda_ml_kmeans(scale(faithful), k = 2)
faithful$cluster <- factor(clusters$labels)

ggplot(faithful, aes(eruptions, waiting, color = cluster)) +
  geom_point(size = 2.5) +
  labs(
    x = "Eruption duration (minutes)",
    y = "Waiting time (minutes)"
  ) +
  theme_minimal()
```

<img src="index.markdown_strict_files/figure-markdown_strict/faithful-clusters-1.png" data-fig-align="center" data-fig-alt="Scatterplot of Old Faithful eruption durations and waiting times, colored by two clusters. Shorter eruptions have shorter waits, while longer eruptions have longer waits." width="768" />

The direct API covers supervised models as well as clustering and
dimensionality reduction, including DBSCAN, k-means, PCA, tSVD, UMAP,
and t-SNE. It also includes stochastic-gradient-descent regression, the
hyperbolic-tangent SVM kernel, and external tree-ensemble inference.

## Run tree ensembles on a GPU or CPU

This release expands where and how you can make predictions with tree
ensembles. The new nvForest support powers prediction for random forests
trained with `cuda_ml_rand_forest()` and can load trained XGBoost
models, LightGBM text models, and Treelite checkpoints. Once a model is
loaded, the API provides standard prediction along with model
information, leaf identifiers, individual-tree predictions, and
checkpoint import and export.

GPU inference uses the complete cuda.ml installation. A deployment that
only needs CPU inference can prepare a smaller, CUDA-free backend:

``` r
cuda.ml::cuda_ml_install(device = "cpu")
```

The CPU backend can run a cuda.ml random forest trained on a GPU as well
as a supported external tree ensemble. The complete installation can
also run these models on a CPU, so the smaller backend is an optional
deployment choice.

## Save and deploy fitted models

cuda.ml 0.4.0 expands model persistence for training, analysis, and
deployment workflows. Supported fitted models can be saved to a
compressed file, restored in another R process, stored as raw bytes, or
wrapped with the bundle package.

The simplest file workflow passes a path directly:

``` r
model <- cuda_ml_rand_forest(
  class ~ .,
  data = modeldata::hpc_data,
  trees = 100
)

cuda_ml_serialize(model, "hpc-runtime-forest.cuda-ml")
```

In another R process or deployment environment, prepare cuda.ml and
restore the fitted model:

``` r
library(cuda.ml)

cuda_ml_install()
model <- cuda_ml_unserialize("hpc-runtime-forest.cuda-ml")

predict(model, modeldata::hpc_data[1:5, ], type = "class")
```

File paths use gzip compression. Passing `connection = NULL` instead
returns the state as an uncompressed raw vector of bytes, which is
convenient for object stores and database BLOB columns. The blob package
can represent raw vectors for database workflows, and the bundle package
is supported for teams that already use bundled model artifacts.

Persistence is available for linear models, logistic and multinomial
regression, PCA, SVC and SVR models, UMAP, random forests, and nvForest
models. cuda.ml checks the saved state and required backend before
restoring it. For an nvForest-backed model, the restore call can select
CPU or GPU inference.

## Highlights for users upgrading from cuda.ml 0.3

This is a breaking update to the earlier package. The most visible
changes are:

- The random-forest API now uses `mtry` for predictor sampling and
  `sample_fraction` for row sampling. `trees` defaults to 100, and an
  omitted `seed` draws from R's random-number generator, so `set.seed()`
  controls the fit.
- Linear, logistic, and multinomial regression now use numeric `penalty`
  and `mixture` arguments that match parsnip. Logistic and multinomial
  regression are unregularized by default.
- `normalize_input` was removed from the linear-model functions. It
  previously requested GPU-side L2 normalization. Use explicit
  preprocessing such as `recipes::step_normalize()` when centering and
  scaling are appropriate; but please note, the two operations are not
  numerically identical.
- `cuda_ml_sgd()` now fits squared-loss regression only. Its `loss`
  argument was removed, and `n_iters_no_change` is now
  `n_iter_no_change`.
- The former FIL interface has been replaced by nvForest. Random
  projection and the KNN IVFSQ index have no replacement in the pinned
  upstream API.

See the
[full changelog](https://mlverse.github.io/cuda.ml/news/index.html) for
the complete list of API changes.

The guides cover first steps and more complete examples:

- [Get started with cuda.ml](https://mlverse.github.io/cuda.ml/articles/cuda-ml.html)
- [Use cuda.ml with tidymodels](https://mlverse.github.io/cuda.ml/articles/tidymodels.html)
- [Save and restore models](https://mlverse.github.io/cuda.ml/articles/model-persistence.html)
- [nvForest inference and deployment](https://mlverse.github.io/cuda.ml/articles/nvforest.html)
