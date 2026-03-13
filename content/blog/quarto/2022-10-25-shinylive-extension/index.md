---
title: Shinylive Extension
subtitle: Embed Shinylive applications in Quarto documents
description: >
  With Shinylive, you can embed Shiny for Python applications into Quarto
  documents and run the entire application (including the Python runtime) inside
  the user's web browser.
categories:
  - Extensions
  - Features
people:
  - Winston Chang
date: '2022-10-25'
image: shinylive-embedded-app.png
image-alt: Screenshot of a Quarto document with an embedded Shinylive application.
ported_from: quarto
port_status: in-progress
---


The new [Shinylive Quarto extension](https://github.com/quarto-ext/shinylive) makes it easy to embed Shiny for Python applications in your Quarto documents. This makes it possible to add interactivity to your documents with just Python code. For example, you can include an interactive Shiny application like this, directly inside your Quarto document.

[<img src="shinylive-embedded-app.png" class="preview-image" data-fig-align="center" data-fig-alt="Shinylive application embedded in a Quarto document." />](https://quarto-ext.github.io/shinylive/sine.html)

In case you're not already familiar with Shiny, here's some background: [Shiny](https://shiny.rstudio.com/) is a framework for creating web applications. Shiny was originally just for R, but we've recently released an alpha version of [Shiny for Python](https://shiny.rstudio.com/py/).

One of the exciting new features of Shiny for Python is a deployment method called Shinylive: the application can be run entirely within the browser, without needing a remote server running Python. Instead, Python runs *in the web browser*, thanks to the magic of [WebAssembly](https://webassembly.org/). In essence, but the server and client sides of the Shiny application run in the browser.

The Shiny for Python [website](https://shiny.rstudio.com/py/) contains many interactive, editable Shiny applications, and is built using this extension.

Bear in mind that not all Shiny applications can be deployed with Shinylive, in part because not all Python packages can run in WebAssembly -- but for those that can, this extension makes it possible to deploy the Quarto document with the embedded application on any web hosting service. To learn more about Shinylive, see [this page](https://shiny.posit.co/py/get-started/shinylive.html).

The new Shinylive Quarto extension makes it easy to embed Shiny for Python applications in Quarto documents. This is a great way of adding interactive components to your Quarto document. And, once again, you don't need a server running Python to share these Quarto documents -- just deploy the generated files as you would for any other Quarto website.
