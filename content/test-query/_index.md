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


## People with a personal website

```
{{</* query-items path="people/*" filter=`{"!=": [{"var": "social.website"}, ""]}` hide-badge="true" cols="5" */>}}
```

{{< query-items path="people/*" filter=`{"!=": [{"var": "social.website"}, ""]}` hide-badge="true" cols="5" >}}
