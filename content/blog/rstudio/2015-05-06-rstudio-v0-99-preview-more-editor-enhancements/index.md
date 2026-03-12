---
title: 'RStudio v0.99 Preview: More Editor Enhancements'
people:
  - Kevin Ushey
date: '2015-05-06'
categories:
- RStudio IDE
slug: rstudio-v0-99-preview-more-editor-enhancements
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


We've blogged previously about various improvements we've made to the source editor in RStudio v0.99 including enhanced [code completion](https://blog.rstudio.com/2015/02/23/rstudio-v0-99-preview-code-completion/), [snippets](https://blog.rstudio.com/2015/04/13/rstudio-v0-99-preview-code-snippets/), [diagnostics](https://blog.rstudio.com/2015/04/28/rstudio-v0-99-preview-code-diagnostics/), and an [improved Vim mode](https://blog.rstudio.com/2015/02/23/rstudio-0-99-preview-vim-mode-improvements/). Besides these larger scale features we've made lots of smaller improvements that we also wanted to highlight. You can try out all of these features now in the RStudio v0.99 [preview release](https://www.rstudio.com/products/rstudio/download/preview/).

### Multiple Cursors

You can now create and use multiple cursors within RStudio. Multiple cursors can be created in a variety of ways:

  * Press **Ctrl + Alt + {Up/Down}** to create a new cursor in the pressed direction,

  * Press **Ctrl + Alt + Shift + {Direction}** to move a second cursor in the specified direction,

  * Use **Alt** and drag with the mouse to create a rectangular selection,

  * Use **Alt + Shift** and click to create a rectangular selection from the current cursor position to the clicked position.

RStudio also makes use of multiple cursors in its Find / Replace toolbar now. After entering a search term, if you press the All button, all items matching that search term are selected.

![Screen Shot 2015-05-05 at 2.58.17 PM](https://rstudioblog.files.wordpress.com/2015/05/screen-shot-2015-05-05-at-2-58-17-pm.png)

You can then begin typing to replace each match with a new term—each matched entry will be updated as you type.

### Rearrangeable Tabs

You can (finally!) move tabs around in the Source pane by clicking and dragging. In the below example, the file 'file_4.R' is currently selected and being dragged into place.

![rearrange-tabs](https://rstudioblog.files.wordpress.com/2015/05/rearrange-tabs2.png)

### New, Improved Editor Themes

A number of new editor themes have been added to RStudio, and older editor themes have been tweaked to ensure that brackets are given a distinct color from text for further legibility.

![themes](https://rstudioblog.files.wordpress.com/2015/05/themes.png)

### Select / Expand Selection

You can use **Ctrl + Shift + E** to select everything within the nearest pair of opening and closing brackets, or use **Ctrl + Alt + Shift + E** to expand the selection up to the next closing bracket.

![Screen Shot 2015-05-05 at 2.56.45 PM](https://rstudioblog.files.wordpress.com/2015/05/screen-shot-2015-05-05-at-2-56-45-pm.png)

### Fuzzy Navigation

You can use **CTRL + .** to quickly navigate between files and symbols within a project. Previously, this search utility performed prefix matching, and so it was difficult to use with long file / symbol names. Now, the **CTRL + .** navigator uses fuzzy matching to narrow the candidate set down based on subsequence matching, which makes it easier to navigate when many files share a common prefix—for example, to **test-** files for a project managing its tests with [testthat](http://r-pkgs.had.co.nz/tests.html).

![Screen Shot 2015-05-05 at 2.41.11 PM](https://rstudioblog.files.wordpress.com/2015/05/screen-shot-2015-05-05-at-2-41-11-pm.png)

### Insert Roxygen Skeleton

RStudio now provides a means for inserting a [Roxygen](http://cran.r-project.org/web/packages/roxygen2/index.html) documentation skeleton above functions. The skeleton generator is smart enough to understand plain R functions, as well as S4 generics, methods and classes—it will automatically fill in documentation for available parameters and slots.

![roxygen-skeleton](https://rstudioblog.files.wordpress.com/2015/05/roxygen-skeleton1.png)

###  More Languages

We've also added syntax highlighting modes for many new languages including Clojure, CoffeeScript, C#, Graphviz, Go, Groovy, Haskell, Java, Julia, Lisp, Lua, Matlab, Perl, Ruby, Rust, Scala, and Stan. There's also some basic keyword and text based code completion for several languages including JavaScript, HTML, CSS, Python, and SQL.

### Try it Out

You can try out all of the new editor features by downloading the latest [preview release](https://www.rstudio.com/products/rstudio/download/preview/) of RStudio. As always, [let us know](https://support.rstudio.com) how the new features are working as well as what else you'd like to see us do.

##

