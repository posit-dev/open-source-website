---
title: "tfhub: R interface to TensorFlow Hub"
description: |
  TensorFlow Hub is a library for the publication, discovery, and consumption of reusable parts of machine learning models. A module is a self-contained piece of a TensorFlow graph, along with its weights and assets, that can be reused across different tasks in a process known as transfer learning.
date: 2019-12-18
categories:
  - TensorFlow/Keras
  - Packages/Releases
author:
  - name: Daniel Falbel
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Daniel Falbel
image: thumbnail.png
ported_from: ai
port_status: raw
---



We are pleased to announce that the first version of [tfhub](https://github.com/rstudio/tfhub) is now on CRAN. tfhub is an R interface to TensorFlow Hub - a library for the publication, discovery, and consumption of reusable parts of machine learning models. A module is a self-contained piece of a TensorFlow graph, along with its weights and assets, that can be reused across different tasks in a process known as transfer learning.

The CRAN version of tfhub can be installed with:

``` r
install.packages("tfhub")
```

After installing the R package you need to install the TensorFlow Hub python package. You can do it by running:

``` r
tfhub::install_tfhub()
```

## Getting started

The essential function of tfhub is `layer_hub` which works just like a [keras](https://github.com/rstudio/keras) layer but allows you to load a complete pre-trained deep learning model.

For example you can:

``` r
library(tfhub)
layer_mobilenet <- layer_hub(
  handle = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
)
```

This will download the MobileNet model pre-trained on the ImageNet dataset. tfhub models are cached locally and don't need to be downloaded the next time you use the same model.

You can now use `layer_mobilenet` as a usual Keras layer. For example you can define a model:

``` r
library(keras)
input <- layer_input(shape = c(224, 224, 3))
output <- layer_mobilenet(input)
model <- keras_model(input, output)
summary(model)
```

    Model: "model"
    ____________________________________________________________________
    Layer (type)                  Output Shape               Param #    
    ====================================================================
    input_2 (InputLayer)          [(None, 224, 224, 3)]      0          
    ____________________________________________________________________
    keras_layer_1 (KerasLayer)    (None, 1001)               3540265    
    ====================================================================
    Total params: 3,540,265
    Trainable params: 0
    Non-trainable params: 3,540,265
    ____________________________________________________________________

This model can now be used to predict Imagenet labels for an image. For example, let's see the results for the famous Grace Hopper's photo:

<figure>
<img src="images/grace-hopper.jpg" style="width:30.0%" alt="Grace Hopper" />
<figcaption aria-hidden="true">Grace Hopper</figcaption>
</figure>

``` r
img <- image_load("images/grace-hopper.jpg", target_size = c(224,224)) %>% 
  image_to_array()
img <- img/255
dim(img) <- c(1, dim(img))
pred <- predict(model, img)
imagenet_decode_predictions(pred[,-1,drop=FALSE])[[1]]
```

      class_name class_description    score
    1  n03763968  military_uniform 9.760404
    2  n02817516          bearskin 5.922512
    3  n04350905              suit 5.729345
    4  n03787032       mortarboard 5.400651
    5  n03929855       pickelhaube 5.008665

TensorFlow Hub also offers many other pre-trained image, text and video models.
All possible models can be found on the TensorFlow hub [website](https://tfhub.dev).

<figure>
<img src="images/tfhub.png" alt="TensorFlow Hub" />
<figcaption aria-hidden="true">TensorFlow Hub</figcaption>
</figure>

You can find more examples of `layer_hub` usage in the following articles on the TensorFlow for R website:

- [Transfer Learning with tfhub](https://tensorflow.rstudio.com/tutorials/beginners/basic-ml/tutorial_basic_text_classification_with_tfhub/)
- [Using tfhub with Keras](https://tensorflow.rstudio.com/guide/tfhub/hub-with-keras/)
- [tfhub Basics](https://tensorflow.rstudio.com/guide/tfhub/intro/)
- [Text classification example](https://tensorflow.rstudio.com/guide/tfhub/examples/text_classification/)

## Usage with Recipes and the Feature Spec API

tfhub also offers [recipes](https://github.com/tidymodels/recipes) steps to make
it easier to use pre-trained deep learning models in your machine learning workflow.

For example, you can define a recipe that uses a pre-trained text embedding model with:

``` r
rec <- recipe(obscene ~ comment_text, data = train) %>%
  step_pretrained_text_embedding(
    comment_text,
    handle = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim-with-oov/1"
  ) %>%
  step_bin2factor(obscene)
```

You can see a complete running example [here](https://tensorflow.rstudio.com/guide/tfhub/examples/recipes/).

You can also use tfhub with the new [Feature Spec API](https://tensorflow.rstudio.com/guide/tfdatasets/feature_spec/) implemented in tfdatasets. You can see a complete example [here](https://tensorflow.rstudio.com/guide/tfhub/examples/feature_column/).

We hope our readers have fun experimenting with Hub models and/or can put them to good use. If you run into any problems, let us know by creating an issue in the tfhub repository
