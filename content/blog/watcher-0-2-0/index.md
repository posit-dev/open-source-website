---
title: "watcher 0.2.0: filesystem watching for R, and the engine behind Shiny auto-reload"
date: 2026-06-25
people:
  - Charlie Gao
description: >
  watcher is a lightweight R package that reacts to filesystem changes in the
  background – and the engine behind Shiny's auto-reload. With 0.2.0 it
  builds with R's standard C/C++ toolchain, so it now installs anywhere R does.
image: featured.png
image-alt: >
  A code editor showing a Shiny app.R file beside the running app in a browser.
  Edited lines are highlighted and the app reflects the change, illustrating
  live auto-reload.
topics:
  - Interactive Apps
software:
  - watcher
  - shiny-r
languages:
  - R
source: shiny
tags:
  - rlib
hidesubscription: false
---

If you have ever saved a file in your Shiny app and watched the browser refresh on its own, you may have already used [watcher](https://watcher.r-lib.org) without knowing it.

watcher is a lightweight R package that watches files and directories for changes and reacts in the background. It shipped quietly last year as the engine behind Shiny's auto-reload, and until now that is mostly where it lived. [watcher 0.2.0](https://watcher.r-lib.org) is on CRAN, and the change in this release is the one that lets it leave home: it now builds with R's standard C/C++ toolchain, so it installs on any platform R supports. The watcher behind Shiny is now a general-purpose filesystem watcher you can drop into any R workflow.

## You have already used it: Shiny auto-reload

The inner loop of building a Shiny app is edit, save, switch to the browser, reload. Auto-reload removes the friction of the last two steps: you save, and the app reloads itself.

The easiest way to turn it on is Shiny's [Developer Mode](https://shiny.posit.co/r/reference/shiny/latest/devmode.html), which flips on a handful of developer-friendly options for the session – auto-reload among them, alongside unminified JavaScript and full stack traces. Call `devmode()` once and run your app as usual:

```r
shiny::devmode()
shiny::runApp("app.R")
```

Now every time you save a file in the app directory, the running app reloads to match:

![A code editor and a running Shiny app side by side. As lines in app.R are edited and saved – the title, the bar colour, the number of bins – the app reloads to match, with no interaction in the browser.](shiny-autoreload.gif)

*Editing `app.R` on the left; the app on the right reloads on each save. No manual refresh, no restart.*

Under the hood, Developer Mode sets `shiny.autoreload = TRUE` (you can set that option directly if you'd rather not switch on the rest of Developer Mode), which hands your app directory to watcher and starts it watching in the background. The instant you save a matching file – `.R`, `.html`, `.css`, `.js`, or an image – watcher's callback fires and Shiny pushes a reload down the websocket it already holds open to the browser.

Previously Shiny did this by polling: every few hundred milliseconds it re-listed the directory and compared modification times. That works, but the cost scales with the size of your project and the reload only ever happens on the next tick. watcher instead subscribes to the operating system's own filesystem-change notifications, so the reload fires on the save itself and an idle app does no work at all. (If watcher isn't installed, Shiny still falls back to the polling watcher – and nudges you to install watcher for a faster one.) Shiny maps its existing `shiny.autoreload.interval` onto watcher's `latency`, a short debounce so that a flurry of saves triggers a single reload.

## watcher, the package

The same machinery is available directly. `watcher()` returns an [R6](https://r6.r-lib.org) object you start and stop:

```r
library(watcher)

dir <- file.path(tempdir(), "watched")
dir.create(dir)

w <- watcher(dir, callback = ~ cat("changed:", .x, "\n"), latency = 0.5)
w$start()
```

From now on, any change under `dir` calls your function back with the paths that changed:

```r
file.create(file.path(dir, "report.csv"))
later::run_now(1)
#> changed: /tmp/Rtmp8fKd2p/watched/report.csv

w$stop()
```

Three arguments cover most needs:

- **`path`** – a file, a directory (watched recursively), or a vector of paths. Defaults to the working directory.
- **`callback`** – a function or `~` formula (via [rlang](https://rlang.r-lib.org)) taking one argument: a character vector of the paths that changed. The default, `NULL`, simply writes the changed paths to `stdout`.
- **`latency`** – seconds to debounce events before reporting them. Defaults to 1.

The returned object also has `$stop()`, `$is_running()` and `$get_path()` alongside `$start()`.

watcher does its watching on a background thread, but your callback runs on R's main thread, scheduled through [later](https://later.r-lib.org). It fires when R is idle at the top level, whenever you call `later::run_now()`, or automatically inside an event loop such as Shiny's. That is what lets it slot into Shiny, plumber, or a [mirai](https://mirai.r-lib.org)-driven app without you managing threads or blocking the session.

## Event-driven, on every platform

watcher binds [libfswatch](https://github.com/emcrisostomo/fswatch), a mature C++ filesystem-monitoring library. On each platform it uses the native, event-driven notification API rather than polling:

- **FSEvents** on macOS
- **inotify** on Linux
- **ReadDirectoryChangesW** on Windows
- **kqueue** on the BSDs
- **File Events Notification** on Solaris / illumos

with a polling backend as a fallback where none of those is available. You get created, updated, removed and renamed events, for individual files or whole directory trees, delivered by the operating system instead of discovered by repeatedly scanning the disk.

## What's new in 0.2.0

The headline of this release isn't a feature – it's the build.

watcher vendors libfswatch so that it has no system dependencies, but compiling that bundled copy used to require `cmake`. On a developer laptop that is usually fine; on a bare server, a minimal CI image, or an HPC login node, a missing `cmake` turned into a failed install from source.

0.2.0 removes that requirement. The bundled libfswatch now compiles with R's own C/C++ toolchain through a plain `Makevars` – no `cmake`, no separate configure-and-install step, no GNU make dependency. If a system libfswatch is already present, watcher links against it; otherwise it builds the vendored copy exactly the way every other R package with C++ code builds. The entire source tarball is around 80 KB.

The practical upshot is that watcher now installs from source on any platform R supports. That is why we're writing about it now: the watcher that has quietly powered Shiny's auto-reload is something you can depend on in your own packages and scripts, everywhere.

## Put it to work

watcher is deliberately small and general. Anything you want to happen when a file changes, you can wire to it:

- rebuild a report or re-render a document when its source or data changes
- reprocess a directory as new files land in it
- re-run tests or reload package code while you develop
- reload configuration without restarting a long-running service

The shape is always the same – give `watcher()` a path and a function:

```r
library(watcher)

rebuild <- function(paths) {
  message(format(Sys.time(), "%H:%M:%S"), " – ", length(paths), " file(s) changed")
  # ... your render / test / reload step here ...
}

w <- watcher("R", rebuild, latency = 1)
w$start()
```

The callback receives the paths that changed, so you can act on exactly what moved.

## Try it

Install from CRAN:

```r
install.packages("watcher")
```

Pointers from here:

- [watcher package site](https://watcher.r-lib.org) – reference and examples.
- [r-lib/watcher](https://github.com/r-lib/watcher) – source, issues, and feedback.
- For Shiny, enable Developer Mode with `shiny::devmode()` (or set `options(shiny.autoreload = TRUE)` directly) and make sure watcher is installed.

## Acknowledgments

watcher builds on [libfswatch](https://github.com/emcrisostomo/fswatch) by Enrico M. Crisostomo, and on earlier R filesystem-watching work by Alan Dipert. Thanks to Garrick Aden-Buie for wiring watcher into Shiny's auto-reload, and to everyone who has contributed issues, fixes, and feedback. Questions and ideas are very welcome on GitHub: [r-lib/watcher](https://github.com/r-lib/watcher/issues).
