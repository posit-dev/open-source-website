#!/usr/bin/env Rscript
# Extract metadata from all blog posts to JSON

library(rmarkdown)
library(jsonlite)

posts_dir <- "content/blog"
source_extensions <- c(".qmd", ".Rmd", ".Rmarkdown", ".ipynb")

# Find all index.md files in blog post directories
md_files <- list.files(

  posts_dir,
  pattern = "^index\\.(md|markdown)$",

  recursive = TRUE,
  full.names = TRUE
)

extract_metadata <- function(md_path) {
  frontmatter <- tryCatch(
    yaml_front_matter(md_path),
    error = function(e) NULL
  )

  if (is.null(frontmatter) || length(frontmatter) == 0) {
    return(NULL)
  }

  # Find source file if it exists
  dir_path <- dirname(md_path)
  source_path <- NULL

  for (ext in source_extensions) {
    candidate <- file.path(dir_path, paste0("index", ext))
    if (file.exists(candidate)) {
      source_path <- candidate
      break
    }
  }

  list(
    md_path = md_path,
    source_path = source_path,
    frontmatter = frontmatter
  )
}

posts <- lapply(md_files, extract_metadata)
posts <- Filter(Negate(is.null), posts)

json_output <- toJSON(posts, auto_unbox = TRUE, pretty = TRUE, null = "null")
cat(json_output)
