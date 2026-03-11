---
title: Shiny 0.13.0
people:
  - Winston Chang
date: '2016-01-20'
categories:
- News
- Packages
- Shiny
slug: shiny-0-13-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- Shiny
events: blog
ported_from: rstudio
port_status: raw
---


Shiny 0.13.0 is now available on CRAN! This release has some of the most exciting features we've shipped since the first version of Shiny. Highlights include:

  * Shiny Gadgets

  * HTML templates

  * Shiny modules

  * Error stack traces

  * Checking for missing inputs

  * New JavaScript events

For a comprehensive list of changes, see the [NEWS file](https://cran.r-project.org/web/packages/shiny/NEWS).

To install the new version from CRAN, run:

```r
install.packages("shiny")
```

Read on for details about these new features!

<!-- more -->

## Shiny Gadgets

With Shiny Gadgets, you can use Shiny to create interactive graphical tools that run locally, taking your data as input and returning a result. This means that Shiny isn't just for creating applications to be delivered over the web – it can also be part of your interactive data analysis toolkit!

Your workflow could, for example, look something like this:

  1. At the R console, read in and massage your data.

  2. Use a Shiny Gadget's graphical interface to build a model and tweak model parameters. When finished, the Gadget returns the model object.

  3. At the R console, use the model to make predictions.

Here's a Shiny Gadget in action ([code here](https://gist.github.com/wch/c4b857d73493e6550cba)). This Gadget fits an `lm` model to a data set, and lets the user interactively exclude data points used to build the model; when finished, it returns the data with points excluded, and the model object:

![lm_gadget](https://rstudioblog.files.wordpress.com/2016/01/lm_gadget.gif)

When used in RStudio, Shiny Gadgets integrate seamlessly, appearing in the Viewer panel, or in a pop-up dialog window. You can even declare your Shiny Gadgets to be [RStudio Add-ins](http://rstudio.github.io/rstudioaddins/), so they can be launched from the RStudio Add-ins menu or a customizable keyboard shortcut.

When used outside of RStudio, Shiny Gadgets have the same functionality – the only differences are that you invoke them by executing their R function, and that they open in a separate browser window.

Best of all, if you know how to write Shiny apps, you're 90% of the way to writing Gadgets! For the other 10%, see the [article](https://shiny.rstudio.com/articles/gadgets.html) in the Shiny Dev Center.

## HTML templates

In previous versions of Shiny, you could choose between writing your UI using either ui.R (R function calls like `fluidPage`, `plotOutput`, and `div`), or index.html (plain old HTML markup).

With Shiny 0.13.0, you can have the best of both worlds in a single app, courtesy of the new HTML templating system (from the **htmltools** package). You can author the structure and style of your page in HTML, but still conveniently insert input and output widgets using R functions.

    <!DOCTYPE html>
    <html>
      <head>
        <link href="custom.css" rel="stylesheet" />
        {{ headContent() }}
      </head>
      <body>
      {{ sliderInput("x", "X", 1, 100, sliderValue) }}
      {{ button }}
      </body>
    </html>

To use the template for your UI, you process it with `htmlTemplate()`. The text within the `{{ ... }}` is evaluated as R code, and is replaced with the return value.

```r
htmlTemplate("template.html",
  button = actionButton("go", "Go")
)
```

In the example above, the template is used to generate an entire web page. Templates can also be used for pieces of HTML that are inserted into a web page. You could, for example, create a reusable UI component which uses an HTML template.

If you want to learn more, see the [HTML templates](https://shiny.rstudio.com/articles/templates.html) article.

## Shiny modules

We've been surprised at the number of users making large, complex Shiny apps – to the point that abstractions for managing Shiny code complexity has become a frequent request.

After much discussion and iteration, we've come up with a [modules feature](https://shiny.rstudio.com/articles/modules.html) that should be a huge help for these apps. A Shiny module is like a fragment of UI and server logic that can be embedded in either a Shiny app, or in another Shiny module. Shiny modules use namespaces, so you can create and interact with UI elements without worrying about their input and output IDs conflicting with anyone else's. You can even embed a Shiny module in a single app multiple times, and each instance of the module will be independent of the others.

To get started, check out the [Shiny modules](https://shiny.rstudio.com/articles/modules.html) article.

(Special thanks to [Ian Lyttle](http://twitter.com/ijlyttle), whose earlier work with [shinychord](https://github.com/ijlyttle/shinychord) provided inspiration for modules.)

## Better debugging with stack traces

In previous versions of Shiny, if your code threw an error, it would tell you that an error occurred (the app would keep running), but wouldn't tell you where it's from:

    Listening on http://127.0.0.1:6212
    Error in : length(n) == 1L is not TRUE

As of 0.13.0, Shiny gives a stack trace so you can easily find where the problem occurred:

    Listening on http://127.0.0.1:6212
    Warning: Error in : length(n) == 1L is not TRUE
    Stack trace (innermost first):
        96: stopifnot
        95: head.default
        94: head
        93: reactive mydata [~/app.R#10]
        82: mydata
        81: ggplot
        80: renderPlot [~/app.R#14]
        72: output$plot
         5: <Anonymous>
         4: do.call
         3: print.shiny.appobj
         2: print
         1: source

In this case, the error was in a reactive named `mydata` in `app.R`, line 10, when it called the `head()` function. Notice that the stack trace only shows stack frames that are relevant to the app – there are many frames that are internal Shiny code, and they are hidden from view by default.

For more information, see the [debugging](https://shiny.rstudio.com/articles/debugging.html) article.

## Checking inputs with `req()`

In Shiny apps, it's common to have a reactive expression or an output that can only proceed if certain conditions are met. For example, an input might need to have a selected value, or an `actionButton` might need to be clicked before an output should be shown.

Previously, you would need to use a check like `if (is.null(input$x)) return()`, or `validate(need(input$x))`, and a similar check would be needed in all downstream reactives/observers that rely on that reactive expression.

Shiny 0.13.0 provides new a function, `req()`, which simplifies this process. It can be used `req(input$x)`. Reactives and observers which are downstream will not need a separate check because a `req()` upstream will cause them to stop.

You can call `req()` with multiple arguments to check multiple inputs. And you can also check for specific conditions besides the presence or absence of an input by passing a logical value, e.g. `req(Sys.time() <= endTime)` will stop if the current time is later than `endTime`.

For more details, see the [article](https://shiny.rstudio.com/articles/req.html) in the Shiny Dev Center.

## JavaScript Events

For developers who want to write JavaScript code to interact with Shiny in the client's browser, Shiny now has a set of JavaScript events to which event handler functions can be attached. For example, the `shiny:inputchanged` event is triggered when an input changes, and the `shiny:disconnected` event is triggered when the connection to the server ends.

See the [article](https://shiny.rstudio.com/articles/js-events.html) for more.

