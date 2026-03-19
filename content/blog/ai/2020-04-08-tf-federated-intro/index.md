---
title: "A first look at federated learning with TensorFlow"
description: |
  The term "federated learning" was coined to describe a form of distributed model training where the data remains on client devices, i.e., is never shipped to the coordinating server. In this post, we introduce central concepts and run first experiments with TensorFlow Federated, using R.
date: 2020-04-08
slug: keydanatffederatedintro
categories:
  - Privacy & Security
  - TensorFlow/Keras
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.png
ported_from: ai
port_status: in-progress
---



Here, stereotypically, is the process of applied deep learning: Gather/get data;
iteratively train and evaluate; deploy. Repeat (or have it all automated as a
continuous workflow). We often discuss training and evaluation;
deployment matters to varying degrees, depending on the circumstances. But the
data often is just assumed to be there: All together, in one place (on your
laptop; on a central server; in some cluster in the cloud.) In real life though,
data could be all over the world: on smartphones for example, or on IoT devices.
There are a lot of reasons why we don't want to ship all that data to some central
location: Privacy, of course (why should some third party get to know about what
you texted your friend?); but also, sheer mass (and this latter aspect is bound
to become more influential all the time).

A solution is that data on client devices stays on client devices, yet
participates in training a global model. How? In so-called *federated
learning*(McMahan et al. 2016), there is a central coordinator ("server"), as well as
a potentially huge number of clients (e.g., phones) who participate in learning
on an "as-fits" basis: e.g., if plugged in and on a high-speed connection.
Whenever they're ready to train, clients are passed the current model weights,
and perform some number of training iterations on their own data. They then send
back gradient information to the server (more on that soon), whose job is to
update the weights accordingly. Federated learning is not the only conceivable
protocol to jointly train a deep learning model while keeping the data private:
A fully decentralized alternative could be *gossip learning* (Blot et al. 2016),
following the [gossip protocol](https://en.wikipedia.org/wiki/Gossip_protocol) .
As of today, however, I am not aware of existing implementations in any of the
major deep learning frameworks.

In fact, even TensorFlow Federated (TFF), the library used in this post, was
officially introduced just about a year ago. Meaning, all this is pretty new
technology, somewhere inbetween proof-of-concept state and production readiness.
So, let's set expectations as to what you might get out of this post.

### What to expect from this post

We start with quick glance at federated learning in the context of *privacy*
overall. Subsequently, we introduce, by example, some of TFF's basic building
blocks. Finally, we show a complete image classification example using Keras --
from R.

While this sounds like "business as usual", it's not -- or not quite. With no R
package existing, as of this writing, that would wrap TFF, we're accessing its
functionality using `$`-syntax -- not in itself a big problem. But there's
something else.

TFF, while providing a Python API, itself is not written in Python. Instead, it
is an internal language designed specifically for serializability and
distributed computation. One of the consequences is that TensorFlow (that is: TF
as opposed to TFF) code has to be wrapped in calls to `tf.function`, triggering
static-graph construction. However, as I write this, the TFF documentation
[cautions](https://github.com/tensorflow/federated/blob/master/docs/federated_learning.md):
"Currently, TensorFlow does not fully support serializing and deserializing
eager-mode TensorFlow." Now when we call TFF from R, we add another layer of
complexity, and are more likely to run into corner cases.

Therefore, at the current
stage, when using TFF from R it's advisable to play around with high-level
functionality -- using Keras models -- instead of, e.g., translating to R the
low-level functionality shown in the [second TFF Core
tutorial](https://github.com/tensorflow/federated/blob/master/docs/tutorials/custom_federated_algorithms_2.ipynb).

One final remark before we get started: As of this writing, there is no
documentation on how to actually run federated training on "real clients". There is, however, a
[document](https://github.com/tensorflow/federated/blob/master/docs/tutorials/high_performance_simulation_with_kubernetes.ipynb)
that describes how to run TFF on Google Kubernetes Engine, and
deployment-related documentation is visibly and steadily growing.)

That said, now how does federated learning relate to privacy, and how does it
look in TFF?

### Federated learning in context

In federated learning, client data never leaves the device. So in an immediate
sense, computations are private. However, gradient updates are sent to a central
server, and this is where privacy guarantees may be violated. In some cases, it
may be easy to reconstruct the actual data from the gradients -- in an NLP task,
for example, when the vocabulary is known on the server, and gradient updates
are sent for small pieces of text.

This may sound like a special case, but general methods have been demonstrated
that work regardless of circumstances. For example, Zhu et
al. (Zhu et al. 2019) use a "generative" approach, with the server starting
from randomly generated fake data (resulting in fake gradients) and then,
iteratively updating that data to obtain gradients more and more like the real
ones -- at which point the real data has been reconstructed.

Comparable attacks would not be feasible were gradients not sent in clear text.
However, the server needs to actually use them to update the model -- so it must
be able to "see" them, right? As hopeless as this sounds, there are ways out
of the dilemma. For example, [homomorphic
encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption), a technique
that enables computation on encrypted data. Or [secure multi-party
aggregation](https://en.wikipedia.org/wiki/Secure_multi-party_computation),
often achieved through [secret
sharing](https://en.wikipedia.org/wiki/Secret_sharing), where individual pieces
of data (e.g.: individual salaries) are split up into "shares", exchanged and
combined with random data in various ways, until finally the desired global
result (e.g.: mean salary) is computed. (These are extremely fascinating topics
that unfortunately, by far surpass the scope of this post.)

Now, with the server prevented from actually "seeing" the gradients, a problem
still remains. The model -- especially a high-capacity one, with many parameters
-- could still memorize individual training data. Here is where *differential
privacy* comes into play. In differential privacy, noise is added to the
gradients to decouple them from actual training examples. ([This
post](/blog/ai/2019-12-20-differential-privacy/)
gives an introduction to differential privacy with TensorFlow, from R.)

As of this writing, TFF's federal averaging mechanism (McMahan et al. 2016) does not
yet include these additional privacy-preserving techniques. But research papers
exist that outline algorithms for integrating both secure aggregation
(Bonawitz et al. 2016) and differential privacy (McMahan et al. 2017) .

### Client-side and server-side computations

Like we said above, at this point it is advisable to mainly stick with
high-level computations using TFF from R. (Presumably that is what we'd be interested in
in many cases, anyway.) But it's instructive to look at a few building blocks
from a high-level, functional point of view.

In federated learning, model training happens on the clients. Clients each
compute their local gradients, as well as local metrics. The server, on the other hand,
calculates global gradient updates, as well as global metrics.

Let's say the metric is accuracy. Then clients and server both compute averages: local
averages and a global average, respectively. All the server will need to know to
determine the global averages are the local ones and the respective sample
sizes.

Let's see how TFF would calculate a simple average.

The code in this post was run with the current TensorFlow release 2.1 and TFF
version 0.13.1. We use `reticulate` to install and import TFF.

``` r
library(tensorflow)
library(reticulate)
library(tfdatasets)

py_install("tensorflow-federated")

tff <- import("tensorflow_federated")
```

First, we need every client to be able to compute their own local averages.

Here is a function that *reduces* a list of values to their sum and count, both
at the same time, and then returns their quotient.

The function contains only TensorFlow operations, not computations described in R
directly; if there were any, they would have to be wrapped in calls to
`tf_function`, calling for construction of a static graph. (The same would apply
to raw (non-TF) Python code.)

Now, this function will still have to be wrapped (we're getting to that in an
instant), as TFF expects functions that make use of TF operations to be
*decorated* by calls to `tff$tf_computation`. Before we do that, one comment on
the use of `dataset_reduce`: Inside `tff$tf_computation`, the data that is
passed in behaves like a `dataset`, so we can perform `tfdatasets` operations
like `dataset_map`, `dataset_filter` etc. on it.

``` r
get_local_temperature_average <- function(local_temperatures) {
  sum_and_count <- local_temperatures %>% 
    dataset_reduce(tuple(0, 0), function(x, y) tuple(x[[1]] + y, x[[2]] + 1))
  sum_and_count[[1]] / tf$cast(sum_and_count[[2]], tf$float32)
}
```

Next is the call to `tff$tf_computation` we already alluded to, wrapping
`get_local_temperature_average`. We also need to indicate the
argument's TFF-level type.
(In the context of this post, TFF datatypes are
definitely out-of-scope, but the TFF documentation has lots of detailed
information in that regard. All we need to know right now is that we will be able to pass the data
as a `list`.)

``` r
get_local_temperature_average <- tff$tf_computation(get_local_temperature_average, tff$SequenceType(tf$float32))
```

Let's test this function:

``` r
get_local_temperature_average(list(1, 2, 3))
```

    [1] 2

So that's a local average, but we originally set out to compute a global one.
Time to move on to server side (code-wise).

Non-local computations are called *federated* (not too surprisingly). Individual
operations start with `federated_`; and these have to be wrapped in
`tff$federated_computation`:

``` r
get_global_temperature_average <- function(sensor_readings) {
  tff$federated_mean(tff$federated_map(get_local_temperature_average, sensor_readings))
}

get_global_temperature_average <- tff$federated_computation(
  get_global_temperature_average, tff$FederatedType(tff$SequenceType(tf$float32), tff$CLIENTS))
```

Calling this on a list of lists -- each sub-list presumedly representing client data -- will display the global (non-weighted) average:

``` r
get_global_temperature_average(list(list(1, 1, 1), list(13)))
```

    [1] 7

Now that we've gotten a bit of a feeling for "low-level TFF", let's train a
Keras model the federated way.

### Federated Keras

The setup for this example looks a bit more Pythonian [^1] than usual. We need the
`collections` module from Python to make use of `OrderedDict`s, and we want them to be passed to Python without
intermediate conversion to R -- that's why we import the module with `convert`
set to `FALSE`.

``` r
library(tensorflow)
library(keras)
library(tfds)
library(reticulate)
library(tfdatasets)
library(dplyr)

tff <- import("tensorflow_federated")
collections <- import("collections", convert = FALSE)
np <- import("numpy")
```

For this example, we use [Kuzushiji-MNIST](https://github.com/rois-codh/kmnist)
(Clanuwat et al. 2018), which may conveniently be obtained through
[tfds](https://github.com/rstudio/tfds), the R wrapper for [TensorFlow
Datasets](https://www.tensorflow.org/datasets).

<figure>
<img src="images/kmnist_examples.png" alt="The 10 classes of Kuzushiji-MNIST, with the first column showing each character&#39;s modern hiragana counterpart. From: https://github.com/rois-codh/kmnist" />
<figcaption aria-hidden="true">The 10 classes of Kuzushiji-MNIST, with the first column showing each
character's modern hiragana counterpart. From:
<a href="https://github.com/rois-codh/kmnist" class="uri">https://github.com/rois-codh/kmnist</a></figcaption>
</figure>

TensorFlow datasets come as -- well -- `dataset`s, which normally would be just
fine; here however, we want to simulate different clients each with their own
data. The following code splits up the dataset into ten arbitrary -- sequential,
for convenience -- ranges and, for each range (that is: client), creates a list of
`OrderedDict`s that have the images as their `x`, and the labels as their `y`
component:

``` r
n_train <- 60000
n_test <- 10000

s <- seq(0, 90, by = 10)
train_ranges <- paste0("train[", s, "%:", s + 10, "%]") %>% as.list()
train_splits <- purrr::map(train_ranges, function(r) tfds_load("kmnist", split = r))

test_ranges <- paste0("test[", s, "%:", s + 10, "%]") %>% as.list()
test_splits <- purrr::map(test_ranges, function(r) tfds_load("kmnist", split = r))

batch_size <- 100

create_client_dataset <- function(source, n_total, batch_size) {
  iter <- as_iterator(source %>% dataset_batch(batch_size))
  output_sequence <- vector(mode = "list", length = n_total/10/batch_size)
  i <- 1
  while (TRUE) {
    item <- iter_next(iter)
    if (is.null(item)) break
    x <- tf$reshape(tf$cast(item$image, tf$float32), list(100L,784L))/255
    y <- item$label
    output_sequence[[i]] <-
      collections$OrderedDict("x" = np_array(x$numpy(), np$float32), "y" = y$numpy())
     i <- i + 1
  }
  output_sequence
}

federated_train_data <- purrr::map(
  train_splits, function(split) create_client_dataset(split, n_train, batch_size))
```

As a quick check, the following are the labels for the first batch of images for
client 5:

``` r
federated_train_data[[5]][[1]][['y']]
```

    > [0. 9. 8. 3. 1. 6. 2. 8. 8. 2. 5. 7. 1. 6. 1. 0. 3. 8. 5. 0. 5. 6. 6. 5.
     2. 9. 5. 0. 3. 1. 0. 0. 6. 3. 6. 8. 2. 8. 9. 8. 5. 2. 9. 0. 2. 8. 7. 9.
     2. 5. 1. 7. 1. 9. 1. 6. 0. 8. 6. 0. 5. 1. 3. 5. 4. 5. 3. 1. 3. 5. 3. 1.
     0. 2. 7. 9. 6. 2. 8. 8. 4. 9. 4. 2. 9. 5. 7. 6. 5. 2. 0. 3. 4. 7. 8. 1.
     8. 2. 7. 9.]

The model is a simple, one-layer sequential Keras model. For TFF to have full
control over graph construction, it has to be defined inside a function. The
blueprint for creation is passed to `tff$learning$from_keras_model`, together
with a "dummy" batch that exemplifies how the training data will look:

``` r
sample_batch = federated_train_data[[5]][[1]]

create_keras_model <- function() {
  keras_model_sequential() %>%
    layer_dense(input_shape = 784,
                units = 10,
                kernel_initializer = "zeros",
                activation = "softmax") 
}

model_fn <- function() {
  keras_model <- create_keras_model()
  tff$learning$from_keras_model(
    keras_model,
    dummy_batch = sample_batch,
    loss = tf$keras$losses$SparseCategoricalCrossentropy(),
    metrics = list(tf$keras$metrics$SparseCategoricalAccuracy()))
}
```

Training is a stateful process that keeps updating model weights (and if
applicable, optimizer states). It is created via
`tff$learning$build_federated_averaging_process` ...

``` r
iterative_process <- tff$learning$build_federated_averaging_process(
  model_fn,
  client_optimizer_fn = function() tf$keras$optimizers$SGD(learning_rate = 0.02),
  server_optimizer_fn = function() tf$keras$optimizers$SGD(learning_rate = 1.0))
```

... and on initialization, produces a starting state:

``` r
state <- iterative_process$initialize()
state
```

    <model=<trainable=<[[0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]
     ...
     [0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]
     [0. 0. 0. ... 0. 0. 0.]],[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]>,non_trainable=<>>,optimizer_state=<0>,delta_aggregate_state=<>,model_broadcast_state=<>>

Thus before training, all the state does is reflect our zero-initialized model
weights.

Now, state transitions are accomplished via calls to `next()`. After one round
of training, the state then comprises the "state proper" (weights, optimizer
parameters ...) as well as the current training metrics:

``` r
state_and_metrics <- iterative_process$`next`(state, federated_train_data)

state <- state_and_metrics[0]
state
```

    <model=<trainable=<[[ 9.9695253e-06 -8.5083229e-05 -8.9266898e-05 ... -7.7834651e-05
      -9.4819807e-05  3.4227365e-04]
     [-5.4778640e-05 -1.5390900e-04 -1.7912561e-04 ... -1.4122366e-04
      -2.4614178e-04  7.7663612e-04]
     [-1.9177950e-04 -9.0706220e-05 -2.9841764e-04 ... -2.2249141e-04
      -4.1685964e-04  1.1348884e-03]
     ...
     [-1.3832574e-03 -5.3664664e-04 -3.6622395e-04 ... -9.0854493e-04
       4.9618416e-04  2.6899918e-03]
     [-7.7253254e-04 -2.4583895e-04 -8.3220737e-05 ... -4.5274393e-04
       2.6396243e-04  1.7454443e-03]
     [-2.4157032e-04 -1.3836231e-05  5.0371520e-05 ... -1.0652864e-04
       1.5947431e-04  4.5250656e-04]],[-0.01264258  0.00974309  0.00814162  0.00846065 -0.0162328   0.01627758
     -0.00445857 -0.01607843  0.00563046  0.00115899]>,non_trainable=<>>,optimizer_state=<1>,delta_aggregate_state=<>,model_broadcast_state=<>>

``` r
metrics <- state_and_metrics[1]
metrics
```

    <sparse_categorical_accuracy=0.5710999965667725,loss=1.8662642240524292,keras_training_time_client_sum_sec=0.0>

Let's train for a few more epochs, keeping track of accuracy:

``` r
num_rounds <- 20

for (round_num in (2:num_rounds)) {
  state_and_metrics <- iterative_process$`next`(state, federated_train_data)
  state <- state_and_metrics[0]
  metrics <- state_and_metrics[1]
  cat("round: ", round_num, "  accuracy: ", round(metrics$sparse_categorical_accuracy, 4), "\n")
}
```

    round:  2    accuracy:  0.6949 
    round:  3    accuracy:  0.7132 
    round:  4    accuracy:  0.7231 
    round:  5    accuracy:  0.7319 
    round:  6    accuracy:  0.7404 
    round:  7    accuracy:  0.7484 
    round:  8    accuracy:  0.7557 
    round:  9    accuracy:  0.7617 
    round:  10   accuracy:  0.7661 
    round:  11   accuracy:  0.7695 
    round:  12   accuracy:  0.7728 
    round:  13   accuracy:  0.7764 
    round:  14   accuracy:  0.7788 
    round:  15   accuracy:  0.7814 
    round:  16   accuracy:  0.7836 
    round:  17   accuracy:  0.7855 
    round:  18   accuracy:  0.7872 
    round:  19   accuracy:  0.7885 
    round:  20   accuracy:  0.7902 

Training accuracy is increasing continuously. These values represent averages of
*local* accuracy measurements, so in the real world, they might well be overly
optimistic (with each client overfitting on their respective data). So
supplementing federated training, a federated evaluation process would need to
be built in order to get a realistic view on performance. This is a topic to
come back to when more related TFF documentation is available.

### Conclusion

We hope you've enjoyed this first introduction to TFF using R. Certainly at this
time, it is too early for use in production; and for application in research (e.g., adversarial attacks on federated learning)
familiarity with "lowish"-level implementation code is required -- regardless
whether you use R or Python.

However, judging from activity on GitHub, TFF is under very active development right now (including new documentation being added!), so we're looking forward
to what's to come. In the meantime, it's never too early to start learning the
concepts...

Thanks for reading!

Blot, Michael, David Picard, Matthieu Cord, and Nicolas Thome. 2016. "Gossip Training for Deep Learning." *CoRR* abs/1611.09726. <http://arxiv.org/abs/1611.09726>.

Bonawitz, Keith, Vladimir Ivanov, Ben Kreuter, et al. 2016. "Practical Secure Aggregation for Federated Learning on User-Held Data." *CoRR* abs/1611.04482. <http://arxiv.org/abs/1611.04482>.

Clanuwat, Tarin, Mikel Bober-Irizar, Asanobu Kitamoto, Alex Lamb, Kazuaki Yamamoto, and David Ha. 2018. "Deep Learning for Classical Japanese Literature." December 3. <https://arxiv.org/abs/cs.CV/1812.01718>.

McMahan, H. Brendan, Eider Moore, Daniel Ramage, and Blaise Agüera y Arcas. 2016. "Federated Learning of Deep Networks Using Model Averaging." *CoRR* abs/1602.05629. <http://arxiv.org/abs/1602.05629>.

McMahan, H. Brendan, Daniel Ramage, Kunal Talwar, and Li Zhang. 2017. "Learning Differentially Private Language Models Without Losing Accuracy." *CoRR* abs/1710.06963. <http://arxiv.org/abs/1710.06963>.

Zhu, Ligeng, Zhijian Liu, and Song Han. 2019. "Deep Leakage from Gradients." *CoRR* abs/1906.08935. <http://arxiv.org/abs/1906.08935>.

[^1]: not *Pythonic* :-)
