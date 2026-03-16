---
title: >-
  Towards easy, delightful, and customizable dashboards in Shiny for R with
  {bslib}
description: >
  The {bslib} R package nows makes it very easy to make delightful and
  customizable dashboard in Shiny for R. This post walks through a Shiny app
  which quickly illustrates what's possible with these components.
people:
  - Carson Sievert
date: '2023-06-07'
image: feature.png
ported_from: shiny
port_status: in-progress
---


<style>
.quarto-video> div {
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}
</style>

I'm excited to share that the latest release of the [`{bslib}` R package](https://rstudio.github.io/bslib) makes a significant step towards being our recommended way to create Shiny dashboards. Grab it now from CRAN with:

``` r
install.packages("bslib")
```

This release includes a major overhaul of our documentation, including new and updated articles and better organization of content. The [bslib site](https://rstudio.github.io/bslib/) nows groups these articles by whether you're just get started, or want to dive deeper into theming, UI components, or layouts.
If you're primarily interested in making dashboards, make sure to visit the [Getting Started with dashboards](https://rstudio.github.io/bslib/articles/dashboards.html) article.

In this blog post, I'll discuss some of the new features that contribute to the dashboarding experience, as well as why we've chosen `{bslib}` as the home for this work.
You can run the examples in this post yourself (without having to install anything!) in [this Posit Cloud project](https://posit.cloud/content/6073069).

### Hello dashboards

`{bslib}`'s [last release](/blog/shiny/announcing-new-r-shiny-ui-components/) first introduced some important dashboard components (e.g., cards, value boxes, etc), but this release adds other essential pieces such as sidebar layouts, filling layouts, new column-wise layouts, accordions, and more. `{bslib}`'s new [Getting Started with dashboards](https://rstudio.github.io/bslib/articles/dashboards.html) article introduces all these pieces by first starting with a basic app and working towards some non-trivial dashboards, like the one below:

![A Shiny dashboard for exploring the palmerpenguins dataset built using bslib](dashboard.mp4)

<a  href="https://posit.cloud/content/6073069" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="01-hello-dashboards.R">
<i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Try on Posit Cloud
</a>
<a class="ms-1" href="https://gist.github.com/gadenbuie/74ba1d0a4d597aba20caf1b6bf41922f#file-01-hello-dashboards-r" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code">
<i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Source
</a>

### Why bslib? Themable dashboards

Since we [announced it at rstudio::conf(2020)](https://posit.co/resources/videos/styling-shiny-apps-with-sass-and-bootstrap-4/)[^1],
bslib has made it easy to theme virtually any Shiny app, R Markdown document, or R project that utilizes Bootstrap.
One notable and unfortunate exception has been `{shinydashboard}`,
arguably the most popular UI extension for Shiny apps.

While projects like `{bs4Dash}` and `{fresh}` have helped provide way to upgrade `{shinydashboard}`'s Bootstrap/AdminLTE dependency and theme dashboards,
AdminLTE has kept shinydashboard from keeping up with modern versions of Bootstrap (now on version 5).

Rather than rewriting `{shinydashboard}`,
we're choosing to expand the footprint of bslib.
It now provides themable and modern Bootstrap components that are perfect for dashboard apps,
meaning that you can expect [real time themes](https://rstudio.github.io/bslib/articles/theming.html#real-time), [Bootswatch themes](https://rstudio.github.io/bslib/articles/theming.html#bootswatch), and [custom themes](https://rstudio.github.io/bslib/articles/theming.html#main-colors) to "just work" like they do for most other Shiny apps and R Markdown docs powered by `{bslib}`.

![Real-time theming a Shiny dashboard with bslib](dashboard-real-time.mp4)

<a  href="https://posit.cloud/content/6073069" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="02-themable-dashboards.R">
<i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Try on Posit Cloud
</a>
<a class="ms-1" href="https://gist.github.com/gadenbuie/74ba1d0a4d597aba20caf1b6bf41922f#file-02-themable-dashboards-r" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code">
<i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Source
</a>

### Layout tooling

This release includes two big improvements to layouts. First, `{bslib}` has been re-worked to fully embrace [filling layouts](https://rstudio.github.io/bslib/articles/dashboards.html#scrolling-vs-filling) by default. This means that things like `page_sidebar()`, `page_navbar()`, and `page_fillable()` all encourage their children to fill the window (by default), and components like `card()` also encourage their contents to fill when made [full-screen](https://rstudio.github.io/bslib/articles/cards.html#filling-outputs). Keep in mind, filling layouts aren't always the best choice for every situation, but you can always [specify fixed sizes, restrict resizing limits, or opt-out of filling layout](https://rstudio.github.io/bslib/articles/dashboards.html#scrolling-vs-filling).

Second, we've added `layout_columns()`, a new approach to [column-wise layout](https://rstudio.github.io/bslib/articles/dashboards.html#multi-column). Compared to `shiny::fluidRow()`/`shiny::column()`, this newer interface to Bootstrap's 12-column grid layout system is much more expressive and is compatible with filling layouts. For example, in just one function call, you can express a 12-column layout with multiple rows (and control the row heights), define negative space, and even responsively change the layout depending on screen size with a new `breakpoints()` helper function.

![A Shiny dashboard with a responsive, filling, layout](layout-columns.mp4)

<a  href="https://posit.cloud/content/6073069" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="03-layout-tooling.R">
<i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Try on Posit Cloud
</a>
<a class="ms-1" href="https://gist.github.com/gadenbuie/74ba1d0a4d597aba20caf1b6bf41922f#file-03-layout-tooling-r" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code">
<i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Source
</a>

### Card-level sidebars

In addition to page-level sidebars (via `page_sidebar()` and `page_navbar()`), `{bslib}` also provides [card-level sidebars](https://rstudio.github.io/bslib/articles/dashboards.html#cards-with-sidebars). This provides a convenient way to create keep visual proximity between the sidebar (input) controls and outputs that they effect, and as a result, helps users to better navigate more complex apps. This can be done through the `layout_sidebar()` function, which can either render standalone or inside of a `card()` (making it easy to add full-screen expansion, a header, footer, etc).

![A couple examples of putting a sidebar inside a card](layout-sidebar.mp4)

<a  href="https://posit.cloud/content/6073069" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="04-card-level-sidebars.R">
<i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Try on Posit Cloud
</a>
<a class="ms-1" href="https://gist.github.com/gadenbuie/74ba1d0a4d597aba20caf1b6bf41922f#file-04-card-level-sidebars-r" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code">
<i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Source
</a>

### Accordions

This release also includes a new [accordion](https://rstudio.github.io/bslib/reference/accordion.html) component, which is a great way to save space by hiding content behind a collapsible header.
Accordions can be useful in a variety of apps, but in the context of dashboards, they're quite useful for grouping numerous related inputs together.

![Using an accordion inside a sidebar to group multiple input controls together](accordion-sidebar.mp4)

<a  href="https://posit.cloud/content/6073069" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="05-accordions.R">
<i class="me-1" style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Try on Posit Cloud
</a>
<a class="ms-1" href="https://gist.github.com/gadenbuie/74ba1d0a4d597aba20caf1b6bf41922f#file-05-accordions-r" target="_blank" data-bs-toggle="tooltip" data-bs-placement="bottom" title="View Source Code">
<i  style="height:1em;width:1em;fill:currentColor;" aria-hidden="true" role="img"></i>
Source
</a>

### Closing thoughts

With this release, we now view `{bslib}` as a viable alternative to `{shinydashboard}`, and plan on making more improvements geared towards making dashboard creation an even more delightful experience. Compared to `{shinydashboard}`, `{bslib}` offers:

- **A fresh take on components** which build on the latest [Bootstrap](https://getbootstrap.com/), add new features (e.g., full screen expansion, sidebars, etc), and are more customizable.

- **More theming options** including [real-time theming](https://rstudio.github.io/bslib/articles/theming.html#real-time), [bootswatch themes](https://rstudio.github.io/bslib/articles/theming.html#bootswatch), [main colors / fonts](https://rstudio.github.io/bslib/articles/theming.html#main-colors), and [more](https://rstudio.github.io/bslib/articles/theming.html#theming-variables).

- **Better layout tools**, like filling and column-wise layouts. You may have noticed that it wasn't easy to get a row of cards generated by `shinydashboard::box()` to have a common height, but `layout_columns()` and `layout_column_wrap()` do this automatically.

- **Portability**: `{bslib}` is [compatible with most Bootstrap projects](https://rstudio.github.io/bslib/articles/any-project.html), and can be used to create dashboards, websites, R Markdown documents, and more.

That said, `{bslib}` is still a work in progress, and we're still working on making it a "complete" dashboarding solution. If you find yourself missing certain aspects of `{shinydashboard}`, or generally have ideas things we should add, please let us know by [filing an issue](https://github.com/rstudio/bslib/issues/new?assignees=&labels=&projects=&template=feature_request.md) and/or [contributing to this discussion](https://github.com/rstudio/bslib/discussions/618).

<script>
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
</script>

[^1]: Joe Cheng's presentation demoed new theming features in the `{bootstraplib}` package, which evolved into the package known as `{bslib}` and was released to CRAN in 2021.
