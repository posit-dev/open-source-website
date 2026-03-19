#!/usr/bin/env Rscript
# Write software and languages tags from posts.json back to source files
#
# Usage:
#   Rscript write-tags-to-files.R [--dry-run]
#
# This script:
# - Reads tags from content/blog/posts.json
# - Writes software/languages to both .md and source files (.qmd, .Rmd, etc.)
# - Overwrites existing software/languages fields
# - Preserves all other metadata and formatting

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)
dry_run <- "--dry-run" %in% args

posts_json <- "content/blog/posts.json"
if (!file.exists(posts_json)) {
  stop("posts.json not found. Run extract-blog-metadata.R first.")
}

posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Format a value as YAML
format_yaml_value <- function(value) {
  if (is.null(value) || length(value) == 0) {
    return(NULL)
  }

  values <- unlist(value)
  if (length(values) == 1) {
    # Single value - use inline format
    paste0("[", paste0('"', values, '"', collapse = ", "), "]")
  } else {
    # Multiple values - use inline array format for consistency
    paste0("[", paste0('"', values, '"', collapse = ", "), "]")
  }
}

# Remove existing software/languages lines from frontmatter
# Handles both inline arrays and multi-line arrays
remove_existing_tags <- function(lines, start_idx, end_idx) {
  result <- c()
  i <- start_idx

  while (i <= end_idx) {
    line <- lines[i]

    # Check if this is a software: or languages: line
    if (grepl("^(software|languages)\\s*:", line)) {
      # Check if it's an inline array (contains [ ])
      if (grepl("\\[.*\\]", line)) {
        # Skip this line (inline array)
        i <- i + 1
        next
      }

      # Check if next lines are array items (start with -)
      i <- i + 1
      while (i <= end_idx && grepl("^\\s*-", lines[i])) {
        i <- i + 1
      }
      next
    }

    result <- c(result, line)
    i <- i + 1
  }

  result
}

# Update a single file with new tags
update_file <- function(file_path, software, languages) {
  if (!file.exists(file_path)) {
    return(list(success = FALSE, reason = "file not found"))
  }

  lines <- readLines(file_path, warn = FALSE)

  if (length(lines) == 0) {
    return(list(success = FALSE, reason = "empty file"))
  }

  # Find frontmatter boundaries
  # First line should be ---
  if (!grepl("^---\\s*$", lines[1])) {
    return(list(success = FALSE, reason = "no frontmatter start"))
  }

  # Find closing ---
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

  # Extract and clean frontmatter (remove existing software/languages)
  frontmatter_lines <- remove_existing_tags(lines, 2, end_idx - 1)

  # Build new tag lines
  new_lines <- c()

  software_yaml <- format_yaml_value(software)
  if (!is.null(software_yaml)) {
    new_lines <- c(new_lines, paste0("software: ", software_yaml))
  }

  languages_yaml <- format_yaml_value(languages)
  if (!is.null(languages_yaml)) {
    new_lines <- c(new_lines, paste0("languages: ", languages_yaml))
  }

  # Reconstruct file
  new_content <- c(
    lines[1],  # opening ---
    frontmatter_lines,
    new_lines,
    lines[end_idx:length(lines)]  # closing --- and rest of file
  )

  if (dry_run) {
    return(list(success = TRUE, reason = "dry run", new_lines = new_lines))
  }

  writeLines(new_content, file_path)
  return(list(success = TRUE, reason = "updated"))
}

# Process all posts
updated <- 0
skipped <- 0
errors <- list()

for (post in posts) {
  fm <- post$frontmatter
  software <- fm$software
  languages <- fm$languages

  # Skip if no tags to write
  if ((is.null(software) || length(software) == 0) &&
      (is.null(languages) || length(languages) == 0)) {
    skipped <- skipped + 1
    next
  }

  # Update md_path
  if (!is.null(post$md_path)) {
    result <- update_file(post$md_path, software, languages)
    if (result$success) {
      updated <- updated + 1
      if (dry_run) {
        message(sprintf("Would update: %s", post$md_path))
        message(sprintf("  + %s", paste(result$new_lines, collapse = "\n  + ")))
      }
    } else {
      errors <- c(errors, list(paste(post$md_path, "-", result$reason)))
    }
  }

  # Update source_path if different from md_path
  if (!is.null(post$source_path) && post$source_path != post$md_path) {
    result <- update_file(post$source_path, software, languages)
    if (result$success) {
      updated <- updated + 1
      if (dry_run) {
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

message(sprintf("Skipped %d posts (no tags)", skipped))

if (length(errors) > 0) {
  message(sprintf("\n%d errors:", length(errors)))
  for (err in errors) {
    message(paste(" -", err))
  }
}
