# Estimates how much auto mode's classifier calls add to the cost of Posit
# Assistant conversations, relative to no classifier review (as with /yolo).
# Reads token usage from Posit Assistant's local conversation storage and
# reprices it under several main agent / classifier model pairs.

library(dplyr)
library(purrr)
library(jsonlite)

storage <- path.expand("~/.posit/assistant/workspaces")

# The 5 most recent results of `find_auto_mode_conversations(as.POSIXct("2026-11-03"))`
# on 2026-11-10, excluding the conversation that ran this analysis.
conversation_ids <- c(
  "be97cef2-1da0-4930-918d-4d1225bfebaf",
  "0dc2b3c7-6b96-437f-8f23-7c88b64db357",
  "c110480b-4df0-4f99-bda8-140bf479d0b6",
  "3f79ec5c-f473-4b8f-b02b-f666bc50f74b",
  "d40f69a6-2aa5-4d79-892e-a703a9527d94"
)

# USD per million tokens, from https://assistant.posit.co/models/. `above` is
# the prompt size (input + cache read + cache write) past which a tier applies.
# A missing `cache_write` rate means writes bill at the input rate; Anthropic
# bills writes by cache TTL instead. Gemini 4 Argon uses its post-introductory
# prices (from 2026-12-01).
prices <- tribble(
  ~model              , ~above , ~input , ~output , ~cache_read , ~cache_write , ~cache_write_5m , ~cache_write_1h ,
  "claude-sonnet-5-5" ,      0 , 2      , 10      , 0.10        , NA           , 2.5             , 4               ,
  "claude-opus-5-5"   ,      0 , 4      , 20      , 0.20        , NA           , 5               , 8               ,
  "claude-haiku-5-5"  ,      0 , 0.1    ,  0.5    , 0.01        , NA           , 0.125           , 0.2             ,
  "claude-haiku-5-5"  , 100000 , 0.5    ,  2.5    , 0.05        , NA           , 0.625           , 1               ,
  "gpt-6.1-sol"       ,      0 , 2      , 10      , 0.10        , 2.5          , NA              , NA              ,
  "gpt-6.1-sol"       , 272000 , 4      , 15      , 0.20        , 5            , NA              , NA              ,
  "gpt-6.1-terra"     ,      0 , 1      ,  5      , 0.05        , 1.25         , NA              , NA              ,
  "gpt-6.1-terra"     , 272000 , 2      ,  7.5    , 0.10        , 2.5          , NA              , NA              ,
  "gemini-4-argon"    ,      0 , 4      , 20      , 0.20        , NA           , NA              , NA              ,
  "gemini-3.8-flash"  ,      0 , 0.75   ,  3.75   , 0.075       , NA           , NA              , NA
)

pairs <- tribble(
  ~main               , ~classifier        , ~main_model         , ~classifier_model  , ~anthropic ,
  "Claude Sonnet 5.5" , "Claude Haiku 5.5" , "claude-sonnet-5-5" , "claude-haiku-5-5" , TRUE       ,
  "Claude Opus 5.5"   , "Claude Haiku 5.5" , "claude-opus-5-5"   , "claude-haiku-5-5" , TRUE       ,
  "GPT 6.1 Sol"       , "GPT 6.1 Terra"    , "gpt-6.1-sol"       , "gpt-6.1-terra"    , FALSE      ,
  "Gemini 4 Argon"    , "Gemini 3.8 Flash" , "gemini-4-argon"    , "gemini-3.8-flash" , FALSE
)

# Helpers ----------------------------------------------------------------------

# Conversations started since `since` with at least one classifier call (i.e.
# auto mode was on) and more than `min_prompts` user prompts on the active branch.
find_auto_mode_conversations <- function(since, min_prompts = 5) {
  usage_files <- list.files(
    storage,
    "^usage-events\\.jsonl$",
    recursive = TRUE,
    full.names = TRUE
  )
  usage_files <- usage_files[
    !grepl("/subagents/", usage_files) & file.mtime(usage_files) > since
  ]
  has_classifier <- map_lgl(usage_files, \(f) {
    any(grepl('"kind":"classifier"', readLines(f, warn = FALSE), fixed = TRUE))
  })

  map(dirname(usage_files[has_classifier]), \(dir) {
    conversation <- fromJSON(
      file.path(dir, "conversation.json"),
      simplifyVector = FALSE
    )
    tibble(
      id = basename(dir),
      title = conversation$root$title %||% NA_character_,
      started = as.POSIXct(conversation$root$timestamp / 1000),
      user_prompts = count_user_prompts(dir, conversation)
    )
  }) |>
    list_rbind() |>
    filter(started >= since, user_prompts > min_prompts) |>
    arrange(desc(started))
}

read_conversation_usage <- function(id) {
  dir <- Sys.glob(file.path(storage, "*", id))
  subagents <- list.dirs(file.path(dir, "subagents"), recursive = FALSE)

  bind_rows(
    read_message_usage(file.path(dir, "lm-messages.jsonl"), "main"),
    read_usage_events(file.path(dir, "usage-events.jsonl")),
    map(subagents, \(s) {
      bind_rows(
        read_message_usage(file.path(s, "lm-messages.jsonl"), "subagent"),
        read_usage_events(file.path(s, "usage-events.jsonl"))
      )
    }) |>
      list_rbind()
  ) |>
    mutate(id = id, .before = 1)
}

# One row per main agent or subagent request, from `positai.usage` on each
# assistant message. Requests without usage (failed or cancelled) are skipped.
read_message_usage <- function(path, kind) {
  readLines(path, warn = FALSE) |>
    map(\(line) fromJSON(line, simplifyVector = FALSE)$message) |>
    keep(\(m) {
      m$role == "assistant" &&
        !is.null(m$providerOptions$providerMetadata$positai$usage)
    }) |>
    map(\(m) {
      usage_row(kind, m$providerOptions$providerMetadata$positai$usage)
    }) |>
    list_rbind()
}

# Classifier, keepalive, and webfetch calls, plus usage from deleted messages.
read_usage_events <- function(path) {
  if (!file.exists(path)) {
    return(NULL)
  }
  readLines(path, warn = FALSE) |>
    map(\(line) fromJSON(line, simplifyVector = FALSE)) |>
    map(\(e) {
      usage_row(if (e$type == "deletedUsage") "deleted" else e$kind, e)
    }) |>
    list_rbind()
}

# `inputTokens` excludes cache reads and writes, so the four token buckets are
# disjoint. The TTL breakdown is NA when the provider didn't report one.
usage_row <- function(kind, u) {
  tibble(
    kind = kind,
    input = u$inputTokens %||% 0,
    output = u$outputTokens %||% 0,
    cache_read = u$cacheReadTokens %||% 0,
    cache_write = u$cacheWriteTokens %||% 0,
    cache_write_5m = u$cacheWrite5mTokens %||% NA_real_,
    cache_write_1h = u$cacheWrite1hTokens %||% NA_real_
  )
}

# Mirrors calculateCostBreakdown() in Posit Assistant's model-pricing.ts.
price_requests <- function(requests, model) {
  rates <- prices[prices$model == model, ] |> arrange(above)
  prompt <- requests$input + requests$cache_read + requests$cache_write
  r <- rates[pmax(1, findInterval(prompt, rates$above, left.open = TRUE)), ]

  by_ttl <- !is.na(r$cache_write_5m) &
    !is.na(requests$cache_write_5m) &
    !is.na(requests$cache_write_1h)
  write_cost <- if_else(
    by_ttl,
    requests$cache_write_5m *
      r$cache_write_5m +
      requests$cache_write_1h * r$cache_write_1h,
    requests$cache_write * coalesce(r$cache_write, r$cache_write_5m, r$input)
  )

  (requests$input *
    r$input +
    requests$output * r$output +
    requests$cache_read * r$cache_read +
    write_cost) /
    1e6
}

count_user_prompts <- function(dir, conversation) {
  active_ids <- conversation$messages |>
    keep(\(n) isTRUE(n$isActive)) |>
    map(\(n) unlist(n$lmMessageIds)) |>
    unlist()

  readLines(file.path(dir, "lm-messages.jsonl"), warn = FALSE) |>
    map(\(line) fromJSON(line, simplifyVector = FALSE)) |>
    keep(\(r) r$id %in% active_ids) |>
    map_lgl(\(r) is_user_prompt(r$message)) |>
    sum()
}

# User messages also carry injected context (environment, system reminders),
# which all start with an XML-style tag.
is_user_prompt <- function(message) {
  if (message$role != "user") {
    return(FALSE)
  }
  if (is.character(message$content)) {
    return(!startsWith(message$content, "<"))
  }
  text <- map_chr(message$content, \(p) {
    if (identical(p$type, "text")) p$text else ""
  })
  any(nzchar(text) & !startsWith(text, "<"))
}

# Analysis ---------------------------------------------------------------------

requests <- map(conversation_ids, read_conversation_usage) |> list_rbind()

increase_by_conversation <- pairs |>
  pmap(\(main, classifier, main_model, classifier_model, anthropic) {
    requests |>
      # Keepalive pings only exist to hold Anthropic's cache TTL
      filter(anthropic | kind != "keepalive") |>
      mutate(
        main = main,
        classifier = classifier,
        priced_as = if_else(kind == "classifier", classifier_model, main_model)
      ) |>
      group_by(priced_as) |>
      mutate(cost = price_requests(pick(everything()), priced_as[1])) |>
      ungroup()
  }) |>
  list_rbind() |>
  summarise(
    classifier_cost = sum(cost[kind == "classifier"]),
    base_cost = sum(cost[kind != "classifier"]),
    .by = c(main, classifier, id)
  ) |>
  mutate(increase = classifier_cost / base_cost)

increase_by_conversation |>
  summarise(mean_increase = mean(increase), .by = c(main, classifier)) |>
  mutate(mean_increase = sprintf("%.2f%%", 100 * mean_increase))
