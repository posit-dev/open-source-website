source("../_common.R", local = TRUE)

capture_screenshots <- function() {
  app <- start_app(app_path("shinychat-traffic"))
  on.exit(stop_app(app), add = TRUE)
  b <- connect(app, width = 1200, height = 860)
  on.exit(b$close(), add = TRUE)

  wait_for_app_ready(b)
  set_zoom(b, 1.3)
  Sys.sleep(1)

  wait_for_response <- function(text, timeout = 30000) {
    wait_for_text(b, text, timeout = timeout)
    wait_for_gone(
      b,
      ".shiny-chat-streaming, .shiny-chat-pending-indicator",
      timeout = timeout
    )
    Sys.sleep(0.8)
  }

  open_history <- function() {
    click_selector(b, ".shiny-chat-page-sidebar-toggle")
    wait_for(
      b,
      paste0(
        "!!document.querySelector('.shiny-chat-history-new') && ",
        "!document.querySelector('.shiny-chat-history-new').disabled"
      )
    )
    Sys.sleep(0.6)
  }

  new_conversation <- function() {
    click_selector(b, ".shiny-chat-history-new")
    wait_for(b, "!!document.querySelector('.shiny-chat-greeting')")
    Sys.sleep(0.5)
  }

  chat_type(
    b,
    "How is traffic trending for our site?",
    press_enter = TRUE
  )
  wait_for_response("increased 22%")
  viewport_png(b, shot_path("shinychat-page-chat.png"))

  open_history()
  new_conversation()
  chat_type(
    b,
    "Which table should I use for site traffic?",
    press_enter = TRUE
  )
  wait_for_response("reviewed daily sessions metric used for reporting")
  click_selector(b, ".shiny-chat-page-sidebar-toggle")
  Sys.sleep(0.6)

  click_selector(b, ".shiny-aside-pill")
  Sys.sleep(0.8)
  js(
    b,
    "(() => {
  const pill = document.querySelector('.shiny-aside-pill');
  const pop = document.querySelector('.shiny-aside-popover');
  if (!pill || !pop) return false;
  const p = pill.getBoundingClientRect();
  const z = parseFloat(document.documentElement.style.zoom) || 1;
  pop.style.transform = 'none';
  pop.style.left = (p.left / z) + 'px';
  pop.style.top = ((p.bottom + 8) / z) + 'px';
  return true;
})()"
  )
  Sys.sleep(0.5)
  union_png(
    b,
    shot_path("shinychat-tools-citations.png"),
    c(".shiny-chat-message", ".shiny-aside-popover"),
    pad = 32,
    dy = 14
  )

  click_selector(b, ".shiny-aside-pill")
  Sys.sleep(0.4)
  open_history()
  new_conversation()
  chat_type(
    b,
    "Which day had the most site visits?",
    press_enter = TRUE
  )
  wait_for_response("August 29")

  first_conversation <- rect_of_text(
    b,
    ".shiny-chat-history-item-select",
    "How is traffic trending"
  )
  cdp_mouse_click(
    b,
    first_conversation$x + first_conversation$w / 2,
    first_conversation$y + first_conversation$h / 2
  )
  wait_for_text(b, "increased 22%", timeout = 15000)
  Sys.sleep(0.8)
  viewport_png(b, shot_path("shinychat-history.png"))
}

capture_screenshots()
