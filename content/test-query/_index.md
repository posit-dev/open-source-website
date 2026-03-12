---
title: "Test Query Items"
layout: single
---

## Videos with the most views

```
{{</* query-items path="resources/videos/*" sort-by="external.view_count" sort-direction="desc" limit="3" cols="3" */>}}
```

{{< query-items path="resources/videos/*" sort-by="external.view_count" sort-direction="desc" limit="3" cols="3" >}}

## Longest videos by Joe Cheng

```
{{</* query-items path="resources/videos/*" filter=`{"in": ["Joe Cheng", {"var": "people"}]}` sort-by="external.duration" sort-direction="desc" limit="3" cols="3" */>}}
```

{{< query-items path="resources/videos/*" filter=`{"in": ["Joe Cheng", {"var": "people"}]}` sort-by="external.duration" sort-direction="desc" limit="3" cols="3" >}}

## Software for both Python and R

```
{{</* query-items path="software/*" filter=`{"and": [{"in": ["R", {"var": "languages"}]}, {"in": ["Python", {"var": "languages"}]}]}` limit="10" cols="3" */>}}
```

{{< query-items path="software/*" filter=`{"and": [{"in": ["R", {"var": "languages"}]}, {"in": ["Python", {"var": "languages"}]}]}` limit="10" cols="3" >}}


## Software that supports both R and Python (contains_all)

```
{{</* query-items path="software/*" filter=`{"contains_all": [{"var": "languages"}, ["R", "Python"]]}` limit="10" cols="3" */>}}
```

{{< query-items path="software/*" filter=`{"contains_all": [{"var": "languages"}, ["R", "Python"]]}` limit="10" cols="3" >}}

## Software that supports Julia or Rust (contains_any)

```
{{</* query-items path="software/*" filter=`{"contains_any": [{"var": "languages"}, ["Julia", "Rust"]]}` limit="10" cols="3" */>}}
```

{{< query-items path="software/*" filter=`{"contains_any": [{"var": "languages"}, ["Julia", "Rust"]]}` limit="10" cols="3" >}}

## Software that supports neither Python nor JavaScript (contains_none)

```
{{</* query-items path="software/*" filter=`{"contains_none": [{"var": "languages"}, ["Python", "JavaScript"]]}` limit="10" cols="3" */>}}
```

{{< query-items path="software/*" filter=`{"contains_none": [{"var": "languages"}, ["Python", "JavaScript"]]}` limit="10" cols="3" >}}

## Columns: text and cards (equal width)

```
{{</* columns */>}}
### Recommended Tools

These are some excellent tools for **data science** that support
both Python and R.

---

{{</* query-items path="software/*" filter=`{"contains_all": [{"var": "languages"}, ["R", "Python"]]}` limit="3" cols="1" */>}}
{{</* /columns */>}}
```

{{< columns >}}
### Recommended Tools

These are some excellent tools for **data science** that support
both Python and R.

---

{{< query-items path="software/*" filter=`{"contains_all": [{"var": "languages"}, ["R", "Python"]]}` limit="3" cols="1" format="tile" hide-badge="true" >}}
{{< /columns >}}

## Columns: custom split (2,1)

```
{{</* columns split="2,1" */>}}
### About Quarto

Quarto is an open-source scientific and technical publishing system.
It supports **Python**, **R**, **Julia**, and **Observable JavaScript**.
Quarto enables you to create dynamic content with executable code blocks
in many formats including HTML, PDF, Word, and presentations.

---

{{</* insert-item item="software/quarto" */>}}
{{</* /columns */>}}
```

{{< columns split="2,1" >}}
## About Quarto

Quarto is an open-source scientific and technical publishing system.
It supports **Python**, **R**, **Julia**, and **Observable JavaScript**.
Quarto enables you to create dynamic content with executable code blocks
in many formats including HTML, PDF, Word, and presentations.

---

{{< insert-item item="software/quarto" >}}
{{< /columns >}}

## Columns: three equal columns

```
{{</* columns */>}}
### Column One

First column with some **markdown** content and a [link](https://example.com).

---

### Column Two

Second column with *different* content.

---

### Column Three

Third column to demonstrate a three-way split.
{{</* /columns */>}}
```

{{< columns >}}
### Column One

First column with some **markdown** content and a [link](https://example.com).

---

### Column Two

Second column with *different* content.

---

### Column Three

Third column to demonstrate a three-way split.
{{< /columns >}}

## People with a personal website

```
{{</* query-items path="people/*" filter=`{"!=": [{"var": "social.website"}, ""]}` hide-badge="true" cols="5" */>}}
```

{{< query-items path="people/*" filter=`{"!=": [{"var": "social.website"}, ""]}` hide-badge="true" cols="5" >}}
