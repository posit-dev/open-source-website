---
draft: true
title: "Keras for R"
description: |
  We are excited to announce that the keras package is now available on CRAN. The package provides an R interface to Keras, a high-level neural networks API developed with a focus on enabling fast experimentation.
date: 2017-09-05
categories:
  - TensorFlow/Keras
  - Packages/Releases
author:
  - name: J.J. Allaire
    url: https://github.com/jjallaire
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com
people:
  - J.J. Allaire
image: thumbnail.png
ported_from: ai
port_status: in-progress
---



We are excited to announce that the [keras package](https://tensorflow.rstudio.com/keras) is now available on CRAN. The package provides an R interface to [Keras](https://keras.io), a high-level neural networks API developed with a focus on enabling fast experimentation. Keras has the following key features:

- Allows the same code to run on CPU or on GPU, seamlessly.

- User-friendly API which makes it easy to quickly prototype deep learning models.

- Built-in support for convolutional networks (for computer vision), recurrent networks (for sequence processing), and any combination of both.

- Supports arbitrary network architectures: multi-input or multi-output models, layer sharing, model sharing, etc. This means that Keras is appropriate for building essentially any deep learning model, from a memory network to a neural Turing machine.

- Is capable of running on top of multiple back-ends including [TensorFlow](https://github.com/tensorflow/tensorflow), [CNTK](https://github.com/Microsoft/cntk), or [Theano](https://github.com/Theano/Theano).

If you are already familiar with Keras and want to jump right in, check out <https://tensorflow.rstudio.com/keras> which has everything you need to get started including over 20 complete examples to learn from.

To learn a bit more about Keras and why we're so excited to announce the Keras interface for R, read on!

## Keras and Deep Learning

Interest in deep learning has been accelerating rapidly over the past few years, and several deep learning frameworks have emerged over the same time frame. Of all the available frameworks, Keras has stood out for its productivity, flexibility and user-friendly API. At the same time, TensorFlow has emerged as a next-generation machine learning platform that is both extremely flexible and well-suited to production deployment.

Not surprisingly, Keras and TensorFlow have of late been pulling away from other deep learning frameworks:

<blockquote class="twitter-tweet" data-lang="en">
<p lang="en" dir="ltr">
Google web search interest around deep learning frameworks over time. If you remember Q4 2015 and Q1-2 2016 as confusing, you weren\'t alone. <a href="https://t.co/1f1VQVGr8n">pic.twitter.com/1f1VQVGr8n</a>
</p>
--- François Chollet (@fchollet) <a href="https://twitter.com/fchollet/status/871089784898310144">June 3, 2017</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The good news about Keras and TensorFlow is that you don't need to choose between them! The default backend for Keras is TensorFlow and Keras can be [integrated seamlessly](https://blog.keras.io/keras-as-a-simplified-interface-to-tensorflow-tutorial.html) with TensorFlow workflows. There is also a pure-TensorFlow implementation of Keras with [deeper integration](https://www.youtube.com/watch?v=UeheTiBJ0Io&t=7s&index=8&list=PLOU2XLYxmsIKGc_NBoIhTn2Qhraji53cv) on the roadmap for later this year.

Keras and TensorFlow are the state of the art in deep learning tools and with the keras package you can now access both with a fluent R interface.

## Getting Started

### Installation

To begin, install the keras R package from CRAN as follows:

``` r
install.packages("keras")
```

The Keras R interface uses the [TensorFlow](https://www.tensorflow.org/) backend engine by default. To install both the core Keras library as well as the TensorFlow backend use the `install_keras()` function:

``` r
library(keras)
install_keras()
```

This will provide you with default CPU-based installations of Keras and TensorFlow. If you want a more customized installation, e.g. if you want to take advantage of NVIDIA GPUs, see the documentation for [`install_keras()`](https://tensorflow.rstudio.com/keras/reference/install_keras.html).

### MNIST Example

We can learn the basics of Keras by walking through a simple example: recognizing handwritten digits from the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset. MNIST consists of 28 x 28 grayscale images of handwritten digits like these:

<img style="width: 50%;" src="https://www.tensorflow.org/images/MNIST.png">

The dataset also includes labels for each image, telling us which digit it is. For example, the labels for the above images are 5, 0, 4, and 1.

#### Preparing the Data

The MNIST dataset is included with Keras and can be accessed using the `dataset_mnist()` function. Here we load the dataset then create variables for our test and training data:

``` r
library(keras)
mnist <- dataset_mnist()
x_train <- mnist$train$x
y_train <- mnist$train$y
x_test <- mnist$test$x
y_test <- mnist$test$y
```

The `x` data is a 3-d array `(images,width,height)` of grayscale values. To prepare the data for training we convert the 3-d arrays into matrices by reshaping width and height into a single dimension (28x28 images are flattened into length 784 vectors). Then, we convert the grayscale values from integers ranging between 0 to 255 into floating point values ranging between 0 and 1:

``` r
# reshape
dim(x_train) <- c(nrow(x_train), 784)
dim(x_test) <- c(nrow(x_test), 784)
# rescale
x_train <- x_train / 255
x_test <- x_test / 255
```

The `y` data is an integer vector with values ranging from 0 to 9. To prepare this data for training we [one-hot encode](https://www.quora.com/What-is-one-hot-encoding-and-when-is-it-used-in-data-science) the vectors into binary class matrices using the Keras `to_categorical()` function:

``` r
y_train <- to_categorical(y_train, 10)
y_test <- to_categorical(y_test, 10)
```

#### Defining the Model

The core data structure of Keras is a model, a way to organize layers. The simplest type of model is the [sequential model](https://tensorflow.rstudio.com/keras/articles/sequential_model.html), a linear stack of layers.

We begin by creating a sequential model and then adding layers using the pipe (`%>%`) operator:

``` r
model <- keras_model_sequential() 
model %>% 
  layer_dense(units = 256, activation = "relu", input_shape = c(784)) %>% 
  layer_dropout(rate = 0.4) %>% 
  layer_dense(units = 128, activation = "relu") %>%
  layer_dropout(rate = 0.3) %>%
  layer_dense(units = 10, activation = "softmax")
```

The `input_shape` argument to the first layer specifies the shape of the input data (a length 784 numeric vector representing a grayscale image). The final layer outputs a length 10 numeric vector (probabilities for each digit) using a [softmax activation function](https://en.wikipedia.org/wiki/Softmax_function).

Use the `summary()` function to print the details of the model:

``` r
summary(model)
```

<pre style="box-shadow: none;"><code>Model
________________________________________________________________________________
Layer (type)                        Output Shape                    Param #     
================================================================================
dense_1 (Dense)                     (None, 256)                     200960      
________________________________________________________________________________
dropout_1 (Dropout)                 (None, 256)                     0           
________________________________________________________________________________
dense_2 (Dense)                     (None, 128)                     32896       
________________________________________________________________________________
dropout_2 (Dropout)                 (None, 128)                     0           
________________________________________________________________________________
dense_3 (Dense)                     (None, 10)                      1290        
================================================================================
Total params: 235,146
Trainable params: 235,146
Non-trainable params: 0
________________________________________________________________________________</code></pre>

Next, compile the model with appropriate loss function, optimizer, and metrics:

``` r
model %>% compile(
  loss = "categorical_crossentropy",
  optimizer = optimizer_rmsprop(),
  metrics = c("accuracy")
)
```

#### Training and Evaluation

Use the `fit()` function to train the model for 30 epochs using batches of 128 images:

``` r
history <- model %>% fit(
  x_train, y_train, 
  epochs = 30, batch_size = 128, 
  validation_split = 0.2
)
```

The `history` object returned by `fit()` includes loss and accuracy metrics which we can plot:

``` r
plot(history)
```

![](https://keras.rstudio.com/images/training_history_ggplot2.png)

Evaluate the model's performance on the test data:

``` r
model %>% evaluate(x_test, y_test,verbose = 0)
```

    $loss
    [1] 0.1149

    $acc
    [1] 0.9807

Generate predictions on new data:

``` r
model %>% predict_classes(x_test)
```

      [1] 7 2 1 0 4 1 4 9 5 9 0 6 9 0 1 5 9 7 3 4 9 6 6 5 4 0 7 4 0 1 3 1 3 4 7 2 7 1 2
     [40] 1 1 7 4 2 3 5 1 2 4 4 6 3 5 5 6 0 4 1 9 5 7 8 9 3 7 4 6 4 3 0 7 0 2 9 1 7 3 2
     [79] 9 7 7 6 2 7 8 4 7 3 6 1 3 6 9 3 1 4 1 7 6 9
     [ reached getOption("max.print") -- omitted 9900 entries ]

Keras provides a vocabulary for building deep learning models that is simple, elegant, and intuitive. Building a question answering system, an image classification model, a neural Turing machine, or any other model is just as straightforward.

The [Guide to the Sequential Model](https://tensorflow.rstudio.com/keras/articles/sequential_model.html) article describes the basics of Keras sequential models in more depth.

## Examples

Over 20 complete examples are available (special thanks to [@dfalbel](https://github.com/dfalbel) for his work on these!). The examples cover image classification, text generation with stacked LSTMs, question-answering with memory networks, transfer learning, variational encoding, and more.

| Example | Description |
|--------------------------------------|----------------------------------|
| [addition_rnn](https://tensorflow.rstudio.com/keras/articles/examples/addition_rnn.html) | Implementation of sequence to sequence learning for performing addition of two numbers (as strings). |
| [babi_memnn](https://tensorflow.rstudio.com/keras/articles/examples/babi_memnn.html) | Trains a memory network on the bAbI dataset for reading comprehension. |
| [babi_rnn](https://tensorflow.rstudio.com/keras/articles/examples/babi_rnn.html) | Trains a two-branch recurrent network on the bAbI dataset for reading comprehension. |
| [cifar10_cnn](https://tensorflow.rstudio.com/keras/articles/examples/cifar10_cnn.html) | Trains a simple deep CNN on the CIFAR10 small images dataset. |
| [conv_lstm](https://tensorflow.rstudio.com/keras/articles/examples/conv_lstm.html) | Demonstrates the use of a convolutional LSTM network. |
| [deep_dream](https://tensorflow.rstudio.com/keras/articles/examples/deep_dream.html) | Deep Dreams in Keras. |
| [imdb_bidirectional_lstm](https://tensorflow.rstudio.com/keras/articles/examples/imdb_bidirectional_lstm.html) | Trains a Bidirectional LSTM on the IMDB sentiment classification task. |
| [imdb_cnn](https://tensorflow.rstudio.com/keras/articles/examples/imdb_cnn.html) | Demonstrates the use of Convolution1D for text classification. |
| [imdb_cnn_lstm](https://tensorflow.rstudio.com/keras/articles/examples/imdb_cnn_lstm.html) | Trains a convolutional stack followed by a recurrent stack network on the IMDB sentiment classification task. |
| [imdb_fasttext](https://tensorflow.rstudio.com/keras/articles/examples/imdb_fasttext.html) | Trains a FastText model on the IMDB sentiment classification task. |
| [imdb_lstm](https://tensorflow.rstudio.com/keras/articles/examples/imdb_lstm.html) | Trains a LSTM on the IMDB sentiment classification task. |
| [lstm_text_generation](https://tensorflow.rstudio.com/keras/articles/examples/lstm_text_generation.html) | Generates text from Nietzsche's writings. |
| [mnist_acgan](https://tensorflow.rstudio.com/keras/articles/examples/mnist_acgan.html) | Implementation of AC-GAN (Auxiliary Classifier GAN ) on the MNIST dataset |
| [mnist_antirectifier](https://tensorflow.rstudio.com/keras/articles/examples/mnist_antirectifier.html) | Demonstrates how to write custom layers for Keras |
| [mnist_cnn](https://tensorflow.rstudio.com/keras/articles/examples/mnist_cnn.html) | Trains a simple convnet on the MNIST dataset. |
| [mnist_irnn](https://tensorflow.rstudio.com/keras/articles/examples/mnist_irnn.html) | Reproduction of the IRNN experiment with pixel-by-pixel sequential MNIST in "A Simple Way to Initialize Recurrent Networks of Rectified Linear Units" by Le et al. |
| [mnist_mlp](https://tensorflow.rstudio.com/keras/articles/examples/mnist_mlp.html) | Trains a simple deep multi-layer perceptron on the MNIST dataset. |
| [mnist_hierarchical_rnn](https://tensorflow.rstudio.com/keras/articles/examples/mnist_hierarchical_rnn.html) | Trains a Hierarchical RNN (HRNN) to classify MNIST digits. |
| [mnist_transfer_cnn](https://tensorflow.rstudio.com/keras/articles/examples/mnist_transfer_cnn.html) | Transfer learning toy example. |
| [neural_style_transfer](https://tensorflow.rstudio.com/keras/articles/examples/neural_style_transfer.html) | Neural style transfer (generating an image with the same "content" as a base image, but with the "style" of a different picture). |
| [reuters_mlp](https://tensorflow.rstudio.com/keras/articles/examples/reuters_mlp.html) | Trains and evaluates a simple MLP on the Reuters newswire topic classification task. |
| [stateful_lstm](https://tensorflow.rstudio.com/keras/articles/examples/stateful_lstm.html) | Demonstrates how to use stateful RNNs to model long sequences efficiently. |
| [variational_autoencoder](https://tensorflow.rstudio.com/keras/articles/examples/variational_autoencoder.html) | Demonstrates how to build a variational autoencoder. |
| [variational_autoencoder_deconv](https://tensorflow.rstudio.com/keras/articles/examples/variational_autoencoder_deconv.html) | Demonstrates how to build a variational autoencoder with Keras using deconvolution layers. |

## Learning More

After you've become familiar with the basics, these articles are a good next step:

- [Guide to the Sequential Model](https://tensorflow.rstudio.com/keras/articles/sequential_model.html). The sequential model is a linear stack of layers and is the API most users should start with.

- [Guide to the Functional API](https://tensorflow.rstudio.com/keras/articles/functional_api.html). The Keras functional API is the way to go for defining complex models, such as multi-output models, directed acyclic graphs, or models with shared layers.

- [Training Visualization](https://tensorflow.rstudio.com/keras/articles/training_visualization.html). There are a wide variety of tools available for visualizing training. These include plotting of training metrics, real time display of metrics within the RStudio IDE, and integration with the TensorBoard visualization tool included with TensorFlow.

- [Using Pre-Trained Models](https://tensorflow.rstudio.com/keras/articles/applications.html). Keras includes a number of deep learning models (Xception, VGG16, VGG19, ResNet50, InceptionVV3, and MobileNet) that are made available alongside pre-trained weights. These models can be used for prediction, feature extraction, and fine-tuning.

- [Frequently Asked Questions](https://tensorflow.rstudio.com/keras/articles/faq.html). Covers many additional topics including streaming training data, saving models, training on GPUs, and more.

Keras provides a productive, highly flexible framework for developing deep learning models. We can't wait to see what the R community will do with these tools!
