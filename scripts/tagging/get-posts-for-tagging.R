#!/usr/bin/env Rscript
# Output posts that need tagging for agent analysis
#
# Usage:
#   Rscript get-posts-for-tagging.R [options]
#
# Options:
#   --limit N        Number of posts to output (default: 10)
#   --offset N       Skip first N posts (default: 0)
#   --source NAME    Filter by ported_from value (e.g., "tidyverse")
#   --untagged-only  Only show posts missing software OR languages (default)
#   --all            Show all posts, not just untagged
#   --content        Include post content in output

library(jsonlite)

# Parse command line arguments
args <- commandArgs(trailingOnly = TRUE)

limit <- 10
offset <- 0
source_filter <- NULL
untagged_only <- TRUE
include_content <- FALSE

i <- 1
while (i <= length(args)) {
  if (args[i] == "--limit" && i < length(args)) {
    limit <- as.integer(args[i + 1])
    i <- i + 2
  } else if (args[i] == "--offset" && i < length(args)) {
    offset <- as.integer(args[i + 1])
    i <- i + 2
  } else if (args[i] == "--source" && i < length(args)) {
    source_filter <- args[i + 1]
    i <- i + 2
  } else if (args[i] == "--untagged-only") {
    untagged_only <- TRUE
    i <- i + 1
  } else if (args[i] == "--all") {
    untagged_only <- FALSE
    i <- i + 1
  } else if (args[i] == "--content") {
    include_content <- TRUE
    i <- i + 1
  } else {
    stop(paste("Unknown argument:", args[i]))
  }
}

# Read posts JSON
posts_json <- "content/blog/posts.json"
if (!file.exists(posts_json)) {
  stop("posts.json not found. Run extract-blog-metadata.R first.")
}

posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Filter functions
is_untagged <- function(post) {
  fm <- post$frontmatter
  no_software <- is.null(fm$software) || length(fm$software) == 0
  no_languages <- is.null(fm$languages) || length(fm$languages) == 0
  no_software || no_languages
}

matches_source <- function(post, source) {
  if (is.null(source)) return(TRUE)
  fm <- post$frontmatter
  !is.null(fm$ported_from) && fm$ported_from == source
}

is_not_draft <- function(post) {
  fm <- post$frontmatter
  is.null(fm$draft) || !isTRUE(fm$draft)
}

# Apply filters
filtered <- Filter(is_not_draft, posts)

if (!is.null(source_filter)) {
  filtered <- Filter(function(p) matches_source(p, source_filter), filtered)
}

if (untagged_only) {
  filtered <- Filter(is_untagged, filtered)
}

# Apply offset and limit
total <- length(filtered)
start_idx <- min(offset + 1, total + 1)
end_idx <- min(offset + limit, total)

if (start_idx > total) {
  selected <- list()
} else {
  selected <- filtered[start_idx:end_idx]
}

# Read content if requested
read_post_content <- function(post) {
  # Prefer source file, fall back to md_path
  path <- if (!is.null(post$source_path) && file.exists(post$source_path)) {
    post$source_path
  } else {
    post$md_path
  }

  if (file.exists(path)) {
    content <- readLines(path, warn = FALSE)
    paste(content, collapse = "\n")
  } else {
    NULL
  }
}

# Build output
output <- lapply(selected, function(post) {
  result <- list(
    md_path = post$md_path,
    source_path = post$source_path,
    title = post$frontmatter$title,
    ported_from = post$frontmatter$ported_from,
    categories = post$frontmatter$categories,
    tags = post$frontmatter$tags,
    software = post$frontmatter$software,
    languages = post$frontmatter$languages
  )

  if (include_content) {
    result$content <- read_post_content(post)
  }

  result
})

# Summary to stderr
message(sprintf(
  "Showing %d of %d posts (offset: %d, limit: %d)",
  length(output), total, offset, limit
))

if (!is.null(source_filter)) {
  message(sprintf("Filtered by source: %s", source_filter))
}

if (untagged_only) {
  message("Showing only untagged posts")
}

# Load valid software and language terms
software_dir <- "content/software"
valid_software <- list.dirs(software_dir, recursive = FALSE, full.names = FALSE)
valid_languages <- c("R", "Python", "Julia")

# Build final output with metadata
final_output <- list(
  valid_software = valid_software,
  valid_languages = valid_languages,
  posts = output
)

# Output JSON to stdout
cat(toJSON(final_output, auto_unbox = TRUE, pretty = TRUE, null = "null"))
