source("../_common.R")

app <- start_app(app_path("toolbars"))
b <- connect(app, width = 1440, height = 760)

wait_for_app_ready(b)
set_zoom(b, 1.15)
Sys.sleep(3)

# Home page with an active conversation: page-scoped toolbar, global
# toolbar, and the input toolbar
chat_type(b, "What did the study find?", press_enter = TRUE)
wait_for_text(b, "monthly surveys", timeout = 20000)
Sys.sleep(1.5)
viewport_png(b, shot_path("toolbars-home.png"))

stop_app(app)
b$close()
