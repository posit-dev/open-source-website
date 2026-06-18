# Plots the running best ("frontier") mocked-condition score against model
# release date, faceted by lab: each point is a model that, when it was
# released, set a new record for its lab on the mocked case. Lab logos sit
# alongside the company name in each panel's strip title.

library(dplyr)
library(stringr)
library(ggplot2)

# Best mocked score per base model, taking the strongest thinking setting
scores <- bluffbench::bluff_results |>
  filter(type == "mocked") |>
  summarise(score = mean(score == "C"), .by = c(model, release_date, lab)) |>
  mutate(model = str_remove(model, " \\(.*\\)$")) |>
  summarise(
    score = max(score),
    release_date = first(release_date),
    lab = first(lab),
    .by = model
  )

# Per-lab frontier: models that set a new record for their lab when released
frontier <- scores |>
  arrange(lab, release_date) |>
  mutate(prev_best = lag(cummax(score), default = -Inf), .by = lab) |>
  filter(score > prev_best) |>
  # Strip "Claude " from Anthropic model names for cleaner labels
  mutate(model = str_remove(model, "^Claude "))

# Strip labels: small lab logo next to the company name, rendered via ggtext
strip_labels <- c(
  Anthropic = "<img src='images/anthropic-logo.png' height='14'/> &nbsp;Anthropic",
  Google = "<img src='images/google-logo.png' height='14'/> &nbsp;Google",
  OpenAI = "<img src='images/openai-logo.png' height='14'/> &nbsp;OpenAI"
)

p <- ggplot(frontier, aes(x = release_date, y = score)) +
  geom_line(color = "#2166ac", linewidth = 0.6) +
  geom_point(size = 3, color = "#2166ac") +
  ggrepel::geom_text_repel(
    aes(label = model),
    direction = "both",
    nudge_x = 10,
    nudge_y = 0.05,
    hjust = 1,
    segment.color = "grey70",
    size = 3,
    min.segment.length = 0.75
  ) +
  facet_wrap(~lab, nrow = 1, labeller = labeller(lab = strip_labels)) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_x_date(
    date_labels = "%b %y",
    date_breaks = "3 months",
    expand = expansion(mult = c(0.08, 0.08))
  ) +
  labs(
    x = NULL,
    y = "Best mocked-case score to date",
    title = "The frontier on the mocked case is climbing toward saturation",
    subtitle = "Each point is a model that set a new record for its lab when released"
  ) +
  theme_minimal() +
  theme(
    plot.subtitle = element_text(face = "italic"),
    strip.text = ggtext::element_markdown(),
    panel.border = element_rect(color = "grey80", fill = NA, linewidth = 0.3)
  )

ggsave("images/mocked-frontier.png", p, width = 11, height = 5, dpi = 200)
