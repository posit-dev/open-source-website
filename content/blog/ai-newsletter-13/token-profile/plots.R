library(ggplot2)
library(dplyr)

profile <- read.csv("data/token-profile.csv") |>
  mutate(
    tool = factor(
      recode_values(tag, c("pa-opus", "pa-gpt") ~ "Assistant (TUI)", "claude" ~ "claude -p", "codex" ~ "codex exec"),
      levels = c("Assistant (TUI)", "claude -p", "codex exec")
    ),
    model = if_else(tag %in% c("pa-opus", "claude"), "Opus", "Sol"),
    section = factor(
      recode_values(
        section,
        "system prompt" ~ "System\nprompt",
        "tool definitions" ~ "Tool\ndescriptions",
        "skill listing" ~ "Skill\ndescriptions",
        default = "Other"
      ),
      levels = c("System\nprompt", "Tool\ndescriptions", "Skill\ndescriptions", "Other")
    )
  ) |>
  summarize(tokens = sum(tokens), .by = c(tool, model, section))

tool_colors <- c("Assistant (TUI)" = "grey60", "claude -p" = "#C44900", "codex exec" = "#2B67E0")
y_lab <- 'Input tokens for a single "Hi" turn'

totals <- profile |>
  summarize(tokens = sum(tokens), .by = c(tool, model)) |>
  ggplot(aes(model, tokens, fill = tool)) +
  geom_col(position = position_dodge(width = 0.9)) +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values = tool_colors) +
  labs(x = NULL, y = y_lab, fill = "Tool")

sections <- profile |>
  ggplot(aes(tool, tokens, fill = tool)) +
  geom_col() +
  facet_grid(section ~ model, scales = "free_x") +
  scale_y_continuous(labels = scales::comma) +
  scale_fill_manual(values = tool_colors) +
  labs(x = NULL, y = y_lab, fill = NULL) +
  theme(axis.text.x = element_blank(), axis.ticks.x = element_blank())

ggsave("images/token-profile-totals.png", totals, width = 5.5, height = 3.4, dpi = 200)
ggsave("images/token-profile-sections.png", sections, width = 6.3, height = 4.5, dpi = 200)
