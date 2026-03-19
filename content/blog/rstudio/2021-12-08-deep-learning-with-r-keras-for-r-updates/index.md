---
title: Using Keras for Deep Learning with R
date: '2021-12-08'
slug: deep-learning-with-r-keras-for-r-updates
tags:
  - AI
  - Artificial intelligence
  - Deep learning
  - Packages
  - RStudio
people:
  - Isabella Velásquez
blogcategories:
  - Products and Technology
description: We are excited to announce new developments in Keras for R. Data scientists
  can use the most popular and powerful deep learning frameworks to guide data-driven
  decisions, all within R.
alttext: Leafless tree branches with red buds against a snowy background
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
software: ["keras3"]
languages: ["R"]
categories:
  - Machine Learning
---
<caption>
Photo by <a href="https://unsplash.com/@sallybrad2016?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Preethi Viswanathan</a> on <a href="https://unsplash.com/s/photos/neural-network?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</caption>

We are excited to announce new developments in <a href="https://blogs.rstudio.com/ai/posts/2021-11-18-keras-updates/" target = "_blank">Keras for R</a>. Together with our current integration with <a href="https://torch.mlverse.org/" target = "_blank">torch</a>, data scientists can use the most popular and powerful deep learning frameworks all within R.

## Expand data science capabilities with deep learning

Data scientists use machine learning to create models that improve without explicit instructions. Deep learning is a subset of machine learning. It is particularly powerful in applications such as image recognition, natural language processing, and audio processing.

Deep learning allows data scientists to create more accurate and efficient models, sometimes even outperforming human cognition.  With improved machine learning capabilities, data scientists can provide better answers to their data questions.

## Add essential tools to your toolkit

Data scientists have done significant work to develop the deep learning sector. Among deep learning libraries, <a href="https://keras.io/" target = "_blank">Keras</a> stands out for its productivity, flexibility, and user-friendly API. TensorFlow is a machine learning platform that is both extremely adaptable and well-suited for production. Together, users can use these libraries to train and deploy powerful deep learning models.

The <a href="https://keras.rstudio.com/" target = "_blank">Keras for R package</a> provides an R interface to Keras. With it, data scientists can leverage the power of Keras and Tensorflow in R.

## Train neural networks with easy-to-write code

Keras for R allows data scientists to run deep learning models in an R interface. They can write in their preferred programming language while taking full advantage of the deep learning methods and architecture.

* **The package provides familiar syntax.** Users can write natural-feeling, idiomatic-looking code with Keras for R (including the pipe operator!). Take a look: the <a href="https://tensorflow.rstudio.com/tutorials/beginners/" target = "_blank">image classification example</a> on the Tensorflow for R website uses code very familiar to those who use the tidyverse syntax.

![Scrolling through a Tensorflow for R tutorial](images/image1.gif)

* **The package supports users in translating Python code.** Using `%py_class%`, data scientists can directly subclass Python objects, making it much easier to translate Python code found on the web.

```
NonNegative(keras$constraints$Constraint) %py_class% {
  "__call__" &lt;- function(x) {
    w * k_cast(w >= 0, k_floatx())
  }
}
```

No need to switch between environments or languages — users can use Keras functionality all within R.

## What’s next?

We will continue developing Keras for R to help R users develop sophisticated deep learning models in R. Stay tuned for:

* A new version of _Deep Learning for R_, with updated functionality and architecture;
* More expansion of Keras for R’s extensive low-level refactoring and enhancements; and
* More detailed introductions to the powerful new features.

Check out the “<a href="https://blogs.rstudio.com/ai/posts/2021-11-18-keras-updates/" target = "_blank">Keras for R is Back!</a>” post to learn about the state of the ecosystem and the package's new functionalities. Subscribe to the <a href="https://blogs.rstudio.com/ai/" target = "_blank">RStudio AI Blog</a> for the latest news, insights, and examples of using AI-related technologies with R.

