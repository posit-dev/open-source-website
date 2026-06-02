library(tidyverse)
library(ggrepel)

# Benchmark cost: cost to run the Artificial Analysis Intelligence Index suite
# Source: https://artificialanalysis.ai
models_tbl <- tribble(
  ~name               , ~model_id          , ~provider   , ~release_date , ~benchmark_cost ,
  "Claude Haiku 3.5"  , "claude_3_5_haiku" , "Anthropic" , "2024-11-03"  ,   56.52         ,
  "Claude Haiku 4.5"  , "haiku_4_5"        , "Anthropic" , "2025-10-15"  ,  246.01         ,
  "Claude Sonnet 4.5" , "sonnet_4_5"       , "Anthropic" , "2025-09-29"  ,  826.79         ,
  "Claude Sonnet 4.6" , "sonnet_4_6"       , "Anthropic" , "2026-02-17"  , 1694.19         ,
  "Claude Opus 4.6"   , "opus_4_6"         , "Anthropic" , "2026-02-05"  , 1745.71         ,
  "Claude Opus 4.7"   , "opus_4_7"         , "Anthropic" , "2026-04-16"  , 5117.14         ,
  "Gemini 3 Pro"      , "gemini_3"         , "Google"    , "2025-11-18"  ,  819.84         ,
  "Gemini 3.1 Pro"    , "gemini_3_1"       , "Google"    , "2026-02-19"  ,  892.28         ,
  "Gemini 3 Flash"    , "gemini_3_flash"   , "Google"    , "2025-11-18"  ,   65.98         ,
  "Gemini 3.5 Flash"  , "gemini_3_5_flash" , "Google"    , "2026-05-19"  , 1551.60         ,
  "GPT-5.4"           , "gpt_5_4"          , "OpenAI"    , "2026-03-05"  , 2851.01         ,
  "GPT-5.5"           , "gpt_5_5"          , "OpenAI"    , "2026-04-23"  , 3357.00
) |>
  mutate(
    release_date = as.Date(release_date),
    short_name = str_remove(name, "^Claude "),
    label_color = case_when(
      provider == "Anthropic" ~ "#be8bd4ff",
      provider == "OpenAI" ~ "#80c8d3ff",
      provider == "Google" ~ "#fcd9b6"
    )
  )

pairs <- tribble(
  ~predecessor       , ~successor         ,
  "claude_3_5_haiku" , "haiku_4_5"        ,
  "sonnet_4_5"       , "sonnet_4_6"       ,
  "opus_4_6"         , "opus_4_7"         ,
  "gemini_3"         , "gemini_3_1"       ,
  "gemini_3_flash"   , "gemini_3_5_flash" ,
  "gpt_5_4"          , "gpt_5_5"
)

paired_ids <- c(pairs$predecessor, pairs$successor)
paired_models <- models_tbl |> filter(model_id %in% paired_ids)


segments <-
  pairs |>
  left_join(
    paired_models |> select(model_id, release_date, benchmark_cost, provider),
    by = c("predecessor" = "model_id")
  ) |>
  left_join(
    paired_models |> select(model_id, release_date, benchmark_cost),
    by = c("successor" = "model_id"),
    suffix = c("_pred", "_succ")
  )

provider_colors <- c(
  "Anthropic" = "#be8bd4ff",
  "OpenAI" = "#80c8d3ff",
  "Google" = "#e8884a"
)

paired_models |>
  ggplot(aes(x = release_date, y = benchmark_cost)) +
  geom_segment(
    data = segments,
    aes(
      x = release_date_pred,
      xend = release_date_succ,
      y = benchmark_cost_pred,
      yend = benchmark_cost_succ,
      color = provider
    ),
    arrow = arrow(length = unit(0.12, "cm"), type = "closed"),
    linewidth = 0.8,
    alpha = 0.5
  ) +
  geom_point(aes(color = provider), size = 3) +
  geom_label_repel(
    aes(label = short_name, fill = alpha(label_color, 0.8)),
    size = 2.8,
    color = "#333333",
    show.legend = FALSE,
    max.overlaps = 20,
    seed = 3192,
    box.padding = 0.3,
    point.padding = 0.2,
    force = 4,
    force_pull = 0.4,
    segment.size = 0,
    nudge_y = 0.28,
    direction = "both"
  ) +
  scale_color_manual(values = provider_colors) +
  scale_fill_identity() +
  scale_x_date(
    date_labels = "%b %Y",
    date_breaks = "4 months",
    expand = expansion(mult = c(0.05, 0.08))
  ) +
  scale_y_continuous(
    labels = scales::label_dollar(),
    breaks = scales::breaks_width(1500),
    expand = expansion(mult = c(0.08, 0.15))
  ) +
  labs(
    title = "Cost to run the Artificial Analysis benchmark suite",
    subtitle = "Prices have increased for recent models compared to their predecessors",
    x = "Release date",
    y = "Benchmark cost (USD)",
    color = "Provider"
  ) +
  theme_minimal(base_size = 16)

ggsave("2026-05-22/images/plot-model-price.png", width = 10, height = 6.5)
