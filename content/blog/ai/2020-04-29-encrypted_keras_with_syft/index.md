---
title: "Towards privacy: Encrypted deep learning with Syft and Keras"
description: |
  Deep learning need not be irreconcilable with privacy protection. Federated learning enables on-device, distributed model training; encryption keeps model and gradient updates private; differential privacy prevents the training data from leaking. As of today, private and secure deep learning is an emerging technology. In this post, we introduce Syft, an open-source framework that integrates with PyTorch as well as TensorFlow. In an example use case, we obtain private predictions from a Keras model.
date: 2020-04-29
categories:
  - R
  - Privacy & Security
  - TensorFlow/Keras
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
---



The word *privacy*, in the context of deep learning (or machine learning, or "AI"), and especially when combined with things
like *security*, sounds like it could be part of a catch phrase: *privacy, safety, security* -- like *liberté, fraternité,
égalité*. In fact, there should probably be a mantra like that. But that's another topic, and like with the other catch phrase
just cited, not everyone interprets these terms in the same way.

So let's think about privacy, narrowed down to its role in training or using deep learning models, in a more technical way.
Since privacy -- or rather, its violations -- may appear in various ways, different violations will demand different
countermeasures. Of course, in the end, we'd like to see them all integrated -- but re privacy-related technologies, the field
is really just starting out on a journey. The most important thing we can do, then, is to learn about the concepts,
investigate the landscape of implementations under development, and -- perhaps -- decide to join the effort.

This post tries to do a tiny little bit of all of those.

## Aspects of privacy in deep learning

Say you work at a hospital, and would be interested in training a deep learning model to help diagnose some disease from brain
scans. Where you work, you don't have many patients with this disease; moreover, they tend to mostly be affected by the same
subtypes: Your training set, were you to create one, would not reflect the overall distribution very well. It would, thus,
make sense to cooperate with other hospitals; but that isn't so easy, as the data collected is protected by privacy
regulations. So, the first requirement is: The data has to stay where it is; e.g., it may not be sent to a central server.

#### Federated learning

This first *sine qua non* is addressed by [federated
learning](https://blogs.rstudio.com/tensorflow/posts/2020-04-08-tf-federated-intro/) (McMahan et al. 2016). Federated learning is
not "just" desirable for privacy reasons. On the contrary, in many use cases, it may be the only viable way (like with
smartphones or sensors, which collect gigantic amounts of data). In federated learning, each participant receives a copy of
the model, trains on their own data, and sends back the gradients obtained to the central server, where gradients are averaged
and applied to the model.

This is good insofar as the data never leaves the individual devices; however, a lot of information can still be extracted
from plain-text gradients. Imagine a smartphone app that provides trainable auto-completion for text messages. Even if
gradient updates from many iterations are averaged, their distributions will greatly vary between individuals. Some form of
encryption is needed. But then how is the server going to make sense of the encrypted gradients?

One way to accomplish this relies on *secure multi-party computation* (SMPC).

#### Secure multi-party computation

In SMPC, we need a system of several agents who collaborate to provide a result no single agent could provide alone: "normal"
computations (like addition, multiplication ...) on "secret" (encrypted) data. The assumption is that these agents are "honest
but curious" -- honest, because they won't tamper with their share of data; curious in the sense that if they *were* (curious,
that is), they wouldn't be able to inspect the data because it's encrypted.

The principle behind this is *secret sharing*. A single piece of data -- a salary, say -- is "split up" into meaningless
(hence, encrypted) parts which, when put together again, yield the original data. Here is an example.

Say the parties involved are Julia, Greg, and me. The below function encrypts a single value, assigning to each of us their
"meaningless" share:

``` r
# a big prime number
# all computations are performed in a finite field, for example, the integers modulo that prime
Q <- 78090573363827
 
encrypt <- function(x) {
  # all but the very last share are random 
  julias <- runif(1, min = -Q, max = Q)
  gregs <- runif(1, min = -Q, max = Q)
  mine <- (x - julias - gregs) %% Q
  list (julias, gregs, mine)
}

# some top secret value no-one may get to see
value <- 77777

encrypted <- encrypt(value)
encrypted
```

    [[1]]
    [1] 7467283737857

    [[2]]
    [1] 36307804406429

    [[3]]
    [1] 34315485297318

Once the three of us put our shares together, getting back the plain value is straightforward:

``` r
decrypt <- function(shares) {
  Reduce(sum, shares) %% Q  
}

decrypt(encrypted)
```

    77777

As an example of how to compute on encrypted data, here's addition. (Other operations will be a lot less straightforward.) To
add two numbers, just have everyone add their respective shares:

``` r
add <- function(x, y) {
  list(
    # julia
    (x[[1]] + y[[1]]) %% Q,
    # greg
    (x[[2]] + y[[2]]) %% Q,
    # me
    (x[[3]] + y[[3]]) %% Q
  )
}
  
x <- encrypt(11)
y <- encrypt(122)

decrypt(add(x, y))
```

    133

Back to the setting of deep learning and the current task to be solved: Have the server apply gradient updates without ever
seeing them. With secret sharing, it would work like this:

Julia, Greg and me each want to train on our own private data. Together, we will be responsible for gradient averaging, that
is, we'll form a *cluster* of *workers* united in that task. Now, the model owner *secret shares* the model, and we start
training, each on their own data. After some number of iterations, we use secure averaging to combine our respective
gradients. Then, all the server gets to see is the mean gradient, and there is no way to determine our respective
contributions.

#### Beyond private gradients

Amazingly, it is even possible to *train* on encrypted data -- amongst others, using that same technique of secret sharing. Of
course, this has to negatively affect training speed. But it's good to know that if one's use case were to demand it, it would
be feasible. (One possible use case is when training on one party's data alone doesn't make any sense, but data is sensitive,
so others won't let you access their data unless encrypted.)

So with encryption available on an all-you-need basis, are we completely safe, privacy-wise? The answer is no. The model can
still leak information. For example, in some cases it is possible to perform *model inversion* \[@abs-1805-04049\], that is,
with just black-box access to a model, train an *attack model* that allows reconstructing some of the original training data.
Needless to say, this kind of leakage has to be avoided. [Differential
privacy](https://blogs.rstudio.com/tensorflow/posts/2019-12-20-differential-privacy/) (Dwork et al. 2006), (Dwork 2006)
demands that results obtained from querying a model be independent from the presence or absence, in the dataset employed for
training, of a single individual. In general, this is ensured by adding noise to the answer to every query. In training deep
learning models, we add noise to the gradients, as well as clip them according to some chosen norm.

At some point, then, we will want all of those in combination: federated learning, encryption, and differential privacy.

*Syft* is a very promising, very actively developed framework that aims for providing all of them. Instead of "aims for", I
should perhaps have written "provides" -- it depends. We need some more context.

## Introducing Syft

Syft -- also known as [PySyft](https://github.com/OpenMined/PySyft), since as of today, its most mature implementation is
written in and for Python -- is maintained by [OpenMined](https://www.openmined.org/), an open source community dedicated to
enabling privacy-preserving AI. It's worth it reproducing their mission statement here:

> Industry standard tools for artificial intelligence have been designed with several assumptions: data is centralized into a
> single compute cluster, the cluster exists in a secure cloud, and the resulting models will be owned by a central authority.
> We envision a world in which we are not restricted to this scenario - a world in which AI tools treat privacy, security, and
> multi-owner governance as first class citizens. \[...\] The mission of the OpenMined community is to create an accessible
> ecosystem of tools for private, secure, multi-owner governed AI.

While far from being the only one, PySyft is their most maturely developed framework. Its role is to provide secure federated
learning, including encryption and differential privacy. For deep learning, it relies on existing frameworks.

PyTorch integration seems the most mature, as of today; with PyTorch, encrypted and differentially private training are
already available. Integration with TensorFlow is a bit more involved; it does not yet include TensorFlow Federated and
TensorFlow Privacy. For encryption, it relies on [TensorFlow Encrypted](https://github.com/tf-encrypted/tf-encrypted) (TFE),
which as of this writing is not an official TensorFlow subproject.

However, even now it is already possible to *secret share* Keras models and administer private predictions. Let's see how.

## Private predictions with Syft, TensorFlow Encrypted and Keras

Our introductory example will show how to use an externally-provided model to classify private data -- without the model owner
ever seeing that data, *and* without the user ever getting hold of (e.g., downloading) the model. (Think about the model owner
wanting to keep the fruits of their labour hidden, as well.)

Put differently: The model is encrypted, and the data is, too. As you might imagine, this involves a cluster of agents,
together performing secure multi-party computation.

This use case presupposing an already trained model, we start by quickly creating one. There is nothing special going on here.

#### Prelude: Train a simple model on MNIST

``` r
# create_model.R

library(tensorflow)
library(keras)

mnist <- dataset_mnist()
mnist$train$x <- mnist$train$x/255
mnist$test$x <- mnist$test$x/255

dim(mnist$train$x) <- c(dim(mnist$train$x), 1)
dim(mnist$test$x) <- c(dim(mnist$test$x), 1)

input_shape <- c(28, 28, 1)

model <- keras_model_sequential() %>%
  layer_conv_2d(filters = 16, kernel_size = c(3, 3), input_shape = input_shape) %>%
  layer_average_pooling_2d(pool_size = c(2, 2)) %>%
  layer_activation("relu") %>%
  layer_conv_2d(filters = 32, kernel_size = c(3, 3)) %>%
  layer_average_pooling_2d(pool_size = c(2, 2)) %>%
  layer_activation("relu") %>%
  layer_conv_2d(filters = 64, kernel_size = c(3, 3)) %>%
  layer_average_pooling_2d(pool_size = c(2, 2)) %>%
  layer_activation("relu") %>%
  layer_flatten() %>%
  layer_dense(units = 10, activation = "linear")
  

model %>% compile(
  loss = "sparse_categorical_crossentropy",
  optimizer = "adam",
  metrics = "accuracy"
)

model %>% fit(
    x = mnist$train$x,
    y = mnist$train$y,
    epochs = 1,
    validation_split = 0.3,
    verbose = 2
)

model$save(filepath = "model.hdf5")
```

#### Set up cluster and serve model

The easiest way to get all required packages is to install the ensemble OpenMined put together for their [Udacity
Course](https://www.udacity.com/course/secure-and-private-ai--ud185) that introduces federated learning and differential
privacy with PySyft. This will install TensorFlow 1.15 and TensorFlow Encrypted, amongst others.

The following lines of code should all be put together in a single file. I found it practical to "source" this script from an
R process running in a console tab.

To begin, we again define the model, two things being different now. First, for technical reasons, we need to pass in
`batch_input_shape` instead of `input_shape`. Second, the final layer is "missing" the softmax activation. This is not an
oversight -- SMPC `softmax` has not been implemented yet. (Depending on when you read this, that statement may no longer be
true.) Were we training this model in *secret sharing* mode, this would of course be a problem; for classification though, all
we care about is the maximum score.

After model definition, we load the actual weights from the model we trained in the previous step. Then, the action begins. We
create an ensemble of TFE workers that together run a distributed TensorFlow cluster. The model is *secret* *shared* with the
workers, that is, model weights are split up into shares that, each inspected alone, are unusable. Finally, the model is
*served*, i.e., made available to clients requesting predictions.

How can a Keras model be *shared* and *served*? These are not methods provided by Keras itself. The magic comes from Syft
*hooking* into Keras, extending the `model` object: cf. `hook <- sy$KerasHook(tf$keras)` right after we import Syft.

``` r
# serve.R
# you could start R on the console and "source" this file

# do this just once
reticulate::py_install("syft[udacity]")

library(tensorflow)
library(keras)

sy <- reticulate::import(("syft"))
hook <- sy$KerasHook(tf$keras)

batch_input_shape <- c(1, 28, 28, 1)

model <- keras_model_sequential() %>%
 layer_conv_2d(filters = 16, kernel_size = c(3, 3), batch_input_shape = batch_input_shape) %>%
 layer_average_pooling_2d(pool_size = c(2, 2)) %>%
 layer_activation("relu") %>%
 layer_conv_2d(filters = 32, kernel_size = c(3, 3)) %>%
 layer_average_pooling_2d(pool_size = c(2, 2)) %>%
 layer_activation("relu") %>%
 layer_conv_2d(filters = 64, kernel_size = c(3, 3)) %>%
 layer_average_pooling_2d(pool_size = c(2, 2)) %>%
 layer_activation("relu") %>%
 layer_flatten() %>%
 layer_dense(units = 10) 
 
pre_trained_weights <- "model.hdf5"
model$load_weights(pre_trained_weights)

# create and start TFE cluster
AUTO <- TRUE
julia <- sy$TFEWorker(host = 'localhost:4000', auto_managed = AUTO)
greg <- sy$TFEWorker(host = 'localhost:4001', auto_managed = AUTO)
me <- sy$TFEWorker(host = 'localhost:4002', auto_managed = AUTO)
cluster <- sy$TFECluster(julia, greg, me)
cluster$start()

# split up model weights into shares 
model$share(cluster)

# serve model (limiting number of requests)
model$serve(num_requests = 3L)
```

Once the desired number of requests have been served, we can go to this R process, stop model sharing, and shut down the
cluster:

``` r
# stop model sharing
model$stop()

# stop cluster
cluster$stop()
```

Now, on to the client(s).

#### Request predictions on private data

In our example, we have one client. The client is a TFE worker, just like the agents that make up the cluster.

We define the cluster here, client-side, as well; create the client; and connect the client to the model. This will set up a
queueing server that takes care of *secret sharing* all input data before submitting them for prediction.

Finally, we have the client asking for classification of the first three MNIST images.

With the server running in some different R process, we can conveniently run this in RStudio:

``` r
# client.R

library(tensorflow)
library(keras)

sy <- reticulate::import(("syft"))
hook <- sy$KerasHook(tf$keras)

mnist <- dataset_mnist()
mnist$train$x <- mnist$train$x/255
mnist$test$x <- mnist$test$x/255

dim(mnist$train$x) <- c(dim(mnist$train$x), 1)
dim(mnist$test$x) <- c(dim(mnist$test$x), 1)

batch_input_shape <- c(1, 28, 28, 1)
batch_output_shape <- c(1, 10)

# define the same TFE cluster
AUTO <- TRUE
julia <- sy$TFEWorker(host = 'localhost:4000', auto_managed = AUTO)
greg <- sy$TFEWorker(host = 'localhost:4001', auto_managed = AUTO)
me <- sy$TFEWorker(host = 'localhost:4002', auto_managed = AUTO)
cluster <- sy$TFECluster(julia, greg, me)

# create the client
client <- sy$TFEWorker()

# create a queueing server on the client that secret shares the data 
# before submitting a prediction request
client$connect_to_model(batch_input_shape, batch_output_shape, cluster)

num_tests <- 3
images <- mnist$test$x[1: num_tests, , , , drop = FALSE]
expected_labels <- mnist$test$y[1: num_tests]

for (i in 1:num_tests) {
  res <- client$query_model(images[i, , , , drop = FALSE])
  predicted_label <- which.max(res) - 1
  cat("Actual: ", expected_labels[i], ", predicted: ", predicted_label)
}
```

    Actual:  7 , predicted:  7 
    Actual:  2 , predicted:  2 
    Actual:  1 , predicted:  1 

There we go. Both model and data did remain secret, yet we were able to classify our data.

Let's wrap up.

## Conclusion

Our example use case has not been too ambitious -- we started with a trained model, thus leaving aside federated learning.
Keeping the setup simple, we were able to focus on underlying principles: *Secret sharing* as a means of encryption, and
setting up a Syft/TFE cluster of workers that together, provide the infrastructure for encrypting model weights as well as
client data.

In case you've read our previous post on [TensorFlow
Federated](https://blogs.rstudio.com/tensorflow/posts/2019-12-20-differential-privacy/) -- that, too, a framework under
development -- you may have gotten an impression similar to the one I got: Setting up Syft was a lot more straightforward,
concepts were easy to grasp, and surprisingly little code was required. As we may gather from a [recent blog
post](https://blog.openmined.org/introducing-pysyft-tensorflow/), integration of Syft with TensorFlow Federated and TensorFlow
Privacy are on the roadmap. I am looking forward *a lot* for this to happen.

Thanks for reading!

## 

Dwork, Cynthia. 2006. "Differential Privacy." *33rd International Colloquium on Automata, Languages and Programming, Part II (ICALP 2006)*, Lecture notes in computer science, vol. 4052: 1--12. <https://www.microsoft.com/en-us/research/publication/differential-privacy/>.

Dwork, Cynthia, Frank McSherry, Kobbi Nissim, and Adam Smith. 2006. "Calibrating Noise to Sensitivity in Private Data Analysis." *Proceedings of the Third Conference on Theory of Cryptography* (Berlin, Heidelberg), TCC'06, 265--84. <https://doi.org/10.1007/11681878_14>.

McMahan, H. Brendan, Eider Moore, Daniel Ramage, and Blaise Agüera y Arcas. 2016. "Federated Learning of Deep Networks Using Model Averaging." *CoRR* abs/1602.05629. <http://arxiv.org/abs/1602.05629>.
