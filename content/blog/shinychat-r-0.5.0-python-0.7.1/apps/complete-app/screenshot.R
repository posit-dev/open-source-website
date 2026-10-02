source("../_common.R")

app <- start_app(app_path("complete-app"))
b <- connect(app, width = 1200, height = 900)

wait_for_app_ready(b)
set_zoom(b, 1.1)
Sys.sleep(1)

stream_done <- function(rec, timeout = 30000) {
  rec$loop_until(
    "!document.querySelector('.shiny-chat-streaming, .shiny-chat-pending-indicator')",
    timeout = timeout
  )
}

# Blank slate: greeting and suggestions only; the sidebar and drawer start
# closed. The cursor enters from the right, picks the first suggestion, and
# the response streams in with its tool activity rows.
rec <- movie_start(b, fps = 12)
cur <- cursor_start(b)
rec$loop(1)

cursor_glideto_el(
  cur,
  ".shiny-chat-greeting .suggestion.submit .shiny-chat-suggestion-list-item-body",
  1.2,
  rec
)
cursor_click_here(cur, rec)
rec$loop_until(
  "document.body.textContent.includes('peaked in May')",
  timeout = 30000
)
stream_done(rec)
rec$loop(1.2)

# Mouse retreats while the reader looks over the answer, then opens the
# history sidebar
cursor_leave(cur, rec, 0.5)
rec$loop(0.6)
cursor_glideto_el(cur, ".shiny-chat-page-sidebar-toggle", 0.9, rec)
cursor_click_here(cur, rec)
wait_for(
  b,
  "!!document.querySelector('.shiny-chat-history-new') && !document.querySelector('.shiny-chat-history-new').disabled"
)
rec$loop(1)

# Start a new conversation; the greeting returns with its suggestions
cursor_glideto_el(cur, ".shiny-chat-history-new", 0.7, rec)
cursor_click_here(cur, rec)
rec$loop_until(
  "!!document.querySelector('.shiny-chat-greeting')",
  timeout = 15000
)
rec$loop(1)

# Ask a second question: click into the input, type it out, submit with Enter.
# This response opens the artifact drawer with the plot.
cursor_glideto_el(cur, "#chat_user_input .ProseMirror", 0.8, rec)
cursor_click_here(cur, rec)
rec$loop(0.8)
type_natural(b, rec, "How do the colonies compare?")
rec$loop(0.5)
press_enter(b)
rec$loop_until(
  "document.body.textContent.includes('Cape Royds')",
  timeout = 30000
)
stream_done(rec)
rec$loop_until(
  "(() => { const d = document.querySelector('.shiny-chat-drawer'); return !!d && !d.hidden; })()",
  timeout = 15000
)
rec$loop(1.5)

# Hide the drawer before changing conversations
cursor_glideto_el(cur, ".shiny-chat-drawer-close", 0.7, rec)
cursor_click_here(cur, rec)
rec$loop(0.8)

# Return to the first conversation from the history sidebar
r <- rect_of_text(
  b,
  ".shiny-chat-history-item-select",
  "What do the observations say"
)
cursor_glideto(cur, r$x + r$w / 2, r$y + r$h / 2, 0.9, rec)
cursor_click_here(cur, rec)
wait_for_text(b, "peaked in May", timeout = 15000)
rec$loop(1.5)

# Start another conversation — the greeting returns — then hide the sidebar,
# back to the blank slate the video opened with
cursor_glideto_el(cur, ".shiny-chat-history-new", 0.7, rec)
cursor_click_here(cur, rec)
rec$loop_until(
  "!!document.querySelector('.shiny-chat-greeting')",
  timeout = 15000
)
rec$loop(1)
cursor_glideto_el(cur, ".shiny-chat-page-sidebar-toggle", 0.8, rec)
cursor_click_here(cur, rec)
rec$loop(1)

movie_save(rec, shot_path("complete-app.mp4"), width = 2400)

# Stills: rebuild the hero state — second conversation in view, sidebar open,
# drawer showing the plot. Asking the colonies question again reopens the
# drawer since drawer state isn't restored from history.
click_selector(b, ".shiny-chat-page-sidebar-toggle")
Sys.sleep(0.8)
chat_type(b, "How do the colonies compare?", press_enter = TRUE)
wait_for_text(b, "Cape Royds", timeout = 30000)
wait_for_gone(b, ".shiny-chat-streaming, .shiny-chat-pending-indicator")
Sys.sleep(1)

set_viewport(b, width = 1440, height = 920)
set_zoom(b, 1.1)
Sys.sleep(1)
js(b, "if (document.activeElement) document.activeElement.blur()")
Sys.sleep(0.3)
viewport_png(b, shot_path("complete-app.png"))

# Navigation pages and the artifact drawer: visit the Sources page and
# return home, with the drawer still showing the plot from the last response
click_selector(b, ".shiny-chat-page-nav-link:not(.shiny-chat-page-home-link)")
Sys.sleep(1)
click_selector(b, ".shiny-chat-page-home-link")
Sys.sleep(2.5)
viewport_png(b, shot_path("complete-app-nav-drawer.png"))

stop_app(app)
b$close()
