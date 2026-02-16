
<!-- README.md is generated from README.Rmd. Please edit that file -->

# watcher

<!-- badges: start -->

[![CRAN
status](https://www.r-pkg.org/badges/version/watcher)](https://CRAN.R-project.org/package=watcher)
[![R-CMD-check](https://github.com/r-lib/watcher/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/watcher/actions/workflows/R-CMD-check.yaml)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/watcher/graph/badge.svg)](https://app.codecov.io/gh/r-lib/watcher)
<!-- badges: end -->

Watch the File System for Changes

[![Ask
DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/r-lib/watcher)

R binding for [libfswatch](https://emcrisostomo.github.io/fswatch/), a
file system monitoring library. This uses an optimal event-driven API
for each platform:

- `ReadDirectoryChangesW` on Windows
- `FSEvents` on MacOS
- `inotify` on Linux
- `kqueue` on BSD
- `File Events Notification` on Solaris/Illumos

Watching is performed asynchronously in the background, without blocking
the session.

- Watch files, or directories recursively.
- Log activity, or call an R function, upon every change event.

## Installation

Install watcher from CRAN with:

``` r
install.packages("watcher")
```

#### Installation from Source

watcher requires the ‘libfswatch’ library.

- On Linux / MacOS, an installed version will be used if found in the
  standard filesystem locations.
- On Windows, or if not found, the bundled version of ‘libfswatch’
  1.19.0-dev will be compiled from source.
- Source compilation of the library requires ‘cmake’.

## Quick Start

Create a ‘Watcher’ using `watcher::watcher()`.

By default this will watch the current working directory recursively and
write events to `stdout`.

Set the `callback` argument to run an R function, or rlang-style
formula, every time a file changes:

- Uses the ‘later’ package to execute the callback when R is idle at the
  top level, or whenever `later::run_now()` is called, for instance
  automatically in Shiny’s event loop.
- Function is called back with a character vector of the paths of all
  files which have changed.

``` r
library(watcher)
dir <- file.path(tempdir(), "watcher-example")
dir.create(dir)

w <- watcher(dir, callback = ~print(.x), latency = 0.5)
w
#> <Watcher>
#>   Public:
#>     get_path: function () 
#>     initialize: function (path, callback, latency) 
#>     is_running: function () 
#>     start: function () 
#>     stop: function () 
#>   Private:
#>     path: /var/folders/38/lgkw9s3d5tn626g4z2r11bzm0000gp/T//RtmpFm ...
#>     running: FALSE
#>     watch: externalptr
w$start()

file.create(file.path(dir, "newfile"))
#> [1] TRUE
file.create(file.path(dir, "anotherfile"))
#> [1] TRUE
later::run_now(1)
#> [1] "/private/var/folders/38/lgkw9s3d5tn626g4z2r11bzm0000gp/T/RtmpFmlhtZ/watcher-example"            
#> [2] "/private/var/folders/38/lgkw9s3d5tn626g4z2r11bzm0000gp/T/RtmpFmlhtZ/watcher-example/newfile"    
#> [3] "/private/var/folders/38/lgkw9s3d5tn626g4z2r11bzm0000gp/T/RtmpFmlhtZ/watcher-example/anotherfile"

newfile <- file(file.path(dir, "newfile"), open = "r+")
cat("hello", file = newfile)
close(newfile)
later::run_now(1)
#> [1] "/private/var/folders/38/lgkw9s3d5tn626g4z2r11bzm0000gp/T/RtmpFmlhtZ/watcher-example/newfile"

file.remove(file.path(dir, "newfile"))
#> [1] TRUE
later::run_now(1)
#> [1] "/private/var/folders/38/lgkw9s3d5tn626g4z2r11bzm0000gp/T/RtmpFmlhtZ/watcher-example/newfile"

w$stop()
unlink(dir, recursive = TRUE, force = TRUE)
```

## Acknowledgements

Thanks to the authors of
[libfswatch](https://emcrisostomo.github.io/fswatch/), upon which this
package is based:

- Alan Dipert
- Enrico M. Crisostomo
