#!/usr/bin/env Rscript
# Move ALL orphaned list items from frontmatter to ported_topics
# These are lines like "- News" or "- Shiny" that aren't under a proper YAML key
#
# Usage:
#   Rscript fix-orphaned-topics.R [--dry-run]

args <- commandArgs(trailingOnly = TRUE)
dry_run <- "--dry-run" %in% args

# Process both .md and source files (.qmd, .Rmd, etc.)
files <- list.files("content/blog", pattern = "index\\.(md|Rmd|qmd|markdown)$",
                    recursive = TRUE, full.names = TRUE)

fixed <- 0

for (f in files) {
  lines <- readLines(f, warn = FALSE)
  if (length(lines) == 0 || !grepl("^---", lines[1])) next

  # Find frontmatter end
  end_idx <- which(grepl("^---\\s*$", lines[-1]))[1] + 1
  if (is.na(end_idx)) next

  # Find orphaned items - top-level list items not following a key line
  to_remove <- c()
  orphans_found <- c()

  for (i in 2:(end_idx - 1)) {
    line <- lines[i]
    # Top-level list item that's just a simple value (no colon, so not "- name: value")
    # Must be "- SomeValue" not "- key: value"
    if (grepl("^- [A-Za-z]", line) && !grepl("^- [A-Za-z_]+:", line)) {
      # Check previous line - if it does not end with ":" and is not a list item, it's orphaned
      prev <- lines[i-1]
      if (!grepl(":\\s*$", prev) && !grepl("^\\s*-", prev)) {
        to_remove <- c(to_remove, i)
        val <- trimws(sub("^-\\s*", "", line))
        orphans_found <- c(orphans_found, val)
      }
    }
  }

  if (length(to_remove) > 0) {
    if (dry_run) {
      message(sprintf("Would fix: %s", f))
      message(sprintf("  Orphans found: %s", paste(orphans_found, collapse = ", ")))
    } else {
      # Find existing ported_topics or where to add them
      ported_idx <- NULL
      for (i in 2:(end_idx - 1)) {
        if (grepl("^ported_topics\\s*:", lines[i])) {
          ported_idx <- i
          break
        }
      }

      # Get existing ported_topics values
      existing_ported <- c()
      if (!is.null(ported_idx)) {
        # Check if inline array
        if (grepl("\\[.*\\]", lines[ported_idx])) {
          # Extract inline array values
          match <- regmatches(lines[ported_idx], regexpr("\\[.*\\]", lines[ported_idx]))
          if (length(match) > 0) {
            inner <- gsub("^\\[|\\]$", "", match)
            existing_ported <- trimws(strsplit(inner, ",")[[1]])
            existing_ported <- gsub("^['\"]|['\"]$", "", existing_ported)
          }
        } else {
          # Multi-line array - collect items
          j <- ported_idx + 1
          while (j < end_idx && grepl("^\\s+-", lines[j])) {
            val <- trimws(sub("^\\s*-\\s*", "", lines[j]))
            existing_ported <- c(existing_ported, val)
            j <- j + 1
          }
        }
      }

      # Add orphans that aren't already in ported_topics
      new_ported <- unique(c(existing_ported, orphans_found))

      # Remove orphaned lines first (in reverse order to preserve indices)
      lines <- lines[-to_remove]

      # Recalculate end_idx after removal
      end_idx <- which(grepl("^---\\s*$", lines[-1]))[1] + 1

      # Find ported_topics again after line removal
      ported_idx <- NULL
      ported_end_idx <- NULL
      for (i in 2:(end_idx - 1)) {
        if (grepl("^ported_topics\\s*:", lines[i])) {
          ported_idx <- i
          # Find end of ported_topics array
          if (grepl("\\[.*\\]", lines[i])) {
            ported_end_idx <- i
          } else {
            j <- i + 1
            while (j < end_idx && grepl("^\\s+-", lines[j])) {
              j <- j + 1
            }
            ported_end_idx <- j - 1
          }
          break
        }
      }

      if (!is.null(ported_idx)) {
        # Replace existing ported_topics with updated list
        new_ported_lines <- c("ported_topics:", paste0("  - ", new_ported))

        # Remove old ported_topics lines
        if (ported_end_idx >= ported_idx) {
          lines <- lines[-(ported_idx:ported_end_idx)]
          # Insert new lines at ported_idx position
          lines <- c(
            lines[1:(ported_idx - 1)],
            new_ported_lines,
            if (ported_idx <= length(lines)) lines[ported_idx:length(lines)] else c()
          )
        }
      } else {
        # Add new ported_topics before closing ---
        end_idx <- which(grepl("^---\\s*$", lines[-1]))[1] + 1
        new_ported_lines <- c("ported_topics:", paste0("  - ", new_ported))
        lines <- c(
          lines[1:(end_idx - 1)],
          new_ported_lines,
          lines[end_idx:length(lines)]
        )
      }

      writeLines(lines, f)
      message(sprintf("Fixed: %s (moved %s to ported_topics)", f, paste(orphans_found, collapse = ", ")))
    }
    fixed <- fixed + 1
  }
}

if (dry_run) {
  message(sprintf("\n[DRY RUN] Would fix %d files", fixed))
} else {
  message(sprintf("\nFixed %d files", fixed))
}
