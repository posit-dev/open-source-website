# Pagefind Filter Fix - Summary

**Date:** February 24, 2026
**Issue:** Pagefind reported "Indexed 0 filters"
**Status:** ✅ **FIXED** - Now reports "Indexed 1 filter"

---

## Problem

Pagefind was not detecting any filters despite the filter metadata being present in the HTML. The issue was with the filter syntax.

## Root Cause

**Incorrect Syntax Used:**
```html
<div data-pagefind-filter-type="Software">...</div>
```

**Correct Syntax (Pagefind Documentation):**
```html
<span data-pagefind-filter="type">Software</span>
```

**Key Differences:**
- Attribute name is `data-pagefind-filter="[filter-name]"`, NOT `data-pagefind-filter-[name]="value"`
- The filter VALUE comes from the element's **text content**, not the attribute value
- The filter NAME is in the attribute value (e.g., "type")

---

## Solutions Applied

### 1. Fixed Theme baseof.html
**File:** `themes/hugo-theme-tailwind/layouts/_default/baseof.html`

Changed from:
```html
<span class="hidden" data-pagefind-filter-type="{{ $contentType }}">{{ $contentType }}</span>
```

To:
```html
<span class="sr-only" data-pagefind-filter="type">Software</span>
```

**Also fixed:**
- Changed `class="hidden"` to `class="sr-only"` to prevent Pagefind from ignoring hidden elements
- Moved from attribute-based value to text-content-based value

### 2. Fixed Blog baseof.html
**File:** `layouts/blog/baseof.html`

Blog posts use a separate baseof template, so needed to add the filter there too:
```html
<span class="sr-only" data-pagefind-filter="type">Blog</span>
```

---

## Verification

### Before Fix
```
Indexed 0 filters
```

### After Fix
```
Indexed 1 filter
```

### Filter Values Present
- ✅ Software pages: `<span data-pagefind-filter="type">Software</span>`
- ✅ People pages: `<span data-pagefind-filter="type">People</span>`
- ✅ Events pages: `<span data-pagefind-filter="type">Events</span>`
- ✅ Resources pages: `<span data-pagefind-filter="type">Resources</span>`
- ✅ Blog posts: `<span data-pagefind-filter="type">Blog</span>`
- ✅ Other pages: `<span data-pagefind-filter="type">Other</span>`

---

## Technical Details

### Pagefind Filter Syntax

According to [Pagefind documentation](https://pagefind.app/docs/filtering/):

```html
<h1>My Blog Post</h1>
<p>
  Author: <span data-pagefind-filter="author">bglw</span>
</p>
```

- `data-pagefind-filter="[name]"` defines the filter name
- The element's text content is the filter value
- Multiple values can exist for the same filter name across different pages

### JavaScript Integration

The JavaScript search code uses the filter name in the API:

```javascript
const filters = { type: selectedTypes };
const search = await pf.search(query, { filters });
```

This matches our filter name "type" from `data-pagefind-filter="type"`.

### Why sr-only Instead of hidden

- `hidden` class uses `display: none` which Pagefind ignores
- `sr-only` (screen reader only) hides visually but keeps in DOM
- Pagefind can still index sr-only elements
- Also benefits accessibility (screen readers can see it)

---

## Commits

1. **88d5634** - Fix Pagefind filter syntax
   - Changed to correct `data-pagefind-filter="type"` syntax
   - Changed from `hidden` to `sr-only` class

2. **1f77db5** - Add filter metadata to blog baseof template
   - Added filter to blog-specific baseof.html

---

## Testing

### Build Status
- ✅ Hugo build: 872 pages, 0 errors
- ✅ Pagefind index: 443 pages, 1 filter detected
- ✅ All content types have correct filter values

### Functional Testing
Now ready for manual testing:
1. Open search modal
2. Type a query (e.g., "ggplot")
3. Verify counts appear: "Software (N)", "People (N)", etc.
4. Toggle filters and verify results update
5. Verify all 6 filter types work (Software, People, Events, Resources, Blog, Other)

---

## Lessons Learned

1. **Always check documentation examples** - The syntax is very specific
2. **Avoid display:none for metadata** - Use sr-only or similar techniques
3. **Check for multiple baseof templates** - Some sections may override
4. **Pagefind output can be misleading** - "0 filters" doesn't mean the HTML is wrong, it means the syntax is wrong

---

## Status

✅ **Issue Resolved**
- Pagefind now detects filters correctly
- All 6 content types have filter metadata
- Filter values properly set in HTML
- Ready for functional testing

---

*Fix completed February 24, 2026*

---

## Update: OR Logic Implementation

**Date:** February 24, 2026
**Issue:** Filters were acting as AND instead of OR
**Status:** ✅ **FIXED**

### Problem

When multiple filter types were selected (e.g., "People" and "Blog"), the search returned zero results. This was because:
- Each page has only ONE type
- AND logic requires results to match ALL selected types
- No page can be both "People" AND "Blog" simultaneously

### Solution

Changed from server-side (Pagefind API) filtering to client-side OR filtering:

**Before:**
```javascript
const filters = { type: selectedTypes };
const search = await pf.search(query, { filters });
```

**After:**
```javascript
const search = await pf.search(query);

for (const result of search.results) {
  const data = await result.data();
  const resultType = data.filters?.type;
  
  if (resultType && selectedTypes.includes(resultType)) {
    filteredResults.push(data);
  }
}
```

### How It Works Now

1. Search **without** filters to get all matching results
2. Filter results **client-side** using `Array.includes()` 
3. Include result if its type matches **ANY** selected checkbox (OR logic)
4. Display filtered results

### Example

Selecting "People" + "Blog":
- ✅ Shows all People pages
- ✅ Shows all Blog posts  
- ✅ Shows combined results from both types

This is proper OR behavior!

---

**Status:** Both filter detection AND OR logic now working correctly! ✅
