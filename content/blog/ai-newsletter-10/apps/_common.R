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

chat_focus <- function(b, selector = "#chat_user_input .ProseMirror") {
  js(
    b,
    sprintf(
      "document.querySelector(%s).focus()",
      jsonlite::toJSON(selector, auto_unbox = TRUE)
    )
  )
}

press_enter <- function(b) {
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
  invisible(TRUE)
}

chat_type <- function(b, text, press_enter = FALSE) {
  chat_focus(b)
  b$Input$insertText(text = text)
  Sys.sleep(0.3)
  if (press_enter) {
    press_enter(b)
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
  rec$clip <- NULL
  rec$snap <- function() {
    args <- list(format = "jpeg", quality = 90)
    if (!is.null(rec$clip)) {
      args$clip <- rec$clip
    }
    img <- do.call(rec$b$Page$captureScreenshot, args)
    rec$frames[[length(rec$frames) + 1]] <<- list(
      data = img$data,
      t = as.numeric(difftime(Sys.time(), rec$t0, units = "secs"))
    )
    invisible(length(rec$frames))
  }
  rec$beat <- function(fps = rec$fps) {
    start <- Sys.time()
    rec$snap()
    elapsed <- as.numeric(difftime(Sys.time(), start, units = "secs"))
    Sys.sleep(max(0, 1 / fps - elapsed))
  }
  rec$loop <- function(seconds, fps = rec$fps) {
    dt <- 1 / fps
    n <- max(1L, ceiling(seconds / dt))
    for (i in seq_len(n)) {
      rec$beat(fps)
    }
    invisible(NULL)
  }
  rec$loop_until <- function(expr, timeout = 20000, fps = rec$fps) {
    deadline <- Sys.time() + timeout / 1000
    while (Sys.time() < deadline) {
      if (isTRUE(tryCatch(js(rec$b, expr), error = function(e) FALSE))) {
        return(invisible(TRUE))
      }
      rec$beat(fps)
    }
    stop("Timed out waiting for: ", expr)
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

# A 4:3 screenshot clip (CSS px) covering the union of `selectors`, for movies
# that should show only part of the app. Anchored at the top of the content so
# headroom for growth (streaming responses, edit boxes) stays inside the clip.
movie_clip_fit <- function(
  b,
  selectors,
  ratio = 4 / 3,
  pad = 24,
  anchor = "top",
  container = NULL
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
          if (!u) { u = { x: r.x, y: r.y, w: r.width, h: r.height }; continue; }
          u.x = Math.min(u.x, r.x);
          u.y = Math.min(u.y, r.y);
          u.w = Math.max(u.x + u.w, r.x + r.width) - u.x;
          u.h = Math.max(u.y + u.h, r.y + r.height) - u.y;
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
  vw <- js(b, "window.innerWidth")
  vh <- js(b, "window.innerHeight")
  w <- min(vw, r$w + 2 * pad)
  w <- round(w / 4) * 4
  h <- w / ratio
  if (h > vh) {
    h <- vh
    w <- round(h * ratio / 4) * 4
  }
  x <- r$x + r$w / 2 - w / 2
  x <- max(0, min(vw - w, x))
  y <- if (identical(anchor, "top")) r$y - pad else r$y + r$h / 2 - h / 2
  y <- max(0, min(vh - h, y))
  if (!is.null(container)) {
    # Never reach above the container: keeps header borders and shadows,
    # which sit just above its top edge, out of the recording.
    top <- js(
      b,
      sprintf(
        "(() => {
        const el = document.querySelector(%s);
        return el ? el.getBoundingClientRect().y : null;
      })()",
        jsonlite::toJSON(container, auto_unbox = TRUE)
      )
    )
    if (!is.null(top)) {
      y <- max(y, top + 2)
    }
  }
  list(
    x = round(x),
    y = round(y),
    width = round(w),
    height = round(h),
    scale = 1
  )
}

# ---- fake cursor ------------------------------------------------------------
# CDP clicks are invisible in captured frames, so demos that need a visible
# pointer render their own cursor element and move it in step with the movie
# frames. Movement uses real CDP mouse events, which also trigger :hover (the
# message edit buttons only reveal on hover) and produce native clicks.

cdp_mouse_move <- function(b, x, y) {
  b$Input$dispatchMouseEvent(
    type = "mouseMoved",
    x = round(x),
    y = round(y)
  )
}

cdp_mouse_click <- function(b, x, y) {
  b$Input$dispatchMouseEvent(
    type = "mousePressed",
    x = round(x),
    y = round(y),
    button = "left",
    buttons = 1,
    clickCount = 1
  )
  b$Input$dispatchMouseEvent(
    type = "mouseReleased",
    x = round(x),
    y = round(y),
    button = "left",
    buttons = 0,
    clickCount = 1
  )
}

ease_in_out <- function(t) {
  if (t < 0.5) 4 * t^3 else 1 - (-2 * t + 2)^3 / 2
}

cursor_start <- function(b) {
  vw <- js(b, "window.innerWidth")
  vh <- js(b, "window.innerHeight")
  svg <- paste0(
    "<svg width='18' height='26' viewBox='0 0 18 26' ",
    "xmlns='http://www.w3.org/2000/svg'>",
    "<path d='M1.5 1 L1.5 19.8 L6.3 15.5 L9.4 22.6 L13.2 20.9 ",
    "L10.1 13.9 L16.5 13.9 Z' fill='#1a1a1a' stroke='#ffffff' ",
    "stroke-width='1.5' stroke-linejoin='round'/></svg>"
  )
  js(
    b,
    sprintf(
      "(() => {
      let el = document.getElementById('demo-cursor');
      if (!el) {
        el = document.createElement('div');
        el.id = 'demo-cursor';
        el.style.cssText = [
          'position:fixed', 'left:0', 'top:0', 'z-index:2147483647',
          'pointer-events:none', 'will-change:transform',
          'filter:drop-shadow(0 1px 2px rgba(0,0,0,.35))'
        ].join(';');
        el.innerHTML = %s;
        document.body.appendChild(el);
      }
      return true;
    })()",
      jsonlite::toJSON(svg)
    )
  )
  cur <- new.env(parent = emptyenv())
  cur$b <- b
  # Root CSS zoom scales the rendered position of fixed elements, so cursor
  # placement divides client-space coordinates by it.
  cur$zoom <- js(b, "parseFloat(document.documentElement.style.zoom) || 1")
  cur$x <- vw + 60
  cur$y <- vh * 0.45
  cursor_place(cur)
  cur
}

cursor_place <- function(cur, scale = 1) {
  js(
    cur$b,
    sprintf(
      "document.getElementById('demo-cursor').style.transform = 'translate(%fpx, %fpx) scale(%f)'",
      cur$x / cur$zoom,
      cur$y / cur$zoom,
      scale
    )
  )
  invisible(cur)
}

rect_of <- function(b, selector, which = "last") {
  sel <- jsonlite::toJSON(selector, auto_unbox = TRUE)
  idx <- if (identical(which, "last")) {
    "els.length - 1"
  } else {
    as.integer(which) - 1
  }
  r <- js(
    b,
    sprintf(
      "(() => {
      const els = document.querySelectorAll(%s);
      if (!els.length) return null;
      const r = els[%s].getBoundingClientRect();
      return { x: r.x, y: r.y, w: r.width, h: r.height };
    })()",
      sel,
      idx
    )
  )
  if (is.null(r)) {
    stop("Element not found: ", selector)
  }
  r
}

rect_of_text <- function(b, selector, text) {
  r <- js(
    b,
    sprintf(
      "(() => {
      const needle = %s;
      for (const el of document.querySelectorAll(%s)) {
        if (!el.textContent.includes(needle)) continue;
        const r = el.getBoundingClientRect();
        if (!r.width) continue;
        return { x: r.x, y: r.y, w: r.width, h: r.height };
      }
      return null;
    })()",
      jsonlite::toJSON(text, auto_unbox = TRUE),
      jsonlite::toJSON(selector, auto_unbox = TRUE)
    )
  )
  if (is.null(r)) {
    stop("No element matching text: ", text)
  }
  r
}

cursor_glideto <- function(cur, x, y, seconds, rec) {
  n <- max(1L, round(seconds * rec$fps))
  x0 <- cur$x
  y0 <- cur$y
  for (i in seq_len(n)) {
    e <- ease_in_out(i / n)
    cur$x <- x0 + (x - x0) * e
    cur$y <- y0 + (y - y0) * e
    cursor_place(cur)
    cdp_mouse_move(cur$b, cur$x, cur$y)
    rec$beat()
  }
  invisible(cur)
}

cursor_glideto_el <- function(
  cur,
  selector,
  seconds,
  rec,
  which = "last",
  dx = 0,
  dy = 0
) {
  r <- rect_of(cur$b, selector, which = which)
  cursor_glideto(cur, r$x + r$w / 2 + dx, r$y + r$h / 2 + dy, seconds, rec)
}

cursor_leave <- function(cur, rec, seconds = 0.5) {
  vw <- js(cur$b, "window.innerWidth")
  cursor_glideto(cur, vw + 60, cur$y, seconds, rec)
}

cursor_click_here <- function(cur, rec) {
  cursor_place(cur, scale = 0.8)
  rec$beat()
  Sys.sleep(0.12)
  cdp_mouse_click(cur$b, cur$x, cur$y)
  cursor_place(cur)
  rec$beat()
  invisible(cur)
}

# Type text one character at a time with human-ish pacing, capturing frames.
type_natural <- function(
  b,
  rec,
  text,
  selector = "#chat_user_input .ProseMirror",
  min_delay = 0.04,
  max_delay = 0.12
) {
  chat_focus(b, selector)
  for (ch in strsplit(text, "")[[1]]) {
    b$Input$insertText(text = ch)
    rec$beat()
    Sys.sleep(runif(1, min_delay, max_delay))
  }
  invisible(TRUE)
}

# Select an exact substring inside a contenteditable editor.
select_edit_text <- function(
  b,
  text,
  selector = ".shiny-chat-edit-box .ProseMirror"
) {
  js(
    b,
    sprintf(
      "(() => {
      const pm = document.querySelector(%s);
      pm.focus();
      const walker = document.createTreeWalker(pm, NodeFilter.SHOW_TEXT);
      const nodes = [];
      let node, full = '';
      while ((node = walker.nextNode())) { nodes.push(node); full += node.textContent; }
      const i = full.indexOf(%s);
      if (i < 0) return false;
      const range = document.createRange();
      let pos = 0, startSet = false;
      for (const n of nodes) {
        const len = n.textContent.length;
        if (!startSet && i < pos + len) { range.setStart(n, i - pos); startSet = true; }
        if (i + %d <= pos + len) { range.setEnd(n, i + %d - pos); break; }
        pos += len;
      }
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      return true;
    })()",
      jsonlite::toJSON(selector, auto_unbox = TRUE),
      jsonlite::toJSON(text, auto_unbox = TRUE),
      nchar(text),
      nchar(text)
    )
  )
}

press_backspace <- function(b) {
  b$Input$dispatchKeyEvent(
    type = "keyDown",
    key = "Backspace",
    code = "Backspace",
    windowsVirtualKeyCode = 8,
    nativeVirtualKeyCode = 8
  )
  b$Input$dispatchKeyEvent(
    type = "keyUp",
    key = "Backspace",
    code = "Backspace",
    windowsVirtualKeyCode = 8,
    nativeVirtualKeyCode = 8
  )
  invisible(TRUE)
}
