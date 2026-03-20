#!/usr/bin/env Rscript
# Fix posts where image field references non-existent file
#
# Usage:
#   Rscript fix-missing-images.R [--dry-run]

library(jsonlite)
library(yaml)
library(rmarkdown)

args <- commandArgs(trailingOnly = TRUE)
dry_run <- "--dry-run" %in% args

posts <- fromJSON("posts.json", simplifyVector = FALSE)

# Find the best image file in a directory
find_image_file <- function(dir_path, current_image) {
  files <- list.files(dir_path, pattern = "\\.(jpg|jpeg|png|gif|webp)$", ignore.case = TRUE)

  if (length(files) == 0) return(NULL)

  # Priority 1: Look for -wd variant (wide format, preferred for thumbnails)
  wd_files <- files[grepl("-wd\\.", files)]
  if (length(wd_files) > 0) {
    return(wd_files[1])
  }

  # Priority 2: Look for thumbnail with different extension
  current_base <- tools::file_path_sans_ext(current_image)
  for (ext in c(".jpg", ".jpeg", ".png", ".gif", ".webp")) {
    candidate <- paste0(current_base, ext)
    if (candidate %in% files) {
      return(candidate)
    }
  }

  # Priority 3: Look for thumb-wd
  thumb_files <- files[grepl("thumb-wd\\.", files)]
  if (length(thumb_files) > 0) {
    return(thumb_files[1])
  }

  # Priority 4: Any file with "thumbnail" in name
  thumb_files <- files[grepl("thumbnail", files, ignore.case = TRUE)]
  if (length(thumb_files) > 0) {
    return(thumb_files[1])
  }

  # Priority 5: First image file alphabetically
  return(files[1])
}

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

  list(lines = lines, yaml_end = end_line)
}

# Fields that should always be arrays
array_fields <- c("people", "categories", "tags", "software", "languages",
                  "ported_categories", "blogcategories", "author", "events", "resources")

ensure_arrays <- function(fm) {
  for (field in array_fields) {
    if (!is.null(fm[[field]]) && !is.list(fm[[field]])) {
      fm[[field]] <- as.list(fm[[field]])
    }
  }
  fm
}

# Update a single file with new image
update_file <- function(file_path, new_image) {
  if (!file.exists(file_path)) {
    return(list(success = FALSE, reason = "file not found"))
  }

  fm <- tryCatch(
    rmarkdown::yaml_front_matter(file_path),
    error = function(e) NULL
  )

  if (is.null(fm)) {
    return(list(success = FALSE, reason = "could not parse frontmatter"))
  }

  file_info <- get_frontmatter_lines(file_path)
  if (is.null(file_info)) {
    return(list(success = FALSE, reason = "could not read file structure"))
  }

  old_image <- fm$image
  fm$image <- new_image

  if (dry_run) {
    return(list(success = TRUE, reason = "dry run", old = old_image, new = new_image))
  }

  fm <- ensure_arrays(fm)

  new_yaml <- yaml::as.yaml(fm, indent.mapping.sequence = TRUE)
  new_yaml <- sub("\n$", "", new_yaml)

  # Convert software and languages to compact inline notation
  for (field in c("software", "languages")) {
    if (!is.null(fm[[field]])) {
      values <- unlist(fm[[field]])
      inline <- paste0(field, ': ["', paste(values, collapse = '", "'), '"]')
      pattern <- paste0(field, ":\n(\\s+-[^\n]+\n?)+")
      new_yaml <- sub(pattern, paste0(inline, "\n"), new_yaml)
    }
  }

  body <- if (file_info$yaml_end < length(file_info$lines)) {
    file_info$lines[(file_info$yaml_end + 1):length(file_info$lines)]
  } else {
    character(0)
  }

  new_content <- c("---", strsplit(new_yaml, "\n")[[1]], "---", body)
  writeLines(new_content, file_path)

  return(list(success = TRUE, reason = "updated", old = old_image, new = new_image))
}

# Process posts
fixed <- 0
skipped <- 0
unfixable <- list()

for (p in posts) {
  img <- p$frontmatter$image
  if (is.null(img) || length(img) == 0 || nchar(img) == 0) next

  # Skip external URLs
  if (grepl("^https?://", img)) next

  dir_path <- dirname(p$md_path)
  img_path <- file.path(dir_path, img)

  # Skip if image exists
  if (file.exists(img_path)) next

  # Find replacement
  new_image <- find_image_file(dir_path, img)

  if (is.null(new_image)) {
    unfixable <- c(unfixable, list(list(post = p$md_path, image = img)))
    next
  }

  # Update md_path
  result <- update_file(p$md_path, new_image)
  if (result$success) {
    fixed <- fixed + 1
    if (dry_run) {
      message(sprintf("Would fix: %s", basename(dirname(p$md_path))))
      message(sprintf("  %s -> %s", result$old, result$new))
    } else {
      message(sprintf("Fixed: %s (%s -> %s)", basename(dirname(p$md_path)), result$old, result$new))
    }
  }

  # Update source_path if different
  if (!is.null(p$source_path) && p$source_path != p$md_path) {
    update_file(p$source_path, new_image)
  }
}

# Report
if (dry_run) {
  message(sprintf("\n[DRY RUN] Would fix %d posts", fixed))
} else {
  message(sprintf("\nFixed %d posts", fixed))
}

if (length(unfixable) > 0) {
  message(sprintf("\n%d posts could not be fixed (no suitable image found):", length(unfixable)))
  for (u in unfixable) {
    message(sprintf("  %s (looking for: %s)", basename(dirname(u$post)), u$image))
  }
}
