---
title: 'Model Monitoring with R Markdown, pins, and RStudio Connect'
people:
  - Julia Silge
date: '2021-04-08'
slug: model-monitoring-with-r-markdown
description: Model monitoring is a key component of ModelOps, and the R ecosystem offers flexible, code-first solutions that meet the model monitoring needs of data science practitioners.
categories:
  - RStudio Connect
  - R Markdown
  - Data Science Leadership
tags:
  - machine learning
  - modeling
  - rmarkdown
  - flexdashboard
  - pins
alttext: Chicago traffic model monitoring dashboard
blogcategories:
  - Data Science Leadership
  - Products and Technology
  - Open Source
events: blog
image: thumbnail.png
ported_from: rstudio
port_status: in-progress
---

ModelOps or MLOps (for "model/machine learning operations") focuses on the real-world processes involved in building, deploying, and maintaining a model within an organization's data infrastructure. Developing a model that meets your organizations needs and goals is a big accomplishment, but whether that model's purpose is <a href="https://www.tmwr.org/software-modeling.html#types-of-models" target="_blank" rel="noopener noreferrer">largely predictive, inferential, or descriptive</a>, the "care and feeding" of your model often doesn't end when you are done developing it. How is the model going to be deployed? Should you retrain the model on a schedule? Based on changes in model performance? When should you kick off retraining the same kind of model with fresh data versus go back to the drawing board for a full round of model development again? These are the kinds of questions that ModelOps deals with.

**Model monitoring** is a key component of ModelOps, and is typically used to answer questions about how a model is performing over time, when to retrain a model, or what kinds of observations are not being predicted well. There are a lot of solutions out there to address the need for model monitoring, but the R ecosystem offers options that are **code-first, flexible, and already in wide use**. When we use this approach to model monitoring, we gain all the benefits of handling our data science logic via reusable, extensible code (as opposed to clicks), as well as the enormous open source community surrounding R Markdown and related tools.

In this post, I'll walk through one option for this approach.

- Deploy a model as a RESTful API using Plumber
- Create an R Markdown document to regularly assess model performance by:
  - Sending the deployed model new observations via httr
  - Evaluating how the model performed with these new predictions using model metrics from yardstick
  - Versioning the model metrics using the pins package
  - Summarize and visualize the results using flexdashboard
- Schedule the R Markdown dashboard to regularly evaluate the model and notify us of the results

## Predicting injuries from traffic data

I recently developed a model to <a href="https://juliasilge.com/blog/chicago-traffic-model/" target="_blank" rel="noopener noreferrer">predict injuries for traffic crashes in Chicago</a>. <a href="https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if" target="_blank" rel="noopener noreferrer">The data set covers traffic crashes</a> on city streets within Chicago city limits under the jurisdiction of the Chicago Police Department, and the model predicts the probability of a crash involving an injury.

{{% youtube "J5gTzoRU9tc" %}}

I work on the <a href="https://www.tidymodels.org/" target="_blank" rel="noopener noreferrer">tidymodels</a> team developing open source tools for modeling and machine learning, but you can use the R ecosystem for monitoring any kind of model, even one trained in Python. I used <a href="https://www.rplumber.io/" target="_blank" rel="noopener noreferrer">Plumber</a> to <a href="https://colorado.rstudio.com/rsc/traffic-crashes/" target="_blank" rel="noopener noreferrer">deploy my model on RStudio Connect</a>, but depending on your own organization's infrastructure, you might consider <a href="https://docs.rstudio.com/connect/user/flask/" target="_blank" rel="noopener noreferrer">deploying a Flask API</a> or another appropriate format.

## Monitor model performance

There are new crashes everyday, so I would like to measure how my model performs over time. I built a <a href="https://rmarkdown.rstudio.com/flexdashboard/" target="_blank" rel="noopener noreferrer">flexdashboard</a> for model monitoring; this dashboard does _not_ use Shiny but it's published on <a href="https://www.rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a> as a <a href="https://docs.rstudio.com/connect/user/scheduling/" target="_blank" rel="noopener noreferrer">scheduled report</a> that re-executes automatically once a week. I get an email in my inbox with the new results every time!

<a href="https://colorado.rstudio.com/rsc/traffic-crash-monitor/monitor.html" target="_blank" rel="noopener noreferrer"><img src="traffic_flexdashboard.png" width="100%" alt="Model monitoring flexdashboard"></a>

The <a href="https://colorado.rstudio.com/rsc/traffic-crash-monitor/monitor.html" target="_blank" rel="noopener noreferrer">monitoring dashboard</a> uses <a href="https://httr.r-lib.org/" target="_blank" rel="noopener noreferrer">httr</a> to call two APIs:

- the city of Chicago's API for the traffic data to get the latest crashes
- the model API to make predictions on those new crashes

The dashboard also makes use of <a href="https://pins.rstudio.com/" target="_blank" rel="noopener noreferrer">pins</a> to **publish** and **version** model metrics each time the dashboard updates. I am a huge fan of the pins package in the context of ModelOps; you can even use it to publish and version models themselves!

<a href="https://colorado.rstudio.com/rsc/traffic-crash-monitor/monitor.html" target="_blank" rel="noopener noreferrer"><img src="traffic_monitor.gif" width="100%" alt="Model monitoring flexdashboard"></a>

Basic model monitoring should cover at least the model metrics of interest, but in the real world, most data practitioners need to track something specific to their domain or use case. This is why inflexible ModelOps tooling is often frustrating to work with. Using flexible tools like R Markdown, on the other hand, let me build a model monitoring dashboard with a table of crashes that were misclassified (so I can explore them) and an interactive map of where they are around the city of Chicago.

## To learn more

All the code for this demo <a href="https://github.com/juliasilge/modelops-playground" target="_blank" rel="noopener noreferrer">is available on GitHub</a>, and future posts will address how to use R for other ModelOps endeavors. If you'd like to learn more about how RStudio products like Connect can be used for tasks from serving model APIs to model monitoring and more, <a href="https://rstudio.chilipiper.com/book/schedule-time-with-rstudio" target="_blank" rel="noopener noreferrer">set up a meeting with our Customer Success team</a>.
