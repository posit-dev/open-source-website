---
title: 'RStudio v0.99 Preview: Code Snippets'
people:
  - RStudio Team
date: '2015-04-13'
categories:
- RStudio IDE
slug: rstudio-v0-99-preview-code-snippets
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


We're getting close to shipping the next version of RStudio (v0.99) and this week will continue our series of posts describing the major new features of the release (previous posts have already covered [code completion](https://blog.rstudio.com/2015/02/23/rstudio-v0-99-preview-code-completion/), the revamped[ data viewer](https://blog.rstudio.com/2015/02/24/rstudio-v0-99-preview-data-viewer-improvements/), and improvements to [vim mode](https://blog.rstudio.com/2015/02/23/rstudio-0-99-preview-vim-mode-improvements/)). Note that if you want to try out any of the new features now you can do so by downloading the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/).

### Code Snippets

Code snippets are text macros that are used for quickly inserting common snippets of code. For example, the `fun` snippet inserts an R function definition:

![Insert Snippet](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-07-at-10-39-50-am.png)

If you select the snippet from the completion list it will be inserted along with several text placeholders which you can fill in by typing and then pressing **Tab** to advance to the next placeholder:

![Screen Shot 2015-04-07 at 10.44.39 AM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-07-at-10-44-39-am.png)

Other useful snippets include:

  * `lib`, `req`, and `source` for the library, require, and source functions

  * `df` and `mat` for defining data frames and matrices

  * `if`, `el`, and `ei` for conditional expressions

  * `apply`, `lapply`, `sapply`, etc. for the apply family of functions

  * `sc`, `sm`, and `sg` for defining S4 classes/methods.

Snippets are a great way to automate inserting common/boilerplate code and are available for R, C/C++, JavaScript, and several other languages.

### Inserting Snippets

As illustrated above, code snippets show up alongside other code completion results and can be inserted by picking them from the completion list. By default the completion list will show up automatically when you pause typing for 250 milliseconds and can also be manually activated via the **Tab** key. In addition, if you have typed the character sequence for a snippet and want to insert it immediately (without going through the completion list) you can press **Shift+Tab**.

### Customizing Snippets

You can edit the built-in snippet definitions and even add snippets of your own via the **Edit Snippets** button in **Global Options** -> **Code**:

![Edit Snippets](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-07-at-10-48-40-am.png)

Custom snippets are defined using the `snippet` keyword. The contents of the snippet should be indented below using the `<tab>` key (rather than with spaces). Variables can be defined using the form `{1:varname}`. For example, here's the definition of the `setGeneric` snippet:

    snippet sg
      setGeneric("${1:generic}", function(${2:x, ...}) {
        standardGeneric("${1:generic}")
      })

Once you've customized snippets for a given language they are written into the `~/.R/snippets` directory. For example, the customized versions of R and C/C++ snippets are written to:

    ~/.R/snippets/r.snippets
    ~/.R/snippets/c_cpp.snippets

You can edit these files directly to customize snippet definitions or you can use the **Edit Snippets** dialog as described above. If you need to move custom snippet definitions to another system then simply place them in `~/.R/snippets` and they'll be used in preference to the built-in snippet definitions.

### Try it Out

You can give code snippets a try now by downloading the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/). If you run into problems or have feedback on how we could make things better let us know on our [Support Forum](https://support.rstudio.com).

