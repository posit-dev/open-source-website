# Reconstructs the initial bluffbench results plot from the introducing-bluffbench
# blog post: the original three models across all three conditions.
#
# The original blog post used Claude Sonnet 4.5, Gemini 2.5 Pro, and GPT-5.
# These are now in the current package data as "(medium)" thinking variants.

library(dplyr)
library(forcats)
library(ggplot2)

results <- bluffbench::bluff_results |>
  filter(model %in% c(
    "Claude Sonnet 4.5 (medium)",
    "Gemini 2.5 Pro (medium)",
    "GPT-5 (medium)"
  )) |>
  mutate(
    model = stringr::str_remove(model, " \\(medium\\)"),
    score = factor(
      fct_recode(score, Correct = "C", Incorrect = "I"),
      levels = c("Incorrect", "Correct")
    ),
    type = factor(
      type,
      levels = c("mocked", "intuitive", "baseline"),
      labels = c("Mocked", "Intuitive", "Baseline")
    )
  )

pct_correct <- results |>
  summarise(pct = mean(score == "Correct"), .by = c(model, type))

p <- ggplot(results, aes(y = model, fill = score)) +
  geom_bar(position = "fill") +
  geom_text(
    data = pct_correct,
    aes(y = model, x = 1.02, label = scales::percent(pct, accuracy = 1)),
    inherit.aes = FALSE,
    hjust = 0,
    size = 3.2,
    color = "grey30"
  ) +
  facet_wrap(~type) +
  scale_x_continuous(
    breaks = c(0, 0.5, 1),
    labels = scales::percent,
    expand = expansion(mult = c(0, 0.15))
  ) +
  scale_fill_manual(
    values = c("Correct" = "#67a9cf", "Incorrect" = "#ef8a62"),
    breaks = c("Correct", "Incorrect")
  ) +
  labs(
    x = NULL,
    y = NULL,
    fill = NULL,
    title = "Models often report what they expect to see, not what's plotted",
    subtitle = "Initial bluffbench results, % correct across all three conditions"
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    panel.grid.major.y = element_blank(),
    axis.text.y = element_text(angle = 45, hjust = 1),
    strip.text = element_text(face = "bold")
  )

ggsave("images/original-bluffbench-results.png", p, width = 10, height = 3.5, dpi = 200)
