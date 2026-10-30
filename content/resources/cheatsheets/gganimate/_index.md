---
title: Animate ggplots with gganimate
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-05-01'
description: Add animation to ggplot2 plots by specifying transitions, view changes, enter/exit effects, and easing.
download_url: gganimate.pdf
people:
- Karl Hailperin
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

gganimate extends the ggplot2 grammar of graphics with animation by adding four groups of functions to existing plots. Animations are driven by transition functions that determine what changes, optionally combined with view functions, enter/exit effects, shadows, and easing specifications.

## What's covered
- Core concepts – transition, view, enter/exit, shadow, ease function groups
- `transition_states()` – cycling between discrete variable values
- `transition_time()` – continuous time-based transitions
- `transition_reveal()` – cumulative data reveal along an axis
- `transition_filters()` – cycling between filter conditions
- Other transitions – `transition_manual()`, `transition_layers()`, `transition_events()`
- `view_follow()` – axes track the data
- `view_step()` – step through views at a controlled pace
- `view_zoom()` – zoom and pan between views
- `ease_aes()` – control pace of change between transition values
