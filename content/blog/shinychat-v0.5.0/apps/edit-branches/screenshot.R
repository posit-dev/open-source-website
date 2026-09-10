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
rec$loop(1)
wait_for(b, "document.querySelectorAll('.shiny-chat-edit-btn').length >= 2")
click_last(b, ".shiny-chat-edit-btn")
wait_for(b, "!!document.querySelector('.shiny-chat-edit-box .ProseMirror')")
Sys.sleep(0.5)
js(
  b,
  "(() => {
  const pm = document.querySelector('.shiny-chat-edit-box .ProseMirror');
  pm.focus();
  const sel = window.getSelection();
  sel.selectAllChildren(pm);
})()"
)
Sys.sleep(0.3)
b$Input$insertText(text = "And what is the tallest in Asia?")
Sys.sleep(0.4)
click_selector(b, ".shiny-chat-edit-box .shiny-chat-btn-send")
rec$loop(5)
movie_save(rec, shot_path("edit-branches-edit.mp4"), width = 2400)

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
