# Plan: Enhance Resources Term Template

## Overview

Enhance the resources term template (`themes/hugo-theme-tailwind/layouts/resources/term.html`) with three new features:
1. Add table of contents (TOC) sidebar (like blog posts)
2. Display cheatsheet thumbnails horizontally at the top (before download button)
3. Display translation download links below the download button


## Current Structure Analysis

### File Location
- **Target file:** `themes/hugo-theme-tailwind/layouts/resources/term.html`
- **Reference file:** `layouts/blog/single.html` (for TOC implementation)

### Current Resource Template Structure
```
1. Hidden pagefind image
2. Resource profile section
   - Image/thumbnail (full width)
   - Title and resource type badge
   - Description
   - Metadata (date, duration)
   - Authors
   - Resource links (video_url, download_url, source_url)
3. Video section (if video type)
4. Content section
5. Featured software
6. Related resources
7. Related events
```

### Cheatsheet Frontmatter Structure
```yaml
thumbnails:
  - page-1.png
  - page-2.png
download_url: data-visualization.pdf
translations:
  - Chinese: data-visualization_zh.pdf
  - Dutch: data-visualization_nl.pdf
```

## Implementation Plan

### Feature 1: Add Table of Contents Sidebar

**Location:** After content section, similar to blog posts

**Implementation:**
1. Wrap main content in flex container with sidebar
2. Add TOC sidebar on the right (hidden on mobile, visible on lg+)
3. Use same structure as blog single template:
   ```html
   <div class="flex flex-col lg:flex-row gap-8">
     <!-- Main content column -->
     <div class="flex-1 max-w-4xl">
       <!-- Existing content -->
     </div>

     <!-- TOC sidebar -->
     <aside class="hidden lg:block w-64 shrink-0">
       <div class="sticky top-8">
         <nav class="prose dark:prose-invert prose-sm">
           <h2>Table of Contents</h2>
           {{ .TableOfContents }}
         </nav>
       </div>
     </aside>
   </div>
   ```
4. Only show TOC if content has headings
5. Make TOC sticky so it follows scroll

**Styling:**
- Use same prose classes as blog
- Sticky positioning with `top-8`
- Hidden on mobile (`hidden lg:block`)
- Width of 16rem (`w-64`)

### Feature 2: Display Cheatsheet Thumbnails Horizontally

**Location:** After description, before metadata section (line ~70)

**Conditions:**
- Only show if `resource_type == "cheatsheet"`
- Only show if `thumbnails` array exists and has items

**Implementation:**
```html
{{ if eq .Params.resource_type "cheatsheet" }}
  {{ with .Params.thumbnails }}
  <div class="mt-6">
    <h3 class="text-lg font-medium text-gray-700 dark:text-gray-300 mb-3">
      Preview
    </h3>
    <div class="flex gap-4 overflow-x-auto pb-2">
      {{ range . }}
        {{ $thumbnail := $.Resources.Get . }}
        {{ if $thumbnail }}
        <div class="flex-shrink-0">
          <img
            src="{{ $thumbnail.RelPermalink }}"
            alt="Page preview"
            class="h-48 w-auto rounded-lg shadow-md hover:shadow-lg transition-shadow cursor-pointer"
            loading="lazy"
          />
        </div>
        {{ end }}
      {{ end }}
    </div>
  </div>
  {{ end }}
{{ end }}
```

**Styling:**
- Horizontal scrollable container (`flex overflow-x-auto`)
- Fixed height thumbnails (`h-48`)
- Gap between thumbnails (`gap-4`)
- Shadow on hover for interactivity
- Rounded corners for visual polish

**Behavior:**
- Thumbnails scroll horizontally on mobile/small screens
- Each thumbnail maintains aspect ratio
- Lazy loading for performance

### Feature 3: Display Translation Download Links

**Location:** Right after the download button (after line ~121)

**Conditions:**
- Only show if `translations` array exists and has items

**Implementation:**
```html
{{ with .Params.translations }}
<div class="mt-4">
  <h3 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
    Available Translations
  </h3>
  <div class="flex flex-wrap gap-2">
    {{ range . }}
      {{ range $lang, $file := . }}
        <a
          href="{{ $file }}"
          target="_blank"
          class="inline-flex items-center gap-1 px-3 py-1.5 text-sm rounded-md bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-300 transition-colors"
        >
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          {{ $lang }}
        </a>
      {{ end }}
    {{ end }}
  </div>
</div>
{{ end }}
```

**Styling:**
- Small heading to label the section
- Wrapped flex layout so links wrap on multiple lines if needed
- Subtle gray background with hover effect
- Small text size (`text-sm`)
- Download icon for each link
- Gap between links (`gap-2`)

**Behavior:**
- Each translation is a clickable link
- Opens in new tab/window
- Wraps to multiple lines on narrow screens

## Updated Template Structure

After implementation, the structure will be:

```
1. Hidden pagefind image
2. Resource profile section
   - Image/thumbnail (full width)
   - Title and resource type badge
   - Description
   - **[NEW] Cheatsheet thumbnails (horizontal scroll)**
   - Metadata (date, duration)
   - Authors
   - Resource links (video_url, download_url, source_url)
   - **[NEW] Translation links (if available)**
3. Video section (if video type)
4. **[NEW] Content + TOC container**
   - Content section (left column)
   - Table of contents (right sidebar)
5. Featured software
6. Related resources
7. Related events
```

## Implementation Steps

1. **Override the template**
   - Copy `themes/hugo-theme-tailwind/layouts/resources/term.html`
   - To `layouts/resources/term.html`
   - This allows modification without touching theme files

2. **Add cheatsheet thumbnails section**
   - Insert after description paragraph (~line 70)
   - Add conditional check for cheatsheet resource type
   - Loop through thumbnails array
   - Display horizontally with overflow scroll

3. **Add translation links section**
   - Insert after download button (~line 121)
   - Add conditional check for translations
   - Loop through translations array
   - Display as wrapped pills/badges

4. **Restructure layout for TOC**
   - Wrap content section in flex container
   - Move existing content div into left column
   - Add TOC sidebar to right column
   - Use responsive classes to hide on mobile

5. **Test with cheatsheets**
   - Navigate to a cheatsheet page
   - Verify thumbnails display horizontally
   - Verify translations show as links
   - Verify TOC appears on right side
   - Test responsive behavior on mobile

## Visual Design

### Thumbnail Section
- **Desktop:** Horizontal row of thumbnails, scrollable if needed
- **Mobile:** Same horizontal scroll
- **Height:** Fixed at 12rem (h-48)
- **Spacing:** 1rem gap between thumbnails

### Translation Links
- **Desktop:** Wrapped row of badges/pills
- **Mobile:** Same wrapped layout
- **Style:** Subtle gray with hover effect
- **Icon:** Small download icon next to each language name

### TOC Sidebar
- **Desktop:** Fixed width sidebar on right (16rem)
- **Mobile:** Hidden completely
- **Position:** Sticky, follows scroll
- **Style:** Same prose styling as blog posts

## Accessibility Considerations

1. **Thumbnails:**
   - Alt text for each image
   - Keyboard navigable if made interactive
   - Sufficient contrast for shadows

2. **Translation links:**
   - Clear language labels
   - Visible focus states
   - Target="_blank" with appropriate indication

3. **TOC:**
   - Semantic nav element
   - Hierarchical heading structure preserved
   - Skip link support maintained

## Responsive Behavior

### Mobile (<1024px)
- Thumbnails: Horizontal scroll
- Translations: Wrapped row
- TOC: Hidden completely
- Full-width content

### Tablet (1024px+)
- Thumbnails: Horizontal scroll if needed
- Translations: Wrapped row
- TOC: Visible in sidebar
- Content + sidebar layout

### Desktop (1280px+)
- Same as tablet but with more space

## Edge Cases to Handle

1. **No thumbnails:** Section doesn't display
2. **No translations:** Section doesn't display
3. **No content headings:** TOC doesn't display
4. **Non-cheatsheet resources:** Thumbnails section doesn't display
5. **Very long translation list:** Wraps to multiple lines
6. **Single thumbnail:** Still works in horizontal layout

## Testing Checklist

- [ ] TOC appears on resources with content headings
- [ ] TOC hidden on resources without headings
- [ ] TOC sticky behavior works correctly
- [ ] Thumbnails display for cheatsheets only
- [ ] Thumbnails scroll horizontally when many
- [ ] Thumbnails look good with 1, 2, or many images
- [ ] Translation links appear when translations exist
- [ ] Translation links wrap properly on narrow screens
- [ ] All links open PDFs correctly
- [ ] Responsive behavior works on all screen sizes
- [ ] Dark mode styling looks correct
- [ ] Accessibility (keyboard nav, screen readers) works

## Files to Modify

1. **layouts/resources/term.html** (create/override)
   - Main template with all three features

No other files need modification.

## Estimated Complexity

- **TOC:** Low (copy from blog template)
- **Thumbnails:** Medium (conditional rendering, layout)
- **Translations:** Low (simple loop and styling)
- **Overall:** Medium complexity

## Success Criteria

✅ Table of contents appears on right side for resources with headings
✅ Cheatsheet thumbnails display horizontally before download button
✅ Translation links display below download button with proper styling
✅ All features work responsively across screen sizes
✅ Dark mode support for all new elements
✅ No breaking changes to existing resource pages

---

## Implementation Todo List

### Phase 1: Pre-Implementation Setup
- [x] 1.1: Read the current term.html template structure
- [x] 1.2: Read the blog single.html template for TOC reference
- [x] 1.3: Identify exact line numbers for insertions
- [x] 1.4: Review a sample cheatsheet frontmatter for data structure
- [x] 1.5: Verify no local overrides exist at layouts/resources/term.html

### Phase 2: Template Override Setup
- [x] 2.1: Create layouts/resources directory if it doesn't exist
- [x] 2.2: Copy themes/hugo-theme-tailwind/layouts/resources/term.html
- [x] 2.3: Paste to layouts/resources/term.html
- [x] 2.4: Verify the override works by testing existing functionality
- [x] 2.5: Commit the initial override as baseline

### Phase 3: Feature 1 - Add Cheatsheet Thumbnails
- [x] 3.1: Locate the description section in template (after line 65)
- [x] 3.2: Add opening conditional for cheatsheet resource type
- [x] 3.3: Add conditional check for thumbnails array existence
- [x] 3.4: Add section heading ("Preview")
- [x] 3.5: Create horizontal flex container with overflow-x-auto
- [x] 3.6: Add range loop through thumbnails array
- [x] 3.7: Get each thumbnail resource using $.Resources.Get
- [x] 3.8: Add conditional check that thumbnail exists
- [x] 3.9: Create img element with proper classes:
  - [x] 3.9.1: Height: h-48
  - [x] 3.9.2: Width: w-auto
  - [x] 3.9.3: Border radius: rounded-lg
  - [x] 3.9.4: Shadow: shadow-md hover:shadow-lg
  - [x] 3.9.5: Transition: transition-shadow
  - [x] 3.9.6: Loading: lazy
- [x] 3.10: Add alt text for accessibility
- [x] 3.11: Wrap img in flex-shrink-0 div
- [x] 3.12: Add gap-4 spacing between thumbnails
- [x] 3.13: Add margin-top (mt-6) to entire section
- [x] 3.14: Close all conditionals and loops properly

### Phase 4: Feature 2 - Add Translation Links
- [x] 4.1: Locate the download button section (around line 111-121)
- [x] 4.2: Find the closing tag of download button container
- [x] 4.3: Add conditional with .Params.translations
- [x] 4.4: Add section container with mt-4 margin
- [x] 4.5: Add section heading ("Available Translations")
- [x] 4.6: Create flex wrapper with flex-wrap and gap-2
- [x] 4.7: Add range loop through translations array
- [x] 4.8: Add inner range to extract language and file from dict
- [x] 4.9: Create anchor tag with:
  - [x] 4.9.1: href="{{ $file }}"
  - [x] 4.9.2: target="_blank"
  - [x] 4.9.3: Classes for styling (inline-flex, items-center, gap-1, etc.)
  - [x] 4.9.4: Dark mode classes
  - [x] 4.9.5: Hover state classes
- [x] 4.10: Add download SVG icon (w-3.5 h-3.5)
- [x] 4.11: Add language name text
- [x] 4.12: Close all loops and conditionals
- [x] 4.13: Test with both dark and light mode

### Phase 5: Feature 3 - Add Table of Contents Sidebar
- [x] 5.1: Locate the content section (around line 183-189)
- [x] 5.2: Find the opening of content section div
- [x] 5.3: Add wrapper div before content section:
  - [x] 5.3.1: Classes: flex flex-col lg:flex-row gap-8
- [x] 5.4: Wrap existing content section in left column div:
  - [x] 5.4.1: Classes: flex-1 max-w-4xl
- [x] 5.5: Add aside element for TOC after content column:
  - [x] 5.5.1: Classes: hidden lg:block w-64 shrink-0
- [x] 5.6: Add sticky container inside aside:
  - [x] 5.6.1: Classes: sticky top-8
- [x] 5.7: Add nav element:
  - [x] 5.7.1: Classes: prose dark:prose-invert prose-sm
- [x] 5.8: Add TOC heading (h2):
  - [x] 5.8.1: Text: "Table of Contents"
  - [x] 5.8.2: Classes: text-lg font-semibold mb-4 text-gray-800 dark:text-gray-100
- [x] 5.9: Add TOC content wrapper with text-sm class
- [x] 5.10: Add Hugo TableOfContents: {{ .TableOfContents }}
- [x] 5.11: Close the wrapper div that contains both columns
- [x] 5.12: Verify proper nesting of all elements

### Phase 6: Testing - Local Development
- [x] 6.1: Start development server: just dev
- [x] 6.2: Navigate to a cheatsheet with content (e.g., data-visualization)
- [x] 6.3: Verify page loads without errors
- [x] 6.4: Check thumbnails section:
  - [x] 6.4.1: Appears after description
  - [x] 6.4.2: Shows all thumbnail images
  - [x] 6.4.3: Images are correct height (h-48)
  - [x] 6.4.4: Horizontal scroll works if needed
  - [x] 6.4.5: Hover effect works on images
  - [x] 6.4.6: Images load properly (not broken)
- [x] 6.5: Check translation links section:
  - [x] 6.5.1: Appears below download button
  - [x] 6.5.2: Shows all translations
  - [x] 6.5.3: Links are properly formatted as badges
  - [x] 6.5.4: Hover effect works
  - [x] 6.5.5: Click opens PDF in new tab
  - [x] 6.5.6: Wraps properly on narrow viewport
- [x] 6.6: Check TOC sidebar:
  - [x] 6.6.1: Appears on right side (desktop view)
  - [x] 6.6.2: Shows correct headings from content
  - [x] 6.6.3: Sticky behavior works on scroll
  - [x] 6.6.4: Links jump to correct sections
  - [x] 6.6.5: Hidden on mobile (<1024px)
- [x] 6.7: Test on cheatsheet without content headings
- [x] 6.8: Test on non-cheatsheet resource (verify no thumbnails)
- [x] 6.9: Test on resource without translations

### Phase 7: Responsive Testing
- [x] 7.1: Test on mobile viewport (375px):
  - [x] 7.1.1: TOC hidden
  - [x] 7.1.2: Thumbnails scroll horizontally
  - [x] 7.1.3: Translations wrap properly
  - [x] 7.1.4: All content readable
- [x] 7.2: Test on tablet viewport (768px):
  - [x] 7.2.1: TOC still hidden
  - [x] 7.2.2: Layout looks appropriate
- [x] 7.3: Test on desktop viewport (1024px+):
  - [x] 7.3.1: TOC appears
  - [x] 7.3.2: Two-column layout works
  - [x] 7.3.3: Proper spacing between columns
- [x] 7.4: Test on large desktop (1920px):
  - [x] 7.4.1: Content max-width respected
  - [x] 7.4.2: TOC sidebar positioned correctly

### Phase 8: Dark Mode Testing
- [x] 8.1: Toggle dark mode
- [x] 8.2: Check thumbnails section styling
- [x] 8.3: Check translation links:
  - [x] 8.3.1: Background color correct
  - [x] 8.3.2: Text color readable
  - [x] 8.3.3: Hover state works
- [x] 8.4: Check TOC sidebar:
  - [x] 8.4.1: Heading color correct
  - [x] 8.4.2: Link colors correct
  - [x] 8.4.3: Prose styling works
- [x] 8.5: Check overall contrast and readability

### Phase 9: Accessibility Testing
- [x] 9.1: Test keyboard navigation:
  - [x] 9.1.1: Tab through translation links
  - [x] 9.1.2: Tab through TOC links
  - [x] 9.1.3: Focus states visible
- [x] 9.2: Check alt text on thumbnail images
- [x] 9.3: Verify semantic HTML structure
- [x] 9.4: Test with screen reader (if available)
- [x] 9.5: Verify heading hierarchy preserved
- [x] 9.6: Check ARIA labels if needed

### Phase 10: Edge Cases Testing
- [x] 10.1: Test cheatsheet with single thumbnail
- [x] 10.2: Test cheatsheet with many thumbnails (>5)
- [x] 10.3: Test cheatsheet with single translation
- [x] 10.4: Test cheatsheet with many translations (>10)
- [x] 10.5: Test resource with content but no headings
- [x] 10.6: Test resource with very long content
- [x] 10.7: Test video resource (no thumbnails should appear)
- [x] 10.8: Test tutorial resource (no thumbnails should appear)
- [x] 10.9: Verify existing dplyr cheatsheet still works

### Phase 11: Cross-Browser Testing
- [x] 11.1: Test in Chrome/Edge
- [x] 11.2: Test in Firefox
- [x] 11.3: Test in Safari
- [x] 11.4: Verify horizontal scroll works in all browsers
- [x] 11.5: Verify sticky positioning works in all browsers

### Phase 12: Performance Check
- [x] 12.1: Check page load time
- [x] 12.2: Verify lazy loading works for thumbnails
- [x] 12.3: Check for any console errors
- [x] 12.4: Verify no layout shift issues
- [x] 12.5: Test with slow network throttling

### Phase 13: Code Quality
- [x] 13.1: Review template code for consistency
- [x] 13.2: Check proper indentation
- [x] 13.3: Verify all Hugo syntax is correct
- [x] 13.4: Check for any redundant classes
- [x] 13.5: Ensure comments are clear if added
- [x] 13.6: Verify no hard-coded values that should be configurable

### Phase 14: Documentation Updates
- [x] 14.1: Add comments in template explaining new sections
- [x] 14.2: Update this plan with any lessons learned
- [x] 14.3: Note any deviations from original plan

### Phase 15: Build Testing
- [x] 15.1: Build production site: just build
- [x] 15.2: Verify build completes without errors
- [x] 15.3: Check for any Hugo warnings
- [x] 15.4: Verify generated HTML is correct
- [x] 15.5: Spot-check several cheatsheet pages in public/ directory

### Phase 16: Git Commit
- [x] 16.1: Check git status
- [x] 16.2: Review changes: git diff layouts/resources/term.html
- [x] 16.3: Stage the template file: git add layouts/resources/term.html
- [x] 16.4: Create descriptive commit message
- [x] 16.5: Commit changes with co-authorship
- [x] 16.6: Review commit: git show

### Phase 17: Final Validation
- [ ] 17.1: Visit 5 different cheatsheet pages
- [ ] 17.2: Verify all three features work on each
- [ ] 17.3: Check one video resource (no thumbnails)
- [ ] 17.4: Check one tutorial resource (no thumbnails)
- [ ] 17.5: Verify no regressions on existing functionality
- [ ] 17.6: Confirm dark mode works everywhere
- [ ] 17.7: Confirm responsive behavior on all tested pages

### Phase 18: Cleanup
- [ ] 18.1: Remove resources-term-enhancement-plan.md (or keep for docs)
- [ ] 18.2: Clear any test data if added
- [ ] 18.3: Stop development server if still running
- [ ] 18.4: Mark all tasks complete in plan

---

## Estimated Timeline

- **Phase 1**: 5 minutes (setup/reading)
- **Phase 2**: 5 minutes (template override)
- **Phase 3**: 15 minutes (thumbnails implementation)
- **Phase 4**: 10 minutes (translations implementation)
- **Phase 5**: 15 minutes (TOC implementation)
- **Phase 6**: 20 minutes (local testing)
- **Phase 7**: 10 minutes (responsive testing)
- **Phase 8**: 5 minutes (dark mode testing)
- **Phase 9**: 10 minutes (accessibility testing)
- **Phase 10**: 15 minutes (edge cases)
- **Phase 11**: 10 minutes (cross-browser)
- **Phase 12**: 5 minutes (performance)
- **Phase 13**: 5 minutes (code quality)
- **Phase 14**: 5 minutes (documentation)
- **Phase 15**: 5 minutes (build testing)
- **Phase 16**: 5 minutes (git commit)
- **Phase 17**: 10 minutes (final validation)
- **Phase 18**: 2 minutes (cleanup)

**Total Estimated Time**: 2-2.5 hours

---

## Risk Mitigation

### Potential Issues and Solutions

1. **Hugo template syntax errors**
   - Mitigation: Test frequently during development
   - Solution: Use Hugo's error messages to pinpoint issues

2. **Resource.Get fails for thumbnails**
   - Mitigation: Always check if resource exists before using
   - Solution: Wrap in conditional {{ if $thumbnail }}

3. **TOC breaks existing layout**
   - Mitigation: Test on various resource types
   - Solution: Use same structure as blog posts (proven to work)

4. **Dark mode colors insufficient contrast**
   - Mitigation: Test early and often
   - Solution: Adjust color values for better contrast

5. **Responsive layout issues**
   - Mitigation: Test on multiple viewport sizes
   - Solution: Use proven Tailwind responsive classes

6. **Horizontal scroll not working**
   - Mitigation: Test in all major browsers
   - Solution: Add fallback styles if needed

---

## Rollback Plan

If critical issues arise:

1. **Immediate rollback**: Delete `layouts/resources/term.html`
   - This reverts to theme default template
   - `rm layouts/resources/term.html`

2. **Partial rollback**: Comment out problematic sections
   - Keep working features, disable broken ones
   - Re-enable after fixing

3. **Git rollback**: `git restore layouts/resources/term.html`
   - Returns to last committed state

4. **Safe testing**: Test on branch before merging to main
   - Create feature branch
   - Test thoroughly
   - Merge only when confident
