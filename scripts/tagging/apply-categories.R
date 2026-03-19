#!/usr/bin/env Rscript
# Apply category assignments to posts.json
#
# Usage:
#   Rscript apply-categories.R assignments.json
#   cat assignments.json | Rscript apply-categories.R -
#
# Input format (JSON array):
#   [
#     {
#       "title": "Post Title",
#       "categories": ["Data Wrangling", "Visualization"]
#     },
#     ...
#   ]
#
# Valid categories:
#   Machine Learning, Artificial Intelligence, Visualization,
#   Interactive Apps, Publishing, MLOps & Admin, Data Wrangling,
#   Best Practices, Community

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 1) {
  stop("Usage: Rscript apply-categories.R <assignments.json | ->")
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

# Read assignments
if (args[1] == "-") {
  input_text <- paste(readLines(file("stdin")), collapse = "\n")
  assignments <- fromJSON(input_text, simplifyVector = FALSE)
} else {
  if (!file.exists(args[1])) {
    stop(paste("File not found:", args[1]))
  }
  assignments <- fromJSON(args[1], simplifyVector = FALSE)
}

# Read current posts.json
posts_json <- "content/blog/posts.json"
if (!file.exists(posts_json)) {
  stop("posts.json not found. Run extract-blog-metadata.R first.")
}

posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Build lookup by title
posts_by_title <- new.env(hash = TRUE)
for (i in seq_along(posts)) {
  posts_by_title[[posts[[i]]$frontmatter$title]] <- i
}

# Track updates and errors
updated <- 0
errors <- list()

for (a in assignments) {
  title <- a$title

  if (is.null(title)) {
    errors <- c(errors, list("Assignment missing title"))
    next
  }

  idx <- posts_by_title[[title]]
  if (is.null(idx)) {
    errors <- c(errors, list(paste("Post not found:", title)))
    next
  }

  # Validate categories
  cats <- if (is.list(a$categories)) unlist(a$categories) else a$categories
  if (length(cats) == 0) {
    errors <- c(errors, list(paste("No categories for:", title)))
    next
  }

  invalid <- setdiff(cats, valid_categories)
  if (length(invalid) > 0) {
    errors <- c(errors, list(paste(
      "Invalid categories for", title, ":",
      paste(invalid, collapse = ", ")
    )))
    next
  }

  posts[[idx]]$frontmatter$categories <- as.list(cats)
  updated <- updated + 1
}

# Write updated posts.json
json_output <- toJSON(posts, auto_unbox = TRUE, pretty = TRUE, null = "null")
writeLines(json_output, posts_json)

# Report to stderr
message(sprintf("Applied categories to %d posts in %s", updated, posts_json))

if (length(errors) > 0) {
  message(sprintf("\n%d errors:", length(errors)))
  for (err in errors) {
    message(paste(" -", err))
  }
}
