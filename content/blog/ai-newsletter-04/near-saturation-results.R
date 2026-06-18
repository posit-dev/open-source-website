# Recent bluffbench results across all three conditions, in the same style as
# the index.qmd bluff_plot(). Uses ggforce::facet_col() per condition to get
# free y-scales and space, then combines with patchwork.

library(dplyr)
library(forcats)
library(stringr)
library(ggplot2)
library(patchwork)

results <- bluffbench::bluff_results |>
  filter(release_date >= "2026-01-01") |>
  mutate(
    score = factor(
      fct_recode(score, Correct = "C", Incorrect = "I"),
      levels = c("Incorrect", "Correct")
    ),
    type = factor(
      type,
      levels = c("mocked", "intuitive", "baseline"),
      labels = c("Mocked", "Intuitive", "Baseline")
    ),
    thinking = factor(
      ifelse(thinking, "Medium thinking", "Non-thinking"),
      levels = c("Medium thinking", "Non-thinking")
    )
  )

# Sort by mocked score
mocked_order <- results |>
  filter(type == "Mocked") |>
  summarise(pct = mean(score == "Correct"), .by = model) |>
  arrange(pct) |>
  pull(model)

results <- mutate(results, model = factor(model, levels = mocked_order))

pct_correct <- results |>
  summarise(pct = mean(score == "Correct"), .by = c(model, type, thinking))

# Strip thinking suffix for display only
strip_thinking <- function(x) str_remove(x, " \\(.*\\)$")

bluff_plot <- function(
  data,
  pct_data,
  condition,
  show_y = TRUE,
  show_strip = TRUE
) {
  d <- filter(data, type == condition)
  pct <- filter(pct_data, type == condition)

  p <- ggplot(d, aes(y = model, fill = score)) +
    geom_bar(position = "fill") +
    geom_text(
      data = pct,
      aes(y = model, x = 1.02, label = scales::percent(pct, accuracy = 1)),
      inherit.aes = FALSE,
      hjust = 0,
      size = 4.1,
      color = "grey30"
    ) +
    ggforce::facet_col(vars(thinking), scales = "free_y", space = "free") +
    scale_x_continuous(
      breaks = c(0, 0.5, 1),
      labels = scales::percent,
      expand = expansion(mult = c(0, 0.15))
    ) +
    scale_y_discrete(labels = strip_thinking) +
    scale_fill_manual(
      values = c("Correct" = "#67a9cf", "Incorrect" = "#ef8a62"),
      breaks = c("Correct", "Incorrect")
    ) +
    labs(x = NULL, y = NULL, fill = NULL, title = condition) +
    theme_minimal(base_size = 16) +
    theme(
      legend.position = "none",
      panel.grid.major.y = element_blank(),
      strip.background = element_blank(),
      strip.text = if (show_strip) {
        element_text(face = "bold", hjust = 0)
      } else {
        element_text(face = "bold", hjust = 0, color = "transparent")
      },
      axis.text.y = if (show_y) element_text(size = 14) else element_blank(),
      plot.title = element_text(size = 16, hjust = 0.5)
    )

  p
}

p1 <- bluff_plot(
  results,
  pct_correct,
  "Mocked",
  show_y = TRUE,
  show_strip = TRUE
)
p2 <- bluff_plot(
  results,
  pct_correct,
  "Intuitive",
  show_y = FALSE,
  show_strip = FALSE
)
p3 <- bluff_plot(
  results,
  pct_correct,
  "Baseline",
  show_y = FALSE,
  show_strip = FALSE
)

p <- p1 +
  p2 +
  p3 +
  plot_annotation(
    title = "The strongest models now reliably interpret counterintuitive plots",
    subtitle = "bluffbench results for models released in 2026, % correct across all three conditions",
    theme = theme(
      plot.title = element_text(size = 21),
      plot.subtitle = element_text(face = "italic", size = 16)
    )
  ) +
  plot_layout(
    guides = "collect",
    widths = c(1.05, 1, 1)
  ) &
  theme(legend.position = "bottom")

ggsave(
  "images/near-saturation-results.png",
  p,
  width = 12,
  height = 8,
  dpi = 200
)
