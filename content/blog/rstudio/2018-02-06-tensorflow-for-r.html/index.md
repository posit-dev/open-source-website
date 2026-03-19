---
title: TensorFlow for R
people:
  - Tareef Kawaf
date: '2018-02-06'
tags:
- data science
slug: tensorflow-for-r
blogcategories:
- Products and Technology
- Open Source
ported_from: rstudio
port_status: in-progress
software: ["tensorflow"]
languages: ["R"]
categories:
  - Machine Learning
ported_categories:
  - Packages
---



<p>Over the past year we’ve been hard at work on creating R interfaces to <a href="https://tensorflow.rstudio.com/">TensorFlow</a>, an open-source machine learning framework from Google. We are excited about TensorFlow for many reasons, not the least of which is its state-of-the-art infrastructure for deep learning applications.</p>
<p>In the 2 years since it was initially open-sourced by Google, TensorFlow has rapidly become the <a href="https://twitter.com/fchollet/status/871089784898310144?lang=en">framework of choice</a> for both machine learning practitioners and researchers. On Saturday, we formally announced our work on TensorFlow during J.J. Allaire’s keynote at <a href="https://www.rstudio.com/conference/">rstudio::conf</a>:</p>
<iframe width="711" height="400" src="https://www.youtube.com/embed/atiYXm7JZv0?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
</iframe>
<p>In the keynote, J.J. describes not only the work we’ve done on TensorFlow but also discusses deep learning more broadly (what it is, how it works, and where it might be relevant to users of R in the years ahead).</p>
<div id="new-packages-and-tools" class="section level2">
<h2>New packages and tools</h2>
<p>The R interface to TensorFlow consists of a suite of R packages that provide a variety of interfaces to TensorFlow for different tasks and levels of abstraction, including:</p>
<ul>
<li><p><a href="https://tensorflow.rstudio.com/keras/">keras</a>—A high-level interface for neural networks, with a focus on enabling fast experimentation.</p></li>
<li><p><a href="https://tensorflow.rstudio.com/tfestimators/">tfestimators</a>— Implementations of common model types such as regressors and classifiers.</p></li>
<li><p><a href="https://tensorflow.rstudio.com/tensorflow/">tensorflow</a>—Low-level interface to the TensorFlow computational graph.</p></li>
<li><p><a href="https://tensorflow.rstudio.com/tools/tfdatasets/">tfdatasets</a>—Scalable input pipelines for TensorFlow models.</p></li>
</ul>
<p>Besides the various R interfaces to TensorFlow, there are tools to help with training workflow, including real time feedback on training metrics within the RStudio IDE:</p>
<p><img src="/blog-images/2018-02-06-keras-training-metrics.gif" /></p>
<p>The <a href="https://tensorflow.rstudio.com/tools/tfruns/">tfruns package</a> provides tools to track, and manage TensorFlow training runs and experiments:</p>
<p><img src="/blog-images/2018-02-06-tfruns.png" style="border: solid 1px #cccccc;" /></p>
</div>
<div id="access-to-gpus" class="section level2">
<h2>Access to GPUs</h2>
<p>Training convolutional or recurrent neural networks can be extremely computationally expensive, and benefits significantly from access to a recent high-end NVIDIA GPU. However, most users don’t have this sort of hardware available locally. To address this we have provided a number of ways to use GPUs in the cloud, including:</p>
<ul>
<li><p>The <a href="https://tensorflow.rstudio.com/tools/cloudml/">cloudml package</a>, an R interface to Google’s hosted machine learning engine.</p></li>
<li><p><a href="https://tensorflow.rstudio.com/tools/cloud_server_gpu.html#amazon-ec2">RStudio Server with Tensorflow-GPU for AWS</a> (an Amazon EC2 image preconfigured with NVIDIA CUDA drivers, TensorFlow, the TensorFlow for R interface, as well as RStudio Server).</p></li>
<li><p>Detailed instructions for setting up an Ubuntu 16.04 <a href="https://tensorflow.rstudio.com/tools/cloud_desktop_gpu.html">cloud desktop with a GPU</a> using the Paperspace service.</p></li>
</ul>
<p>There is also documentation on <a href="https://tensorflow.rstudio.com/tools/local_gpu.html">setting up a GPU</a> on your local workstation if you already have the required NVIDIA GPU hardware.</p>
</div>
<div id="learning-resources" class="section level2">
<h2>Learning resources</h2>
<p>We’ve also made a significant investment in learning resources, all of these resources are available on the TensorFlow for R website at <a href="https://tensorflow.rstudio.com" class="uri">https://tensorflow.rstudio.com</a>.</p>
<p>Some of the learning resources include:</p>
<table>
<colgroup>
<col width="21%" />
<col width="78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><a href="https://www.amazon.com/Deep-Learning-R-Francois-Chollet/dp/161729554X"><img class="nav-image illustration" src="https://images.manning.com/720/960/resize/book/a/4e5e97f-4e8d-4d97-a715-f6c2b0eb95f5/Allaire-DLwithR-HI.png" width=250/></a></td>
<td><a href="https://www.amazon.com/Deep-Learning-R-Francois-Chollet/dp/161729554X">Deep Learning with R</a> <br/>Deep Learning with R is meant for statisticians, analysts, engineers, and students with a reasonable amount of R experience but no significant knowledge of machine learning and deep learning. You’ll learn from more than 30 code examples that include detailed commentary and practical recommendations. You don’t need previous experience with machine learning or deep learning: this book covers from scratch all the necessary basics. You don’t need an advanced mathematics background, either—high school level mathematics should suffice in order to follow along.</td>
</tr>
<tr class="even">
<td><a href="https://github.com/rstudio/cheatsheets/raw/master/keras.pdf"><img class="nav-image illustration" src="https://tensorflow.rstudio.com/learn/images/resources-cheatsheet.png" width=250/></a></td>
<td><a href="https://github.com/rstudio/cheatsheets/raw/master/keras.pdf">Deep Learning with Keras Cheatsheet</a> <br/>A quick reference guide to the concepts and available functions in the R interface to Keras. Covers the various types of Keras layers, data preprocessing, training workflow, and pre-trained models.</td>
</tr>
<tr class="odd">
<td><a href="https://tensorflow.rstudio.com/gallery/"><img class="nav-image illustration" src="https://tensorflow.rstudio.com/learn/images/keras-customer-churn.png" width=250/></a></td>
<td><a href="https://tensorflow.rstudio.com/gallery/">Gallery</a> <br/>In-depth examples of using TensorFlow with R, including detailed explanatory narrative as well as coverage of ancillary tasks like data preprocessing and visualization. A great resource for taking the next step after you’ve learned the basics.</td>
</tr>
<tr class="even">
<td><a href="https://tensorflow.rstudio.com/learn/examples.html"><img class="nav-image illustration" src="https://tensorflow.rstudio.com/learn/images/resources-examples.png" width=250/></a></td>
<td><a href="https://tensorflow.rstudio.com/learn/examples.html">Examples</a> <br/> Introductory examples of using TensorFlow with R. These examples cover the basics of training models with the keras, tfestimators, and tensorflow packages.</td>
</tr>
</tbody>
</table>
</div>
<div id="whats-next" class="section level2">
<h2>What’s next</h2>
<p>We’ll be continuing to build packages and tools that make using TensorFlow from R easy to learn, productive, and capable of addressing the most challenging problems in the field. We’ll also be making an ongoing effort to add to our gallery of in-depth examples. To stay up to date on our latest tools and additions to the gallery, you can subscribe to the <a href="https://tensorflow.rstudio.com/blog/">TensorFlow for R Blog</a>.</p>
<p>While TensorFlow and deep learning have done some impressive things in fields like image classification and speech recognition, its use within other domains like biomedical and time series analysis is more experimental and not yet proven to be of broad benefit. We’re excited to how the R community will push the frontiers of what’s possible, as well as find entirely new applications. If you are an R user who has been curious about TensorFlow and/or deep learning applications, now is a great time to dive in and learn more!</p>
<style type="text/css">
.illustration {
  border: solid 1px #cccccc;
}

.nav-image {
  margin-top: 8px;
  
}
</style>
</div>
