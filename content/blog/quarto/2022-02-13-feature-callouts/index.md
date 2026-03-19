---
title: Using Callouts
subtitle: Use callouts to draw attention to important complementary content without
  interupting the document flow
description: |
  Callouts are an excellent way to draw extra attention to certain concepts, or to more clearly indicate that certain content is supplemental or applicable to only some scenarios.
categories:
  - Publishing
people:
  - Charles Teague
date: '2022-02-13'
image: callouts.png
image-alt: 'Three calout boxes: A note (has a blue banner with info icon preceding
  the header), a tip (has a green banner with lightbulb icon preceding the header),
  and an important (has a red banner with info exclamation-point icon preceding the
  header).'
ported_from: quarto
port_status: in-progress
software: ["quarto"]
languages: ["R", "Python", "Julia"]
ported_categories:
  - Features
  - Authoring
tags:
  - Quarto
  - Features
  - Authoring
---


Callouts are an excellent way to draw extra attention to certain concepts, or to more clearly indicate that certain content is supplemental or applicable to only some scenarios.

<img src="callouts.png" class="preview-image" data-fig-align="center" data-fig-alt="Three calout boxes: A note (has a blue banner with info icon preceding the header), a tip (has a green banner with lightbulb icon preceding the header), and an important (has a red banner with info exclamation-point icon preceding the header)." />

## Callout Basics

There are five different types of callouts available.

- note
- tip
- important
- caution
- warning

The color and icon will be different depending upon the type that you select.

## Syntax

Create callouts in markdown using the following syntax (note that the first markdown heading used within the callout is used as the callout heading):

``` markdown
:::{.callout-note}
Note that there are five types of callouts, including:
`note`, `tip`, `warning`, `caution`, and `important`.
:::

:::{.callout-tip}
## Tip With Caption

This is an example of a callout with a caption.
:::
```

See our documentation on [Callouts](https://quarto.org/docs/authoring/callouts.html), to learn more, including more about how to customize the appearance and behavior of callouts.
