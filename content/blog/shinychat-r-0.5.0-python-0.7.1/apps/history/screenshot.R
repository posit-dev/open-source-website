source("../_common.R")

app <- start_app(app_path("history"))
b <- connect(app, width = 1440, height = 800)

wait_for_app_ready(b)
set_zoom(b, 1.15)
Sys.sleep(1)

open_history <- function() {
  click_selector(b, ".shiny-chat-page-sidebar-toggle")
  Sys.sleep(0.6)
}

new_conversation <- function() {
  click_selector(b, ".shiny-chat-history-new")
  Sys.sleep(0.6)
}

ask <- function(text, wait_for) {
  chat_type(b, text, press_enter = TRUE)
  wait_for_text(b, wait_for, timeout = 20000)
  Sys.sleep(0.5)
}

drawer_png <- function(path, pad = 16) {
  union_png(
    b,
    path,
    c(
      ".shiny-chat-history-toprow",
      ".shiny-chat-history-item",
      ".shiny-chat-history-menu"
    ),
    pad = pad,
    # captureBeyondViewport's re-render pass distorts the sidebar while the
    # search field is focused; these clips are inside the viewport anyway
    beyond = FALSE
  )
}

open_history()

# Conversation 1
ask("What is the tallest mountain in Africa?", "Tanzania")

# Conversation 2
new_conversation()
ask("How do I pivot a data frame to longer format in R?", "value columns")

# Conversation 3
new_conversation()
ask("Explain vector recycling in R", "explicit control")

# The history drawer with several saved conversations
Sys.sleep(0.5)
viewport_png(b, shot_path("history-list.png"))

# Searching conversations: the field ignores synthetic input events,
# so type through CDP key events instead
js(b, "document.querySelector('.shiny-chat-history-search').focus()")
Sys.sleep(0.3)
b$Input$insertText(text = "pivot")
# Wait until the list is actually filtered down to the pivot conversation
wait_for(
  b,
  "(() => {
  const drawer = document.querySelector('.shiny-chat-history');
  if (!drawer) return false;
  const els = [...drawer.querySelectorAll('*')].filter(
    el => el.offsetParent && el.children.length === 0 &&
      el.textContent.includes('tallest')
  );
  return els.length === 0;
})()",
  timeout = 15000
)
Sys.sleep(0.5)
drawer_png(shot_path("history-search.png"))

# Clear the search and open a conversation's actions menu
for (i in 1:8) {
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
}
Sys.sleep(0.8)
click_selector(b, 'button[aria-label="Conversation actions"]')
Sys.sleep(0.8)
drawer_png(shot_path("history-actions-menu.png"))

stop_app(app)
b$close()
