library(ggimage)
library(ggplot2)

image_dir <- here::here(
  "content",
  "blog",
  "ai-newsletter-08",
  "images"
)

plot_data <- tibble::tribble(
  ~section          , ~measure             , ~lab            , ~score ,
  "Capabilities"    , "Agentic coding"     , "Anthropic"     , 1      ,
  "Capabilities"    , "Agentic coding"     , "OpenAI"        ,  .8    ,
  "Capabilities"    , "Agentic coding"     , "Google Gemini" ,  .4    ,
  "Capabilities"    , "Vision"             , "Anthropic"     , 1      ,
  "Capabilities"    , "Vision"             , "OpenAI"        ,  .75   ,
  "Capabilities"    , "Vision"             , "Google Gemini" ,  .9    ,
  # Anthropic doesn't have image generation models.
  # "Capabilities", "Image generation", "Anthropic", 0,
  "Capabilities"    , "Image generation"   , "OpenAI"        ,  .8    ,
  "Capabilities"    , "Image generation"   , "Google Gemini" , 1      ,
  "Value"           , "Cost effectiveness" , "Anthropic"     ,  .45   ,
  "Value"           , "Cost effectiveness" , "OpenAI"        , 1      ,
  "Value"           , "Cost effectiveness" , "Google Gemini" ,  .55   ,
  "User experience" , "Intuitiveness"      , "Anthropic"     , 1      ,
  "User experience" , "Intuitiveness"      , "OpenAI"        ,  .9    ,
  "User experience" , "Intuitiveness"      , "Google Gemini" ,  .5    ,
  "User experience" , "Latency"            , "Anthropic"     ,  .5    ,
  "User experience" , "Latency"            , "OpenAI"        ,  .9    ,
  "User experience" , "Latency"            , "Google Gemini" , 1      ,
  "User experience" , "Communication"      , "Anthropic"     ,  .5    ,
  "User experience" , "Communication"      , "OpenAI"        , 1      ,
  "User experience" , "Communication"      , "Google Gemini" ,  .8
)

plot_data$measure <- factor(
  plot_data$measure,
  levels = rev(unique(plot_data$measure))
)

logo_files <- c(
  Anthropic = "anthropic-logo.png",
  OpenAI = "openai-logo.png",
  `Google Gemini` = "google-logo.png"
)

logo_paths <- stats::setNames(
  file.path(image_dir, unname(logo_files)),
  names(logo_files)
)

plot_data$logo <- unname(logo_paths[plot_data$lab])

# Logo size is scaled relative to each panel.
plot_data$logo_size <- c(
  Capabilities = 0.2,
  `User experience` = 0.2,
  Value = 0.55
)[plot_data$section]

measures <- unique(plot_data[c("section", "measure")])

legend_logos <- stats::setNames(
  lapply(logo_paths, \(path) as.raster(magick::image_read(path))),
  seq_along(logo_paths)
)

draw_key_model_logo <- function(data, params, size) {
  grid::rasterGrob(
    legend_logos[[as.character(data$shape)]],
    width = grid::unit(0.9, "npc"),
    height = grid::unit(0.9, "npc"),
    interpolate = TRUE
  )
}

model_landscape_plot <-
  ggplot(plot_data, aes(score, measure)) +
  geom_segment(
    data = measures,
    aes(x = 0, xend = 1, y = measure, yend = measure),
    inherit.aes = FALSE,
    colour = "grey70",
    linewidth = 0.2
  ) +
  geom_text(
    data = measures,
    aes(x = 0, y = measure, label = measure),
    inherit.aes = FALSE,
    hjust = 0,
    nudge_y = 0.3,
    size = 4.5
  ) +
  geom_point(
    aes(shape = lab),
    alpha = 0,
    size = 3,
    show.legend = TRUE,
    key_glyph = draw_key_model_logo
  ) +
  geom_image(aes(image = logo, size = logo_size)) +
  ggforce::facet_col(vars(section), scales = "free_y", space = "free") +
  scale_shape_manual(
    name = NULL,
    values = seq_along(logo_paths),
    breaks = c("Anthropic", "OpenAI", "Google Gemini")
  ) +
  scale_size_identity() +
  scale_x_continuous(
    limits = c(0, 1),
    breaks = c(0, 1),
    labels = c("Lower", "Higher"),
    expand = expansion(mult = c(0.02, 0.05))
  ) +
  guides(
    shape = guide_legend(
      override.aes = list(alpha = 1)
    )
  ) +
  theme_minimal(base_size = 15) +
  theme(
    axis.text.y = element_blank(),
    axis.ticks.y = element_blank(),
    axis.title.y = element_blank(),
    axis.text.x = element_text(size = 13),
    axis.title.x = element_text(size = 15),
    panel.grid = element_blank(),
    strip.text = element_text(hjust = 0, size = 16),
    legend.position = "top",
    legend.justification = "left",
    legend.title = element_text(size = 15),
    legend.text = element_text(size = 14),
    legend.key.width = grid::unit(0.65, "cm"),
    legend.key.height = grid::unit(0.65, "cm")
  ) +
  labs(x = "Relative level (vibes)")

ggsave(
  filename = file.path(image_dir, "model-landscape.png"),
  plot = model_landscape_plot,
  width = 12,
  height = 7.5,
  dpi = 300,
  bg = "white"
)
