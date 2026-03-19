---
title: "R Interface to Google CloudML"
description: |
  We are excited to announce the availability of the cloudml package, which provides an R interface to Google Cloud Machine Learning Engine. CloudML provides a number of services including on-demand access to training on GPUs and hyperparameter tuning to optimize key attributes of model architectures.
date: 2018-01-10
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
software: ["cloudml", "keras3", "tfestimators", "tensorflow"]
languages: ["R"]
categories:
  - Machine Learning
  - MLOps & Admin
ported_categories:
  - Cloud
  - Packages/Releases
---



## Overview

We are excited to announce the availability of the [cloudml](https://tensorflow.rstudio.com/tools/cloudml) package, which provides an R interface to [Google Cloud Machine Learning Engine](https://cloud.google.com/ml-engine). CloudML provides a number of services including:

- Scalable training of models built with the [keras](https://keras.rstudio.com/), [tfestimators](https://tensorflow.rstudio.com/tfestimators), and [tensorflow](https://tensorflow.rstudio.com/) R packages.

- On-demand access to training on GPUs, including the new [Tesla P100 GPUs](http://www.nvidia.com/object/tesla-p100.html) from NVIDIA®.

- Hyperparameter tuning to optmize key attributes of model architectures in order to maximize predictive accuracy.

- Deployment of trained models to the Google global prediction platform that can support thousands of users and TBs of data.

## Training with CloudML

Once you've configured your system to publish to CloudML, training a model is as straightforward as calling the `cloudml_train()` function:

``` r
library(cloudml)
cloudml_train("train.R")
```

CloudML provides a variety of GPU configurations, which can be easily selected when calling `cloudml_train()`. For example, the following would train the same model as above but with a [Tesla K80 GPU](http://www.nvidia.com/object/tesla-k80.html):

``` r
cloudml_train("train.R", master_type = "standard_gpu")
```

To train using a [Tesla P100 GPU](http://www.nvidia.com/object/tesla-p100.html) you would specify `"standard_p100"`:

``` r
cloudml_train("train.R", master_type = "standard_p100")
```

When training completes the job is collected and a training run report is displayed:

<img src="images/training-run.png" style="border: 1px solid rgba(0,0,0,0.1);" />

<br/>

## Learning More

Check out the [cloudml package documentation](https://tensorflow.rstudio.com/tools/cloudml) to get started with training and deploying models on CloudML.

You can also find out more about the various capabilities of CloudML in these articles:

- [Training with CloudML](https://tensorflow.rstudio.com/tools/cloudml/articles/training.html) goes into additional depth on managing training jobs and their output.

- [Hyperparameter Tuning](https://tensorflow.rstudio.com/tools/cloudml/articles/tuning.html) explores how you can improve the performance of your models by running many trials with distinct hyperparameters (e.g. number and size of layers) to determine their optimal values.

- [Google Cloud Storage](https://tensorflow.rstudio.com/tools/cloudml/articles/storage.html) provides information on copying data between your local machine and Google Storage and also describes how to use data within Google Storage during training.

- [Deploying Models](https://tensorflow.rstudio.com/tools/cloudml/articles/deployment.html) describes how to deploy trained models and generate predictions from them.
