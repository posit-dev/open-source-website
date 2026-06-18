# Anthropic-only variant of mocked-frontier.R: the running best mocked-condition
# score against release date, restricted to Claude models. Each point is a Claude
# model that set a new record when released.

library(dplyr)
library(stringr)
library(ggplot2)

scores <- bluffbench::bluff_results |>
  filter(type == "mocked", lab == "Anthropic") |>
  summarise(score = mean(score == "C"), .by = c(model, release_date)) |>
  mutate(model = str_remove(model, " \\(.*\\)$")) |>
  summarise(score = max(score), release_date = first(release_date), .by = model)

frontier <- scores |>
  arrange(release_date) |>
  mutate(prev_best = lag(cummax(score), default = -Inf)) |>
  filter(score > prev_best)

p <- ggplot(frontier, aes(x = release_date, y = score)) +
  geom_point(size = 3, color = "#2166ac") +
  ggrepel::geom_text_repel(
    aes(label = paste0(model, " (", scales::percent(score, accuracy = 1), ")")),
    nudge_y = 0.06,
    direction = "y",
    hjust = 0,
    segment.color = "grey70",
    size = 4.4
  ) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_x_date(date_labels = "%b %Y", expand = expansion(mult = c(0.05, 0.25))) +
  labs(
    x = NULL,
    y = "Best mocked-case score to date",
    title = "The mocked-case frontier, Anthropic models only",
    subtitle = "Each point is a Claude model that set a new record when released"
  ) +
  theme_minimal(base_size = 14) +
  theme(plot.subtitle = element_text(face = "italic"))

ggsave("images/mocked-frontier-anthropic.png", p, width = 9, height = 5, dpi = 200)
