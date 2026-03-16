---
title: Shiny 0.14
people:
  - Winston Chang
date: '2016-09-12'
categories:
- News
- Shiny
slug: shiny-0-14
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
tags:
- Shiny
events: blog
ported_from: rstudio
port_status: in-progress
---


A new Shiny release is upon us! There are many new exciting features, bug fixes, and library updates. We'll just highlight the most important changes here, but you can browse through the [full changelog](https://shiny.rstudio.com/articles/upgrade-0.14.html#full-changelog) for details. This will likely be the last release before shiny 1.0, so get out your party hats!

To install it, you can just run:

```r
install.packages("shiny")
```

## Bookmarkable state

Shiny now supports bookmarkable state: users can save the state of an application and get a URL which will restore the application with that state. There are two types of bookmarking: encoding the state in a URL, and saving the state to the server. With an encoded state, the entire state of the application is contained in the URL's query string. You can see this in action with this app: <https://gallery.shinyapps.io/113-bookmarking-url/>. An example of a bookmark URL for this app is [https://gallery.shinyapps.io/113-bookmarking-url/?inputs&n=200](https://gallery.shinyapps.io/113-bookmarking-url/?_inputs_&n=200). When the state is saved to the server, the URL might look something like: https://gallery.shinyapps.io/bookmark-saved/?state_id=d80625dc681e913a (note that this URL is not for an active app).

**_Important note_:** Saved-to-server bookmarking currently works with Shiny Server Open Source. Support on Shiny Server Pro, RStudio Connect, and [shinyapps.io](http://shinyapps.io) is under development and testing. However, URL-encoded bookmarking works on all hosting platforms.

See [this article](https://shiny.rstudio.com/articles/bookmarking-state.html) to get started with bookmarkable state. There is also an [advanced-level article](https://shiny.rstudio.com/articles/advanced-bookmarking.html), and [a modules article](https://shiny.rstudio.com/articles/bookmarking-modules.html) that details how to use bookmarking in conjunction with modules.

## Notifications

Shiny can now display notifications on the client browser by using the `showNotification()` function. Use [this demo app](https://gallery.shinyapps.io/116-notifications/) to play around with the notification API. For more, see our [article](https://shiny.rstudio.com/articles/notifications.html) about notifications.

## Progress indicators

If your Shiny app contains computations that take a long time to complete, a progress bar can improve the user experience by communicating how far along the computation is, and how much is left. Progress bars were added in Shiny 0.10.2. In Shiny 0.14, we've changed them to use the notifications system, which gives them a different look.

**_Important note_:** If you were already using progress bars and had customized them with your own CSS, you can add the `style = "old"` argument to your `withProgress()` call (or `Progress$new()`). This will result in the same appearance as before. You can also call `shinyOptions(progress.style = "old")` in your app's server function to make all progress indicators use the old styling.

To see new progress bars in action, see [this app](https://gallery.shinyapps.io/085-progress/) in the gallery. You can also learn more about them in [here](https://shiny.rstudio.com/articles/progress.html).

## Modal windows

Shiny has now built-in support for displaying modal dialogs like the one below ([live app here](https://gallery.shinyapps.io/114-modal-dialog/)):

![Modal dialog](https://rstudioblog.files.wordpress.com/2016/09/modal-dialog.png)

To learn more about modal dialogs in Shiny, read the [article](https://shiny.rstudio.com/articles/modal-dialogs.html) about them.

## `insertUI` and `removeUI`

Sometimes in a Shiny app, arbitrary HTML UI may need to be created on-the-fly in response to user input. The existing `uiOutput` and `renderUI` functions let you continue using reactive logic to call UI functions and make the results appear in a predetermined place in the UI. The `insertUI` and `removeUI` functions, which are used in the server code, allow you to use imperative logic to add and remove arbitrary chunks of HTML (all independent from one another), as many times as you want, whenever you want, wherever you want. This option may be more convenient when you want to, for example, add a new model to your app each time the user selects a different option (and leave previous models unchanged, rather than substitute the previous one for the latest one).

See [this simple demo app](https://gallery.shinyapps.io/111-insert-ui/) of how one could use `insertUI` and `removeUI` to insert and remove text elements using a queue. Also see [this other app](https://gallery.shinyapps.io/insertUI/) that demonstrates how to insert and remove a few common Shiny input objects. Finally, [this app](https://gallery.shinyapps.io/insertUI-modules/) shows how to dynamically insert modules using `insertUI`.

For more, read [our article](https://shiny.rstudio.com/articles/dynamic-ui.html) about dynamic UI generation and the reference documentation about [`insertUI`](https://shiny.rstudio.com/reference/shiny/latest/insertUI.html) and [`removeUI`](https://shiny.rstudio.com/reference/shiny/latest/removeUI.html).

## Documentation for connecting to an external database

Many Shiny users have asked about best practices for accessing external databases from their Shiny applications. Although database access has long been possible using various database connector packages in R, it can be challenging to use them robustly in the dynamic environment that Shiny provides. So far, it has been mostly up to application authors to find the appropriate database drivers and to discover how to manage the database connections within an application. In order to demystify this process, we wrote a series of articles ([first one here](https://shiny.rstudio.com/articles/overview.html)) that covers the basics of connecting to an external database, as well as some security precautions to keep in mind (e.g. [how to avoid SQL injection attacks](https://shiny.rstudio.com/articles/sql-injections.html)).

There are a few packages that you should look at if you're using a relational database in a Shiny app: the `dplyr` and `DBI` packages (both featured in the article linked to above), and the brand new `pool` package, which provides a further layer of abstraction to make it easier and safer to use either `DBI` or `dplyr`. `pool` is not yet on CRAN. In particular, `pool` will take care of managing connections, preventing memory leaks, and ensuring the best performance. See this [`pool` basics article](https://shiny.rstudio.com/articles/pool-basics.html) and the [more advanced-level article](https://shiny.rstudio.com/articles/pool-advanced.html) if you're feeling adventurous! (Both of these articles contain Shiny app examples that use `DBI` to connect to an external MySQL database.) If you are more comfortable with `dplyr` than `DBI`, don't miss the article about the [integration of `pool` and `dplyr`](https://shiny.rstudio.com/articles/pool-dplyr.html).

If you're new to databases in the Shiny world, we recommend using `dplyr` and `pool` if possible. If you need greater control than `dplyr` offers (for example, if you need to modify data in the database or use transactions), then use `DBI` and `pool`. The `pool` package was introduced to make your life easier, but in no way constrains you, so we don't envision any situation in which you'd be better off _not_ using it. The only caveat is that `pool` is not yet on CRAN, so you may prefer to wait for that.

## Others

There are many more minor features, small improvements, and bug fixes than we can cover here, so we'll just mention a few of the more noteworthy ones. (For more, you can see the [full changelog](https://shiny.rstudio.com/articles/upgrade-0.14.html#full-changelog).).

  * **Error Sanitization**: you now have the option to sanitize error messages; in other words, the content of the original error message can be suppressed so that it doesn't leak any sensitive information. To sanitize errors everywhere in your app, just add `options(shiny.sanitize.errors = TRUE)` somewhere in your app. Read [this article](https://shiny.rstudio.com/articles/sanitize-errors.html) for more, or play with the [demo app](https://gallery.shinyapps.io/110-error-sanitization/).

  * **Code Diagnostics**: if there is an error parsing `ui.R`, `server.R`, `app.R`, or `global.R`, Shiny will search the code for missing commas, extra commas, and unmatched braces, parens, and brackets, and will print out messages pointing out those problems. ([#1126](https://github.com/rstudio/shiny/pull/1126))

  * **Reactlog visualization**: by default, the [`showReactLog()` function](https://shiny.rstudio.com/reference/shiny/latest/showReactLog.html) (which brings up the reactive graph) also displays the time that each reactive and observer were active for:

![reactlog](https://rstudioblog.files.wordpress.com/2016/09/reactlog.png)

Additionally, to organize the graph, you can now drag any of the nodes to a specific position and leave it there.

  * **Nicer-looking tables**: we've made tables generated with `renderTable()` look cleaner and more modern. While this won't break any older code, the finished look of your table will be quite a bit different, as the following image shows:

![render-table](https://rstudioblog.files.wordpress.com/2016/09/render-table.png)

For more, read our [short article](https://shiny.rstudio.com/articles/render-table.html) about this update, experiment with all the new features in this [demo app](https://gallery.shinyapps.io/109-render-table/), or check out the [reference documentation](https://shiny.rstudio.com/reference/shiny/latest/renderTable.html).

