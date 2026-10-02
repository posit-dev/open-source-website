source("../_common.R")

app <- start_app(app_path("og-header"))
b <- connect(app, width = 1200, height = 630)

wait_for_app_ready(b)
set_zoom(b, 1.4)
# Let the composer finish its entrance fade so the input isn't caught
# mid-animation in the screenshot
wait_for(
  b,
  "(() => { const c = document.querySelector('.shiny-chat-composer');
  return !!c && getComputedStyle(c).opacity === '1'; })()"
)
Sys.sleep(0.5)

viewport_png(b, shot_path("og-header.png"))

stop_app(app)
b$close()
