---
title: "TensorFlow v1.3 Released"
description: |
  The final release of TensorFlow v1.3 is now available. This release marks the initial availability of several canned estimators including DNNClassifier and DNNRegressor.
date: 2017-08-17
categories:
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



The final release of TensorFlow v1.3 is now available. This release of TensorFlow marks the initial availability of several canned estimators, including:

- DNNClassifier
- DNNRegressor
- LinearClassifier
- LinearRegressor
- DNNLinearCombinedClassifier
- DNNLinearCombinedRegressor.

The [tfestimators package](https://tensorflow.rstudio.com/tfestimators) provides a high level R interface for these estimators.

Full details on the release of TensorFlow v1.3 are available here: https://github.com/tensorflow/tensorflow/releases/tag/v1.3.0

You can update your R installation of TensorFlow using the `install_tensorflow` function:

``` r
library(tensorflow)
install_tensorflow()
```

Note that you should also provide any options used in your original installation (e.g. `method = "conda"`, `version = "gpu"`, etc. )

### cuDNN 6.0

TensorFlow v1.3 is built against version 6.0 of the [cuDNN library](https://developer.nvidia.com/cudnn) from NVIDIA. Previous versions were built against cuDNN v5.1, so for installations running the GPU version of TensorFlow this means that you will need to install an updated version of cuDNN along with TensorFlow v1.3.

Updated installation instructions are available here: [https://tensorflow.rstudio.com/tensorflow/installation_gpu.html](https://tensorflow.rstudio.com/tensorflow/articles/installation_gpu.html).

Version 1.4 of TensorFlow is expected to migrate again to version 7.0 of cuDNN.
