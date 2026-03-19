#!/usr/bin/env Rscript
# Write categories and ported_categories from posts.json back to source files
#
# Usage:
#   Rscript write-categories-to-files.R [--dry-run]
#
# This script:
# - Reads categories/ported_categories from content/blog/posts.json
# - Writes to both .md and source files (.qmd, .Rmd, etc.)
# - Replaces existing categories with new taxonomy
# - Adds ported_categories (only if not already present)
# - Preserves all other metadata and formatting

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)
dry_run <- "--dry-run" %in% args

posts_json <- "content/blog/posts.json"
if (!file.exists(posts_json)) {
  stop("posts.json not found. Run extract-blog-metadata.R first.")
}

posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Valid categories for the new taxonomy
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

# Format a value as YAML array
format_yaml_array <- function(value) {
  if (is.null(value) || length(value) == 0) {
    return(NULL)
  }
  values <- unlist(value)
  if (length(values) == 0) return(NULL)

  # Use multi-line format for readability
  lines <- paste0("  - ", values)
  lines
}

# Check if a line starts a YAML array field
is_yaml_field <- function(line, field_name) {
  grepl(paste0("^", field_name, "\\s*:"), line)
}

# Remove existing field from frontmatter (handles inline and multi-line arrays)
remove_field <- function(lines, start_idx, end_idx, field_name) {
  result <- c()
  i <- start_idx

  while (i <= end_idx) {
    line <- lines[i]

    if (is_yaml_field(line, field_name)) {
      # Check if it's an inline array or null
      if (grepl("\\[.*\\]", line) || grepl(":\\s*$", line) || grepl(":\\s*null\\s*$", line)) {
        # Inline array or empty - skip just this line
        if (!grepl(":\\s*$", line)) {
          i <- i + 1
          next
        }
      }

      # Skip array items that follow
      i <- i + 1
      while (i <= end_idx && grepl("^\\s+-", lines[i])) {
        i <- i + 1
      }
      next
    }

    result <- c(result, line)
    i <- i + 1
  }

  result
}

# Check if field exists in frontmatter
field_exists <- function(lines, start_idx, end_idx, field_name) {
  for (i in start_idx:end_idx) {
    if (is_yaml_field(lines[i], field_name)) {
      return(TRUE)
    }
  }
  FALSE
}

# Update a single file
update_file <- function(file_path, categories, ported_categories) {
  if (!file.exists(file_path)) {
    return(list(success = FALSE, reason = "file not found"))
  }

  lines <- readLines(file_path, warn = FALSE)

  if (length(lines) == 0) {
    return(list(success = FALSE, reason = "empty file"))
  }

  # Find frontmatter boundaries
  if (!grepl("^---\\s*$", lines[1])) {
    return(list(success = FALSE, reason = "no frontmatter start"))
  }

  end_idx <- NULL
  for (i in 2:length(lines)) {
    if (grepl("^---\\s*$", lines[i])) {
      end_idx <- i
      break
    }
  }

  if (is.null(end_idx)) {
    return(list(success = FALSE, reason = "no frontmatter end"))
  }

  # Check if ported_categories already exists
  has_ported <- field_exists(lines, 2, end_idx - 1, "ported_categories")

  # Remove existing categories field
  frontmatter_lines <- remove_field(lines, 2, end_idx - 1, "categories")

  # Build new lines to add
  new_lines <- c()
  changes <- c()

  # Add categories
  cat_yaml <- format_yaml_array(categories)
  if (!is.null(cat_yaml)) {
    new_lines <- c(new_lines, "categories:", cat_yaml)
    changes <- c(changes, paste("categories:", paste(unlist(categories), collapse = ", ")))
  }

  # Add ported_categories only if not already present
  if (!has_ported && !is.null(ported_categories) && length(ported_categories) > 0) {
    ported_yaml <- format_yaml_array(ported_categories)
    if (!is.null(ported_yaml)) {
      new_lines <- c(new_lines, "ported_categories:", ported_yaml)
      changes <- c(changes, "ported_categories: (added)")
    }
  }

  # Reconstruct file
  new_content <- c(
    lines[1],  # opening ---
    frontmatter_lines,
    new_lines,
    lines[end_idx:length(lines)]  # closing --- and rest of file
  )

  if (dry_run) {
    return(list(success = TRUE, reason = "dry run", changes = changes))
  }

  writeLines(new_content, file_path)
  return(list(success = TRUE, reason = "updated", changes = changes))
}

# Process all posts
updated <- 0
skipped <- 0
errors <- list()

for (post in posts) {
  fm <- post$frontmatter
  categories <- fm$categories
  ported_categories <- fm$ported_categories

  # Skip drafts
  if (isTRUE(fm$draft)) {
    skipped <- skipped + 1
    next
  }

  # Skip if no categories
  if (is.null(categories) || length(categories) == 0) {
    skipped <- skipped + 1
    next
  }

  # Update md_path
  if (!is.null(post$md_path)) {
    result <- update_file(post$md_path, categories, ported_categories)
    if (result$success) {
      updated <- updated + 1
      if (dry_run && length(result$changes) > 0) {
        message(sprintf("Would update: %s", post$md_path))
        for (ch in result$changes) {
          message(sprintf("  + %s", ch))
        }
      }
    } else {
      errors <- c(errors, list(paste(post$md_path, "-", result$reason)))
    }
  }

  # Update source_path if different from md_path
  if (!is.null(post$source_path) && post$source_path != post$md_path) {
    result <- update_file(post$source_path, categories, ported_categories)
    if (result$success) {
      updated <- updated + 1
      if (dry_run && length(result$changes) > 0) {
        message(sprintf("Would update: %s", post$source_path))
      }
    } else {
      errors <- c(errors, list(paste(post$source_path, "-", result$reason)))
    }
  }
}

# Report
if (dry_run) {
  message(sprintf("\n[DRY RUN] Would update %d files", updated))
} else {
  message(sprintf("Updated %d files", updated))
}

message(sprintf("Skipped %d posts (drafts or no categories)", skipped))

if (length(errors) > 0) {
  message(sprintf("\n%d errors:", length(errors)))
  for (err in errors) {
    message(paste(" -", err))
  }
}
