---
title: 'RStudio v0.99 Preview: Vim Mode Improvements'
people:
  - Jonathan McPherson
date: '2015-02-23'
categories:
- RStudio IDE
tags:
- preview
- rstudio
- vim
- RStudio IDE
slug: rstudio-0-99-preview-vim-mode-improvements
blogcategories:
- Products and Technology
- Open Source
events: blog
ported_from: rstudio
port_status: raw
---


RStudio's code editor includes a set of lightweight [Vim](http://en.wikipedia.org/wiki/Vim_%28text_editor%29) key bindings. You can turn these on in Tools | Global Options | Code | Editing:

![global options](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-9-33-49-am.png)

For those not familiar, Vim is a popular text editor built to enable efficient text editing. It can take some practice and dedication to master Vim style editing but those who have done so typically swear by it. RStudio's "vim mode" enables the use of many of the most common keyboard operations from Vim right inside RStudio.

As part of the [0.99 preview release](https://www.rstudio.com/products/rstudio/download/preview/), we've included an upgraded version of the [ACE editor](http://ace.c9.io/), which has a completely revamped Vim mode. This mode extends the range of Vim key bindings that are supported, and implements a number of Vim "power features" that go beyond basic text motions and editing. These include:

  * **Vertical block selection** via `Ctrl + V`. This integrates with the new multiple cursor support in ACE and allows you to type in multiple lines at once.

  * **Macro playback and recording**, using `q{register}` / `@{register}`.

  * **Marks**, which allow you drop markers in your source and jump back to them quickly later.

  * **A selection of Ex commands**, such as `:wq` and `:%s` that allow you to perform editor operations as you would in native Vim.

  * **Fast in-file search** with e.g. `/` and `*`, and support for JavaScript regular expressions.

We've also added a Vim quick reference card to the IDE that you can bring up at any time to show the supported key bindings. To see it, switch your editor to Vim mode (as described above) and type `:help` in Command mode.

![vim quick reference card](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-11-03-00-am.png)

Whether you're a Vim novice or power user, we hope these improvements make the RStudio IDE's editor a more productive and enjoyable environment for you. You can try the new Vim features out now by downloading the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).

