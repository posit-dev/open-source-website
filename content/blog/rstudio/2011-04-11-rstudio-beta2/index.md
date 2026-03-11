---
title: RStudio Beta 2 (v0.93)
people:
  - RStudio Team
date: '2011-04-11'
categories:
- RStudio IDE
slug: rstudio-beta2
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


RStudio Beta 2 (v0.93) is [available for download](http://www.rstudio.org/download/) today. We've gotten incredibly helpful input from the R community and this release reflects a lot of that feedback.

The [release notes](http://www.rstudio.org/docs/release_notes_v0.93.html) have the full details on what's new. Some of the highlights include:

#### Source Editor Enhancements

  * Highlight all instances of selected text

  * Insert spaces for tabs (soft-tabs)

  * Customizable print margin line

  * Selected line highlight

  * Toggle line numbers on/off

  * Optional soft-wrapping for R source files

#### Customizable Layout and Appearance

  * The layout of panes and tabs is now configurable (enabling side-by-side source and console view, among others).

  * Support for a variety of editing themes, including TextMate, Eclipse, and others.

[](https://rstudioblog.files.wordpress.com/2011/04/options_appearance1.png)[![](https://rstudioblog.files.wordpress.com/2011/04/options-appearance.png)](http://www.rstudio.org/docs/using/customizing)

#### Interactive Plotting

This release features [manipulate](http://www.rstudio.org/docs/advanced/manipulate), a new interactive plotting feature that enables you to create plots with inputs bound to custom controls (e.g. slider, picker, etc.) rather than hard-coded to a single value. For example:

```r
manipulate(
  # plot expression
  plot(cars, xlim = c(0, x.max), type = type, ann = label),
  # controls
  x.max = slider(10, 25, step = 5, initial = 25),
  type = picker("Points" = "p", "Line" = "l", "Step" = "s"),
  label = checkbox(TRUE, "Draw Labels")
)
```

[![](https://rstudioblog.files.wordpress.com/2011/04/manipulate_reduced_noborder3.png)](http://www.rstudio.org/docs/advanced/manipulate)

#### More

  * RStudio now works with versions of R installed from source (either via make install or packaged by MacPorts, Homebrew, etc.).

  * Enhanced support for Unicode and non-ASCII character encodings.

  * Improved working directory management including new options for default behavior, support for shell "open with" context menus, and optional file assocations for common R file types (.RData, .R, .Rnw).

  * Many other small enhancements and bug fixes (see the [release notes](http://www.rstudio.org/docs/release_notes_v0.93.html) for full details).

We hope you try out the new release and keep talking to us on our [support forum](http://support.rstudio.org) about what works, what doesn't, and what else you'd like RStudio to do.

