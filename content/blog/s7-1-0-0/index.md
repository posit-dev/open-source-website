---
title: S7 1.0.0
date: 2026-10-06T00:00:00.000Z
draft: true
people:
  - Tomasz Kalinowski
  - Hadley Wickham
description: >
  S7 1.0.0 brings faster construction, lower memory use, S4 inheritance, and new
  tools for exploring and maintaining object-oriented R code.
image: ''
image-alt: ''
topics:
  - Best Practices
software:
  - s7
languages:
  - R
source: tidyverse
---


We're excited to announce that S7 1.0.0 is now available on CRAN!

[S7](https://rconsortium.github.io/S7/) is an object-oriented
programming system for R that combines the approachable style of S3 with
the explicit structure of S4. It gives you clearly defined classes,
properties that check their values, and methods that can respond to the
classes of multiple arguments.

This major release brings faster object construction, lower memory use,
inheritance between S7 and S4 classes, and new tools for exploring,
debugging, and maintaining your code.

Since our [previous release announcement](../../blog/2024-11-07_s7-0-2-0/),
[ggplot2 4.0.0](../../blog/2025-09-11_ggplot2-4-0-0/) has adopted S7 for many
of its core objects. S7 1.0.0 builds on that experience, with broader
support for existing R code and more tools for package authors.

``` r
install.packages("S7")
```

## Performance

Object construction is substantially faster, with
[development benchmarks](https://github.com/RConsortium/S7/issues/723#issuecomment-5131171440) showing roughly
**2--3× faster construction for deeper class hierarchies** compared with
S7 0.2.2. Objects now share class definitions, reducing memory use and
avoiding duplicate definitions when saving collections of objects. S7
also preserves R's compact `ALTREP` representation of sequences such as
`seq_len(1000000)`, rather than expanding them into full vectors when
wrapping them in an S7 object.

## Class and generic definitions with `:=`

The new [`:=` operator](https://rconsortium.github.io/S7/reference/named-bind.html) lets you create and name a class in one step. Instead of repeating the
name in `Point <- new_class("Point", ...)`, write:

``` r
library(S7)

Point := new_class(
  properties = list(
    x = class_numeric,
    y = class_numeric
  )
)
```

A *class* describes the information its objects contain. Here, a `Point`
has two numeric properties, `x` and `y`. The class also acts as a
constructor--a function for making points:

``` r
p <- Point(x = 3, y = 4)
p@x
```

    [1] 3

Use `@` to read or update a property. S7 checks its type, so assigning
text to `p@x` produces an error. Validators can add further rules, such
as requiring a positive value. You can also validate relationships
between properties--for example, checking that a start time comes before
an end time.

The new syntax works for generics, too. A *generic* selects an
implementation, called a *method*, based on the classes of its
arguments:

``` r
distance := new_generic("x")

method(distance, Point) <- function(x) {
  sqrt(x@x^2 + x@y^2)
}

distance(p)
```

    [1] 5

Here, `distance()` selects the method for `Point`. Adding a method for
another class lets the same function work with that class, too.

The existing `<-` syntax remains supported; `:=` simply supplies the
name and assigns the result in one operation.

## S4 inheritance

**S7 classes can now extend S4 classes, and S4 classes can extend S7 classes.**
You can introduce S7 into an existing class hierarchy while keeping its
methods and behavior.

For example, suppose an existing S4 class has a method that computes its
distance from the origin:

``` r
LegacyPoint <- methods::setClass(
  "LegacyPoint",
  slots = c(x = "numeric", y = "numeric")
)

methods::setGeneric("radius", function(object) {
  methods::standardGeneric("radius")
})

methods::setMethod("radius", "LegacyPoint", function(object) {
  sqrt(object@x^2 + object@y^2)
})
```

We can extend it with S7, adding a label:

``` r
LabeledPoint <- S7::new_class(
  "LabeledPoint",
  parent = LegacyPoint,
  properties = list(label = S7::class_character)
)

q <- LabeledPoint(x = 3, y = 4, label = "A")

q@label
```

    [1] "A"

``` r
radius(q)
```

    [1] 5

The S4 slots become S7 properties, and the existing S4 method works with
the new subclass. S7 handles the registration between the two systems.

In the other direction, `S7::S4_register()` and `S7::S4_contains()` let
an S4 class extend an S7 class and expose its stored properties as
slots. The [compatibility guide](https://rconsortium.github.io/S7/articles/compatibility.html) covers both directions.

## Methods for S3 and S4 objects

S7's `method(generic, class) <- function(...)` interface now supports
more combinations of S3 and S4 generics with base types, S3 classes, and
class unions. Unions let you register one implementation for several
classes.

Operators such as `+`, `==`, and `%*%` can now use S7's double
dispatch--selecting a method based on both operands--even when both
operands are ordinary S3 or S4 objects. Neither has to be an S7 object.
Unary operators, including `-` and `!`, also gain method-registration
support.

These changes extend the interoperability work described in our earlier
[R Blog post on functional OOP](https://blog.r-project.org/2024/05/17/generalizing-support-for-functional-oop-in-r/index.html).

## Quality of life

### Inspecting classes and methods

New helpers make it easier to explore an unfamiliar API:

``` r
prop_info(Point)
```

      name default                 class getter setter validator
    1    x         <integer> or <double>  FALSE  FALSE     FALSE
    2    y         <integer> or <double>  FALSE  FALSE     FALSE

``` r
S7_methods(generic = distance)
```

       generic package signature
    1 distance    <NA>   <Point>

[`prop_info()`](https://rconsortium.github.io/S7/reference/prop_names.html) returns a data frame describing each property's type, default, getter,
setter, and validator. `S7_methods()` lists the methods registered on a
generic.

`S7_classes()` and `S7_generics()` list definitions in an environment or
package namespace. For example, `S7_classes(asNamespace("ggplot2"))`
lists the S7 classes defined in ggplot2. `S7_methods()` can also find
methods associated with a class across S7 generics in attached packages.

Class printing now shows property defaults and marks read-only
properties. And `S7_class()` returns a class specification for any R
object, not just S7 objects.

### Debugging and errors

S7 generics and methods now work with R's standard debugging workflows.
With `trace()`, you can set a method to enter the debugger when it runs,
inspect its arguments, and step through its code without editing the
method definition. `untrace()` removes the tracing code afterward.

Errors now identify the function where they occurred. Errors from
property getters and setters name the class and property involved,
making the source easier to locate. Validation failures also have a
dedicated error class, so you can catch them separately with
`tryCatch()`.

### Construction and conversion

`set_props()` and `new_object()` now accept a list of property values,
simplifying programmatic updates and construction. For example, you can
update several properties at once from a named list:

``` r
p <- set_props(p, list(x = 6, y = 8))
distance(p)
```

    [1] 10

Subclasses also handle custom parent constructors, overridden defaults,
and property setters more consistently.

`convert()` supports more automatic conversions, including conversion to
base types through their usual `as.*()` functions. The new
`convert_lazy()` leaves an object unchanged when it already inherits
from the requested class, preserving any extra subclass properties.

## Package development

New `deprecated_generic()`, `deprecated_class()`, and
`deprecated_property()` helpers let you update an API while keeping
existing code working. For example, when renaming a property from
`label` to `title`:

``` r
Record := new_class(
  properties = list(
    title = class_character,
    deprecated_property("label", new = "title", when = "2.0.0")
  )
)

record <- Record(title = "Annual summary")
record@label
```

    Warning: `<Record>@label` was deprecated in version 2.0.0.
    Please use `<Record>@title` instead.

    [1] "Annual summary"

The old property forwards reads and writes to the new one. Deprecated
generics can forward both calls and method registrations to a
replacement; deprecated classes retain their methods and subclasses.
Package authors can provide migration warnings without immediately
breaking extensions written against the old API. Warnings can use base R
or the lifecycle package.

[`new_external_class()`](https://rconsortium.github.io/S7/reference/new_external_class.html) lets you refer to a class before it is available. This supports
methods for optional dependencies and self-referential classes, such as
tree nodes that contain other nodes.

`S7_on_load()`, `S7_on_unload()`, and `S7_on_build()` handle method
registration and cleanup during package loading, unloading, and
building. Repeated development loads are quieter, and
method-compatibility checks focus on development and package checking
rather than warning end users about code they cannot fix. See the
updated [package-development guide](https://rconsortium.github.io/S7/articles/packages.html) for setup instructions.

## Learn more

Start with the
[S7 introduction](https://rconsortium.github.io/S7/articles/S7.html), or
explore the guides to [classes and objects](https://rconsortium.github.io/S7/articles/classes-objects.html) and [generics and methods](https://rconsortium.github.io/S7/articles/generics-methods.html). The [full release notes](https://github.com/RConsortium/S7/blob/main/NEWS.md) cover additional improvements and changes for package authors
upgrading existing code.

S7 is an R Consortium collaboration involving contributors from R-Core,
Bioconductor, Posit/tidyverse, and the wider R community. Thank you to
everyone who contributed code, reported issues, tested development
versions, and shared experience from their packages.
