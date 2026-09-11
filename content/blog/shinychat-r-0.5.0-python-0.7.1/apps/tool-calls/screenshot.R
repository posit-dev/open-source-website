source("../_common.R")

app <- start_app(app_path("tool-calls"))
b <- connect(app, width = 1000, height = 780)

wait_for_app_ready(b)
set_zoom(b, 1.25)
Sys.sleep(1)

chat_type(b, "How did each region perform this year?", press_enter = TRUE)
wait_for_text(b, "break any region down by product line", timeout = 20000)
wait_for_gone(b, ".shiny-chat-pending-indicator, .shiny-chat-streaming")
Sys.sleep(3)

# Scroll the chat back to the top so the user question is in frame and the
# scroll-to-bottom affordance is gone before capturing.
js(
  b,
  "(() => { const m = document.querySelector('.shiny-chat-messages'); if (m) m.scrollTop = 0; })()"
)
Sys.sleep(0.5)

union_png(
  b,
  shot_path("tool-calls-collapsed.png"),
  ".shiny-chat-messages",
  pad = 32,
  dy = 14
)

click_selector(b, ".shiny-chat-tool-group__row")
wait_for(
  b,
  "(() => { const ul = document.querySelector('.shiny-chat-tool-group__calls'); return !!ul && !ul.hidden && getComputedStyle(ul).display !== 'none'; })()",
  timeout = 5000
)
Sys.sleep(0.8)
union_png(
  b,
  shot_path("tool-calls-expanded.png"),
  ".shiny-chat-messages",
  pad = 32,
  dy = 14
)

click_selector(b, ".shiny-chat-tool-call-row__summary")
wait_for(
  b,
  "(() => { const d = document.querySelector('.shiny-chat-tool-call-row__detail'); return !!d && !d.hidden && d.getBoundingClientRect().height > 20; })()",
  timeout = 5000
)
Sys.sleep(0.8)
union_png(
  b,
  shot_path("tool-calls-result.png"),
  ".shiny-chat-messages",
  pad = 32,
  dy = 14
)

stop_app(app)
b$close()
