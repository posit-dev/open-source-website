---
title: Interactive Web-Based Data Visualization with R, plotly, and shiny
date: '2020-01-20'
description: Create interactive web graphics from R with plotly, including linked views, animations, and maps, and embed them in Shiny apps, without having to learn web programming.
image: cover.jpg
color: '#EC4439'
resource_type: book
edition: 1
publisher: CRC Press
isbn: '9781138331457'
pages: 448
people:
- Carson Sievert
website: https://plotly-r.com/
read_url: https://plotly-r.com/
buy_url: https://www.routledge.com/Interactive-Web-Based-Data-Visualization-with-R-plotly-and-shiny/Sievert/p/book/9781138331457
github: cpsievert/plotly_book
software:
- shiny-r
- crosstalk
languages:
- R
topics:
- Visualization
- Interactive Apps
---

Carson Sievert, the author and maintainer of the `plotly` R package, wrote this book for data analysts who want the benefits of interactive web graphics without first having to learn web programming.
It focuses on the practical process of creating interactive, web-based visualizations from R for exploring and presenting multidimensional data, and on sharing the results over email, as standalone HTML, or as static exports.

The book is driven by R code examples throughout.
It starts with the two main ways to create plotly graphics, `plot_ly()` and `ggplotly()`, then moves on to publishing, arranging, and animating views, and to linking multiple views together.
Client-side linking lets you build graphical queries that run entirely in the browser, while server-side linking uses `shiny` to respond to plotly events.
Later chapters show how to add custom behavior with JavaScript and cover practical details such as tooltips, colors, performance, and LaTeX rendering.
Along the way you also meet tidyverse tools such as `dplyr` and `tidyr`, and best practices for statistical graphics, graphical perception, and visualizing high-dimensional data.

You will learn how to:

- Turn static `ggplot2` graphics into interactive web graphics
- Visualize continuous, discrete, multivariate, and geospatial data
- Save, embed, and export interactive views for publication
- Arrange, animate, and link multiple plots in standalone HTML
- Embed plotly graphics in Shiny apps and respond to user events
- Extend graphics with custom JavaScript event handlers

An online version of the book is free to read and continues to evolve between printings.
