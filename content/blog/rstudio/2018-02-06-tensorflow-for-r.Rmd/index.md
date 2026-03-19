---
title: TensorFlow for R
people:
  - Tareef Kawaf
date: '2018-02-06'
categories:
  - Machine Learning
tags:
  - data science
  - Packages
slug: tensorflow-for-r
blogcategories:
  - Products and Technology
ported_from: rstudio
port_status: in-progress
software: ["tensorflow"]
languages: ["R"]
ported_categories:
  - Packages
---



Over the past year we've been hard at work on creating R interfaces to [TensorFlow](https://tensorflow.rstudio.com/), an open-source machine learning framework from Google. We are excited about TensorFlow for many reasons, not the least of which is its state-of-the-art infrastructure for deep learning applications. 

In the 2 years since it was initially open-sourced by Google, TensorFlow has rapidly become the [framework of choice](https://twitter.com/fchollet/status/871089784898310144?lang=en) for both machine learning practitioners and researchers. On Saturday, we formally announced our work on TensorFlow during J.J. Allaire's keynote at [rstudio::conf](https://www.rstudio.com/conference/):

<iframe width="711" height="400" src="https://www.youtube.com/embed/atiYXm7JZv0?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

In the keynote, J.J. describes not only the work we've done on TensorFlow but also discusses deep learning more broadly (what it is, how it works, and where it might be relevant to users of R in the years ahead). 

## New packages and tools

The R interface to TensorFlow consists of a suite of R packages that provide a variety of interfaces to TensorFlow for different tasks and levels of abstraction, including:

- [keras](https://tensorflow.rstudio.com/keras/)---A high-level interface for neural networks, with a focus on enabling fast experimentation.

- [tfestimators](https://tensorflow.rstudio.com/tfestimators/)--- Implementations of common model types such as regressors and classifiers. 

- [tensorflow](https://tensorflow.rstudio.com/tensorflow/)---Low-level interface to the TensorFlow computational graph.

- [tfdatasets](https://tensorflow.rstudio.com/tools/tfdatasets/)---Scalable input pipelines for TensorFlow models. 

Besides the various R interfaces to TensorFlow, there are tools to help with training workflow, including real time feedback on training metrics within the RStudio IDE:

![](/blog-images/2018-02-06-keras-training-metrics.gif)

The [tfruns package](https://tensorflow.rstudio.com/tools/tfruns/) provides tools to track, and manage TensorFlow training runs and experiments:

![](/blog-images/2018-02-06-tfruns.png){style="border: solid 1px #cccccc;"}

## Access to GPUs

Training convolutional or recurrent neural networks can be extremely computationally expensive, and benefits significantly from access to a recent high-end NVIDIA GPU. However, most users don't have this sort of hardware available locally. To address this we have provided a number of ways to use GPUs in the cloud, including:

- The [cloudml package](https://tensorflow.rstudio.com/tools/cloudml/), an R interface to Google's hosted machine learning engine. 

- [RStudio Server with Tensorflow-GPU for AWS](https://tensorflow.rstudio.com/tools/cloud_server_gpu.html#amazon-ec2) (an Amazon EC2 image preconfigured with NVIDIA CUDA drivers, TensorFlow, the TensorFlow for R interface, as well as RStudio Server).

- Detailed instructions for setting up an Ubuntu 16.04 [cloud desktop with a GPU](https://tensorflow.rstudio.com/tools/cloud_desktop_gpu.html) using the Paperspace service.

There is also documentation on [setting up a GPU](https://tensorflow.rstudio.com/tools/local_gpu.html) on your local workstation if you already have the required NVIDIA GPU hardware.

## Learning resources

We've also made a significant investment in learning resources, all of these resources are available on the TensorFlow for R website at https://tensorflow.rstudio.com.

Some of the learning resources include:

|  |  |
|-----------------|---------------------------------------------------------------|
| <a href="https://www.amazon.com/Deep-Learning-R-Francois-Chollet/dp/161729554X"><img class="nav-image illustration" src="https://images.manning.com/720/960/resize/book/a/4e5e97f-4e8d-4d97-a715-f6c2b0eb95f5/Allaire-DLwithR-HI.png" width=250/></a>  | [Deep Learning with R](https://www.amazon.com/Deep-Learning-R-Francois-Chollet/dp/161729554X) <br/>Deep Learning with R is meant for statisticians, analysts, engineers, and students with a reasonable amount of R experience but no significant knowledge of machine learning and deep learning. You’ll learn from more than 30 code examples that include detailed commentary and practical recommendations. You don’t need previous experience with machine learning or deep learning: this book covers from scratch all the necessary basics. You don’t need an advanced mathematics background, either—high school level mathematics should suffice in order to follow along. |
| <a href="https://github.com/rstudio/cheatsheets/raw/master/keras.pdf"><img class="nav-image illustration" src="https://tensorflow.rstudio.com/learn/images/resources-cheatsheet.png" width=250/></a>  | [Deep Learning with Keras Cheatsheet](https://github.com/rstudio/cheatsheets/raw/master/keras.pdf) <br/>A quick reference guide to the concepts and available functions in the R interface to Keras. Covers the various types of Keras layers, data preprocessing, training workflow, and pre-trained models.  |
| <a href="https://tensorflow.rstudio.com/gallery/"><img class="nav-image illustration" src="https://tensorflow.rstudio.com/learn/images/keras-customer-churn.png" width=250/></a>  | [Gallery](https://tensorflow.rstudio.com/gallery/) <br/>In-depth examples of using TensorFlow with R, including detailed explanatory narrative as well as coverage of ancillary tasks like data preprocessing and visualization. A great resource for taking the next step after you've learned the basics. |
| <a href="https://tensorflow.rstudio.com/learn/examples.html"><img class="nav-image illustration" src="https://tensorflow.rstudio.com/learn/images/resources-examples.png" width=250/></a>  | [Examples](https://tensorflow.rstudio.com/learn/examples.html) <br/> Introductory examples of using TensorFlow with R. These examples cover the basics of training models with the keras, tfestimators, and tensorflow packages.  |

## What's next

We'll be continuing to build packages and tools that make using TensorFlow from R easy to learn, productive, and capable of addressing the most challenging problems in the field. We'll also be making an ongoing effort to add to our gallery of in-depth examples. To stay up to date on our latest tools and additions to the gallery, you can subscribe to the [TensorFlow for R Blog](https://tensorflow.rstudio.com/blog/).

While TensorFlow and deep learning have done some impressive things in fields like image classification and speech recognition, its use within other domains like biomedical and time series analysis is more experimental and not yet proven to be of broad benefit. We're excited to how the R community will push the frontiers of what's possible, as well as find entirely new applications. If you are an R user who has been curious about TensorFlow and/or deep learning applications, now is a great time to dive in and learn more!


<style type="text/css">
.illustration {
  border: solid 1px #cccccc;
}

.nav-image {
  margin-top: 8px;
  
}
</style>









