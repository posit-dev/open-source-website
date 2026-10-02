source("../_common.R")

app <- start_app(app_path("thinking"))
b <- connect(app, width = 1000, height = 760)

wait_for_app_ready(b)
set_zoom(b, 1.25)
Sys.sleep(1)

chat_type(b, "Which penguin species is the heaviest?", press_enter = TRUE)

# While the model is thinking, the send button becomes a stop button.
# Wide clip: the stop button with some of the input box for context.
wait_for(
  b,
  "!!document.querySelector('.shiny-chat-btn-send[data-state=\"cancel\"]')",
  timeout = 10000
)
Sys.sleep(1)
clip <- js(
  b,
  "(() => {
  const i = document.querySelector('.shiny-chat-input').getBoundingClientRect();
  const c = document.querySelector('.shiny-chat-btn-send[data-state=\"cancel\"]').getBoundingClientRect();
  return {
    x: i.x + window.scrollX, y: Math.min(i.y, c.y) + window.scrollY,
    right: Math.max(i.right, c.right) + window.scrollX,
    bottom: Math.max(i.bottom, c.bottom) + window.scrollY
  };
})()"
)
save_png(
  b,
  shot_path("streaming-stop.png"),
  list(
    x = clip$x + (clip$right - clip$x) * 0.38,
    y = clip$y - 12,
    width = clip$right - clip$x - (clip$right - clip$x) * 0.38 + 12,
    height = clip$bottom - clip$y + 24,
    scale = 1
  )
)

# The thinking panel collapses on its own once the answer starts; wait for
# the completed "Thought for Ns" label before capturing
wait_for_gone(
  b,
  ".shiny-chat-btn-send[data-state=\"cancel\"]",
  timeout = 30000
)
wait_for_text(b, "Thought for ", timeout = 15000)
wait_for_gone(b, ".shiny-chat-pending-indicator, .shiny-chat-streaming")
Sys.sleep(1)
union_png(
  b,
  shot_path("thinking-collapsed.png"),
  c(".shiny-chat-user-message", ".shiny-chat-thinking", ".shiny-chat-message"),
  pad = 32,
  dy = 14
)

stop_app(app)
b$close()
