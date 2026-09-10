source("../_common.R")

app <- start_app(app_path("complete-app"))
b <- connect(app, width = 1200, height = 900)

wait_for_app_ready(b)
set_zoom(b, 1.1)
Sys.sleep(1)

# The history sidebar (app menu) is open by default on desktop.

# Submit the survey question from the greeting and record the response.
# Record a beat before the click so the video doesn't open mid-action.
rec <- movie_start(b, fps = 12)
rec$loop(1)
click_selector(
  b,
  ".shiny-chat-greeting .suggestion.submit .shiny-chat-suggestion-list-item-body"
)
rec$loop(8)
movie_save(rec, shot_path("complete-app.mp4"), width = 2400)

wait_for_text(b, "peaked in May", timeout = 20000)
Sys.sleep(1)

# Roomier hero shot: widen the viewport for the final frame
set_viewport(b, width = 1440, height = 920)
Sys.sleep(1)
viewport_png(b, shot_path("complete-app.png"))

# Navigation pages and the artifact drawer: visit the Sources page and
# return home, with the drawer still showing the plot from the last response
click_selector(b, ".shiny-chat-page-nav-link:not(.shiny-chat-page-home-link)")
Sys.sleep(1)
click_selector(b, ".shiny-chat-page-home-link")
Sys.sleep(1.5)
viewport_png(b, shot_path("complete-app-nav-drawer.png"))

stop_app(app)
b$close()
