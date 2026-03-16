---
title: "Revisiting Keras for R"
description: |
  It's been a while since this blog featured content about Keras for R, so you might've thought that the project was dormant. It's not! In fact, Keras for R is better than ever, with two recent releases adding powerful capabilities that considerably lighten previously tedious tasks. This post provides a high-level overview. Future posts will go into more detail on some of the most helpful new features, as well as dive into the powerful low-level enhancements that make the former possible.
date: 2021-11-18
slug: keydanakalinowskikeras
categories:
  - Packages/Releases
  - TensorFlow/Keras
  - R
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
---



Before we even talk about new features, let us answer the obvious question. Yes, there will be a second edition of *Deep Learning for R*! Reflecting what has been going on in the meantime, the new edition covers an extended set of proven architectures; at the same time, you'll find that intermediate-to-advanced designs already present in the first edition have become rather more intuitive to implement, thanks to the new low-level enhancements alluded to in the summary.

But don't get us wrong -- the scope of the book is completely unchanged. It is still the perfect choice for people new to machine learning and deep learning. Starting from the basic ideas, it systematically progresses to intermediate and advanced topics, leaving you with both a conceptual understanding and a bag of useful application templates.

*Now, what has been going on with Keras?*

## State of the ecosystem

Let us start with a characterization of the ecosystem, and a few words on its history.

In this post, when we say *Keras*, we mean R -- as opposed to Python -- *Keras*[^1]. Now, this immediately translates to the R package `keras`. But `keras` alone wouldn't get you far. While `keras` provides the high-level functionality -- neural network layers, optimizers, workflow management, and more -- the basic data structure operated upon, *tensors*, lives in `tensorflow`. Thirdly, as soon as you'll need to perform less-then-trivial pre-processing, or can no longer keep the whole training set in memory because of its size, you'll want to look into `tfdatasets`.

So it is these three packages -- [`tensorflow`](https://github.com/rstudio/tensorflow), [`tfdatasets`](https://github.com/rstudio/tfdatasets), and [`keras`](https://github.com/rstudio/keras) -- that should be understood by "Keras" in the current context[^2]. (The R-Keras ecosystem, on the other hand, is quite a bit bigger. But other packages, such as `tfruns` or `cloudml`, are more decoupled from the core.)

Matching their tight integration, the aforementioned packages tend to follow a common release cycle, itself dependent on the underlying Python library, [TensorFlow](http://tensorflow.org). For each of `tensorflow`, `tfdatasets`, and `keras` , the current CRAN version is 2.7.0, reflecting the corresponding Python version. The synchrony of versioning between the two Kerases, R and Python, seems to indicate that their fates had developed in similar ways. Nothing could be less true, and knowing this can be helpful.

In R, between present-from-the-outset packages `tensorflow` and `keras`, responsibilities have always been distributed the way they are now: `tensorflow` providing indispensable basics, but often, remaining completely transparent to the user; `keras` being the thing you use in your code. In fact, it is possible to train a Keras model without ever consciously using `tensorflow`.

On the Python side, things have been undergoing significant changes, ones where, in some sense, the latter development has been inverting the first. In the beginning, TensorFlow and [Keras](https://keras.io) were separate libraries, with TensorFlow providing a backend -- one among several -- for Keras to make use of. At some point, Keras code got incorporated into the TensorFlow codebase. Finally (as of today), following an extended period of slight confusion, Keras got moved out again, and has started to -- again -- considerably grow in features.

It is just that quick growth that has created, on the R side, the need for extensive low-level refactoring and enhancements. (Of course, the user-facing new functionality itself also had to be implemented!)

Before we get to the promised highlights, a word on how we think about Keras.

## Have your cake and eat it, too: A philosophy of (R) Keras

If you've used Keras in the past, you know what it's always been intended to be: a high-level library, making it easy (as far as such a thing *can* be easy) to train neural networks in R. Actually, it's not just about *ease*. Keras enables users to write natural-feeling, idiomatic-looking code. This, to a high degree, is achieved by its allowing for object composition though the pipe operator; it is also a consequence of its abundant wrappers, convenience functions, and functional (stateless) semantics.[^3]

However, due to the way TensorFlow and Keras have developed on the Python side -- referring to the big architectural and semantic changes between versions 1.x and 2.x, first comprehensively characterized on this blog [here](/blog/ai/2019-10-08-tf2-whatchanges/) -- it has become more challenging to provide all of the functionality available on the Python side to the R user. In addition, maintaining compatibility with several versions of Python TensorFlow -- something R Keras has always done -- by necessity gets more and more challenging, the more wrappers and convenience functions you add.

So this is where we complement the above "make it R-like and natural, where possible" with "make it easy to port from Python, where necessary". With the new low-level functionality, you won't have to wait for R wrappers to make use of Python-defined objects. Instead, Python objects may be sub-classed directly from R; and any additional functionality you'd like to add to the subclass is defined in a Python-like syntax. What this means, concretely, is that translating Python code to R has become a lot easier. We'll catch a glimpse of this in the second of our three highlights.

## New in Keras 2.6/7: Three highlights

Among the many new capabilities added in Keras 2.6 and 2.7, we quickly introduce three of the most important.

- *Pre-processing layers* significantly help to streamline the training workflow, integrating data manipulation and data augmentation.

- The ability to subclass Python objects (already alluded to several times) is the new low-level magic available to the `keras` user *and* which powers many user-facing enhancements underneath.

- Recurrent neural network (RNN) layers gain a new cell-level API.

Of these, the first two definitely deserve some deeper treatment; more detailed posts will follow.

### Pre-processing layers

Before the advent of these dedicated layers, pre-processing used to be done as part of the `tfdatasets` pipeline. You would chain operations as required; maybe, integrating random transformations to be applied while training. Depending on what you wanted to achieve, significant programming effort may have ensued.

This is one area where the new capabilities can help. Pre-processing layers exist for several types of data, allowing for the usual "data wrangling", as well as data augmentation and feature engineering (as in, hashing categorical data, or vectorizing text).

The mention of text vectorization leads to a second advantage. Unlike, say, a random distortion, vectorization is not something that may be forgotten about once done. We don't want to lose the original information, namely, the words. The same happens, for numerical data, with normalization. We need to keep the summary statistics. This means there are two types of pre-processing layers: stateless and stateful ones. The former are part of the training process; the latter are called in advance.

Stateless layers, on the other hand, can appear in two places in the training workflow: as part of the `tfdatasets` pipeline, or as part of the model.

This is, schematically, how the former would look.

``` r
library(tfdatasets)
dataset <- ... # define dataset
dataset <- dataset %>%
  dataset_map(function(x, y) list(preprocessing_layer(x), y))
```

While here, the pre-processing layer is the first in a larger model:

``` r
input <- layer_input(shape = input_shape)
output <- input %>%
  preprocessing_layer() %>%
  rest_of_the_model()
model <- keras_model(input, output)
```

We'll talk about which way is preferable when, as well as showcase a few specialized layers in a future post. Until then, please feel free to consult the -- detailed and example-rich [vignette](https://github.com/rstudio/keras/blob/master/vignettes/new-guides/preprocessing_layers.Rmd).

### Subclassing Python

Imagine you wanted to port a Python model that made use of the following constraint:

``` python
class NonNegative(tf.keras.constraints.Constraint):
    def __call__(self, w):
        return w * tf.cast(tf.math.greater_equal(w, 0.), w.dtype)
```

How can we have such a thing in R? Previously, there used to exist[^4] various methods to create Python-based objects, both R6-based and functional-style. The former, in all but the most straightforward cases, could be effort-rich and error-prone; the latter, elegant-in-style but hard to adapt to more advanced requirements.

The new way, `%py_class%`, now allows for translating the above code like this:

``` r
NonNegative(keras$constraints$Constraint) %py_class% {
  "__call__" <- function(x) {
    w * k_cast(w >= 0, k_floatx())
  }
}
```

Using `%py_class%`, we directly subclass the *Python* `object tf.keras.constraints.Constraint`, and override its `__call__` method.

Why is this so powerful? The first advantage is visible from the example: Translating Python code becomes an almost mechanical task. But there's more: The above method is independent from what *kind* of object you're subclassing. Want to implement a new layer? A callback? A loss? An optimizer? The procedure is always the same. No need to find a pre-defined R6 object in the `keras` codebase; one `%py_class%` delivers them all.

There is a lot more to say on this topic, though; in fact, if you don't *want* to use `%py_class%` directly, there are wrappers available for the most frequent use cases. More on this in a dedicated post. Until then, consult the [vignette](https://github.com/rstudio/keras/blob/master/vignettes/new-guides/python_subclasses.Rmd) for numerous examples, syntactic sugar, and low-level details.

### RNN cell API

Our third point is at least half as much shout-out to excellent documentation as alert to a new feature. The piece of documentation in question is a new [vignette on RNNs](https://github.com/rstudio/keras/blob/master/vignettes/new-guides/working_with_rnns.Rmd). The vignette gives a useful overview of how RNNs function in Keras, addressing the usual questions that tend to come up once you haven't been using them in a while: What exactly are states vs. outputs, and when does a layer return what? How do I initialize the state in an application-dependent way? What's the difference between stateful and stateless RNNs?

In addition, the vignette covers more advanced questions: How do I pass nested data to an RNN? How do I write custom cells?

In fact, this latter question brings us to the new feature we wanted to call out: the new cell-level API. Conceptually, with RNNs, there's always two things involved: the logic of what happens at a single timestep; and the threading of state across timesteps. So-called "simple RNNs" are concerned with the latter (recursion) aspect only; they tend to exhibit the classic vanishing-gradients problem. Gated architectures, such as the LSTM and the GRU, have specially been designed to avoid those problems; both can be easily integrated into a model using the respective `layer_x()` constructors. What if you'd like, not a GRU, but *something like* a GRU (using some fancy new activation method, say)?

With Keras 2.7, you can now create a single-timestep RNN cell (using the above-described `%py_class%` API), and obtain a recursive version -- a complete layer -- using `layer_rnn()`:

``` r
rnn <- layer_rnn(cell = cell)
```

If you're interested, check out the [vignette](https://github.com/rstudio/keras/blob/master/vignettes/new-guides/working_with_rnns.Rmd) for an extended example.

With that, we end our *news from Keras*, for today. Thanks for reading, and stay tuned for more!

Photo by [Hans-Jurgen Mager](https://unsplash.com/@hansjurgen007?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

[^1]: Originally, both Keras and Tensorflow are Python libraries, bound to by R at runtime. In practice, this means that those Python libraries have to be present on the R user's machine. This is in contrast to R `torch` , which has no Python dependencies. (Instead, it directly binds to a C++ library.)

[^2]: Definitely, `tfautograph` belongs in this group as well, providing even-lower-level support for already-low-level `tensorflow`. But normally, the user will not have to call its functions directly.

[^3]: Provided stateless semantics is possible, in some context. This is anything but a matter of course, with an object-oriented language like Python in the background.

[^4]: We're not implying they don't exist anymore; they do. But the preferred method is now `%py_class%`.
