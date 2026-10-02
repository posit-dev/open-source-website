# Detects, per sample-epoch, whether the model added a modeled result
# (a `geom_smooth()`) to the *artifact plot* -- the plot it makes in response
# to the scripted request for the plot containing the artifact. Writes a
# compact per-sample csv that index.qmd reads to compare accuracy with vs.
# without that modeled overlay.
#
# The logs and model metadata live in posit-dev/bluffbench2. This reads them
# from a sibling clone by default, falling back to the copies on GitHub (the
# logs are tracked there, even though inst/run/logs is dropped from the package
# build) when the clone isn't present.

library(tidyverse)
library(vitals)
library(ellmer)

logs_dir <- Sys.getenv(
  "BLUFF2_LOGS_DIR",
  "../../bluffbench2/inst/run/logs"
)
metadata_path <- file.path(dirname(dirname(dirname(logs_dir))), "data-raw/model_metadata.csv")

gh_contents <- "https://api.github.com/repos/posit-dev/bluffbench2/contents"
gh_raw <- "https://raw.githubusercontent.com/posit-dev/bluffbench2/main"

# Local log files if the clone is present, otherwise the GitHub copies
# downloaded into a temp dir (vitals_log_read needs a local path).
resolve_log_files <- function(dir) {
  local <- sort(list.files(dir, pattern = "[.]json$", full.names = TRUE))
  if (length(local) > 0) {
    return(local)
  }
  entries <- jsonlite::fromJSON(file.path(gh_contents, "inst/run/logs"))
  entries <- entries[grepl("[.]json$", entries$name), ]
  dest_dir <- file.path(tempdir(), "bluff2-logs")
  dir.create(dest_dir, showWarnings = FALSE)
  purrr::map_chr(seq_len(nrow(entries)), function(i) {
    dest <- file.path(dest_dir, entries$name[i])
    if (!file.exists(dest)) {
      utils::download.file(entries$download_url[i], dest, quiet = TRUE)
    }
    dest
  })
}

# Mirrors posit-dev/bluffbench2's data-raw/bluff2_results.R so model names and
# labs line up with the shipped `bluff2_results`.
run_names <- c(
  "claude-opus-4-8" = "opus_4_8_medium",
  "claude-fable-5" = "fable_5_medium",
  "claude-sonnet-5" = "sonnet_5_medium",
  "gpt-5.5" = "gpt_5_5_medium",
  "gpt-5.6-terra" = "gpt_5_6_terra_medium",
  "gpt-5.6-sol" = "gpt_5_6_sol_medium",
  "gemini-3.5-flash" = "gemini_3_5_flash_medium"
)

pretty_model <- c(
  opus_4_8_medium = "Claude Opus 4.8",
  fable_5_medium = "Claude Fable 5",
  sonnet_5_medium = "Claude Sonnet 5",
  gemini_3_5_flash_medium = "Gemini 3.5 Flash",
  gpt_5_5_medium = "GPT-5.5",
  gpt_5_6_terra_medium = "GPT-5.6 Terra",
  gpt_5_6_sol_medium = "GPT-5.6 Sol"
)

run_r_names <- c("run_r", "run_r_code", "execute_r", "execute_r_code")

# A scripted user turn is one the harness wrote (it carries prose), as opposed
# to a tool-result turn. They arrive in a fixed order -- load, lull(s), artifact
# request, follow-up -- so the artifact request is the second-to-last and the
# follow-up is the last. This matches how the eval's own scorer locates them.
is_scripted_user_turn <- function(turn) {
  inherits(turn, "ellmer::UserTurn") &&
    any(vapply(
      turn@contents,
      function(x) inherits(x, "ellmer::ContentText"),
      logical(1)
    ))
}

# The R code the model ran while answering the artifact-plot request: every
# run-R tool call in the assistant turns strictly between the artifact request
# and the follow-up.
artifact_plot_code <- function(chat) {
  turns <- chat$get_turns()
  scripted <- which(vapply(turns, is_scripted_user_turn, logical(1)))
  if (length(scripted) < 2) {
    return(NA_character_)
  }
  followup_idx <- scripted[length(scripted)]
  artifact_idx <- scripted[length(scripted) - 1]

  code <- character(0)
  for (i in seq_along(turns)) {
    if (i <= artifact_idx || i >= followup_idx) next
    turn <- turns[[i]]
    if (!inherits(turn, "ellmer::AssistantTurn")) next
    for (content in turn@contents) {
      if (
        inherits(content, "ellmer::ContentToolRequest") &&
          content@name %in% run_r_names
      ) {
        code <- c(code, content@arguments$code %||% "")
      }
    }
  }
  paste(code, collapse = "\n")
}

log_files <- resolve_log_files(logs_dir)
slugs <- gsub(
  "^[^_]+_bluffbench2-|-[0-9a-f]+[.]json$",
  "",
  basename(log_files)
)
latest <- tapply(log_files, slugs, function(files) files[length(files)])

metadata_src <- if (file.exists(metadata_path)) {
  metadata_path
} else {
  file.path(gh_raw, "data-raw/model_metadata.csv")
}
model_metadata <- read_csv(metadata_src, show_col_types = FALSE) %>%
  select(task_name, lab)

samples <- imap(latest, function(file, slug) {
  res <- vitals_log_read(file)
  tibble(
    task_name = run_names[[slug]],
    id = res$id,
    epoch = res$epoch,
    score = as.character(res$score),
    has_smooth = grepl("geom_smooth", map_chr(res$solver_chat, artifact_plot_code))
  )
}) %>%
  list_rbind() %>%
  left_join(model_metadata, by = "task_name") %>%
  mutate(model = unname(pretty_model[task_name])) %>%
  select(model, lab, id, epoch, score, has_smooth)

dir.create("data", showWarnings = FALSE)
write_csv(samples, "data/geom-smooth.csv")
