# Cost–performance Pareto frontier on the mocked condition. Uses lab logos as
# scatter points via ggimage. Labeled points are Pareto-efficient.

library(dplyr)
library(stringr)
library(ggplot2)
library(ggimage)

logo_paths <- c(
  Anthropic = "images/anthropic-logo.png",
  Google = "images/google-logo.png",
  OpenAI = "images/openai-logo.png"
)

cost_score <- bluffbench::bluff_results |>
  filter(type == "mocked") |>
  summarise(
    pct = mean(score == "C"),
    cost = first(cost),
    lab = first(lab),
    .by = model
  ) |>
  mutate(
    model_label = str_remove(model, " \\(.*\\)$"),
    logo = logo_paths[lab]
  )

# Pareto frontier: no other model is both cheaper AND higher-scoring
cost_score <- cost_score |>
  mutate(
    pareto = purrr::map_lgl(seq_len(n()), \(i) {
      !any(cost[-i] <= cost[i] & pct[-i] >= pct[i])
    })
  )

# Labels: show thinking level only when a base model appears >1 time on frontier
pareto_base_counts <- cost_score |>
  filter(pareto) |>
  count(model_label)

cost_score <- cost_score |>
  left_join(pareto_base_counts, by = "model_label") |>
  mutate(
    pareto_label = case_when(
      !pareto ~ NA_character_,
      lab == "Anthropic" ~ str_remove(model, "^Claude ") |>
        str_remove(" \\(medium\\)$"),
      n > 1 ~ model |>
        str_replace(" \\(medium\\)", " (med.)") |>
        str_replace(" \\(non-thinking\\)", " (NT)"),
      TRUE ~ model_label
    )
  ) |>
  select(-n)

p <- ggplot(cost_score, aes(cost, pct)) +
  annotate("text", x = 0.03, y = Inf, label = "Low cost, high score",
           hjust = 0, vjust = 1.5, color = "grey75", size = 3.3,
           fontface = "italic") +
  annotate("text", x = 12, y = Inf, label = "High cost, high score",
           hjust = 1, vjust = 1.5, color = "grey75", size = 3.3,
           fontface = "italic") +
  annotate("text", x = 0.03, y = -Inf, label = "Low cost, low score",
           hjust = 0, vjust = -0.5, color = "grey75", size = 3.3,
           fontface = "italic") +
  annotate("text", x = 12, y = -Inf, label = "High cost, low score",
           hjust = 1, vjust = -0.5, color = "grey75", size = 3.3,
           fontface = "italic") +
  geom_image(aes(image = logo), size = 0.04, asp = 1.3) +
  ggrepel::geom_text_repel(
    data = filter(cost_score, pareto),
    aes(label = pareto_label),
    size = 3.5, seed = 8412, max.overlaps = 20,
    nudge_y = 0.04, segment.color = "grey70"
  ) +
  scale_x_log10(labels = scales::dollar) +
  scale_y_continuous(labels = scales::percent,
                     expand = expansion(mult = c(0.1, 0.1))) +
  coord_cartesian(clip = "off") +
  labs(
    x = "Solver cost (full eval, log scale)",
    y = "Mocked-condition accuracy",
    title = "Cost\u2013performance Pareto frontier on the mocked condition",
    subtitle = "Labeled points are Pareto-efficient (no model is both cheaper and better)"
  ) +
  theme_minimal() +
  theme(plot.subtitle = element_text(face = "italic", size = 9))

ggsave("images/pareto-frontier.png", p, width = 9, height = 5.5, dpi = 200)
