#!/usr/bin/env Rscript
# Find ALL orphaned list items in frontmatter (not just known values)

files <- list.files("content/blog", pattern = "index\\.(md|Rmd|qmd|markdown)$",
                    recursive = TRUE, full.names = TRUE)

for (f in files) {
  lines <- readLines(f, warn = FALSE)
  if (length(lines) == 0 || !grepl("^---", lines[1])) next

  end_idx <- which(grepl("^---\\s*$", lines[-1]))[1] + 1
  if (is.na(end_idx)) next

  for (i in 2:(end_idx - 1)) {
    line <- lines[i]
    # Top-level list item (no leading whitespace, starts with "- ")
    if (grepl("^- [A-Za-z]", line)) {
      # Check previous line - if it does not end with ":" it's orphaned
      prev <- lines[i-1]
      if (!grepl(":\\s*$", prev) && !grepl("^\\s*-", prev)) {
        cat(sprintf("%s:%d: %s\n", f, i, line))
      }
    }
  }
}
