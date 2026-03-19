---
title: 'Pre-processing layers in keras: What they are and how to use them'
description: |
  For keras, the last two releases have brought important new functionality, in terms of both low-level infrastructure and workflow enhancements. This post focuses on an outstanding example of the latter category: a new family of layers designed to help with pre-processing, data-augmentation, and feature-engineering tasks.
date: '2021-12-09'
slug: kkkspreproclayers
categories:
  - Machine Learning
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
  - name: Tomasz Kalinowski
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
  - Tomasz Kalinowski
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
software: ["keras3"]
languages: ["R"]
ported_categories:
  - TensorFlow/Keras
  - R
---



Data pre-processing: What you do to the data before feeding it to the model.  
--- A simple definition that, in practice, leaves open many questions. Where, exactly, should pre-processing stop, and the model begin? Are steps like normalization, or various numerical transforms, part of the model, or the pre-processing? What about data augmentation? In sum, the line between what is pre-processing and what is modeling has always, at the edges, felt somewhat fluid.

In this situation, the advent of `keras` pre-processing layers changes a long-familiar picture.

In concrete terms, with `keras`, two alternatives tended to prevail: one, to do things upfront, in R; and two, to construct a `tfdatasets` pipeline. The former applied whenever we needed the complete data to extract some summary information. For example, when normalizing to a mean of zero and a standard deviation of one. But often, this meant that we had to transform back-and-forth between normalized and un-normalized versions at several points in the workflow. The `tfdatasets` approach, on the other hand, was elegant; however, it could require one to write a lot of low-level `tensorflow` code.

Pre-processing layers, available as of `keras` version 2.6.1, remove the need for upfront R operations, and integrate nicely with `tfdatasets`. But that is not all there is to them. In this post, we want to highlight four essential aspects:

1.  Pre-processing layers significantly reduce coding effort. You *could* code those operations yourself; but not having to do so saves time, favors modular code, and helps to avoid errors.
2.  Pre-processing layers -- a subset of them, to be precise -- can produce summary information before training proper, and make use of a saved state when called upon later.
3.  Pre-processing layers can speed up training.
4.  Pre-processing layers are, or can be made, part of the model, thus removing the need to implement independent pre-processing procedures in the deployment environment.

Following a short introduction, we'll expand on each of those points. We conclude with two end-to-end examples (involving [images](#example-1-image-data-augmentation) and [text](#example-2-text-vectorization), respectively) that nicely illustrate those four aspects.

## Pre-processing layers in a nutshell

Like other `keras` layers, the ones we're talking about here all start with `layer_`, and may be instantiated independently of model and data pipeline. Here, we create a layer that will randomly rotate images while training, by up to 45 degrees in both directions:

``` r
library(keras)
aug_layer <- layer_random_rotation(factor = 0.125)
```

Once we have such a layer, we can immediately test it on some dummy image.

``` r
library(tensorflow)
img <- k_eye(5) %>% k_reshape(c(5, 5, 1))
img[ , , 1]
```

    tf.Tensor(
    [[1. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]], shape=(5, 5), dtype=float32)

"Testing the layer" now literally means *calling it like a function*:

``` r
aug_layer(img)[ , , 1]
```

    tf.Tensor(
    [[0.         0.         0.         0.         0.        ]
     [0.44459596 0.32453176 0.05410459 0.         0.        ]
     [0.15844001 0.4371609  1.         0.4371609  0.15844001]
     [0.         0.         0.05410453 0.3245318  0.44459593]
     [0.         0.         0.         0.         0.        ]], shape=(5, 5), dtype=float32)

Once instantiated, a layer can be used in two ways. Firstly, as part of the input pipeline.

In pseudocode:

``` r
# pseudocode
library(tfdatasets)
 
train_ds <- ... # define dataset
preprocessing_layer <- ... # instantiate layer

train_ds <- train_ds %>%
  dataset_map(function(x, y) list(preprocessing_layer(x), y))
```

Secondly, the way that seems most natural, for a *layer*: as a layer inside the model. Schematically:

``` r
# pseudocode
input <- layer_input(shape = input_shape)

output <- input %>%
  preprocessing_layer() %>%
  rest_of_the_model()

model <- keras_model(input, output)
```

In fact, the latter seems so obvious that you might be wondering: Why even allow for a `tfdatasets`-integrated alternative? We'll expand on that shortly, when talking about [performance](#using-pre-processing-layers-for-performance).

*Stateful* layers -- who are special enough to deserve their [own section](#pre-processing-layers-that-keep-state) -- can be used in both ways as well, but they require an additional step. More on that below.

## How pre-processing layers make life easier

Dedicated layers exist for a multitude of data-transformation tasks. We can subsume them under two broad categories, feature engineering and data augmentation.

##### Feature engineering

The need for feature engineering may arise with all types of data. With images, we don't normally use that term for the "pedestrian" operations that are required for a model to process them: resizing, cropping, and such. Still, there are assumptions hidden in each of these operations , so we feel justified in our categorization. Be that as it may, layers in this group include `layer_resizing()`, `layer_rescaling()`, and `layer_center_crop()`.

With text, the one functionality we couldn't do without is vectorization. `layer_text_vectorization()` takes care of this for us. We'll encounter this layer in the next section, as well as in the [second full-code example](#example-2-text-vectorization).

Now, on to what is normally seen as *the* domain of feature engineering: numerical and categorical (we might say: "spreadsheet") data.

First, numerical data often need to be normalized for neural networks to perform well -- to achieve this, use `layer_normalization()`. Or maybe there is a reason we'd like to put continuous values into discrete categories. That'd be a task for `layer_discretization()`.

Second, categorical data come in various formats (strings, integers ...), and there's always *something* that needs to be done in order to process them in a meaningful way. Often, you'll want to embed them into a higher-dimensional space, using `layer_embedding()`. Now, embedding layers expect their inputs to be integers; to be precise: consecutive integers. Here, the layers to look for are `layer_integer_lookup()` and `layer_string_lookup()`: They will convert random integers (strings, respectively) to consecutive integer values. In a different scenario, there might be too many categories to allow for useful information extraction. In such cases, use `layer_hashing()` to bin the data. And finally, there's `layer_category_encoding()` to produce the classical one-hot or multi-hot representations.

##### Data augmentation

In the second category, we find layers that execute \[configurable\] random operations on images. To name just a few of them: `layer_random_crop()`, `layer_random_translation()`, `layer_random_rotation()` ... These are convenient not just in that they implement the required low-level functionality; when integrated into a model, they're also workflow-aware: Any random operations will be executed during training only.

Now we have an idea what these layers do for us, let's focus on the specific case of state-preserving layers.

## Pre-processing layers that keep state

A layer that randomly perturbs images doesn't need to know anything about the data. It just needs to follow a rule: With probability $p$, do $x$. A layer that's supposed to vectorize text, on the other hand, needs to have a lookup table, matching character strings to integers. The same goes for a layer that maps contingent integers to an ordered set. And in both cases, the lookup table needs to be built upfront.

With stateful layers, this information-buildup is triggered by calling `adapt()` on a freshly-created layer instance. For example, here we instantiate and "condition" a layer that maps strings to consecutive integers:

``` r
colors <- c("cyan", "turquoise", "celeste");

layer <- layer_string_lookup()
layer %>% adapt(colors)
```

We can check what's in the lookup table:

``` r
layer$get_vocabulary()
```

    [1] "[UNK]"     "turquoise" "cyan"      "celeste"  

Then, calling the layer will encode the arguments:

``` r
layer(c("azure", "cyan"))
```

    tf.Tensor([0 2], shape=(2,), dtype=int64)

`layer_string_lookup()` works on individual character strings, and consequently, is the transformation adequate for string-valued categorical features. To encode whole sentences (or paragraphs, or any chunks of text) you'd use `layer_text_vectorization()` instead. We'll see how that works in our [second end-to-end example](#example-2-text-vectorization).

## Using pre-processing layers for performance

Above, we said that pre-processing layers could be used in two ways: as part of the model, or as part of the data input pipeline. If these are *layers*, why even allow for the second way?

The main reason is performance. GPUs are great at regular matrix operations, such as those involved in image manipulation and transformations of uniformly-shaped numerical data. Therefore, if you have a GPU to train on, it is preferable to have image processing layers, or layers such as `layer_normalization()`, be part of the model (which is run completely on GPU).

On the other hand, operations involving text, such as `layer_text_vectorization()`, are best executed on the CPU. The same holds if no GPU is available for training. In these cases, you would move the layers to the input pipeline, and strive to benefit from parallel -- on-CPU -- processing. For example:

``` r
# pseudocode

preprocessing_layer <- ... # instantiate layer

dataset <- dataset %>%
  dataset_map(~list(text_vectorizer(.x), .y),
              num_parallel_calls = tf$data$AUTOTUNE) %>%
  dataset_prefetch()
model %>% fit(dataset)
```

Accordingly, in the end-to-end examples below, you'll see image data augmentation happening as part of the model, and text vectorization, as part of the input pipeline.

## Exporting a model, complete with pre-processing

Say that for training your model, you found that the `tfdatasets` way was the best. Now, you deploy it to a server that does not have R installed. It would seem like that either, you have to implement pre-processing in some other, available, technology. Alternatively, you'd have to rely on users sending already-pre-processed data.

Fortunately, there is something else you can do. Create a new model specifically for inference, like so:

``` r
# pseudocode

input <- layer_input(shape = input_shape)

output <- input %>%
  preprocessing_layer(input) %>%
  training_model()

inference_model <- keras_model(input, output)
```

This technique makes use of the [functional API](https://tensorflow.rstudio.com/guide/keras/functional_api/) to create a new model that prepends the pre-processing layer to the pre-processing-less, original model.

Having focused on a few things especially "good to know", we now conclude with the promised examples.

## Example 1: Image data augmentation

Our first example demonstrates image data augmentation. Three types of transformations are grouped together, making them stand out clearly in the overall model definition. This group of layers will be active during training only.

``` r
library(keras)
library(tfdatasets)

# Load CIFAR-10 data that come with keras
c(c(x_train, y_train), ...) %<-% dataset_cifar10()
input_shape <- dim(x_train)[-1] # drop batch dim
classes <- 10

# Create a tf_dataset pipeline 
train_dataset <- tensor_slices_dataset(list(x_train, y_train)) %>%
  dataset_batch(16) 

# Use a (non-trained) ResNet architecture
resnet <- application_resnet50(weights = NULL,
                               input_shape = input_shape,
                               classes = classes)

# Create a data augmentation stage with horizontal flipping, rotations, zooms
data_augmentation <-
  keras_model_sequential() %>%
  layer_random_flip("horizontal") %>%
  layer_random_rotation(0.1) %>%
  layer_random_zoom(0.1)

input <- layer_input(shape = input_shape)

# Define and run the model
output <- input %>%
  layer_rescaling(1 / 255) %>%   # rescale inputs
  data_augmentation() %>%
  resnet()

model <- keras_model(input, output) %>%
  compile(optimizer = "rmsprop", loss = "sparse_categorical_crossentropy") %>%
  fit(train_dataset, steps_per_epoch = 5)
```

## Example 2: Text vectorization

In natural language processing, we often use embedding layers to present the "workhorse" (recurrent, convolutional, self-attentional, what have you) layers with the continuous, optimally-dimensioned input they need. Embedding layers expect tokens to be encoded as integers, and transform text to integers is what `layer_text_vectorization()` does.

Our second example demonstrates the workflow: You have the layer learn the vocabulary upfront, then call it as part of the pre-processing pipeline. Once training has finished, we create an "all-inclusive" model for deployment.

``` r
library(tensorflow)
library(tfdatasets)
library(keras)

# Example data
text <- as_tensor(c(
  "From each according to his ability, to each according to his needs!",
  "Act that you use humanity, whether in your own person or in the person of any other, always at the same time as an end, never merely as a means.",
  "Reason is, and ought only to be the slave of the passions, and can never pretend to any other office than to serve and obey them."
))

# Create and adapt layer
text_vectorizer <- layer_text_vectorization(output_mode="int")
text_vectorizer %>% adapt(text)

# Check
as.array(text_vectorizer("To each according to his needs"))

# Create a simple classification model
input <- layer_input(shape(NULL), dtype="int64")

output <- input %>%
  layer_embedding(input_dim = text_vectorizer$vocabulary_size(),
                  output_dim = 16) %>%
  layer_gru(8) %>%
  layer_dense(1, activation = "sigmoid")

model <- keras_model(input, output)

# Create a labeled dataset (which includes unknown tokens)
train_dataset <- tensor_slices_dataset(list(
    c("From each according to his ability", "There is nothing higher than reason."),
    c(1L, 0L)
))

# Preprocess the string inputs
train_dataset <- train_dataset %>%
  dataset_batch(2) %>%
  dataset_map(~list(text_vectorizer(.x), .y),
              num_parallel_calls = tf$data$AUTOTUNE)

# Train the model
model %>%
  compile(optimizer = "adam", loss = "binary_crossentropy") %>%
  fit(train_dataset)

# export inference model that accepts strings as input
input <- layer_input(shape = 1, dtype="string")
output <- input %>%
  text_vectorizer() %>%
  model()

end_to_end_model <- keras_model(input, output)

# Test inference model
test_data <- as_tensor(c(
  "To each according to his needs!",
  "Reason is, and ought only to be the slave of the passions."
))
test_output <- end_to_end_model(test_data)
as.array(test_output)
```

## Wrapup

With this post, our goal was to call attention to `keras`' new pre-processing layers, and show how -- and why -- they are useful. Many more use cases can be found in the [vignette](https://github.com/rstudio/keras/blob/master/vignettes/new-guides/preprocessing_layers.Rmd).

Thanks for reading!

Photo by [Henning Borgersen](https://unsplash.com/@hebo79?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
