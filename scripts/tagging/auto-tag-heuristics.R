#!/usr/bin/env Rscript
# Apply heuristic tags based on ported_from and existing tags/categories
#
# Usage:
#   Rscript auto-tag-heuristics.R [--apply]
#
# Without --apply, outputs recommendations to stdout as JSON
# With --apply, updates posts.json directly

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)
apply_changes <- "--apply" %in% args

# Read posts JSON
posts_json <- "content/blog/posts.json"
posts <- fromJSON(posts_json, simplifyVector = FALSE)

# Load valid software values
software_dir <- "content/software"
valid_software <- list.dirs(software_dir, recursive = FALSE, full.names = FALSE)

# Mapping from ported_from to likely software/language
source_mappings <- list(
  tidyverse = list(software = c("tidyverse"), languages = c()),
  shiny = list(software = c(), languages = c()),
  ai = list(software = c(), languages = c()),
  quarto = list(software = c("quarto"), languages = c()),

  great_tables = list(software = c("great-tables"), languages = c()),
  plotnine = list(software = c("plotnine"), languages = c()),
  pointblank = list(software = c("pointblank"), languages = c()),
  positron = list(software = c("positron"), languages = c()),
  rstudio = list(software = c(), languages = c()),
  education = list(software = c(), languages = c())
)

# Software to language mapping
# Python-only packages
python_packages <- c(
  "plotnine", "great-tables", "pointblank",
  "shiny-python", "py-shinylive", "py-shinyswatch", "py-shinywidgets",
  "pins-python", "vetiver-python", "rsconnect-python"
)

# R-only packages (most packages are R)
r_packages <- c(
  # Tidyverse
  "tidyverse", "dplyr", "ggplot2", "tidyr", "readr", "purrr", "tibble",
  "stringr", "forcats", "lubridate", "glue", "haven", "readxl", "rvest",
  "httr", "httr2", "xml2", "dbplyr", "dtplyr", "magrittr", "reprex",
  # Tidymodels
 "tidymodels", "parsnip", "recipes", "rsample", "tune", "yardstick",
  "broom", "infer", "workflows", "workflowsets", "hardhat", "corrr",
  "dials", "stacks", "probably", "embed", "textrecipes", "themis",
  "tidyclust", "spatialsample", "finetune", "bonsai", "rules",
  "brulee", "multilevelmod", "censored", "orbital", "bundle", "butcher",
  # Shiny R
 "shiny-r", "shinydashboard", "shinytest", "shinytest2", "shinythemes",
  "shinyvalidate", "shinymeta", "shinyloadtest", "bslib", "thematic",
  "htmltools", "httpuv", "promises", "later",
  # AI/ML
  "tensorflow", "keras3", "tfestimators", "tfruns", "tfdatasets",
  "tfprobability", "cloudml", "torch", "luz", "reticulate", "lime",
  # Publishing
  "rmarkdown", "knitr", "blogdown", "bookdown", "distill", "pagedown",
  "flexdashboard", "learnr", "xaringan", "rticles", "tinytex",
  # Tables
  "gt", "gt-extras", "reactable", "DT", "kableExtra", "flextable",
  # Dev tools
  "devtools", "usethis", "testthat", "roxygen2", "pkgdown", "rcmdcheck",
  "remotes", "pak", "renv", "covr", "lintr", "styler", "desc",
  # Data
  "dbi", "odbc", "pool", "bigrquery", "RPostgres", "RMariaDB",
  # Comms
  "plumber", "pins-r", "vetiver-r", "connectapi", "rsconnect", "blastula",
  # Other
  "cli", "rlang", "vctrs", "pillar", "lifecycle", "scales", "fs",
  "withr", "memoise", "cachem", "callr", "processx", "ps", "crayon",
  "R6", "gargle", "googledrive", "googlesheets4", "gmailr"
)

# Multi-language packages (map to all supported languages)
multilang_packages <- list(
  "quarto" = c("R", "Python", "Julia"),
  "positron" = c("R", "Python"),
  "rstudio" = c("R"),
  "shinylive" = c("R", "Python"),
  "brand-yml" = c("R", "Python")
)

# Common tag/category to software mappings (lowercase keys)
tag_to_software <- list(
  # Tidyverse packages
  "dplyr" = "dplyr",
  "ggplot2" = "ggplot2",
  "tidyr" = "tidyr",
  "readr" = "readr",
  "purrr" = "purrr",
  "tibble" = "tibble",
  "stringr" = "stringr",
  "forcats" = "forcats",
  "lubridate" = "lubridate",
  "tidyverse" = "tidyverse",

  # Shiny
  "shiny" = "shiny-r",

  # Modeling
  "tidymodels" = "tidymodels",
  "parsnip" = "parsnip",
  "recipes" = "recipes",
  "rsample" = "rsample",
  "tune" = "tune",
  "yardstick" = "yardstick",
  "broom" = "broom",
  "infer" = "infer",

  # AI/ML
  "tensorflow" = "tensorflow",
  "keras" = "keras3",
  "tensorflow/keras" = "keras3",
  "torch" = "",

  # Publishing
  "rmarkdown" = "rmarkdown",
  "quarto" = "quarto",
  "blogdown" = "blogdown",
  "bookdown" = "bookdown",
  "distill" = "distill",
  "gt" = "gt",
  "knitr" = "",

  # Dev tools
  "devtools" = "devtools",
  "testthat" = "testthat",
  "usethis" = "usethis",
  "roxygen2" = "roxygen2",
  "pkgdown" = "pkgdown",

  # Data
  "dbi" = "dbi",
  "dbplyr" = "dbplyr",
  "haven" = "haven",
  "readxl" = "readxl",
  "httr" = "httr",
  "httr2" = "httr2",
  "rvest" = "rvest",
  "xml2" = "xml2",
  "jsonlite" = "",

  # Other
  "reticulate" = "reticulate",
  "plumber" = "plumber",
  "pins" = "pins-r",
  "vetiver" = "vetiver-r",
  "connectapi" = "connectapi",

  # Categories (lowercase)
  "package" = "",
  "packages/releases" = "",
  "programming" = "",
  "news" = ""
)

# Function to extract software from tags/categories
extract_from_tags <- function(tags, categories) {
  all_terms <- c()

  if (!is.null(tags)) {
    all_terms <- c(all_terms, unlist(tags))
  }
  if (!is.null(categories)) {
    all_terms <- c(all_terms, unlist(categories))
  }

  all_terms <- tolower(all_terms)
  software <- c()

  for (term in all_terms) {
    # Direct match to valid software
    if (term %in% valid_software) {
      software <- c(software, term)
    }
    # Mapped match
    if (term %in% names(tag_to_software) && tag_to_software[[term]] != "") {
      software <- c(software, tag_to_software[[term]])
    }
  }

  unique(software)
}

# Process each post
recommendations <- list()

for (i in seq_along(posts)) {
  post <- posts[[i]]
  fm <- post$frontmatter

  # Skip if already tagged
  has_software <- !is.null(fm$software) && length(fm$software) > 0
  has_languages <- !is.null(fm$languages) && length(fm$languages) > 0

  if (has_software && has_languages) {
    next
  }

  # Skip drafts
  if (!is.null(fm$draft) && isTRUE(fm$draft)) {
    next
  }

  # Start with empty recommendations
  software <- c()
  languages <- c()

  # Apply source mapping
  if (!is.null(fm$ported_from) && fm$ported_from %in% names(source_mappings)) {
    mapping <- source_mappings[[fm$ported_from]]
    software <- c(software, mapping$software)
    languages <- c(languages, mapping$languages)
  }

  # Extract from existing tags/categories
  from_tags <- extract_from_tags(fm$tags, fm$categories)
  software <- c(software, from_tags)

  # Deduplicate software
  software <- unique(software)

  # Infer languages from software packages
  for (pkg in software) {
    if (pkg %in% python_packages) {
      languages <- c(languages, "Python")
    } else if (pkg %in% r_packages) {
      languages <- c(languages, "R")
    } else if (pkg %in% names(multilang_packages)) {
      languages <- c(languages, multilang_packages[[pkg]])
    }
  }

  # Deduplicate languages
  languages <- unique(languages)

  # Only include if we found something
  if (length(software) > 0 || length(languages) > 0) {
    recommendations[[length(recommendations) + 1]] <- list(
      md_path = post$md_path,
      software = as.list(software),
      languages = as.list(languages),
      # Include context for review
      title = fm$title,
      ported_from = fm$ported_from,
      existing_tags = fm$tags,
      existing_categories = fm$categories
    )
  }
}

message(sprintf("Generated %d recommendations", length(recommendations)))

if (apply_changes) {
  # Apply to posts.json via update script logic
  for (rec in recommendations) {
    idx <- which(sapply(posts, function(p) p$md_path == rec$md_path))
    if (length(idx) == 1) {
      if (length(rec$software) > 0) {
        posts[[idx]]$frontmatter$software <- rec$software
      }
      if (length(rec$languages) > 0) {
        posts[[idx]]$frontmatter$languages <- rec$languages
      }
    }
  }

  json_output <- toJSON(posts, auto_unbox = TRUE, pretty = TRUE, null = "null")
  writeLines(json_output, posts_json)
  message(sprintf("Applied to %s", posts_json))
} else {
  # Output as JSON for review
  cat(toJSON(recommendations, auto_unbox = TRUE, pretty = TRUE, null = "null"))
}
