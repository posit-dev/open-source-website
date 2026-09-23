# Run every demo's screenshot.R in its own R process, in sequence.

file_arg <- grep("^--file=", commandArgs(FALSE), value = TRUE)
file_arg <- sub("^--file=", "", file_arg)
if (!length(file_arg)) {
  stop("Run with Rscript: Rscript apps/run-all.R")
}
apps_dir <- dirname(normalizePath(file_arg[1]))

demos <- sort(list.dirs(apps_dir, recursive = FALSE))
demos <- demos[!grepl("_", basename(demos))]

results <- lapply(demos, function(dir) {
  message("Running ", basename(dir), "...")
  t0 <- Sys.time()
  callr::r(
    function(d) {
      setwd(d)
      source("screenshot.R")
    },
    args = list(d = dir),
    stdout = "|",
    stderr = "|",
    show = TRUE
  )
  message(
    "Done ",
    basename(dir),
    " in ",
    round(as.numeric(difftime(Sys.time(), t0, units = "secs")), 1),
    "s"
  )
  TRUE
})

names(results) <- basename(demos)
invisible(results)
