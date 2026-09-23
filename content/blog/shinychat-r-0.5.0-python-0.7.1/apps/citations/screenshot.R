source("../_common.R")

app <- start_app(app_path("citations"))
b <- connect(app, width = 1000, height = 760)

wait_for_app_ready(b)
set_zoom(b, 1.25)
Sys.sleep(1)

chat_type(b, "What does the training report recommend?", press_enter = TRUE)
wait_for_text(b, "embedding layer", timeout = 20000)
# The mock streams in chunks; wait until the message text stops changing so
# layout is stable before measuring/screenshotting.
len <- function() {
  js(b, "document.querySelector('.shiny-chat-messages').textContent.length")
}
repeat {
  n1 <- len()
  Sys.sleep(0.7)
  n2 <- len()
  if (n1 == n2) break
}
Sys.sleep(0.5)

click_selector(b, ".shiny-aside-pill")
Sys.sleep(0.8)
# Floating-ui positions the popover in unzoomed coordinates, so under the
# emulated page zoom it drifts away from the pill. Re-anchor it just below
# the pill, dividing by the zoom to land at the intended visual position.
js(
  b,
  "(() => {
  const pill = document.querySelector('.shiny-aside-pill');
  const pop = document.querySelector('.shiny-aside-popover');
  if (!pill || !pop) return false;
  const p = pill.getBoundingClientRect();
  const z = parseFloat(document.documentElement.style.zoom) || 1;
  pop.style.transform = 'none';
  pop.style.left = (p.left / z) + 'px';
  pop.style.top = ((p.bottom + 8) / z) + 'px';
  return true;
})()"
)
Sys.sleep(0.5)
union_png(
  b,
  shot_path("citations-popover.png"),
  c(".shiny-chat-message", ".shiny-aside-popover"),
  pad = 32,
  dy = 14
)

stop_app(app)
b$close()
