---
title: 'RStudio 1.2 Preview: Stan'
people:
  - RStudio Team
date: '2018-10-16'
slug: rstudio-1-2-preview-stan
categories:
- RStudio IDE
tags:
- Stan
- RStudio IDE
blogcategories:
- Products and Technology
- Open Source
events: blog
ported_from: rstudio
port_status: in-progress
---

<img src="/blog-images/2018-10-16-rstudio-1-2-preview-stan_files/stan_logo.png" width="100px" align="right" style="margin-left: 16px;" alt="Stan Logo" />

We previously discussed improved support in RStudio v1.2 for [SQL](https://blog.rstudio.com/2018/10/02/rstudio-1-2-preview-sql/), [D3](https://blog.rstudio.com/2018/10/05/r2d3-r-interface-to-d3-visualizations/), [Python](https://blog.rstudio.com/2018/10/09/rstudio-1-2-preview-reticulated-python/), and [C/C++](https://blog.rstudio.com/2018/10/11/rstudio-1-2-preview-cpp/). Today, we're excited to announce improved support for the [Stan programming language](http://mc-stan.org/). The Stan programming language makes it possible for researchers and analysts to write high-performance and scalable statistical models.

> Stan® is a state-of-the-art platform for statistical modeling and high-performance statistical computation. Thousands of users rely on Stan for statistical modeling, data analysis, and prediction in the social, biological, and physical sciences, engineering, and business.

With RStudio v1.2, we now provide:

- Improved, context-aware autocompletion for Stan files and chunks

- A document outline, which allows for easy navigation between Stan code blocks

- Inline diagnostics, which help to find issues while you develop your Stan model

- The ability to interrupt Stan parallel workers launched within the IDE

Together, these features bring the editing experience in Stan programs in-line with what you're familiar with in R.

## Autocompletion

RStudio provides autocompletion results for Stan functions, drawing from the set of pre-defined Stan keywords and functions. The same autocompletion features you might be familiar with in R, like fuzzy matching, are now also available in Stan programs.

<img src="/blog-images/2018-10-16-rstudio-1-2-preview-stan_files/autocomplete.png" width=720 />

As with R, RStudio will also provide a small tooltip describing the arguments accepted by a particular function.

<img src="/blog-images/2018-10-16-rstudio-1-2-preview-stan_files/autocomplete-2.png" width=722 />

## Document Outline

The document outline allows for easy navigation between Stan blocks. This can be especially useful as your model definition grows in size, and you need to quickly reference the different blocks used in your program.

<img src="/blog-images/2018-10-16-rstudio-1-2-preview-stan_files/document-outline.png" width=720 />

## Diagnostics

RStudio now uses the Stan parser to provide inline diagnostics, and will report any problems discovered as you prepare your model.

<img src="/blog-images/2018-10-16-rstudio-1-2-preview-stan_files/diagnostics.png" width=717 />

If the Stan compiler discovers any issues in your model, RStudio's diagnostics will show you exactly where those issues live so you can fix them quickly and easily.

## Worker Interruption

One aspect that had previously made working with Stan in RStudio frustrating was the inability to interrupt parallel Stan workers. This implied that attempts to fit a computationally expensive model could not be interrupted, and the only remedy previously was to restart the IDE or forcefully shut down the workers through another mechanism.

We're very happy to share that this limitation has been lifted with RStudio v1.2. Now, when fitting a Stan model with parallel workers, you can interrupt the workers as you would any regular R code -- either use the Escape key, or press the Stop button in the Console pane.

## Try it Out

With the improvements to Stan integration coming in RStudio v1.2, getting started with Stan has never been easier. If you'd like to get more familiar with Stan, we think these resources will be helpful:

- Stan website: http://mc-stan.org/
- RStan "Getting Started" guide: https://github.com/stan-dev/rstan/wiki/RStan-Getting-Started
- Tutorials and Examples using Stan: http://mc-stan.org/users/documentation/tutorials

You can download the RStudio v1.2 Preview Release at <https://www.rstudio.com/products/rstudio/download/preview/>. If you have any questions or comments, please get in touch with us on the [community forums](https://community.rstudio.com/c/rstudio-ide).

