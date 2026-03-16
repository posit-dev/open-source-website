# Link Checking

How to check links in ported blog posts.

## Running lychee

Use [lychee](https://github.com/lycheeverse/lychee) to check links in ported posts.

### Basic usage

```bash
# Start Hugo dev server first: hugo server
lychee --base-url http://localhost:1313 content/blog/<blog>/*/index.md
```

### Recommended workflow: JSON output

Output to JSON for easier analysis:

```bash
lychee --base-url http://localhost:1313 --format json content/blog/<blog>/*/index.md \
  > content/blog/_lychee/<blog>.json
```

**Step 1: Generate error table**

```bash
scripts/lychee-errors.py content/blog/_lychee/<blog>.json -o content/blog/_lychee/<blog>-errors.md
```

The script prints a summary and generates a markdown table with columns: Domain, Status, URL, Posts, Count.

**Step 2: Fix `localhost` errors first**

Localhost errors are usually fixable issues in the content. Filter the error table for `localhost:1313` rows:

Common localhost issues:
- Missing protocol: `[link](example.com)` → `[link](https://example.com)`
- R code as URL: `[Issue 13](options(...))` → `[Issue 13](https://github.com/.../issues/13)`
- Relative paths that don't exist (vs valid ones like `images/foo.png`)

## Interpreting results

### False positives to ignore

- **Relative file paths** (e.g., `[500] http://localhost:1313/image.png` or `http://localhost:1313/data.csv`) - lychee misresolves relative paths like `![](image.png)` or `[data](./data.csv)` to site root instead of post folder. These work correctly in Hugo. Includes images, data files (`.csv`, `.txt`), and uppercase extensions (`.PNG`).
- **429 Too Many Requests** - GitHub rate limiting. Not broken, just throttled.
- **403 Forbidden** - Some sites block automated requests (NOAA, academic journals).
- **Conference registration links** - `reg.conf.posit.co` often blocks bots.

### Actual issues to fix

- **404 Not Found** - Dead external links
- **Relative paths to other site sections** - e.g., `../r/getstarted/` should be `https://shiny.posit.co/r/getstarted/`
- **Root-relative blog links** - e.g., `../blog/posts/foo/` should be `/blog/shiny/foo/`
- **Malformed URLs** - e.g., `../../https://` from sed replacement gone wrong

## Writing links in source files

**Important:**
- Fix links in BOTH the source file (`.qmd`, `.Rmd`, `.Rmarkdown`, `.ipynb`) AND the rendered file (`.md`, `.markdown`). Otherwise re-rendering will revert your fixes.
- In source files, never use relative links like `../`. Always use site-root paths or absolute URLs.
- Never use `https://posit.co/blog/...` for internal links — that's a different site.

### How Quarto processes links

Quarto's `_quarto.yml` is at `content/` (not `content/blog/`), so site-root links resolve correctly:

| In source file | Rendered `.md` output |
|----------------|----------------------|
| Absolute URL (`https://...`) | Unchanged |
| Site-root (`/blog/foo/`) | Converted to relative (e.g., `../../../blog/foo/`) |
| Relative (`../foo/`) | Unchanged |

Quarto converts site-root links to relative paths based on the output file's location. The paths may look verbose but resolve correctly. Hugo handles both site-root and relative links.

### What to use

| Link type | Use for | Example |
|-----------|---------|---------|
| **Absolute URL** | External sites, legacy blog docs | `https://posit-dev.github.io/pointblank/...` |
| **Site-root** | Internal blog links (this site) | `/blog/great-tables/foo/` |

## Link patterns to fix during porting

| Pattern | Fix |
|---------|-----|
| `https://shiny.posit.co/blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `/blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `../blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `/r/...` or `/py/...` | `https://shiny.posit.co/r/...` or `https://shiny.posit.co/py/...` |
| `../r/...` or `../py/...` | `https://shiny.posit.co/r/...` or `https://shiny.posit.co/py/...` |
| `https://connect.rstudioservices.com/...` | `https://connect.posit.it/...` |
| `../../../../get-started/...` (great-tables) | `https://posit-dev.github.io/great-tables/get-started/...` |
| `../../user-guide/...` (pointblank) | `https://posit-dev.github.io/pointblank/user-guide/...` |
