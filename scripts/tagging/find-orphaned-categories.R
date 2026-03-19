#!/usr/bin/env Rscript
# Find files with orphaned category list items in frontmatter
# These are lines like "- News" that aren't under a proper YAML key

files <- list.files("content/blog", pattern = "index\\.(md|Rmd|markdown)$",
                    recursive = TRUE, full.names = TRUE)

problems <- list()

for (f in files) {
  lines <- readLines(f, warn = FALSE)
  if (length(lines) == 0 || !grepl("^---", lines[1])) next

  # Find frontmatter end
  end_idx <- which(grepl("^---\\s*$", lines[-1]))[1] + 1
  if (is.na(end_idx)) next

  # Check for orphaned list items in frontmatter
  # These are lines starting with "- " where the previous non-list line
  # doesn't end with a colon (indicating a key)
  i <- 2
  while (i < end_idx) {
    line <- lines[i]

    # Check if this is a top-level list item (no leading whitespace)
    if (grepl("^- [A-Za-z]", line)) {
      # Look back to find the previous non-list line
      j <- i - 1
      while (j >= 2 && grepl("^\\s*-", lines[j])) {
        j <- j - 1
      }

      # If the previous non-list line doesn't end with ":" or is the start,
      # this is likely an orphaned item
      if (j < 2 || (!grepl(":\\s*$", lines[j]) && !grepl("^[a-z_]+:", lines[j]))) {
        problems[[length(problems) + 1]] <- list(
          file = f,
          line = i,
          content = line
        )
      }
    }
    i <- i + 1
  }
}

cat(sprintf("Found %d potential orphaned entries:\n\n", length(problems)))

for (p in problems) {
  cat(sprintf("%s:%d\n  %s\n", p$file, p$line, p$content))
}
