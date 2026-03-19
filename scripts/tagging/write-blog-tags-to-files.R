#!/usr/bin/env Rscript
# Write tags from posts.json back to source files
#
# Usage:
#   Rscript write-blog-tags-to-files.R [--dry-run]
#
# Uses rmarkdown::yaml_front_matter() for proper YAML parsing.
# Note: This rewrites frontmatter which may change formatting (dates, descriptions).

library(jsonlite)
library(yaml)
library(rmarkdown)

args <- commandArgs(trailingOnly = TRUE)
dry_run <- "--dry-run" %in% args

posts_json <- "posts.json"
if (!file.exists(posts_json)) {
  stop("posts.json not found. Run prepare-tag-migration.R first.")
}

posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Get frontmatter boundaries from file
get_frontmatter_lines <- function(file_path) {
  lines <- readLines(file_path, warn = FALSE)
  if (length(lines) == 0 || !grepl("^---\\s*$", lines[1])) {
    return(NULL)
  }

  end_line <- NULL
  for (i in 2:length(lines)) {
    if (grepl("^---\\s*$", lines[i])) {
      end_line <- i
      break
    }
  }

  list(
    lines = lines,
    yaml_end = end_line
  )
}

# Fields that should always be arrays (never collapsed to scalars)
array_fields <- c("people", "categories", "tags", "software", "languages",
                  "ported_categories", "blogcategories", "author", "events", "resources")

# Ensure specified fields remain as lists for yaml output
ensure_arrays <- function(fm) {
  for (field in array_fields) {
    if (!is.null(fm[[field]]) && !is.list(fm[[field]])) {
      fm[[field]] <- as.list(fm[[field]])
    }
  }
  fm
}

# Update a single file
update_file <- function(file_path, new_tags) {
  if (!file.exists(file_path)) {
    return(list(success = FALSE, reason = "file not found"))
  }

  # Use rmarkdown to properly parse the frontmatter
  fm <- tryCatch(
    rmarkdown::yaml_front_matter(file_path),
    error = function(e) NULL
  )

  if (is.null(fm)) {
    return(list(success = FALSE, reason = "could not parse frontmatter"))
  }

  # Get file structure
  file_info <- get_frontmatter_lines(file_path)
  if (is.null(file_info)) {
    return(list(success = FALSE, reason = "could not read file structure"))
  }

  # Check if tags changed
  old_tags <- sort(unlist(fm$tags))
  new_tags_sorted <- sort(unlist(new_tags))

  if (identical(old_tags, new_tags_sorted)) {
    return(list(success = TRUE, reason = "no changes needed", changes = c()))
  }

  changes <- c()

  # Update tags
  if (!is.null(new_tags) && length(new_tags) > 0) {
    fm$tags <- as.list(unlist(new_tags))
    changes <- c(changes, paste("tags:", paste(unlist(new_tags), collapse = ", ")))
  } else {
    # Remove tags if empty
    fm$tags <- NULL
    changes <- c(changes, "tags: (removed)")
  }

  if (dry_run) {
    return(list(success = TRUE, reason = "dry run", changes = changes))
  }

  # Ensure array fields stay as arrays
  fm <- ensure_arrays(fm)

  # Convert back to YAML
  new_yaml <- yaml::as.yaml(fm, indent.mapping.sequence = TRUE)
  new_yaml <- sub("\n$", "", new_yaml)  # Remove trailing newline

  # Convert software and languages to compact inline notation
  for (field in c("software", "languages")) {
    if (!is.null(fm[[field]])) {
      values <- unlist(fm[[field]])
      inline <- paste0(field, ': ["', paste(values, collapse = '", "'), '"]')
      pattern <- paste0(field, ":\n(\\s+-[^\n]+\n?)+")
      new_yaml <- sub(pattern, paste0(inline, "\n"), new_yaml)
    }
  }

  # Rebuild file
  body <- if (file_info$yaml_end < length(file_info$lines)) {
    file_info$lines[(file_info$yaml_end + 1):length(file_info$lines)]
  } else {
    character(0)
  }

  new_content <- c(
    "---",
    strsplit(new_yaml, "\n")[[1]],
    "---",
    body
  )

  writeLines(new_content, file_path)
  return(list(success = TRUE, reason = "updated", changes = changes))
}

# Process all posts
updated <- 0
skipped <- 0
errors <- list()

for (post in posts) {
  fm <- post$frontmatter
  tags <- fm$tags

  # Update md_path
  if (!is.null(post$md_path)) {
    result <- update_file(post$md_path, tags)
    if (result$success && result$reason == "updated") {
      updated <- updated + 1
    } else if (result$success && result$reason == "no changes needed") {
      skipped <- skipped + 1
    } else if (!result$success) {
      errors <- c(errors, list(paste(post$md_path, "-", result$reason)))
    }
    if (dry_run && length(result$changes) > 0) {
      message(sprintf("Would update: %s", post$md_path))
      for (ch in result$changes) {
        message(sprintf("  + %s", ch))
      }
    }
  }

  # Update source_path if different from md_path
  if (!is.null(post$source_path) && post$source_path != post$md_path) {
    result <- update_file(post$source_path, tags)
    if (result$success && result$reason == "updated") {
      updated <- updated + 1
    } else if (!result$success) {
      errors <- c(errors, list(paste(post$source_path, "-", result$reason)))
    }
    if (dry_run && length(result$changes) > 0) {
      message(sprintf("Would update: %s", post$source_path))
    }
  }
}

# Report
if (dry_run) {
  message(sprintf("\n[DRY RUN] Would update %d files", updated))
} else {
  message(sprintf("\nUpdated %d files", updated))
}

message(sprintf("Skipped %d posts (no changes needed)", skipped))

if (length(errors) > 0) {
  message(sprintf("\n%d errors:", length(errors)))
  for (err in errors) {
    message(paste(" -", err))
  }
}
