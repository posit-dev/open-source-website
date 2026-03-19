---
title: Quarto Extensions
subtitle: Extend Quarto with new capabilities
description: |
  Quarto Extensions are a powerful way to modify or extend the behavior of Quarto, and can be created and distributed by anyone. Extension types include filters, shortcodes, and custom formats.
categories:
  - Publishing
people:
  - J.J. Allaire
date: '2022-07-25'
image: extensions.png
image-alt: The main page for the quarto-ext GitHub organization which lists extensions
  published by the Quarto core team.
ported_from: quarto
port_status: in-progress
software: ["quarto"]
languages: ["R", "Python", "Julia"]
ported_categories:
  - Extensions
  - Features
tags:
  - Quarto
  - Extensions
  - Features
---


Quarto Extensions are a powerful way to modify or extend the behavior of Quarto, and can be created and distributed by anyone. There are three types of extensions available:

- [Shortcodes](https://quarto.org/docs/extensions/shortcodes.html) are special markdown directives that generate various types of content. For example, you could create shortcodes to embed tweets or videos in a document.

- [Filters](https://quarto.org/docs/extensions/filters.html) are a flexible and powerful tool for introducing new global behaviors and/or new markdown rendering behaviors. For example, you could create filters to implement output folding, an image carousel, or just about anything you can imagine!

- [Formats](https://quarto.org/docs/extensions/formats.html) enable you to create new output formats by bundling together document options, templates, stylesheets, and other content.

Here are some examples of extensions developed and maintained by the core Quarto team:

| **Extension** | **Description** |
|----------------------|--------------------------------------------------|
| [lightbox](https://github.com/quarto-ext/lightbox/) | Create lightbox treatments for images in your HTML documents. |
| [fancy-text](https://github.com/quarto-ext/fancy-text) | Output nicely formatted versions of fancy strings such as LaTeX and BibTeX in multiple formats. |
| [fontawesome](https://github.com/quarto-ext/fontawesome) | Use Font Awesome icons in HTML and PDF documents. |
| [latex-environment](https://github.com/quarto-ext/latex-environment) | Quarto extension to output custom LaTeX environments. |

To learn more about using extensions, see the [Extensions](https://quarto.org/docs/extensions/index.html) documentation on the Quarto website. If you want to dive in to creating your own extensions check out the articles on [Creating Shortcodes](https://quarto.org/docs/extensions/shortcodes.html), [Creating Filters](https://quarto.org/docs/extensions/filters.html), and [Creating Formats](https://quarto.org/docs/extensions/formats.html).
