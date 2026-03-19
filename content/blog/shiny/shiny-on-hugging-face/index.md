---
title: Shiny on Hugging Face
description: Deploy Shiny on Hugging Face with the click of a button
people:
  - Gordon Shotwell
date: '2023-05-08'
image: shiny-on-hf-thumb.jpg
image-alt: The Shiny hex next to the Hugging Face emoji logo
ported_from: shiny
port_status: in-progress
software: ["shiny-python", "shiny-r"]
languages: ["R", "Python"]
categories:
  - Interactive Apps
tags:
  - Shiny
---


We're thrilled to announce that we've partnered with [Hugging Face](https://huggingface.co/) to provide templated Spaces for both the R and Python Shiny packages.
These Spaces allow you to deploy an R or Python Shiny app on Hugging Face with a click of a button, and make it easy to integrate Hugging Face models into your app.

## About Hugging Face

Hugging Face is the most used open platform for AI, where the machine learning (ML) community has shared more than 150,000 models; 25,000 datasets; and 30,000 ML apps, including Stable Diffusion, Bloom, GPT-J, and open source ChatGPT alternatives.
These apps enable the community to explore models, replicate results, and lower the barrier of entry for ML.
At Posit, we've been extremely impressed with the Hugging Face community, and their commitment to supporting open source machine learning models.

## What does Shiny add?

We think that Shiny is a great front-end for Hugging Face models because it is an efficient and developer-friendly GUI framework. Our reactive execution model allows Shiny to infer the relationships between inputs and outputs and minimally re-render application components.
This means that you can quickly build intuitive and beautiful model demos without writing callback functions or caching data, and is particularly useful when calling expensive inference endpoints.
Shiny is easy to learn, and there are great educational resources in both [R](https://shiny.posit.co/r/getstarted/) and [Python](https://shiny.posit.co/py/docs/overview.html).

Shiny is great for simple demos, but it also has all of the tools you need to build complex, mission-critical applications.
You can design [delightful layouts](https://shiny.posit.co/py/docs/ui-page-layouts.html) and user interfaces, control [application routing](https://shiny.posit.co/py/docs/workflow-server.html), and encapsulate and share components using [modules](https://shiny.posit.co/py/docs/workflow-modules.html).

## Which Space should I use?

We have both R and Python templates available, so you can use your language of choice to write Shiny apps.

Most of the Hugging Face toolchain is built around Python, and as a result the Shiny for Python [Space](https://huggingface.co/new-space?template=posit/shiny-for-python-template) is a bit easier to use on Hugging Face.
Shiny for Python is a pure python implementation of Shiny, and does not require an R installation.
This means that Shiny for Python apps will deploy faster on Hugging Face infrastructure, and integrate better with their Python SDKs.

If you are an R user, or want to make use of some of the amazing [R extensions](https://github.com/nanxstats/awesome-shiny-extensions), then the [Shiny for R Space](https://huggingface.co/new-space?template=posit/shiny-for-r-template) is an excellent option.
To call Hugging Face tools we recommend communicating with Hugging Face using an [API](https://huggingface.co/inference-api) or calling one of their Python SDKs using [reticulate](https://rstudio.github.io/reticulate/).

## Conclusion

Our [mission](https://posit.co/about/pbc-report/) at Posit is to support open-source scientific software, and so we're very proud to support the effort to build advanced AI models under open-source licenses.
We can't wait to see what you build with this integration.
