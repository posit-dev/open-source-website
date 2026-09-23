source("../_common.R")

app <- start_app(app_path("slash-commands"))
b <- connect(app, width = 1000, height = 760)

wait_for_app_ready(b)
set_zoom(b, 1.25)
Sys.sleep(1)

chat_type(b, "/")
wait_for(b, "!!document.querySelector('.shiny-chat-slash-palette')")
Sys.sleep(0.8)
union_png(
  b,
  shot_path("slash-commands-palette.png"),
  c(".shiny-chat-slash-palette", "#chat_user_input"),
  pad = 24
)

stop_app(app)
b$close()
