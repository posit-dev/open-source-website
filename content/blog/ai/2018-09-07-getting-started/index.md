---
title: "Getting started with deep learning in R"
description: |
  Many fields are benefiting from the use of deep learning, and with the R keras, tensorflow and related packages, you can now easily do state of the art deep learning in R. In this post, we want to give some orientation as to how to best get started.
date: 2018-09-07
slug: keydana2018gettingstarted
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.png
ported_from: ai
port_status: in-progress
software: ["keras3"]
languages: ["R"]
categories:
  - Machine Learning
ported_categories:
  - TensorFlow/Keras
---



There are good reasons to get into deep learning: Deep learning has been outperforming the respective "classical" techniques in areas like image recognition and natural language processing for a while now, and it has the potential to bring interesting insights even to the analysis of tabular data. For many R users interested in deep learning, the hurdle is not so much the mathematical prerequisites (as many have a background in statistics or empirical sciences), but rather how to get started in an efficient way.

This post will give an overview of some materials that should prove useful. In the case that you don't have that background in statistics or similar, we will also present a few helpful resources to catch up with "the math".

## Keras tutorials

The easiest way to get started is using the Keras API. It is a high-level, declarative (in feel) way of specifying a model, training and testing it, originally developed in [Python](http://keras.io) by Francois Chollet and ported to R by JJ Allaire.

Check out the tutorials on the [Keras website](https://tensorflow.rstudio.com/keras/): They introduce basic tasks like classification and regression, as well as basic workflow elements like saving and restoring models, or assessing model performance.

- [Basic classification](https://tensorflow.rstudio.com/keras/articles/tutorial_basic_classification.html) gets you started doing image classification using the *Fashion MNIST* dataset.

- [Text classification](https://tensorflow.rstudio.com/keras/articles/tutorial_basic_text_classification.html) shows how to do sentiment analysis on movie reviews, and includes the important topic of how to preprocess text for deep learning.

- [Basic regression](https://tensorflow.rstudio.com/keras/articles/tutorial_basic_regression.html) demonstrates the task of predicting a continuous variable by example of the famous Boston housing dataset that ships with Keras.

- [Overfitting and underfitting](https://tensorflow.rstudio.com/keras/articles/tutorial_overfit_underfit.html) explains how you can assess if your model is under- or over-fitting, and what remedies to take.

- Last but not least, [Save and restore models](https://tensorflow.rstudio.com/keras/articles/tutorial_save_and_restore.html) shows how to save checkpoints during and after training, so you don't lose the fruit of the network's labor.

Once you've seen the basics, the website also has more advanced information on implementing custom logic, monitoring and tuning, as well as using and adapting pre-trained models.

## Videos and book

If you want a bit more conceptual background, the [Deep Learning with R in motion](https://bit.ly/2oPtXWv) video series provides a nice introduction to basic concepts of machine learning and deep learning, including things often taken for granted, such as derivatives and gradients.

<figure>
<a href="https://bit.ly/2oPtXWv"><img src="images/dl_in_motion.png" class="l-body" style="border: 1px solid rgba(0, 0, 0, 0.2);" /></a>
<figcaption>Example from Deep Learning with R in motion, video 2.7, <em>From Derivatives to Gradients</em></figcaption>
</figure>

The first 2 components of the video series ([Getting Started](https://bit.ly/2oPtXWv) and the [MNIST Case Study](https://bit.ly/2MY6YHj)) are free. The remainder of the videos introduce different neural network architectures by way of detailed case studies.

The series is a companion to the [Deep Learning with R](https://www.amazon.com/Deep-Learning-R-Francois-Chollet/dp/161729554X) book by Francois Chollet and JJ Allaire. Like the videos, the book has excellent, high-level explanations of deep learning concepts. At the same time, it contains lots of ready-to-use code, presenting examples for all the major architectures and use cases (including fancy stuff like variational autoencoders and GANs).

<aside>
[<img src="images/dlwR.png" style="border: 1px solid rgba(0, 0, 0, 0.2);" width="100" />](https://www.amazon.com/Deep-Learning-R-Francois-Chollet/dp/161729554X)
</aside>

## Inspiration

If you're not pursuing a specific goal, but in general curious about what can be done with deep learning, a good place to follow is the [TensorFlow for R Blog](https://blogs.rstudio.com/tensorflow/). There, you'll find applications of deep learning to business as well as scientific tasks, as well as technical expositions and introductions to new features.

In addition, the [TensorFlow for R Gallery](https://blogs.rstudio.com/tensorflow/gallery.html) highlights several case studies that have proven especially useful for getting started in various areas of application.

## Reality

Once the ideas are there, realization should follow, and for most of us the question will be: Where can I actually *train* that model? As soon as real-world-size images are involved, or other kinds of higher-dimensional data, you'll need a modern, high performance GPU so training on your laptop won't be an option any more.

There are a few different ways you can train in the cloud:

- RStudio provides [Amazon EC2 AMIs for cloud GPU instances](https://tensorflow.rstudio.com/tools/cloud_server_gpu.html). The AMI has both RStudio Server and the R TensorFlow package suite preinstalled.

- You can also try out [Paperspace cloud GPU desktops](https://tensorflow.rstudio.com/tools/cloud_desktop_gpu.html) (again with the RStudio and the R TensorFlow package suite preinstalled).

- The *cloudml* package provides an [interface to the Google Cloud Machine Learning engine](https://tensorflow.rstudio.com/tools/cloudml/articles/getting_started.html), which makes it easy to submit batch GPU training jobs to CloudML.

## More background

If you don't have a very "mathy" background, you might feel that you'd like to supplement the concepts-focused approach from *Deep Learning with R* with a bit more low-level basics (just as some people feel the need to know at least a bit of C or Assembler when learning a high-level language).

Personal recommendations for such cases would include Andrew Ng's [deep learning specialization](https://www.coursera.org/specializations/deep-learning) on Coursera (videos are free to watch), and the book(s) and recorded lectures on linear algebra by [Gilbert Strang](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/).

Of course, the ultimate reference on deep learning, as of today, is the [Deep Learning](https://www.deeplearningbook.org) textbook by Ian Goodfellow, Yoshua Bengio and Aaron Courville. The book covers everything from background in linear algebra, probability theory and optimization via basic architectures such as CNNs or RNNs, on to unsupervised models on the frontier of the very latest research.

## Getting help

Last not least, should you encounter problems with the software (or with mapping your task to runnable code), a good idea is to create a GitHub issue in the respective repository, e.g., [rstudio/keras](https://github.com/rstudio/keras/).

Best of luck for your deep learning journey with R!
