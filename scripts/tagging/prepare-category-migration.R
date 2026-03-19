#!/usr/bin/env Rscript
# Prepare posts.json for category migration
#
# - Copies original `categories` to `ported_categories` (preserving originals)
# - Sets `categories` to empty array (to be assigned from new taxonomy)
#
# Usage:
#   Rscript prepare-category-migration.R

library(jsonlite)

posts_json <- "content/blog/posts.json"
posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Target categories (for reference/validation later)
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

migrated <- 0
already_migrated <- 0

for (i in seq_along(posts)) {
 fm <- posts[[i]]$frontmatter

 # Skip if already migrated (has ported_categories)
 if (!is.null(fm$ported_categories)) {
   already_migrated <- already_migrated + 1
   next
 }

 # Copy original categories to ported_categories
 if (!is.null(fm$categories) && length(fm$categories) > 0) {
   posts[[i]]$frontmatter$ported_categories <- fm$categories
 } else {
   posts[[i]]$frontmatter$ported_categories <- list()
 }

 # Reset categories to empty
 posts[[i]]$frontmatter$categories <- list()

 migrated <- migrated + 1
}

# Write updated posts.json
json_output <- toJSON(posts, auto_unbox = TRUE, pretty = TRUE, null = "null")
writeLines(json_output, posts_json)

message(sprintf("Prepared %d posts for category migration", migrated))
message(sprintf("Skipped %d posts (already migrated)", already_migrated))
message(sprintf("Total posts: %d", length(posts)))
