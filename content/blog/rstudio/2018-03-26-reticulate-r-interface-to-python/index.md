---
title: 'reticulate: R interface to Python'
people:
  - JJ Allaire
date: '2018-03-26'
slug: reticulate-r-interface-to-python
categories:
  - Publishing
tags:
  - Packages
  - R Markdown
  - Python
  - RStudio
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
software: ["reticulate"]
languages: ["R"]
ported_categories:
  - Packages
  - R Markdown
---


We are pleased to announce the **reticulate** package, a comprehensive set of tools for interoperability between Python and R. The package includes facilities for:

<img src="https://rstudio.github.io/reticulate/images/reticulated_python.png" width=200 align=right style="margin-left: 15px;" alt="reticulated python"/>

- Calling Python from R in a variety of ways including R Markdown, sourcing Python scripts, importing Python modules, and using Python interactively within an R session.

- Translation between R and Python objects (for example, between R and Pandas data frames, or between R matrices and NumPy arrays).

- Flexible binding to different versions of Python including virtual environments and Conda environments.

Reticulate embeds a Python session within your R session, enabling seamless, high-performance interoperability. If you are an R developer that uses Python for some of your work or a member of data science team that uses both languages, reticulate can dramatically streamline your workflow! 

You can install the **reticulate** pacakge from CRAN as follows:

```
install.packages("reticulate")
```

Read on to learn more about the features of reticulate, or see the [reticulate website](https://rstudio.github.io/reticulate) for detailed documentation on using the package.  

## Python in R Markdown

The **reticulate** package includes a Python engine for [R Markdown](http://rmarkdown.rstudio.com) with the following features:

- Run Python chunks in a single Python session embedded within your R session (shared variables/state between Python chunks)

- Printing of Python output, including graphical output from [matplotlib](https://matplotlib.org/).

- Access to objects created within Python chunks from R using the `py` object (e.g. `py$x` would access an `x` variable created within Python from R).

- Access to objects created within R chunks from Python using the `r` object (e.g. `r.x` would access to `x` variable created within R from Python)

<div style="clear: both;"></div>

Built in conversion for many Python object types is provided, including [NumPy](http://www.numpy.org/) arrays and [Pandas](https://pandas.pydata.org/) data frames. From example, you can use Pandas to read and manipulate data then easily plot the Pandas data frame using [ggplot2](http://ggplot2.org/):

<img src="https://rstudio.github.io/reticulate/images/rmarkdown_engine_zoomed.png" class="screenshot"/>

Note that the reticulate Python engine is enabled by default within R Markdown whenever reticulate is installed.

See the [R Markdown Python Engine](https://rstudio.github.io/reticulate/articles/r_markdown.html) documentation for additional details.

## Importing Python modules

You can use the `import()` function to import any Python module and call it from R. For example, this code imports the Python `os` module and calls the `listdir()` function:

```r
library(reticulate)
os <- import("os")
os$listdir(".")
```
```
 [1] ".git"             ".gitignore"       ".Rbuildignore"    ".RData"          
 [5] ".Rhistory"        ".Rproj.user"      ".travis.yml"      "appveyor.yml"    
 [9] "DESCRIPTION"      "docs"             "external"         "index.html"      
[13] "index.Rmd"        "inst"             "issues"           "LICENSE"         
[17] "man"              "NAMESPACE"        "NEWS.md"          "pkgdown"         
[21] "R"                "README.md"        "reticulate.Rproj" "src"             
[25] "tests"            "vignettes"      
```

Functions and other data within Python modules and classes can be accessed via the `$` operator (analogous to the way you would interact with an R list, environment, or reference class).

Imported Python modules support code completion and inline help:

<img src="https://rstudio.github.io/reticulate/images/reticulate_completion.png" class="screenshot"/>


See [Calling Python from R](https://rstudio.github.io/reticulate/articles/calling_python.html) for additional details on interacting with Python objects from within R.


## Sourcing Python scripts

You can source any Python script just as you would source an R script using the `source_python()` function. For example, if you had the following Python script *flights.py*:

```python
import pandas

def read_flights(file):
  flights = pandas.read_csv(file)
  flights = flights[flights['dest'] == "ORD"]
  flights = flights[['carrier', 'dep_delay', 'arr_delay']]
  flights = flights.dropna()
  return flights
```

Then you can source the script and call the `read_flights()` function as follows:

```r
source_python("flights.py")
flights <- read_flights("flights.csv")

library(ggplot2)
ggplot(flights, aes(carrier, arr_delay)) + geom_point() + geom_jitter()
```

See the [`source_python()`](https://rstudio.github.io/reticulate/reference/source_python.html) documentation for additional details on sourcing Python code.

## Python REPL

If you want to work with Python interactively you can call the `repl_python()` function, which provides a Python REPL embedded within your R session. Objects created within the Python REPL can be accessed from R using the `py` object exported from reticulate. For example:

<img src="https://rstudio.github.io/reticulate/images/python_repl.png" class="screenshot"/>

Enter `exit` within the Python REPL to return to the R prompt.

Note that Python code can also access objects from within the R session using the `r` object (e.g. `r.flights`). See the [`repl_python()`](https://rstudio.github.io/reticulate/reference/repl_python.html) documentation for additional details on using the embedded Python REPL.

## Type conversions

When calling into Python, R data types are automatically converted to their equivalent Python types. When values are returned from Python to R they are converted back to R types. Types are converted as follows:

| R  | Python | Examples |
|-----------|-----------|---------------------------------------------------------|
| Single-element vector   | Scalar |  `1`, `1L`, `TRUE`, `"foo"` |
| Multi-element vector | List  |  `c(1.0, 2.0, 3.0)`, `c(1L, 2L, 3L)` |
| List of multiple types  | Tuple  |  `list(1L, TRUE, "foo")`
| Named list | Dict  |  `list(a = 1L, b = 2.0)`, `dict(x = x_data)`
| Matrix/Array | NumPy ndarray  | `matrix(c(1,2,3,4), nrow = 2, ncol = 2)`
| Data Frame | Pandas DataFrame | ` data.frame(x = c(1,2,3), y = c("a", "b", "c"))`  |
| Function | Python function | `function(x) x + 1`
| NULL, TRUE, FALSE  | None, True, False  |  `NULL`, `TRUE`, `FALSE`

If a Python object of a custom class is returned then an R reference to that object is returned. You can call methods and access properties of the object just as if it was an instance of an R reference class.

## Learning more

The [reticulate website](https://rstudio.github.io/reticulate/) includes comprehensive documentation on using the package, including the following articles that cover various aspects of using reticulate:

- [Calling Python from R](https://rstudio.github.io/reticulate/articles/calling_python.html) &mdash; Describes the various ways to access Python objects from R as well as functions available for more advanced interactions and conversion behavior.

- [R Markdown Python Engine](https://rstudio.github.io/reticulate/articles/r_markdown.html) &mdash; Provides details on using Python chunks within R Markdown documents, including how call Python code from R chunks and vice-versa.

- [Python Version Configuration](https://rstudio.github.io/reticulate/articles/versions.html) &mdash; Describes facilities for determining which version of Python is used by reticulate within an R session.

- [Installing Python Packages](https://rstudio.github.io/reticulate/articles/python_packages.html) &mdash; Documentation on installing Python packages from PyPI or Conda, and managing package installations using virtualenvs and Conda environments.

- [Using reticulate in an R Package](https://rstudio.github.io/reticulate/articles/package.html) &mdash; Guidelines and best practices for using reticulate in an R package.

- [Arrays in R and Python](https://rstudio.github.io/reticulate/articles/arrays.html) &mdash; Advanced discussion of the differences between arrays in R and Python and the implications for conversion and interoperability.


## Why reticulate?

From the [Wikipedia](https://en.wikipedia.org/wiki/Reticulated_python) article on the reticulated python:

> The reticulated python is a speicies of python found in Southeast Asia. They are the world's longest snakes and longest reptiles...The specific name, reticulatus, is Latin meaning "net-like", or reticulated, and is a reference to the complex colour pattern. 

From the [Merriam-Webster](https://www.merriam-webster.com/dictionary/reticulate) definition of reticulate:

> 1: resembling a net or network; especially : having veins, fibers, or lines crossing a reticulate leaf. 2: being or involving evolutionary change dependent on genetic recombination involving diverse interbreeding populations.

The package enables you to *reticulate* Python code into R, creating a new breed of project that weaves together the two languages.

***UPDATE:*** *Nov. 27, 2019*  
*Learn more about [how R and Python work together in RStudio](https://rstudio.com/solutions/python-and-r/).*

<style type="text/css">
.screenshot, .illustration {
  margin-bottom: 20px;
  border: 1px solid #ddd;
  box-shadow: 5px 5px 5px #eee;
}
</style>


