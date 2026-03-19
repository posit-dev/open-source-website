---
title: "Deep Learning with R, 2nd Edition"
description: |
  Announcing the release of "Deep Learning with R, 2nd Edition," a book that shows you how to get started with deep learning in R.
date: 2022-05-31T00:00:00.000Z
slug: kalinowskiDLwR2e
author:
  - name: Tomasz Kalinowski
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Tomasz Kalinowski
image: thumbnail.png
ported_from: ai
port_status: in-progress
software: ["keras3"]
languages: ["R"]
categories:
  - Machine Learning
ported_categories:
  - TensorFlow/Keras
  - R
---



Today we're pleased to announce the launch of [*Deep Learning with R,
2nd Edition*](https://rstd.io/dlwr-2e). Compared to the first edition,
the book is over a third longer, with more than 75% new content. It's
not so much an updated edition as a whole new book.

This book shows you how to get started with deep learning in R, even if
you have no background in mathematics or data science. The book covers:

- Deep learning from first principles

- Image classification and image segmentation

- Time series forecasting

- Text classification and machine translation

- Text generation, neural style transfer, and image generation

Only modest R knowledge is assumed; everything else is explained from
the ground up with examples that plainly demonstrate the mechanics.
Learn about gradients and backpropogation---by using `tf$GradientTape()`
to rediscover Earth's gravity acceleration constant (9.8 $m/s^2$). Learn
what a keras `Layer` is---by implementing one from scratch using only
base R. Learn the difference between batch normalization and layer
normalization, what `layer_lstm()` does, what happens when you call
`fit()`, and so on---all through implementations in plain R code.

Every section in the book has received major updates. The chapters on
computer vision gain a full walk-through of how to approach an image
segmentation task. Sections on image classification have been updated to
use {tfdatasets} and Keras preprocessing layers, demonstrating not just
how to compose an efficient and fast data pipeline, but also how to
adapt it when your dataset calls for it.

The chapters on text models have been completely reworked. Learn how to
preprocess raw text for deep learning, first by implementing a text
vectorization layer using only base R, before using
`keras::layer_text_vectorization()` in nine different ways. Learn about
embedding layers by implementing a custom
`layer_positional_embedding()`. Learn about the transformer architecture
by implementing a custom `layer_transformer_encoder()` and
`layer_transformer_decoder()`. And along the way put it all together by
training text models---first, a movie-review sentiment classifier, then,
an English-to-Spanish translator, and finally, a movie-review text
generator.

Generative models have their own dedicated chapter, covering not only
text generation, but also variational auto encoders (VAE), generative
adversarial networks (GAN), and style transfer.

Along each step of the way, you'll find sprinkled intuitions distilled
from experience and empirical observation about what works, what
doesn't, and why. Answers to questions like: when should you use
bag-of-words instead of a sequence architecture? When is it better to
use a pretrained model instead of training a model from scratch? When
should you use GRU instead of LSTM? When is it better to use separable
convolution instead of regular convolution? When training is unstable,
what troubleshooting steps should you take? What can you do to make
training faster?

The book shuns magic and hand-waving, and instead pulls back the curtain
on every necessary fundamental concept needed to apply deep learning.
After working through the material in the book, you will not only know
how to apply deep learning to common tasks, but also have the context to
go and apply deep learning to new domains and new problems.

[*Deep Learning with R, Second Edition*](https://rstd.io/dlwr-2e)
