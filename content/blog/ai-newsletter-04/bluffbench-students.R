library(tidyverse)
library(bluffbench)
library(patchwork)

plot_students <- function(data) {
  data |>
    ggplot(aes(x = study_hours_weekly, y = exam_score)) +
    geom_point() +
    labs(
      x = "Weekly study hours",
      y = "Exam score"
    )
}

# Bluffbench data
set.seed(1010)
n <- 75

study_hours_weekly <- runif(n, 2, 35)

exam_score <- 62 +
  0.2 * study_hours_weekly +
  ifelse(study_hours_weekly >= 20 & study_hours_weekly <= 25, 28, 0) +
  rnorm(n, 0, 4)

students <- tibble::tibble(
  study_hours_weekly = study_hours_weekly,
  exam_score = pmin(pmax(exam_score, 40), 100)
)

p1 <-
  plot_students(students) +
  labs(
    title = "bluffbench relationship",
    subtitle = "Data in bluffbench has an unexpected discontinuity"
  )

# Expected relationship
exam_score <- 62 +
  0.2 * study_hours_weekly +
  rnorm(n, 0, 2)

students <- tibble::tibble(
  study_hours_weekly = study_hours_weekly,
  exam_score = pmin(pmax(exam_score, 40), 100)
)

p2 <-
  plot_students(students) +
  labs(
    title = "Expected relationship",
    subtitle = "What you might expect exam score vs. study time to look like"
  )

ggsave(
  "images/students.png",
  p2 + p1,
  width = 10,
  height = 3.5,
  dpi = 200
)
