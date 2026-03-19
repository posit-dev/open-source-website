#!/usr/bin/env Rscript
# Update posts.json with agent tag recommendations
#
# Usage:
#   Rscript update-posts-json.R recommendations.json
#   cat recommendations.json | Rscript update-posts-json.R -
#
# Input format (JSON array):
#   [
#     {
#       "md_path": "content/blog/tidyverse/...",
#       "software": ["dplyr", "tidyr"],
#       "languages": ["R"]
#     },
#     ...
#   ]
#
# Valid software values are folder names in content/software/
# Valid language values: R, Python, Julia

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 1) {
  stop("Usage: Rscript update-posts-json.R <recommendations.json | ->")
}

# Read recommendations
if (args[1] == "-") {
  recs_text <- paste(readLines(file("stdin")), collapse = "\n")
  recommendations <- fromJSON(recs_text, simplifyVector = FALSE)
} else {
  if (!file.exists(args[1])) {
    stop(paste("File not found:", args[1]))
  }
  recommendations <- fromJSON(args[1], simplifyVector = FALSE)
}

# Read current posts.json
posts_json <- "content/blog/posts.json"
if (!file.exists(posts_json)) {
  stop("posts.json not found. Run extract-blog-metadata.R first.")
}

posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Load valid software values
software_dir <- "content/software"
valid_software <- list.dirs(software_dir, recursive = FALSE, full.names = FALSE)

# Valid languages
valid_languages <- c("R", "Python", "Julia")

# Build lookup by md_path
posts_by_path <- new.env(hash = TRUE)
for (i in seq_along(posts)) {
  posts_by_path[[posts[[i]]$md_path]] <- i
}

# Track updates and errors
updated <- 0
errors <- list()

for (rec in recommendations) {
  md_path <- rec$md_path

  if (is.null(md_path)) {
    errors <- c(errors, list("Recommendation missing md_path"))
    next
  }

  idx <- posts_by_path[[md_path]]
  if (is.null(idx)) {
    errors <- c(errors, list(paste("Post not found:", md_path)))
    next
  }

  # Validate and update software
  # Note: null means "don't change", empty array means "clear"
  if (!is.null(rec$software)) {
    software <- if (is.list(rec$software)) unlist(rec$software) else rec$software
    if (length(software) == 0) {
      # Explicitly clear software
      posts[[idx]]$frontmatter$software <- list()
    } else {
      invalid <- setdiff(software, valid_software)
      if (length(invalid) > 0) {
        errors <- c(errors, list(paste(
          "Invalid software for", md_path, ":",
          paste(invalid, collapse = ", ")
        )))
      }
      valid <- intersect(software, valid_software)
      if (length(valid) > 0) {
        posts[[idx]]$frontmatter$software <- as.list(valid)
      }
    }
  }

  # Validate and update languages
  # Note: null means "don't change", empty array means "clear"
  if (!is.null(rec$languages)) {
    languages <- if (is.list(rec$languages)) unlist(rec$languages) else rec$languages
    if (length(languages) == 0) {
      # Explicitly clear languages
      posts[[idx]]$frontmatter$languages <- list()
    } else {
      invalid <- setdiff(languages, valid_languages)
      if (length(invalid) > 0) {
        errors <- c(errors, list(paste(
          "Invalid languages for", md_path, ":",
          paste(invalid, collapse = ", ")
        )))
      }
      valid <- intersect(languages, valid_languages)
      if (length(valid) > 0) {
        posts[[idx]]$frontmatter$languages <- as.list(valid)
      }
    }
  }

  updated <- updated + 1
}

# Write updated posts.json
json_output <- toJSON(posts, auto_unbox = TRUE, pretty = TRUE, null = "null")
writeLines(json_output, posts_json)

# Report to stderr
message(sprintf("Updated %d posts in %s", updated, posts_json))

if (length(errors) > 0) {
  message(sprintf("\n%d errors:", length(errors)))
  for (err in errors) {
    message(paste(" -", err))
  }
}
