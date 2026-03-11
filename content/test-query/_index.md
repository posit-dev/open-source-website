---
title: "Test Query Items"
layout: single
---

## Blog Posts

### Latest 3 Blog Posts (3 Columns)
{{< query-items path="blog/*" sort-by="date" sort-direction="desc" limit="3" cols="3" >}}

### Latest 6 Blog Posts (2 Columns)
{{< query-items path="blog/*" sort-by="date" sort-direction="desc" limit="6" cols="2" >}}

## Software

### Top 6 by Stars (3 Columns)
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" limit="6" cols="3" >}}

### Top 10 by Stars (5 Columns)
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" limit="10" cols="5" >}}

### Top 12 by Stars (6 Columns, no badges)
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" limit="12" cols="6" hide-badge="true" >}}

## Videos

### Latest 4 Videos (2 Columns)
{{< query-items path="resources/videos/*" sort-by="date" sort-direction="desc" limit="4" cols="2" >}}

### Latest 6 Videos (3 Columns)
{{< query-items path="resources/videos/*" sort-by="date" sort-direction="desc" limit="6" cols="3" >}}

## Cheatsheets

### Latest 4 Cheatsheets (4 Columns)
{{< query-items path="resources/cheatsheets/*" sort-by="date" sort-direction="desc" limit="4" cols="4" >}}

## Events

### Latest 3 Events (3 Columns)
{{< query-items path="events/*" sort-by="date" sort-direction="desc" limit="3" cols="3" >}}

## People

### 4 People (4 Columns)
{{< query-items path="people/*" sort-by="title" sort-direction="asc" limit="4" cols="4" >}}

## Mixed: Oldest First

### Oldest 3 Blog Posts (3 Columns)
{{< query-items path="blog/*" sort-by="date" sort-direction="asc" limit="3" cols="3" >}}

## Filter Tests

### Numeric `>`: Software with more than 1000 stars
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{">": [{"var": "external.stars"}, 1000]}` cols="4" >}}

### Numeric `>=`: Software with at least 5000 stars
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{">=": [{"var": "external.stars"}, 5000]}` cols="3" >}}

### Numeric `<`: Software with fewer than 100 stars
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{"<": [{"var": "external.stars"}, 100]}` limit="12" cols="4" >}}

### Equality `==`: Software with GPL-3.0 license
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{"==": [{"var": "external.license"}, "GPL-3.0"]}` cols="4" >}}

### Inequality `!=`: Software without NOASSERTION license
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{"!=": [{"var": "external.license"}, "NOASSERTION"]}` limit="12" cols="4" >}}

### `in` (array): Software with Python as a language
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{"in": ["Python", {"var": "languages"}]}` cols="4" >}}

### `and`: Software with R language AND more than 100 stars
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{"and": [{"in": ["R", {"var": "languages"}]}, {">": [{"var": "external.stars"}, 100]}]}` cols="4" >}}

### `or`: Software with Python OR R
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{"or": [{"in": ["Python", {"var": "languages"}]}, {"in": ["R", {"var": "languages"}]}]}` limit="12" cols="4" >}}

### `!` (negation): Software where license is NOT GPL-3.0
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{"!": {"==": [{"var": "external.license"}, "GPL-3.0"]}}` limit="12" cols="4" >}}

### `var` with default: Stars > 500 (default 0 for missing)
{{< query-items path="software/*" sort-by="external.stars" sort-direction="desc" filter=`{">": [{"var": ["external.stars", 0]}, 500]}` cols="4" >}}

### No path (filter only): All pages with software that has more than 5000 stars
{{< query-items sort-by="external.stars" sort-direction="desc" filter=`{">": [{"var": "external.stars"}, 5000]}` cols="3" >}}
