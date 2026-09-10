# Screenshot and screen-recording harness for the shinychat post demos.
# Sourced by each apps/<name>/screenshot.R script.

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
# demo scripts live in apps/<name>/; when sourcing from the apps/ dir
# directly (e.g. an ad-hoc probe), treat that dir as apps_dir.
if (file.exists(file.path(demo_dir, "app.R"))) {
  apps_dir <- dirname(demo_dir)
} else {
  apps_dir <- demo_dir
}
post_dir <- dirname(apps_dir)
images_dir <- file.path(post_dir, "images")
dir.create(images_dir, showWarnings = FALSE, recursive = TRUE)

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

click_selector <- function(b, selector) {
  sel <- jsonlite::toJSON(selector, auto_unbox = TRUE)
  clicked <- js(
    b,
    sprintf(
      "(() => {
      const el = document.querySelector(%s);
      if (!el) return false;
      el.scrollIntoView({ block: 'center' });
      el.click();
      return true;
    })()",
      sel
    )
  )
  if (!isTRUE(clicked)) {
    stop("Element not found: ", selector)
  }
  invisible(TRUE)
}

union_png <- function(
  b,
  path,
  selectors,
  pad = 24,
  dx = 0,
  dy = 0,
  beyond = TRUE
) {
  sel <- jsonlite::toJSON(selectors, auto_unbox = FALSE)
  r <- js(
    b,
    sprintf(
      "(() => {
      let u = null;
      for (const s of %s) {
        for (const el of document.querySelectorAll(s)) {
          const r = el.getBoundingClientRect();
          const box = { x: r.x + window.scrollX, y: r.y + window.scrollY, w: r.width, h: r.height };
          if (!u) { u = {...box}; continue; }
          u.x = Math.min(u.x, box.x);
          u.y = Math.min(u.y, box.y);
          u.w = Math.max(u.x + u.w, box.x + box.w) - u.x;
          u.h = Math.max(u.y + u.h, box.y + box.h) - u.y;
        }
      }
      return u;
    })()",
      sel
    )
  )
  if (is.null(r)) {
    stop("No elements found for: ", paste(selectors, collapse = ", "))
  }
  save_png(
    b,
    path,
    list(
      x = max(0, r$x - pad + dx),
      y = max(0, r$y - pad + dy),
      width = r$w + 2 * pad,
      height = r$h + 2 * pad,
      scale = 1
    ),
    beyond = beyond
  )
}

html <- function(b, expr) {
  js(
    b,
    sprintf(
      "(() => { const el = %s; return el ? el.outerHTML : null; })()",
      expr
    )
  )
}

document_html <- function(b) js(b, "document.documentElement.outerHTML")

# ---- chat input helpers ----------------------------------------------------

chat_focus <- function(b) {
  js(b, "document.querySelector('#chat_user_input .ProseMirror').focus()")
}

chat_type <- function(b, text, press_enter = FALSE) {
  chat_focus(b)
  b$Input$insertText(text = text)
  Sys.sleep(0.3)
  if (press_enter) {
    b$Input$dispatchKeyEvent(
      type = "keyDown",
      key = "Enter",
      code = "Enter",
      windowsVirtualKeyCode = 13,
      nativeVirtualKeyCode = 13,
      text = "\r"
    )
    b$Input$dispatchKeyEvent(
      type = "keyUp",
      key = "Enter",
      code = "Enter",
      windowsVirtualKeyCode = 13,
      nativeVirtualKeyCode = 13
    )
  }
  invisible(TRUE)
}

chat_send_click <- function(b) {
  click_selector(b, ".shiny-chat-btn-send:not([disabled])")
}

wait_for_text <- function(b, text, timeout = 20000) {
  wait_for(
    b,
    sprintf(
      "document.body.textContent.includes(%s)",
      jsonlite::toJSON(text, auto_unbox = TRUE)
    ),
    timeout = timeout
  )
}

wait_for_gone <- function(b, selector, timeout = 10000) {
  wait_for(
    b,
    sprintf(
      "!document.querySelector(%s)",
      jsonlite::toJSON(selector, auto_unbox = TRUE)
    ),
    timeout = timeout
  )
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

full_page_png <- function(b, path) {
  cs <- b$Page$getLayoutMetrics()$cssContentSize
  save_png(
    b,
    path,
    list(
      x = 0,
      y = 0,
      width = cs$width,
      height = cs$height,
      scale = 1
    )
  )
}

element_png <- function(b, path, selector, pad = 10) {
  sel <- jsonlite::toJSON(selector, auto_unbox = TRUE)
  r <- js(
    b,
    sprintf(
      "(() => {
      const el = document.querySelector(%s);
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return { x: r.x + window.scrollX, y: r.y + window.scrollY, w: r.width, h: r.height };
    })()",
      sel
    )
  )
  if (is.null(r)) {
    stop("Element not found: ", selector)
  }
  save_png(
    b,
    path,
    list(
      x = max(0, r$x - pad),
      y = max(0, r$y - pad),
      width = r$w + 2 * pad,
      height = r$h + 2 * pad,
      scale = 1
    )
  )
}

# ---- movies ----------------------------------------------------------------
#
# Capture a timed sequence of JPEG frames while the script performs actions,
# then assemble them into an MP4 with ffmpeg at real-time pacing.

movie_start <- function(b, fps = 12) {
  rec <- new.env(parent = emptyenv())
  rec$b <- b
  rec$fps <- fps
  rec$frames <- list()
  rec$t0 <- Sys.time()
  rec$snap <- function() {
    img <- rec$b$Page$captureScreenshot(format = "jpeg", quality = 90)
    rec$frames[[length(rec$frames) + 1]] <<- list(
      data = img$data,
      t = as.numeric(difftime(Sys.time(), rec$t0, units = "secs"))
    )
    invisible(length(rec$frames))
  }
  rec$loop <- function(seconds, fps = rec$fps) {
    dt <- 1 / fps
    n <- max(1L, ceiling(seconds / dt))
    for (i in seq_len(n)) {
      start <- Sys.time()
      rec$snap()
      elapsed <- as.numeric(difftime(Sys.time(), start, units = "secs"))
      Sys.sleep(max(0, dt - elapsed))
    }
    invisible(NULL)
  }
  rec
}

movie_save <- function(rec, path, fps = 15, width = NULL) {
  if (length(rec$frames) < 2) {
    stop("Not enough frames recorded.")
  }
  tmp <- file.path(tempdir(), sprintf("shinychat-movie-%d", Sys.getpid()))
  dir.create(tmp, recursive = TRUE, showWarnings = FALSE)
  on.exit(unlink(tmp, recursive = TRUE), add = TRUE)

  times <- vapply(rec$frames, `[[`, numeric(1), "t")
  durations <- diff(c(0, times))
  lines <- character()
  for (i in seq_along(rec$frames)) {
    f <- file.path(tmp, sprintf("f%04d.jpg", i))
    writeBin(jsonlite::base64_dec(rec$frames[[i]]$data), f)
    lines <- c(
      lines,
      sprintf("file '%s'\nduration %.3f", f, max(durations[i], 0.02))
    )
  }
  lines <- c(
    lines,
    sprintf(
      "file '%s'",
      file.path(tmp, sprintf("f%04d.jpg", length(rec$frames)))
    )
  )
  concat <- file.path(tmp, "list.txt")
  writeLines(lines, concat)

  vf <- sprintf("fps=%d,format=yuv420p", fps)
  if (!is.null(width)) {
    vf <- sprintf("fps=%d,scale=%d:-2,format=yuv420p", fps, width)
  }
  cmd <- sprintf(
    "ffmpeg -y -hide_banner -loglevel error -f concat -safe 0 -i %s -vf %s -movflags +faststart %s",
    shQuote(concat),
    shQuote(vf),
    shQuote(path)
  )
  status <- system(cmd)
  if (status != 0) {
    stop("ffmpeg failed while writing ", path)
  }
  invisible(path)
}
