# Screenshot harness for the querychat-tables-handoff post demos.
# Sourced by each apps/<name>/screenshot.R script.
#
# Adapted from the shinychat-r-0.5.0-python-0.7.1 post's apps/_common.R.
# This post keeps generated images at the post root (no images/ subdir),
# so shot_path() writes there directly instead of into "images/".

suppressPackageStartupMessages({
  library(chromote)
  library(callr)
  library(jsonlite)
  library(httpuv)
})

# ---- paths -----------------------------------------------------------------

file_arg <- grep("^--file=", commandArgs(FALSE), value = TRUE)
file_arg <- sub("^--file=", "", file_arg)
file_arg <- file_arg[file_arg != "-"]
if (length(file_arg)) {
  demo_dir <- dirname(normalizePath(file_arg[1]))
} else {
  demo_dir <- getwd()
}
if (file.exists(file.path(demo_dir, "app.R"))) {
  apps_dir <- dirname(demo_dir)
} else {
  apps_dir <- demo_dir
}
post_dir <- dirname(apps_dir)
images_dir <- post_dir

shot_path <- function(name) file.path(images_dir, name)
app_path <- function(name) file.path(apps_dir, name)

# ---- app lifecycle ---------------------------------------------------------

free_port <- function() {
  for (i in 1:20) {
    port <- as.integer(sample(20000:39999, 1))
    s <- tryCatch(
      httpuv::startServer("127.0.0.1", port, list()),
      error = function(e) NULL
    )
    if (!is.null(s)) {
      on.exit(s$stop())
      return(port)
    }
  }
  stop("Could not find a free port.")
}

start_app <- function(
  app_dir,
  env = character(0),
  port = free_port(),
  timeout = 30
) {
  px <- callr::r_bg(
    function(dir, p) {
      shiny::runApp(dir, port = p, host = "127.0.0.1", launch.browser = FALSE)
    },
    args = list(dir = app_dir, p = port),
    env = env,
    stdout = "|",
    stderr = "|"
  )
  app <- list(
    process = px,
    port = port,
    url = sprintf("http://127.0.0.1:%d", port)
  )
  deadline <- Sys.time() + timeout
  up <- FALSE
  while (Sys.time() < deadline) {
    up <- tryCatch(
      {
        con <- suppressWarnings(url(app$url, open = "rb", method = "libcurl"))
        readBin(con, "raw", n = 10)
        close(con)
        TRUE
      },
      error = function(e) FALSE
    )
    if (up || !px$is_alive()) {
      break
    }
    Sys.sleep(0.25)
  }
  if (!up) {
    stop(
      "App failed to start at ",
      app$url,
      "\n",
      paste(px$read_error(), collapse = "\n")
    )
  }
  app
}

stop_app <- function(app) {
  if (!app$process$is_alive()) {
    return(invisible(NULL))
  }
  app$process$signal(tools::SIGTERM)
  for (i in 1:10) {
    if (!app$process$is_alive()) {
      return(invisible(NULL))
    }
    Sys.sleep(0.2)
  }
  app$process$kill()
}

# ---- browser session -------------------------------------------------------

connect <- function(
  app,
  width = 1440,
  height = 1000,
  scale = 2,
  mobile = FALSE
) {
  b <- ChromoteSession$new()
  b$Emulation$setDeviceMetricsOverride(
    width = width,
    height = height,
    deviceScaleFactor = scale,
    mobile = mobile
  )
  # Keep captures consistent regardless of the OS color scheme
  b$Emulation$setEmulatedMedia(
    features = list(list(name = "prefers-color-scheme", value = "light"))
  )
  b$Page$navigate(app$url)
  for (i in 1:60) {
    if (
      isTRUE(tryCatch(
        js(b, "document.readyState === 'complete'"),
        error = function(e) FALSE
      ))
    ) {
      break
    }
    Sys.sleep(0.25)
  }
  b
}

js <- function(b, expr, by_value = TRUE) {
  res <- b$Runtime$evaluate(expr, returnByValue = by_value)
  err <- res$exceptionDetails
  if (!is.null(err)) {
    stop("JS error: ", paste(deparse(err), collapse = " "))
  }
  res$result$value
}

wait_for <- function(b, expr, timeout = 15000, interval = 0.2) {
  deadline <- Sys.time() + timeout
  while (Sys.time() < deadline) {
    if (isTRUE(tryCatch(js(b, expr), error = function(e) FALSE))) {
      return(invisible(TRUE))
    }
    Sys.sleep(interval)
  }
  stop("Timed out waiting for: ", expr)
}

wait_for_app_ready <- function(
  b,
  expr = "!!document.querySelector('.shiny-chat-messages')",
  timeout = 20000
) {
  wait_for(b, expr, timeout = timeout)
}

set_viewport <- function(b, width, height, scale = 2, mobile = FALSE) {
  b$Emulation$setDeviceMetricsOverride(
    width = width,
    height = height,
    deviceScaleFactor = scale,
    mobile = mobile
  )
  Sys.sleep(0.4)
}

# CSS zoom enlarges layout and fonts without affecting media queries, so the
# desktop layout survives at any viewport width >= 800px. vh units scale with
# zoom, so the page_chat root (sized in vh) is shrunk to keep the app exactly
# filling the window instead of overflowing and triggering page scroll.
set_zoom <- function(b, zoom = 1.2) {
  js(
    b,
    sprintf(
      "(() => {
      document.documentElement.style.zoom = %g;
      const page = document.querySelector('shiny-chat-page');
      if (page) page.style.height = (window.innerHeight / %g) + 'px';
      window.scrollTo(0, 0);
    })()",
      zoom,
      zoom
    )
  )
  Sys.sleep(0.4)
  invisible(TRUE)
}

# ---- screenshots -----------------------------------------------------------

capture_clip <- function(b, clip, beyond = TRUE) {
  img <- b$Page$captureScreenshot(
    format = "png",
    clip = clip,
    captureBeyondViewport = beyond
  )
  jsonlite::base64_dec(img$data)
}

save_png <- function(b, path, clip, beyond = TRUE) {
  writeBin(capture_clip(b, clip, beyond = beyond), path)
  invisible(path)
}

viewport_png <- function(b, path) {
  vs <- b$Page$getLayoutMetrics()$cssVisualViewport
  save_png(
    b,
    path,
    list(
      x = vs$pageX,
      y = vs$pageY,
      width = vs$clientWidth,
      height = vs$clientHeight,
      scale = 1
    )
  )
}
