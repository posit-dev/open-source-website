---
title: Test Filename on Code Blocks
layout: single
---


## Code block with filename

``` python { filename="app.py" }
from shiny.express import input, ui
import shinyswatch

ui.input_slider("num", "Number:", min=10, max=100, value=30)
```

## Code block without filename

``` python
print("hello world")
```

## Another filename

``` yaml { filename="_quarto.yml" }
project:
  type: website
format:
  html:
    theme: cosmo
```

## Plain text with filename

``` { filename="Makefile" }
build:
    echo "building..."
```

## Filename with code-line-numbers

``` python { filename="app.py" }
from shiny.express import input, ui

ui.input_slider("num", "Number:", min=10, max=100, value=30)
```

## Filename with custom class

``` python { filename="example.py" }
print("hello world")
```

## Filename with shortcodes=false

``` yaml { filename="_quarto.yml" }
project:
  type: website
```
