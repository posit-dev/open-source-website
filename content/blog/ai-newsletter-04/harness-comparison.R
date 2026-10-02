# Reproduces the harness-comparison plot from the gen-ai-pharma-26 talk
# ("Tell the model to care about being right"): bluffbench performance on the
# intuitive condition, Posit Assistant's harness vs. the minimal open-source
# harness, for the models the two share.

library(dplyr)
library(stringr)
library(ggplot2)

# Minimal harness results from the bluffbench package. The harness data uses
# names without "(non-thinking)", so strip that suffix to match.
raw <- bluffbench::bluff_results |>
  filter(
    type == "intuitive",
    model %in% c(
      "Claude Haiku 4.5 (non-thinking)",
      "Claude Sonnet 4.6 (non-thinking)",
      "Claude Sonnet 4.6 (medium)",
      "Claude Opus 4.8 (medium)"
    )
  ) |>
  mutate(model = str_remove(model, " \\(non-thinking\\)")) |>
  summarise(pct = mean(score == "C"), .by = model) |>
  mutate(source = "Minimal harness")

# Posit Assistant harness results (separate eval, not in the package)
harness <- read.csv("data/harness_data.csv") |>
  filter(harness == "PositAssistant", condition == "intuitive") |>
  mutate(
    model = paste0(
      "Claude ",
      model,
      ifelse(thinking == "Medium", " (medium)", "")
    )
  ) |>
  summarise(pct = mean(correct), .by = model) |>
  mutate(source = "Posit Assistant")

p <- bind_rows(raw, harness) |>
  filter(model %in% intersect(raw$model, harness$model)) |>
  mutate(
    model = factor(
      model,
      levels = c(
        "Claude Haiku 4.5",
        "Claude Sonnet 4.6",
        "Claude Sonnet 4.6 (medium)",
        "Claude Opus 4.8 (medium)"
      )
    ),
    source = factor(source, levels = c("Minimal harness", "Posit Assistant"))
  ) |>
  ggplot(aes(y = model, x = pct, fill = source)) +
  geom_col(position = position_dodge()) +
  scale_x_continuous(labels = scales::percent) +
  scale_fill_manual(
    values = c("Minimal harness" = "#d9d9d9", "Posit Assistant" = "#75AADB")
  ) +
  guides(fill = guide_legend(reverse = TRUE)) +
  labs(
    y = NULL,
    x = "% correct (intuitive)",
    fill = NULL,
    title = "Performance on bluffbench eval",
    subtitle = "Posit Assistant vs. minimal harness, intuitive condition"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    legend.position = "bottom",
    plot.subtitle = element_text(face = "italic")
  )

ggsave("images/harness-comparison.png", p, width = 8, height = 5, dpi = 200)
