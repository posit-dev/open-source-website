
<!-- README.md is generated from README.Rmd. Please edit that file -->

<img src="man/figures/logo.png" align="right" alt="lang's hex logo" width="120" />

# lang

<!-- badges: start -->

[![R-CMD-check](https://github.com/mlverse/lang/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/mlverse/lang/actions/workflows/R-CMD-check.yaml)
[![Codecov test
coverage](https://codecov.io/gh/mlverse/lang/branch/main/graph/badge.svg)](https://app.codecov.io/gh/mlverse/lang?branch=main)
<a href="https://CRAN.R-project.org/package=lang"><img src="https://www.r-pkg.org/badges/version/lang" alt="CRAN status"></a>
<!-- badges: end -->

Use an **LLM to translate a function’s help documentation on the fly**.
`lang` overrides the `?` and `help()` functions in your R session. If
you are using RStudio or Positron, the translated help page will appear
in the ‘Help’ pane.

## Installing

To install the CRAN version of `lang` use:

``` r
install.packages("lang")
```

To install the GitHub version of `lang`, use:

``` r
install.packages("pak")
pak::pak("mlverse/lang")
```

## Using `lang`

In order to work, `lang` needs two things:

1.  An LLM connection

2.  A target language (e.g.: Spanish, French, Korean)

These two can be defined using `lang_use()`. For example, the following
code shows how to use OpenAI’s GPT-4o model to translate `lm()`’s help
into Spanish:

``` r
library(lang)

chat <- ellmer::chat_openai(model = "gpt-4o")

lang_use(backend = chat, .lang = "spanish")

?lm
#> ■■                                 4% | Title
```

<img src="man/figures/lm-spanish.png" align="center" width="100%"
alt="Screenshot of the lm function's help page in Spanish"/>

After setup, simply use `?` to trigger and display the translated
documentation. Note that R enforces the printed names of each section,
so titles such as “Description”, “Usage”, and “Arguments” will always
remain untranslated.

During translation, `lang` will display its progress by showing which
section of the documentation is currently translating. During the R
session, if you request the same R function’s help more than one time
then `lang` will use its cached results, which will run immediately.

### Context summary

Because each section of a help page is translated independently, the LLM
can lose track of the broader topic and produce inconsistent or
out-of-context translations. To address this, `lang` first summarizes
the full help page in English, translates that summary into the target
language, and then uses it as context when translating each individual
section. You can control the length of this summary with the
`context_size` argument in `lang_use()` or `lang_help()` — set it to `0`
to disable it, or increase it to give the LLM more context.

To avoid the LLM getting confused by a context summary that is longer
than the content being translated, context is automatically omitted for
fields of 10 words or fewer.

### LLM connections

There are two ways to define the LLM in `lang_use()`:

1.  Use an [`ellmer`](https://ellmer.tidyverse.org/) chat object:

    ``` r
    lang_use(backend = ellmer::chat_openai(model = "gpt-4o"))
    ```

2.  Use local LLMs available through [Ollama](https://ollama.com/). Pass
    `"ollama"` as the `backend` argument, and specify which installed
    model to use:

    ``` r
    lang_use(backend = "ollama", model = "llama3.2", seed = 100)
    ```

    Under the hood, `lang` uses the
    [`ollamar`](https://hauselin.github.io/ollama-r/) package to
    integrate with Ollama. Any additional arguments, such as `seed` as
    shown above, will be passed as-is to `ollamar`’s `chat()` function.

### Target language

In order of priority, these are the ways in which `lang` determines the
language it will translate to:

1.  Value in `.lang` when calling `lang_use()`
2.  `LANGUAGE` environment variable
3.  `LANG` environment variable

It is likely that your `LANG` variable already defaults to your locale.
For example, mine is set to: `en_US.UTF-8` (that means English, United
States). For someone in France, the locale would be something such as
`fr_FR.UTF-8`. Llama3.2 recognizes these UTF locales, and using `lang`,
calling `?` will result in translating the function’s help documentation
into French.

If both environment variables are set, and are different from each
other, `lang` will display a one-time message indicating which value it
will use. If the target language is English, `lang` will re-route help
calls back to base R.

To check the current target language at any point during the R session,
simply run: `lang_use()`, with no arguments, and it will print out the
current settings, which include language:

``` r
lang_use()
#> Model: gpt-4o via OpenAI
#> Lang: spanish
```

## Tips

### Caching

By default, `lang` will cache the translations it performs in a
temporary folder. If R is restarted, a new folder will be used.

If you notice that you are translating the same function’s help over and
over and across different R sessions, then fixing the cache location
would be helpful. Use `.cache` to define the folder:

``` r
lang::lang_use(
  backend = "ollama", 
  model = "llama3.2", 
  .cache = "~/help-translations/", 
  .lang = "spanish"
  )
```

### Auto-initialize at startup

If `lang` becomes a regular part of your workflow, and running
`lang_use()` at the beginning of every R session becomes cumbersome,
then consider letting R connect at start up.

If present, the *.Rprofile* file runs at the beginning of any R session.
If you wish to automatically set the model and language to use, add a
call to `lang_use()` to this file. You can call
`usethis::edit_r_profile()` to open your .Rprofile file so you can add
the option.

Here is an example using Ollama:

``` r
lang::lang_use(
  backend = "ollama",
  model = "llama3.2",
  .cache = "~/help-translations/",
  .lang = "spanish",
  .silent = TRUE
  )
```

And here is an example using an `ellmer` chat object:

``` r
lang::lang_use(
  backend = ellmer::chat_openai(model = "gpt-4o"),
  .cache = "~/help-translations/",
  .lang = "spanish",
  .silent = TRUE
  )
```

In both examples, `.silent` is set to `TRUE` so that there is no message
every time the R session is restarted. The `.cache` argument points to a
fixed folder so that translations persist across sessions. You can also
set `.context_size` here to control how much context the LLM receives
when translating each section.

## Considerations

### Translations are not perfect

As you can imagine, the quality of translation will mostly depend on the
LLM being used. This solution is meant to be as helpful as possible, but
we acknowledge that at this stage of LLMs, only a human curated
translation will be the best solution. Having said that, I believe that
even an imperfect translation could go a long way with someone who is
struggling to understand how to use a specific function in a package and
may also struggle with the English language.

### Debugging

If the original English help page displays, check your environment
variables:

``` r
Sys.getenv("LANG")
#> [1] "en_US.UTF-8"
Sys.getenv("LANGUAGE")
#> [1] ""
```

In my case, `lang` recognizes that the environment is set to English,
because of the `en` code in the variable. If your `LANG` variable is set
to `en_...` then no translation will occur.

If this is your case, set the `LANGUAGE` variable to your preference.
You can use the full language name, such as ‘spanish’, or ‘french’, etc.
You can use `Sys.setenv(LANGUAGE = "[my language]")`, or, for a more
permanent solution, add the entry to your .Renviron file
(`usethis::edit_r_environ()`).

### Translation errors

If you experience unexpected translation errors and you are using a
local LLM without a `seed` set, try restarting your R session and
running the translation again. Non-deterministic LLM output can
occasionally produce output that causes errors. If the problem persists,
please open an issue at <https://github.com/mlverse/lang/issues>.

### Interaction with `mall`

`lang` uses the `mall` package to produce the translations. To avoid
conflicts in the setup and use of both packages during the R session,
`lang` runs `mall` in a separate R process which is only alive while
translating the documentation. This means that you can have a specific
LLM setup for `lang`, and a different one for `mall` during your R
session.
