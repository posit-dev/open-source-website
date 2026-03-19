---
title: Shiny 1.0.1
people:
  - Bárbara Borges Ribeiro
date: '2017-04-05'
slug: shiny-1-0-1
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
categories:
  - Interactive Apps
ported_categories:
  - Packages
  - Shiny
---


Shiny 1.0.1 is now available on CRAN! This release primarily includes bug fixes and minor new features.

The most notable additions in this version of Shiny are the introduction of the `reactiveVal()` function (like `reactiveValues()`, but it only stores a single value), and that the choices of `radioButtons()` and `checkboxGroupInput()` can now contain HTML content instead of just plain text. We've also added compatibility for the development version of `ggplot2`.

## Breaking changes

We unintentionally introduced a minor breaking change in that `checkboxGroupInput` used to accept `choices = NULL` to create an empty input. With Shiny 1.0.1, this throws an error; using `choices = character(0)` works. We intend to eliminate this breakage in Shiny 1.0.2.

**Update** (4/20/2017): This has now been fixed in Shiny 1.0.2, currently available on CRAN.

Also, the `selected` argument for `radioButtons`, `checkboxGroupInput`, and `selectInput` once upon a time accepted the name of a choice, instead of the value of a choice; this behavior has been deprecated with a warning for several years now, and in Shiny 1.0.1 it is no longer supported at all.

## Storing single reactive values with `reactiveVal`

The `reactiveValues` object has been a part of Shiny since the earliest betas. It acts like a reactive version of an environment or named list, in that you can store and retrieve values using names:

```r
rv <- reactiveValues(clicks = 0)

observeEvent(input$button, {
 currentValue <- rv$clicks
 rv$clicks <- currentValue + 1
})
```

If you only have a single value to store, though, it's a little awkward that you have to use a data structure designed for multiple values.

With the new `reactiveVal` function, you can now create a reactive object for a single variable:

```r
clicks <- reactiveVal(0)

observeEvent(input$button, {
 currentValue <- clicks()
 clicks(currentValue + 1)
})
```

As you can see in this example, you can read the value by calling it like a function with no arguments; and you set the value by calling it with one argument.

This has the added benefit that you can easily pass the `clicks` object to another function or module (no need to wrap it in a `reactive()`).

## More flexible `radioButtons` and `checkboxGroupInput`

It's now possible to create radio button and checkbox inputs with arbitrary HTML as labels. To do so, however, you need to pass different arguments to the functions. Now, when creating (or updating) either of `radioButtons()` or `checkboxGroupInput()`, you can specify the options in one of two (mutually exclusive) ways:

  * **What we've always had**:
Use the `choices` argument, which must be a vector or list. The names of each element are displayed in the app UI as labels (i.e. what the user sees in your app), and the values are used for computation (i.e. the value is what's returned by `input$rd`, where `rd` is a `radioButtons()` input). If the vector (or list) is unnamed, the values provided are used for both the UI labels and the server values.

  * **What's new and allows HTML**:
Use both the `choiceNames` and the `choiceValues` arguments, each of which must be an _unnamed_ vector or list (and both must have the same length). The elements in `choiceValues` must still be plain text (these are the values used for computation). But the elements in `choiceNames` (the UI labels) can be constructed out of HTML, either using the `HTML()` function, or an HTML tag generation function, like `tags$img()` and `icon()`.

[Here's an example app](https://gist.github.com/bborgesr/f2c865556af3b92e6991e1a34ced2a4a) that demos the new functionality (in this case, we have a `checkboxGroupInput()` whose labels include the flag of the country they correspond to):

![](https://rstudioblog.files.wordpress.com/2017/04/countries-shadow.png)

## `ggplot2` > 2.2.1 compatibility

The development version of `ggplot2` has some changes that break compatibility with earlier versions of Shiny. The fixes in Shiny 1.0.1 will allow it to work with any version of `ggplot2`.

## A note on Shiny v1.0.0

In January of this year, we quietly released Shiny 1.0.0 to CRAN. A lot of work went into that release, but other than minor bug fixes and features, it was mostly laying the foundation for some important features that will arrive in the coming months. So if you're wondering if you missed the blog post for Shiny 1.0.0, you didn't.

## Full changes

As always, you can view the full changelog for Shiny 1.0.1 (and 1.0.0!) in our [NEWS.md](https://github.com/rstudio/shiny/blob/master/NEWS.md) file.

