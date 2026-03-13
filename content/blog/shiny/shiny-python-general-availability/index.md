---
title: Shiny for Python out of alpha
description: Shiny for Python has moved from alpha to general availability.
people:
  - Winston Chang
date: '2023-04-18'
image: shiny-for-python.jpg
image-alt: >-
  The Shiny hex sticker next to the Python language logo, saying Shiny for
  Python
ported_from: shiny
port_status: raw
---


We are thrilled to announce that [Shiny for Python](https://shiny.posit.co/py/) has moved from the alpha stage to general availability. With Shiny for Python, data scientists can build interactive web applications with the expressiveness and power of reactive programming, and combine that with the extensive array of data analysis tools and visualization libraries in Python.

We believe that Shiny for Python strikes the perfect balance between simplicity and power. Unlike Streamlit, Shiny is not constrained by the top-to-bottom computing model, and there's no limit to how sophisticated your applications can be. Compared to Dash, Shiny is more developer-friendly and boasts a more efficient reactive programming model.

## What does it mean to be out of Alpha?

When we first introduced Shiny for Python at rstudio::conf last year, we labeled it as an alpha version, acknowledging that we could learn from early users and make changes to the API. After gaining ample experience and feedback, we're now confident that Shiny for Python is ready for production work.

We've gotten some great feedback during the alpha phase of the project, leading to several enhancements:

- We've added a [quickstart guide](../py/docs/r-quickstart.html) for R users.
- You can now interact with plots created using matplotlib, seaborn, and plotnine. ([Example](https://shinylive.io/py/examples/#selecting-data))
- We've improved the [API documentation](https://shiny.posit.co/py/api/).
- We've created a new package, [shinyswatch](https://github.com/posit-dev/py-shinyswatch), which lets you modify an app's visual style with a single line of code. ([Example](https://shinylive.io/py/examples/#shinyswatch))
- We released [shinywidgets](https://github.com/posit-dev/py-shinywidgets), which makes it possible to use Jupyter widgets in a Shiny app, including [Plotly](https://shinylive.io/py/examples/#plotly) and maps with [Leaflet](https://shinylive.io/py/examples/#map).

## Get started

If you want to learn more Shiny for Python check out [the web site](https://shiny.posit.co/py/) and [live examples](https://shinylive.io/py/examples/).

If you're a Shiny for R user who's curious about learning Shiny for Python, read our [Quickstart guide](https://shiny.posit.co/py/docs/r-quickstart.html)!
