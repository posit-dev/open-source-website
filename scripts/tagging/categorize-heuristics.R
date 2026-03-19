#!/usr/bin/env Rscript
# Apply heuristic category assignments based on ported_from and ported_categories
#
# Posts can have MULTIPLE categories assigned.
#
# Usage:
#   Rscript categorize-heuristics.R [--apply]
#
# Without --apply, outputs summary and flagged posts
# With --apply, updates posts.json directly

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)
apply_changes <- "--apply" %in% args

posts_json <- "content/blog/posts.json"
posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Target categories
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

# ported_from → categories (can be multiple)
source_mappings <- list(
  shiny = c("Interactive Apps"),
  quarto = c("Publishing"),
  great_tables = c("Visualization"),
  plotnine = c("Visualization"),
  pointblank = c("Data Wrangling")
  # ai, education, rstudio, tidyverse → need ported_categories or content review
)

# ported_categories → categories (can be multiple)
# Using lowercase keys for case-insensitive matching
category_mappings <- list(
  # ML/AI - some topics span both

  "tensorflow/keras" = c("Machine Learning"),
  "torch" = c("Machine Learning"),
  "image recognition & image processing" = c("Machine Learning"),
  "natural language processing" = c("Machine Learning"),
  "generative models" = c("Machine Learning"),
  "llm" = c("Artificial Intelligence"),
  "probabilistic ml/dl" = c("Machine Learning"),
  "time series" = c("Machine Learning"),
  "tabular data" = c("Machine Learning"),
  "distributed computing" = c("MLOps & Admin"),
  "training" = c("MLOps & Admin"),

  # Interactive
  "shiny" = c("Interactive Apps"),

  # Publishing
  "r markdown" = c("Publishing"),
  "authoring" = c("Publishing"),

  # Data
  "tidyverse" = c("Data Wrangling"),

  # Community/Education
  "learn" = c("Community"),
  "teach" = c("Community"),
  "certify" = c("Community"),

  # Best Practices
  "concepts" = c("Best Practices"),
  "deep-dive" = c("Best Practices"),
  "programming" = c("Best Practices")
)

# Categories that don't map to topics (need content review)
non_topic_categories <- c(
  "package", "packages", "packages/releases", "r",
  "news", "other", "roundup", "meta", "features"
)

assign_categories <- function(post) {
  fm <- post$frontmatter
  ported_from <- fm$ported_from
  ported_cats <- tolower(unlist(fm$ported_categories))

  categories <- c()
  reasons <- c()

  # 1. Check ported_from
  if (!is.null(ported_from) && ported_from %in% names(source_mappings)) {
    categories <- c(categories, source_mappings[[ported_from]])
    reasons <- c(reasons, paste0("ported_from: ", ported_from))
  }

  # 2. Check ALL ported_categories (collect all matches)
  for (cat in ported_cats) {
    if (cat %in% names(category_mappings)) {
      categories <- c(categories, category_mappings[[cat]])
      reasons <- c(reasons, paste0("ported_category: ", cat))
    }
  }

  # Deduplicate
  categories <- unique(categories)
  reasons <- unique(reasons)

  # Determine confidence
  if (length(categories) > 0) {
    # High if from ported_from, medium if only from ported_categories
    if (!is.null(ported_from) && ported_from %in% names(source_mappings)) {
      confidence <- "high"
    } else {
      confidence <- "medium"
    }
  } else {
    # No matches - needs review
    confidence <- "needs_review"
    if (length(ported_cats) > 0) {
      topic_cats <- setdiff(ported_cats, non_topic_categories)
      if (length(topic_cats) == 0) {
        reasons <- "only non-topic categories"
      } else {
        reasons <- paste0("unmapped: ", paste(topic_cats, collapse = ", "))
      }
    } else {
      reasons <- "no ported_categories"
    }
  }

  list(
    categories = categories,
    confidence = confidence,
    reasons = paste(reasons, collapse = "; ")
  )
}

# Process all posts
results <- list()
for (i in seq_along(posts)) {
  post <- posts[[i]]
  fm <- post$frontmatter

  # Skip drafts
  if (isTRUE(fm$draft)) next

  # Skip if already has category assigned
  if (length(fm$categories) > 0) next

  assignment <- assign_categories(post)

  results[[length(results) + 1]] <- list(
    idx = i,
    md_path = post$md_path,
    title = fm$title,
    ported_from = fm$ported_from,
    ported_categories = fm$ported_categories,
    assigned_categories = assignment$categories,
    confidence = assignment$confidence,
    reasons = assignment$reasons
  )
}

# Summary
high_conf <- Filter(function(r) r$confidence == "high", results)
med_conf <- Filter(function(r) r$confidence == "medium", results)
needs_review <- Filter(function(r) r$confidence == "needs_review", results)

message(sprintf("\n=== Category Assignment Summary ==="))
message(sprintf("High confidence:   %d posts", length(high_conf)))
message(sprintf("Medium confidence: %d posts", length(med_conf)))
message(sprintf("Needs review:      %d posts", length(needs_review)))
message(sprintf("Total processed:   %d posts\n", length(results)))

# Show breakdown by assigned category (counting each category assignment)
assigned <- Filter(function(r) length(r$assigned_categories) > 0, results)
if (length(assigned) > 0) {
  all_cats <- unlist(lapply(assigned, function(r) r$assigned_categories))
  message("=== Category Assignments (posts may have multiple) ===")
  print(sort(table(all_cats), decreasing = TRUE))

  # Show distribution of category counts per post
  cat_counts <- sapply(assigned, function(r) length(r$assigned_categories))
  message("\n=== Categories per post ===")
  print(table(cat_counts))
}

if (apply_changes) {
  # Apply high and medium confidence assignments
  applied <- 0
  for (r in c(high_conf, med_conf)) {
    if (length(r$assigned_categories) > 0) {
      posts[[r$idx]]$frontmatter$categories <- as.list(r$assigned_categories)
      applied <- applied + 1
    }
  }

  json_output <- toJSON(posts, auto_unbox = TRUE, pretty = TRUE, null = "null")
  writeLines(json_output, posts_json)
  message(sprintf("\nApplied categories to %d posts in %s", applied, posts_json))
} else {
  # Show some examples of multi-category assignments
  multi_cat <- Filter(function(r) length(r$assigned_categories) > 1, assigned)
  if (length(multi_cat) > 0) {
    message("\n=== Multi-category examples (first 10) ===")
    for (r in head(multi_cat, 10)) {
      message(sprintf("- %s", r$title))
      message(sprintf("  → %s", paste(r$assigned_categories, collapse = ", ")))
    }
  }

  message("\n=== Posts Needing Review (first 20) ===")
  for (r in head(needs_review, 20)) {
    message(sprintf("- %s", r$title))
    message(sprintf("  ported_from: %s, reason: %s", r$ported_from, r$reasons))
  }

  message(sprintf("\nRun with --apply to assign %d posts (high + medium confidence)",
    length(high_conf) + length(med_conf)))
}
