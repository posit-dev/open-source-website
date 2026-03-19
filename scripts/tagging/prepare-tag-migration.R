#!/usr/bin/env Rscript
# Prepare tag migration:
# 1. Add ported_from to tags if not already there
# 2. Add non-redundant ported_categories as tags (normalized)
# 3. Remove tags that duplicate software/languages (except if they match ported_from)
# 4. Apply sentence case to all tags

library(jsonlite)

posts <- fromJSON("posts.json", simplifyVector = FALSE)

# Sentence case: capitalize first letter, lowercase rest
sentence_case <- function(x) {
  paste0(toupper(substr(x, 1, 1)), tolower(substr(x, 2, nchar(x))))
}

# Normalization mapping for ported_categories (before split/sentence case)
# Note: tags with "/" will be split later, so don't consolidate those here
normalize_ported_cat <- function(pc) {
  mapping <- list(
    # Typo fix
    "Generenative Models" = "Generative models",

    # Consolidate package variants (but not Packages/Releases - that will split)
    "package" = "Packages",
    "packages" = "Packages",
    "R package" = "Packages",

    # Consolidate R Markdown variants
    "r-markdown" = "R markdown",
    "R Markdown" = "R markdown",
    "rmarkdown" = "R markdown",

    # Consolidate talk variants
    "Talk" = "Talks",

    # Consolidate teach variants
    "teach" = "Teaching",
    "teaching" = "Teaching",

    # Skip these
    "other" = NULL
  )
  if (pc %in% names(mapping)) {
    return(mapping[[pc]])
  }
  pc
}

# Final tag normalization (applied after all tags collected)
normalize_final_tag <- function(tag) {
  tag_lower <- tolower(tag)

  # Explicit mappings for consolidation
  mapping <- list(
    # Package variants
    "package" = "Packages",
    "packages" = "Packages",

    # Teach variants
    "teach" = "Teaching",
    "teaching" = "Teaching",

    # R Markdown variants (preserve R capitalization)
    "r markdown" = "R Markdown",
    "rmarkdown" = "R Markdown",
    "markdown" = "Markdown",

    # RStudio variants
    "rstudio" = "RStudio",
    "rstudio-cloud" = "RStudio Cloud",
    "rstudio cloud" = "RStudio Cloud",
    "rstudio connect" = "RStudio Connect",
    "rstudio ide" = "RStudio IDE",
    "rstudio::conf" = "rstudio::conf",

    # TensorFlow
    "tensorflow" = "TensorFlow",

    # tidyverse (lowercase)
    "tidyverse" = "tidyverse",

    # AI (acronym)
    "ai" = "AI",

    # rlib (lowercase)
    "r-lib" = "rlib",

    # BI tools (acronym)
    "bi tools" = "BI tools",

    # LLM (acronym)
    "llm" = "LLM",

    # DL -> Deep learning
    "dl" = "Deep learning",

    # ML -> Machine learning
    "ml" = "Machine learning",

    # great_tables -> Great Tables
    "great_tables" = "Great Tables",

    # News
    "news" = "News",

    # Shiny
    "shiny" = "Shiny",

    # Deep learning
    "deep learning" = "Deep learning",

    # Data visualization
    "data visualization" = "Data visualization",

    # Python
    "python" = "Python",

    # Pins
    "pins" = "Pins",

    # Education
    "education" = "Education"
  )

  if (tag_lower %in% names(mapping)) {
    return(mapping[[tag_lower]])
  }

  # Default: apply sentence case
  sentence_case(tag)
}

# Get reference lists for redundancy checks
all_software <- unique(tolower(unlist(lapply(posts, function(p) p$frontmatter$software))))
all_languages <- unique(tolower(unlist(lapply(posts, function(p) p$frontmatter$languages))))
all_categories <- unique(tolower(unlist(lapply(posts, function(p) p$frontmatter$categories))))

# ported_categories that are redundant with categories/software/languages
is_redundant_ported_cat <- function(pc) {
  pc_lower <- tolower(pc)
  pc_lower %in% all_software || pc_lower %in% all_languages || pc_lower %in% all_categories
}

# Process each post
for (i in seq_along(posts)) {
  p <- posts[[i]]

  # Start with existing tags (or empty)
  tags <- p$frontmatter$tags
  if (is.null(tags)) tags <- character(0)
  tags <- unique(as.character(tags))

  # Get software/languages for this post (for removal check)
  post_software <- tolower(as.character(p$frontmatter$software %||% character(0)))
  post_languages <- tolower(as.character(p$frontmatter$languages %||% character(0)))

  # Get ported_from
  ported_from <- p$frontmatter$ported_from

  # 1. Add ported_from to tags if not already there
  if (!is.null(ported_from) && length(ported_from) > 0) {
    if (!tolower(ported_from) %in% tolower(tags)) {
      tags <- c(tags, ported_from)
    }
  }

  # 2. Add non-redundant ported_categories (normalized)
  ported_cats <- p$frontmatter$ported_categories
  if (!is.null(ported_cats)) {
    for (pc in ported_cats) {
      normalized <- normalize_ported_cat(pc)
      if (!is.null(normalized) && !is_redundant_ported_cat(normalized)) {
        if (!tolower(normalized) %in% tolower(tags)) {
          tags <- c(tags, normalized)
        }
      }
    }
  }

  # 3. Remove tags that match software/languages (unless they match ported_from)
  ported_from_lower <- if (!is.null(ported_from)) tolower(ported_from) else ""

  keep_tag <- function(tag) {
    tag_lower <- tolower(tag)
    # Keep if it matches ported_from
    if (tag_lower == ported_from_lower) return(TRUE)
    # Remove if it matches this post's software or languages
    if (tag_lower %in% post_software) return(FALSE)
    if (tag_lower %in% post_languages) return(FALSE)
    TRUE
  }

  tags <- tags[sapply(tags, keep_tag)]

  # 4. Split tags with "/" or "&" into separate tags
  # Special case handling first
  expand_special_cases <- function(t) {
    t_lower <- tolower(t)
    if (t_lower == "probabilistic ml/dl") {
      return(c("Probabilistic machine learning", "Probabilistic deep learning"))
    }
    if (t_lower == "image recognition & image processing") {
      return(c("Image recognition", "Image processing"))
    }
    t
  }

  tags <- unlist(lapply(tags, expand_special_cases))

  # General splitting on "/" and "&"
  split_tags <- unlist(lapply(tags, function(t) {
    if (grepl("/", t)) {
      trimws(unlist(strsplit(t, "/")))
    } else if (grepl(" & ", t)) {
      trimws(unlist(strsplit(t, " & ")))
    } else {
      t
    }
  }))
  tags <- unique(split_tags)

  # 5. Apply final normalization (sentence case + consolidation)
  tags <- unique(sapply(tags, normalize_final_tag))

  # Update the post
  if (length(tags) > 0) {
    posts[[i]]$frontmatter$tags <- as.list(tags)
  } else {
    posts[[i]]$frontmatter$tags <- NULL
  }
}

# Write updated posts.json
json_output <- toJSON(posts, auto_unbox = TRUE, pretty = TRUE, null = "null")
writeLines(json_output, "posts.json")

cat("Migration prepared. Updated posts.json\n")

# Summary stats
tags_after <- unlist(lapply(posts, function(p) p$frontmatter$tags))
cat("\nUnique tags after migration:", length(unique(tags_after)), "\n")
cat("\nTop 30 tags:\n")
print(head(sort(table(tags_after), decreasing = TRUE), 30))
