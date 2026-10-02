promise1 <- function() {
  promise_resolve(\() Sys.sleep(2))
}
promise2 <- function(x) {
  Sys.sleep(2)
  x
}
promise3 <- function(x) {
  Sys.sleep(2)
  x
}

with_ospan_promise_domain({
  # Start a root span for the promise chain
  otel::start_local_active_span("my-promise-chain")

  # Span context properly maintained throughout the chain
  promise1() |>
    then(\(x) {
      # `middle-span` is child of `my-promise-chain`
      otel::start_local_active_span("middle-span")
      promise2(x)
    }) |>
    then(\(x) {
      # `last-span` is child of `my-promise-chain`
      otel::start_local_active_span("last-span")
      promise3(x)
    })

  # `my-promise-chain` otel span ends here
})

while (!later::loop_empty()) {
  later::run_now()
}
