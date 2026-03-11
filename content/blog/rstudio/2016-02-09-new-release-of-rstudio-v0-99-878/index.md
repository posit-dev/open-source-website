---
title: New Release of RStudio (v0.99.878)
people:
  - RStudio Team
date: '2016-02-09'
categories:
- News
- RStudio IDE
slug: new-release-of-rstudio-v0-99-878
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


We're pleased to announce that a new release of RStudio (v0.99.878) is [available for download](https://www.rstudio.com/products/rstudio/) now. Highlights of this release include:

  * Support for registering custom [RStudio Addins](http://rstudio.github.io/rstudioaddins/).

  * R Markdown editing improvements including outline view and inline UI for chunk execution.

  * Support for multiple [source windows](https://support.rstudio.com/hc/en-us/articles/207126217) (tear editor tabs off main window).

  * Pane zooming for working distraction free within a single pane.

  * Editor and IDE keyboard shortcuts can [now be customized](https://support.rstudio.com/hc/en-us/articles/206382178).

  * New [Emacs keybindings](https://support.rstudio.com/hc/en-us/articles/210928128) mode for the source editor.

  * Support for [parameterized](https://rmarkdown.rstudio.com/developer_parameterized_reports.html) R Markdown reports.

  * Various improvements to RStudio Server Pro including [multiple concurrent R sessions](https://support.rstudio.com/hc/en-us/articles/211789298), use of [multiple R versions](https://support.rstudio.com/hc/en-us/articles/212364537), and [shared projects](https://support.rstudio.com/hc/en-us/articles/211659737) for collaboration.

There are lots of other small improvements across the product, check out the [release notes](https://www.rstudio.com/products/rstudio/release-notes/) for full details.

### RStudio Addins

RStudio Addins provide a mechanism for executing custom R functions interactively from within the RStudio IDE—either through keyboard shortcuts, or through the _Addins_ menu. Coupled with the [rstudioapi](https://cran.rstudio.com/web/packages/rstudioapi/index.html) package, users can now write R code to interact with and modify the contents of documents open in RStudio.

An addin can be as simple as a function that inserts a commonly used snippet of text, and as complex as a Shiny application that accepts input from the user and uses it to transform the contents of the active editor. The sky is the limit!

Here's an example of addin that enables interactive subsetting of a data frame with live preview:

![subset-addin](https://rstudioblog.files.wordpress.com/2015/12/subset-addin.gif)

This addin is implemented using a [Shiny Gadget](https://shiny.rstudio.com/articles/gadgets.html) (see the [source code](https://github.com/rstudio/addinexamples/blob/master/R/subsetAddin.R) for more details). RStudio Addins are distributed as [R packages](http://r-pkgs.had.co.nz/). Once you've installed an R package that contains addins, they'll be immediately become available within RStudio.

You can learn more about using and developing addins here: <http://rstudio.github.io/rstudioaddins/>.

### R Markdown

We've made a number of improvements to R Markdown authoring. There's now an optional outline view that enables quick navigation across larger documents:

![Screen Shot 2015-12-22 at 9.27.34 AM](https://rstudioblog.files.wordpress.com/2015/12/screen-shot-2015-12-22-at-9-27-34-am.png)

We've also added inline UI to code chunks for running individual chunks, running all previous chunks, and specifying various commonly used knit options:

![Screen Shot 2015-12-22 at 9.30.11 AM](https://rstudioblog.files.wordpress.com/2015/12/screen-shot-2015-12-22-at-9-30-11-am.png)

### Multiple Source Windows

There are two ways to open a new source window:

**Pop out an editor**: click the Show in New Window button in any source editor tab.

![](https://support.rstudio.com/hc/en-us/article_attachments/202540607/popout.png)

**Tear off a pane:** drag a tab out of the main window and onto the desktop; a new source window will be opened where you dropped the tab.

![](https://support.rstudio.com/hc/en-us/article_attachments/202617168/tabassign.gif)

You can have as many source windows open as you like. Each source window has its own set of tabs; these tabs are independent of the tabs in RStudio's main source pane.

### Customizable Keyboard Shortcuts

You can now customize keyboard shortcuts in RStudio -- you can bind keys to execute RStudio application commands, editor commands, or even user-defined R functions.

Access the keyboard shortcuts by clicking `Tools -> Modify Keyboard Shortcuts...`:

This will present a dialog that enables remapping of all available editor commands (commands that affect the current document's contents, or the current selection) and RStudio commands (commands whose actions are scoped beyond just the current editor).

![](https://support.rstudio.com/hc/en-us/article_attachments/202570217/Screen_Shot_2015-07-31_at_12.52.59_PM.png)

## Emacs Keybindings

We've introduced a new keybindings mode to go along with the default bindings and Vim bindings already supported. Emacs mode provides a base set of keybindings for navigation and selection, including:

  * `C-p`, `C-n`, `C-b` and `C-f` to move the cursor up, down left and right by characters

  * `M-b`, `M-f` to move left and right by words

  * `C-a`, `C-e` to navigate to the start, or end, of line;

  * `C-k` to 'kill' to end of line, and `C-y` to 'yank' the last kill,

  * `C-s`, `C-r` to initiate an Emacs-style incremental search (forward / reverse),

  * `C-Space` to set/unset mark, and `C-w` to kill the marked region.

There are some additional keybindings that [Emacs Speaks Statistics (ESS)](http://ess.r-project.org/) users might find familiar:

  * `C-c C-v` displays help for the object under the cursor,

  * `C-c C-n` evaluates the current line / selection,

  * `C-x b` allows you to visit another file,

  * `M-C-a` moves the cursor to the beginning of the current function,

  * `M-C-e` moves to the end of the current function,

  * `C-c C-f` evaluates the current function.

We've also introduced a number of keybindings that allow you to interact with the IDE as you might normally do in Emacs:

  * `C-x C-n` to create a new document,

  * `C-x C-f` to find / open an existing document,

  * `C-x C-s` to save the current document,

  * `C-x k` to close the current file.

###

### RStudio Server Pro

We've introduced a number of significant enhancements to [RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro/) in this release, including:

  * The ability to open multiple concurrent R sessions. Multiple concurrent sessions are useful for running multiple analyses in parallel and for switching between different tasks.

![](https://support.rstudio.com/hc/en-us/article_attachments/203432748/multipleRSessions3.png)

  * Flexible use of multiple R versions on the same server. This is useful when you have some analysts or projects that require older versions of R or R packages and some that require newer versions.

![](https://support.rstudio.com/hc/en-us/article_attachments/203432008/mutlipleRVersions2.png)

  * Project sharing for easy collaboration within workgroups. When you share a project, RStudio Server securely grants other users access to the project, and when multiple users are active in the project at once, you can see each others' activity and work together in a shared editor.

![](https://support.rstudio.com/hc/en-us/article_attachments/203236337/Screen_Shot_2015-09-30_at_3.55.46_PM.png)

See the updated [RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro/) page for additional details, including a set of videos which demonstrate the new features.

### Try it Out

RStudio v0.99.878 is [available for download](https://www.rstudio.com/products/rstudio/download/) now. We hope you enjoy the new release and as always please [let us know](https://support.rstudio.com/) how it's working and what else we can do to make the product better.

