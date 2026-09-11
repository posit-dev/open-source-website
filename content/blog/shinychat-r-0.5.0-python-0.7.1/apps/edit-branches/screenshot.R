source("../_common.R")

app <- start_app(app_path("edit-branches"))
b <- connect(app, width = 1000, height = 760)

wait_for_app_ready(b)
set_zoom(b, 1.25)
Sys.sleep(1)

ask <- function(text, wait_for) {
  chat_type(b, text, press_enter = TRUE)
  wait_for_text(b, wait_for, timeout = 20000)
  Sys.sleep(0.5)
}

ask("What is the tallest mountain in Africa?", "Kilimanjaro")
ask("And what is the tallest in South America?", "Aconcagua")

click_last <- function(b, selector) {
  sel <- jsonlite::toJSON(selector, auto_unbox = TRUE)
  clicked <- js(
    b,
    sprintf(
      "(() => {
      const els = document.querySelectorAll(%s);
      if (!els.length) return false;
      const el = els[els.length - 1];
      el.scrollIntoView({ block: 'center' });
      el.click();
      return true;
    })()",
      sel
    )
  )
  if (!isTRUE(clicked)) {
    stop("Element not found: ", selector)
  }
  invisible(TRUE)
}

# Movie needs an exactly 4:3 visual viewport (embedded with aspect-ratio 4:3)
set_viewport(b, 1200, 900)
set_zoom(b, 1.25)

rec <- movie_start(b, fps = 12)
cur <- cursor_start(b)

# Record only the conversation (no header, no input), still exactly 4:3
rec$clip <- movie_clip_fit(
  b,
  c(".shiny-chat-user-message", ".shiny-chat-message"),
  pad = 24,
  container = ".shiny-chat-messages"
)

rec$loop(0.8)

# Mouse enters from the right edge and hovers the second user message, which
# reveals its edit button
r <- rect_of(b, ".shiny-chat-user-message")
cursor_glideto(cur, r$x + r$w * 0.85, r$y + r$h / 2, 0.9, rec)
wait_for(
  b,
  "(() => {
  const els = document.querySelectorAll('.shiny-chat-edit-btn');
  return els.length && getComputedStyle(els[els.length - 1]).opacity === '1';
})()"
)
rec$loop(0.4)

cursor_glideto_el(cur, ".shiny-chat-edit-btn", 0.5, rec)
cursor_click_here(cur, rec)
wait_for(b, "!!document.querySelector('.shiny-chat-edit-box .ProseMirror')")
rec$loop(0.5)

select_edit_text(b, "South America?")
rec$loop(0.6)
press_backspace(b)
wait_for(
  b,
  "!document.querySelector('.shiny-chat-edit-box .ProseMirror').textContent.includes('South America')",
  timeout = 5000
)
rec$loop(0.3)
type_natural(b, rec, "Asia?", selector = ".shiny-chat-edit-box .ProseMirror")
rec$loop(0.4)

cursor_glideto_el(cur, ".shiny-chat-edit-box .shiny-chat-btn-send", 0.6, rec)
cursor_click_here(cur, rec)
rec$loop_until(
  "!document.querySelector('.shiny-chat-edit-box')",
  timeout = 5000
)
rec$loop_until("document.body.textContent.includes('Everest')", timeout = 20000)
rec$loop(0.8)
rec$loop_until(
  "!!document.querySelector('button[aria-label=\"Previous version\"]')",
  timeout = 10000
)

# Mouse retreats off the right edge, then returns for the branch navigation
cursor_leave(cur, rec, 0.5)
rec$loop(0.4)

cursor_glideto_el(cur, 'button[aria-label="Previous version"]', 0.9, rec)
cursor_click_here(cur, rec)
rec$loop(1.2)

cursor_glideto_el(cur, 'button[aria-label="Next version"]', 0.7, rec)
cursor_click_here(cur, rec)
rec$loop(1.5)

movie_save(
  rec,
  shot_path("edit-branches-edit.mp4"),
  width = rec$clip$width * 2
)

wait_for_text(b, "Everest", timeout = 20000)
Sys.sleep(1)
union_png(
  b,
  shot_path("edit-branches-new.png"),
  c(
    ".shiny-chat-user-message",
    ".shiny-chat-message",
    'button[aria-label="Previous version"]'
  ),
  pad = 32,
  dy = 14
)

click_selector(b, 'button[aria-label="Previous version"]')
Sys.sleep(1)
union_png(
  b,
  shot_path("edit-branches-original.png"),
  c(
    ".shiny-chat-user-message",
    ".shiny-chat-message",
    'button[aria-label="Previous version"]'
  ),
  pad = 32,
  dy = 14
)

stop_app(app)
b$close()
