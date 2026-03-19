#!/usr/bin/env Rscript
# Output posts that need category assignment for review
#
# Usage:
#   Rscript get-posts-for-categorizing.R [options]
#
# Options:
#   --limit N        Number of posts to output (default: 30)
#   --offset N       Skip first N posts (default: 0)
#   --source NAME    Filter by ported_from value (e.g., "tidyverse")
#   --content        Include post content in output

library(jsonlite)

# Parse command line arguments
args <- commandArgs(trailingOnly = TRUE)

limit <- 30
offset <- 0
source_filter <- NULL
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
  } else if (args[i] == "--content") {
    include_content <- TRUE
    i <- i + 1
  } else {
    stop(paste("Unknown argument:", args[i]))
  }
}

# Valid categories
valid_categories <- c(
  "Machine Learning",
  "Artificial Intelligence",
  "Visualization",
  "Interactive Apps",
  "Publishing",
  "MLOps & Admin",
  "Data Wrangling",
  "Best Practices",
  "Community"
)

# Read posts JSON
posts_json <- "content/blog/posts.json"
if (!file.exists(posts_json)) {
  stop("posts.json not found. Run extract-blog-metadata.R first.")
}

posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Filter functions
needs_category <- function(post) {
  fm <- post$frontmatter
  is.null(fm$categories) || length(fm$categories) == 0
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
filtered <- Filter(needs_category, filtered)

if (!is.null(source_filter)) {
  filtered <- Filter(function(p) matches_source(p, source_filter), filtered)
}

# Sort by date
filtered <- filtered[order(sapply(filtered, function(p) p$frontmatter$date %||% ""))]

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
    title = post$frontmatter$title,
    description = post$frontmatter$description,
    date = post$frontmatter$date,
    ported_from = post$frontmatter$ported_from,
    ported_categories = post$frontmatter$ported_categories
  )

  if (include_content) {
    result$content <- read_post_content(post)
  }

  result
})

# Summary to stderr
message(sprintf(
  "Showing %d of %d posts needing categories (offset: %d)",
  length(output), total, offset
))

if (!is.null(source_filter)) {
  message(sprintf("Filtered by source: %s", source_filter))
}

# Output simple format for review
message("\n=== Posts for review ===\n")
for (i in seq_along(output)) {
  p <- output[[i]]
  message(sprintf("%d. %s", i + offset, p$title))
  if (!is.null(p$description)) {
    desc <- gsub("\n", " ", p$description)
    if (nchar(desc) > 100) desc <- paste0(substr(desc, 1, 97), "...")
    message(sprintf("   %s", desc))
  }
  message(sprintf("   ported_categories: %s",
    paste(unlist(p$ported_categories), collapse = ", ")))
  message("")
}

message("=== Valid categories ===")
message(paste(valid_categories, collapse = ", "))
