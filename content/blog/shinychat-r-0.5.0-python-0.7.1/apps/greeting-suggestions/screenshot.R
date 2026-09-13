source("../_common.R")

app <- start_app(app_path("greeting-suggestions"))
b <- connect(app, width = 1100, height = 720)

wait_for_app_ready(b)
set_zoom(b, 1.2)
# Let the composer finish its entrance fade so the input isn't caught
# mid-animation in the greeting screenshot
wait_for(
  b,
  "(() => { const c = document.querySelector('.shiny-chat-composer');
  return !!c && getComputedStyle(c).opacity === '1'; })()"
)
Sys.sleep(0.5)

# 1. Fresh chat: greeting with three suggestion cards. Focus the input so
#    the composer shows its enabled look instead of the idle dimmed style.
chat_focus(b)
Sys.sleep(1)
union_png(
  b,
  shot_path("greeting-suggestions-greeting.png"),
  c(".shiny-chat-greeting", "#chat_user_input"),
  pad = 32
)

# 2. A suggestion clicked fills the input; the greeting stays put
click_selector(
  b,
  ".shiny-chat-greeting .suggestion:not(.submit) .shiny-chat-suggestion-list-item-body"
)
Sys.sleep(0.5)
union_png(
  b,
  shot_path("greeting-suggestions-fill-input.png"),
  c(".shiny-chat-greeting", "#chat_user_input"),
  pad = 32
)

# 3. An attached plot and a prompt, clipped to the left side of the composer
#    so the attach button and the attachment chip are the focus
plot_file <- file.path(tempdir(), "penguin-bill-length.png")
ggplot2::ggsave(
  plot_file,
  ggplot2::ggplot(
    palmerpenguins::penguins,
    ggplot2::aes(x = species, y = bill_length_mm, fill = species)
  ) +
    ggplot2::geom_boxplot() +
    ggplot2::labs(y = "Bill length (mm)") +
    ggplot2::theme_minimal(base_size = 14),
  width = 5,
  height = 3.5,
  dpi = 150,
  bg = "white"
)
b$Page$navigate(app$url)
wait_for_app_ready(b)
set_zoom(b, 1.2)
wait_for(
  b,
  "(() => { const c = document.querySelector('.shiny-chat-composer');
  return !!c && getComputedStyle(c).opacity === '1'; })()"
)
Sys.sleep(0.5)

doc <- b$DOM$getDocument()
file_node <- b$DOM$querySelector(doc$root$nodeId, "input[type=file]")
b$DOM$setFileInputFiles(files = list(plot_file), nodeId = file_node$nodeId)
wait_for(
  b,
  "(() => { const a = document.querySelector('.shiny-chat-input-attachments');
  return !!a && a.children.length > 0; })()"
)
# The input gets a disabled class while the attachment processes
wait_for(
  b,
  "!document.querySelector('.shiny-chat-input').className.includes('disabled')"
)
Sys.sleep(0.3)
chat_type(b, "Explain this plot")
Sys.sleep(0.5)

clip <- js(
  b,
  "(() => {
  const c = document.querySelector('.shiny-chat-composer').getBoundingClientRect();
  return { x: c.x + window.scrollX, y: c.y + window.scrollY, w: c.width, h: c.height };
})()"
)
save_png(
  b,
  shot_path("attachments-plot.png"),
  list(
    x = clip$x - 12,
    y = clip$y - 12,
    width = clip$w * 0.62,
    height = clip$h + 24,
    scale = 1
  ),
  beyond = FALSE
)

stop_app(app)
b$close()
