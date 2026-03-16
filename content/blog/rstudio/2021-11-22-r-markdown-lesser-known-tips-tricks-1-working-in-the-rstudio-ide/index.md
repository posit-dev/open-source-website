---
title: 'R Markdown Lesser-Known Tips & Tricks #1: Working in the RStudio IDE'
date: '2021-11-22'
slug: r-markdown-tips-tricks-1-rstudio-ide
tags:
  - R Markdown
  - Product How-to
people:
  - Brendan Cullen
  - Alison Hill
  - Isabella Velásquez
blogcategories:
  - Training and Education
  - Open Source
events: blog
alttext: Trail in forest with a light at the end of the path during sunset
description: In this series, we walk through lesser-known tips and tricks to help you work more effectively and efficiently in R Markdown. This first post focuses on working with R Markdown in the RStudio IDE.
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---

<caption>

Photo by <a href="https://unsplash.com/@jplenio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Johannes Plenio</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

</caption>

The R Markdown file format combines R programming and the markdown language to create dynamic, reproducible documents. R Markdown can be used for reports, slide shows, blogs, books --- even <a href="https://bookdown.org/yihui/rmarkdown/shiny-start.html" target = "_blank">Shiny apps</a>! With so many possibilities, authors learn how to use their tools in effective ways.

We asked our Twitter friends <a href="https://twitter.com/_bcullen/status/1333878752741191680" target = "_blank">the tips and tricks that they have picked up</a> along their R Markdown journey. There was a flurry of insightful replies, ranging from organizing files to working with YAML. We wanted to highlight some of the responses so that you can also use them when creating R Markdown documents.

This is the first of a four-part series to help you on your path to R Markdown success, starting with **working with R Markdown documents in the RStudio IDE.**

**1. Create new chunks with shortcuts**

We understand the pain of typing out all those backticks to create a new chunk, and <a href="https://yihui.org/en/2021/10/unbalanced-delimiters/" target = "_blank">it is also error-prone</a>. Instead, insert an R code chunk by clicking the Insert button on the document toolbar.

<center>

<img src="img/img9.png" alt="Insert button in document toolbar that looks like a green square with a C and a plus sign." width="80%"/>

</center>
<br>
You can also type the keyboard shortcut <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> (<kbd>Cmd</kbd> + <kbd>Option</kbd> + <kbd>I</kbd> on macOS). Use the shortcut inside a chunk to split it into two:

![Breaking up one code chunk into two using Ctrl+Cmd+I Shortcut in RStudio IDE](img/img1.gif)

**2. Run all (or some) chunks**

Within RStudio, the Run button on the right-hand side of the document toolbar opens a drop-down menu. The menu contains handy shortcuts for running code chunks.

<center>

<img src="img/img10.png" alt="Run dropdown menu with various options for running code chunks." width="50%"/>

</center>
<br>

For example, you don't have to run chunks individually. Run all chunks below your cursor by clicking **Run All Chunks Below**.

![Selections available from the Run button menu in RStudio](img/img2.gif)

**3. Show plots in the Viewer pane**

By default, code chunks display R Markdown plots "inline", or directly underneath the code chunk. If you would rather see the plot in the Viewer pane, go to **RStudio** \> **Preferences** \> **R Markdown** and unselect "Show output inline for all R Markdown documents".

<center>

<img src="img/img3.png" alt="R Markdown checkbox for the output options in Global Options" width="70%"/>

</center>

Voilà! Next time you run the document, the plot will show in the Viewer pane as opposed to inline.

*Before...*

![*Output inline with code*](img/img4.png)

*After...*

![*Output in Viewer pane*](img/img5.png)

**4. Drag and drop formulas from Wikipedia into your R Markdown document**

You can include LaTeX formulas in your R Markdown files. Enclose them between dollar signs (`$`) to see the rendered formula.

Since Wikipedia uses LaTeX HTML formatting on its website, this means you can highlight formulas and drag them into your R Markdown document.

![Pasting phi LaTeX formula from Wikipedia into R Markdown](img/img6.gif)

**5. Use the visual markdown editor**

<a href="https://www.rstudio.com/products/rstudio/download/" target = "_blank">RStudio v1.4</a> has a visual markdown editing mode. This lets you see what your R Markdown document will look like without knitting. You can edit your document in this mode, as well.

Click the compass button on the far-right end of the document toolbar to switch into visual markdown editing mode.

<center>

<img src="img/img11.png" alt="Visual markdown editor button on the right-hand side of toolbar." width="80%"/>

</center>
<br>


Alternatively, you can use the <kbd>⇧</kbd>+<kbd>⌘</kbd>+<kbd>F4</kbd> keyboard shortcut.

![Switching to Visual Markdown Editing Mode on RStudio using shortcuts](img/img7.gif)

Typing <kbd>⌘/</kbd> finds and inserts what you need into the document:

![*Inserting a header using the visual editor shortcut*](img/img8.gif)

These are only a few of the many features available in the visual markdown editor. Read more in <a href="https://rstudio.github.io/visual-markdown-editing/" target = "_blank">the RStudio Visual Markdown Editing documentation</a>.

## Continue the Journey

We hope that these tips & tricks help you when you are working with R Markdown documents in the RStudio IDE. Thank you to everybody who shared advice, workflows, and features!

Stay tuned for the second post in this four-part series: **Cleaning up your code.**

## Resources

- For more information on R Markdown and the RStudio IDE, see <a href="https://rmarkdown.rstudio.com/articles_integration.html" target = "_blank">R Markdown Integration in the IDE</a>.
- Read more about Visual R Markdown in the <a href="https://rstudio.github.io/visual-markdown-editing/" target = "_blank">documentation</a> and the <a href="https://blog.rstudio.com/2020/09/30/rstudio-v1-4-preview-visual-markdown-editing/" target = "_blank">accompanying blog post</a>.
- To learn about RStudio Connect, a platform on which you can schedule and deploy for R Markdown documents so they are accessible to all the relevant stakeholders in your organization, check out the <a href="https://www.rstudio.com/products/connect/" target = "_blank">RStudio Connect product page</a>.
