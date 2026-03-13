---
title: Code Annotation
subtitle: Add line based annotations to your code chunks
description: >
  In Quarto 1.3, you can add line based annotations to code chunks to highlight
  or explain parts of your code.
categories:
  - Features
  - Authoring
  - Quarto 1.3
people:
  - Charlotte Wickham
date: '2023-03-13'
image: annotation.png
image-alt: >-
  Screenshot a code chunk with annotations. Annotations appear in the code chunk
  as numbers within circles, and repeat below the code chunk along with the text
  content of the annotations.
code-annotations: below
ported_from: quarto
port_status: in-progress
---


> **Quarto 1.3 Feature**
>
> This post is part of a series highlighting new features in the 1.3 release of Quarto. Get the latest release the [download page](https://quarto.org/docs/download/)

Code blocks and executable code cells in Quarto may now include line-based annotations. Line-based annotations provide a way to attach explanation to lines of code much like footnotes.

For example, this code uses annotation to describe the steps in an R dplyr pipeline in plain language:

``` r
library(tidyverse)
library(palmerpenguins)
penguins |>
  mutate(
    bill_ratio = bill_depth_mm / bill_length_mm,
    bill_area  = bill_depth_mm * bill_length_mm
  )
```

Line 3
:   Take `penguins`, and then,

Lines 4-7
:   add new columns for the bill ratio and bill area.

The default HTML annotation style displays annotations in a list below the code block. Clicking on the annotation number in the list highlights the relevant lines in the code. Other HTML styles hide the annotations, revealing them in a tooltip when a user hovers or selects a marker.

The PDF format also allows for annotations, numbering, and displaying the annotation text below the code. In other formats, like Word and GitHub Markdown, annotations are instead labeled with the line of code (or lines of code) to which the annotation text applies.

#### PDF

<img src="annote-pdf.png" data-fig-alt="Screenshot of output in PDF format showing code annotation." />

#### GitHub Flavored Markdown

```` markdown
``` r
library(tidyverse)
library(palmerpenguins)
penguins |>
  mutate(
    bill_ratio = bill_depth_mm / bill_length_mm,
    bill_area  = bill_depth_mm * bill_length_mm
  )
```

Line 3  
Take `penguins`, and then,

Lines 4-7  
add new columns for the bill ratio and bill area.
````

To add code annotation to a code block, you need to add two things: specially formatted code comments in your code cell, and an ordered list below the code cell with the annotation text:

1.  **Code Comments**: Each annotated line in the code cell should be terminated with a comment (using the code cell's language comment character) followed by a space and then an annotation number enclosed in angle brackets (e.g. `# <2>`). You may repeat an annotation number if the annotation spans multiple lines.

2.  **Ordered List**: An ordered list should appear immediately after the code cell, and include the contents of each annotation. Each numbered item in the ordered list will correspond to the line(s) of code with the same annotation number.

For example, the annotations above were produced by including the following in the Quarto document:

```` markdown
```r
library(tidyverse)
library(palmerpenguins)
penguins |>                                      # <1>
  mutate(                                        # <2>
    bill_ratio = bill_depth_mm / bill_length_mm, # <2>
    bill_area  = bill_depth_mm * bill_length_mm  # <2>
  )                                              # <2>
```
1. Take `penguins`, and then,
2. add new columns for the bill ratio and bill area.
````

You can read more about how to control the annotation style, and whether annotations appear at all on the [Code Annotation page](https://quarto.org/docs/authoring/code-annotation.html) of the pre-release highlights.
