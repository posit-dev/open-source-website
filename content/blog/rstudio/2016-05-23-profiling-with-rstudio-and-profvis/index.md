---
title: Profiling with RStudio and profvis
people:
  - Winston Chang
date: '2016-05-23'
categories:
- Packages
- RStudio IDE
slug: profiling-with-rstudio-and-profvis
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


"How can I make my code faster?" If you write R code, then you've probably asked yourself this question. A profiler is an important tool for doing this: it records how the computer spends its time, and once you know that, you can focus on the slow parts to make them faster.

The [preview releases](https://www.rstudio.com/products/rstudio/download/preview/) of RStudio now have integrated support for profiling R code and for visualizing profiling data. R itself has long had a built-in profiler, and now it's easier than ever to use the profiler and interpret the results.

To profile code with RStudio, select it in the editor, and then click on **Profile -> Profile Selected Line(s)**. R will run that code with the profiler turned on, and then open up an interactive visualization.

![](https://rstudioblog.files.wordpress.com/2016/05/profile1.gif)

In the visualization, there are two main parts: on top, there is the code with information about the amount of time spent executing each line, and on the bottom there is a _flame graph_, which shows R was doing over time. In the flame graph, the horizontal direction represents time, moving from left to right, and the vertical direction represents the _call stack_, which are the functions that are currently being called. (Each time a function calls another function, it goes on top of the stack, and when a function exits, it is removed from the stack.)

![profile.png](https://rstudioblog.files.wordpress.com/2016/05/profile.png)

The **Data** tab contains a call tree, showing which function calls are most expensive:

![Profiling data pane](https://rstudioblog.files.wordpress.com/2016/05/data1.png)

Armed with this information, you'll know what parts of your code to focus on to speed things up!

The interactive profile visualizations are created with the [profvis](https://rstudio.github.io/profvis/) package, which can be used separately from the RStudio IDE. If you use profvis outside of RStudio, the visualizations will open in a web browser.

To learn more about interpreting profiling data, check out the [profvis website](https://rstudio.github.io/profvis/), which has interactive demos. You can also find out more about [profiling with RStudio](http://rstudio.github.io/profvis/rstudio.html) there.

