source("../_common.R")

app <- start_app(app_path("greeting-stream"))
b <- connect(app, width = 1200, height = 900)
zoom <- 1.25

composer_settled <- paste0(
  "(() => { const c = document.querySelector('.shiny-chat-composer'); ",
  "return !!c && getComputedStyle(c).opacity === '1'; })()"
)

# Pass 1: let the greeting stream to completion so its final layout sizes the
# movie clip. The greeting and composer are vertically centered, so measuring
# the empty chat would put the clip in the wrong place.
wait_for_app_ready(b)
set_zoom(b, zoom)
wait_for_text(b, "Plot bill length by species")
wait_for(b, composer_settled)
Sys.sleep(0.5)

clip <- movie_clip_fit(
  b,
  c(".shiny-chat-greeting", "#chat_user_input"),
  pad = 32,
  container = ".shiny-chat-messages"
)

# Pass 2: fresh session, same clip. The greeting streams again on load --
# lead-in on the empty chat, the welcome message arrives word by word, then
# the suggestion cards appear.
b$Page$navigate(app$url)
wait_for_app_ready(b)
set_zoom(b, zoom)
wait_for(b, composer_settled)
Sys.sleep(0.3)

rec <- movie_start(b, fps = 12)
rec$clip <- clip

rec$loop(0.6)
rec$loop_until(
  "document.body.textContent.includes('Plot bill length by species')",
  timeout = 20000
)
rec$loop(1.5)

movie_save(rec, shot_path("greeting-stream.mp4"), width = clip$width * 2)

stop_app(app)
b$close()
