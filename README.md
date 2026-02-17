# Posit Open Source Website

An interconnected knowledge hub showcasing 356+ open-source software projects from the Posit ecosystem, along with the people behind them, blog posts, events, and learning resources.

## Overview

This website is a data-driven catalog that brings together software, people, and resources into a cohesive community portal. Each project page features automatically synchronized metadata from GitHub—including stars, releases, and contributor activity—while connecting visitors to the team members behind the code, related blog posts, tutorials, and educational materials.

The site uses a modern static site generation stack combining Hugo for fast site building with Quarto for scientific computing content, supporting multiple content formats including standard Markdown, Quarto documents, and executable Jupyter notebooks.

**Live Site**: https://positopensource.netlify.app

## Tech Stack

- **Hugo** (v0.153.2) - Static site generator
- **Quarto** - Renders scientific documents (.qmd and .ipynb files)
- **Tailwind CSS** (v4.0.17) - Utility-first CSS framework
- **Pagefind** (v1.4.0) - Static site search indexing
- **Node.js** (v20) - Build tooling and package management
- **Python** - Automation scripts for GitHub data synchronization
- **UV** - Python package manager (for Quarto and scripts)
- **Netlify** - Hosting and deployment

## Project Structure

```
open-source-website/
├── content/                      # Website content (markdown, Quarto, notebooks)
│   ├── _index.md                # Home page content
│   ├── blog/                    # Blog posts (356+ entries in .md, .qmd, .ipynb)
│   ├── software/                # Software projects (356+ entries)
│   │   ├── ggplot2/_index.md   # Individual software pages
│   │   └── ...
│   ├── people/                  # Team member profiles (45+ entries)
│   ├── events/                  # Event pages
│   ├── resources/               # Learning resources
│   │   ├── tutorials.md
│   │   ├── videos.md
│   │   ├── cheatsheets.md
│   │   └── webinars.md
│   └── categories/              # Category taxonomy pages
│
├── themes/                      # Hugo themes
│   └── hugo-theme-tailwind/     # Custom Tailwind CSS theme
│       ├── layouts/             # Theme template files
│       ├── assets/              # Theme stylesheets
│       └── i18n/                # Internationalization files
│
├── layouts/                     # Project-specific template overrides
│   ├── _default/               # Default layouts
│   ├── blog/                   # Blog-specific layouts
│   ├── categories/             # Category page layouts
│   ├── events/                 # Event listing layouts
│   ├── people/                 # People/team page layouts
│   ├── resources/              # Resource type layouts
│   ├── software/               # Software catalog layouts
│   ├── partials/               # Reusable template components
│   └── shortcodes/             # Custom Hugo shortcodes
│
├── assets/                      # Web assets
│   └── css/                     # CSS source files
│       └── main.css            # Tailwind CSS input file
│
├── static/                      # Static files (served as-is)
│   └── images/                 # Static images
│
├── data/                        # Data files
│   ├── github-repos.toml        # GitHub repository metadata (496KB, 356+ repos)
│   └── github-orgs.toml         # GitHub organization metadata
│
├── scripts/                     # Python automation scripts
│   ├── create-new-software.py           # Create new software project pages
│   ├── update-github-repos.py           # Sync data from GitHub API
│   ├── update-software-frontmatter.py   # Update software YAML from github-repos.toml
│   ├── download-software-images.py      # Download project logos
│   ├── download-software-readmes.py     # Fetch README files
│   └── summarize-software-readmes.py    # Generate AI summaries
│
├── archetypes/                  # Content templates for hugo new
│   ├── default.md
│   └── blog.md
│
├── public/                      # Generated site output (build artifact, gitignored)
│
├── .github/workflows/           # CI/CD automation
│   ├── deploy.yml              # Main deployment workflow
│   └── netlify-cleanup.yml     # Preview cleanup on PR close
│
└── Configuration Files
    ├── hugo.toml                # Hugo configuration
    ├── _quarto.yml             # Quarto configuration
    ├── tailwind.config.js       # Tailwind CSS configuration
    ├── netlify.toml            # Netlify deployment settings
    ├── package.json            # NPM dependencies
    └── justfile                # Task runner commands
```

## Key Features

### Software Catalog
- **356+ projects** with rich metadata automatically synced from GitHub
- **Data-driven architecture** using `data/github-repos.toml` as the source of truth
- **People cross-referencing** linking contributors across projects and blog posts
- **Search** powered by Pagefind for fast static site search

### Content Types
- **Blog posts** in Markdown, Quarto, and Jupyter notebook formats
- **Software pages** with logos, descriptions, GitHub stats, releases, and contributors
- **People profiles** with social links, roles, and associated projects
- **Events** with dates, locations, and associated content
- **Resources** including tutorials, videos, cheatsheets, and webinars

### Taxonomies
Custom Hugo taxonomies for organizing content:
- `software` - Software projects
- `person` - People/team members
- `category` - Content categories
- `tag` - Content tags
- `languages` - Programming languages
- `event` - Events
- `resource` - Learning resources

## Getting Started

### Prerequisites

- [just](https://github.com/casey/just) - Command runner
- **Node.js** v20 or higher
- **Hugo Extended** v0.153.2 or higher
- **Quarto** (for rendering .qmd and .ipynb files)
- **UV** (Python package manager) - `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Python** 3.8+ (for automation scripts)

### Installation

```bash
# Install Node.js dependencies
just install
```

### Development

```bash
# Start local development server (Hugo + Tailwind watcher)
just dev
```

This command runs Hugo server and Tailwind watcher in parallel. The site will be available at `http://localhost:1313` with live reload enabled.

### Building

```bash
# Build Tailwind CSS
just build-tailwind

# Build the site (compiles Tailwind CSS and runs Hugo)
just build

# Build search index (run after hugo build)
just build-search
```

The generated site will be in the `public/` directory.

### Available Commands

Run `just` (without arguments) to see all available commands:

```bash
just                             # List all available commands
just install                     # Install Node.js dependencies
just dev                         # Run Hugo + Tailwind dev servers in parallel
just build                       # Build Tailwind CSS + Hugo site
just build-tailwind              # Build Tailwind CSS only
just build-search                # Generate Pagefind search index
just update-github-repos         # Sync GitHub repository metadata to data/github-repos.toml
just update-software-frontmatter # Update software frontmatter from github-repos.toml
just quarto-preview              # Preview Quarto documents
just hugo-serve                  # Start Hugo dev server with drafts
```

## Content Management

### Adding Software Projects

Software projects are managed through a two-step process:

1. **Create the software page** (one-time):
   ```bash
   ./scripts/create-new-software.py
   ```
   This creates a new directory under `content/software/` with a `_index.md` file containing the initial frontmatter.

2. **Update metadata from GitHub** (automatic):
   ```bash
   just update-github-repos          # Fetch latest data from GitHub API
   just update-software-frontmatter  # Update frontmatter in all software pages
   ```

### Software Frontmatter Structure

Each software project's `_index.md` file contains YAML frontmatter with the following structure:

```yaml
---
# Manual fields (edited by humans)
title: ggplot2
description: An implementation of the Grammar of Graphics in R
github: tidyverse/ggplot2
website: https://ggplot2.tidyverse.org
image: ggplot2.png
languages:
  - R
people:
  - Hadley Wickham
  - Winston Chang
latest_release: '2026-02-02T09:41:41+00:00'

# Optional control fields (see below)
include:
  languages:
    - Python

exclude:
  people:
    - Bot User

override:
  description: Custom description that overrides external data

# Automatic external data (do not edit manually)
external:
  repo: tidyverse/ggplot2
  title: ggplot2
  description: An implementation of the Grammar of Graphics in R
  website: https://ggplot2.tidyverse.org
  stars: 6876
  forks: 2132
  latest_release: '2026-02-02T09:41:41+00:00'
  first_commit: '2008-05-25T01:21:32+00:00'
  license: MIT
  readme_image: man/figures/logo.png
  last_updated: '2026-02-13T14:17:08+00:00'
  languages:
    - R
  people:
    - Hadley Wickham
    - Winston Chang
---

Content about the software project goes here...
```

### Understanding Frontmatter Control Fields

The software frontmatter uses a powerful system to manage data that comes from GitHub while allowing manual overrides. There are four special keys that control how top-level fields are computed:

#### `external` (automatic, do not edit)

Contains metadata automatically fetched from GitHub via the `update-github-repos.py` script:
- `repo` - GitHub repository path (e.g., "tidyverse/ggplot2")
- `title` - Repository name
- `description` - Repository description
- `website` - Project website URL
- `stars` - Number of GitHub stars
- `forks` - Number of forks
- `latest_release` - ISO timestamp of latest release
- `first_commit` - ISO timestamp of first commit
- `license` - SPDX license identifier
- `readme_image` - Path to logo in repository
- `last_updated` - When this data was last synced
- `languages` - List of programming languages detected
- `people` - List of contributor names (mapped from GitHub usernames)

**Important**: Never edit the `external` section manually! It gets overwritten every time `update-software-frontmatter.py` runs.

#### `include` (optional, manual)

Adds items to list fields from the `external` section. Useful when you want to add additional metadata that GitHub doesn't provide.

**Example**: A Rust-based R package where you want to highlight R as well:
```yaml
include:
  languages:
    - R
```

This adds "R" to the languages list in addition to what GitHub detects (e.g., "Rust").

**Result**: If `external.languages` is `["Rust"]`, the top-level `languages` becomes `["Rust", "R"]`.

#### `exclude` (optional, manual)

Removes items from list fields. Useful for filtering out unwanted entries from GitHub data.

**Example**: Remove bot accounts or non-primary contributors:
```yaml
exclude:
  people:
    - dependabot[bot]
    - github-actions[bot]
```

**Result**: These names will be filtered out of the top-level `people` list.

#### `override` (optional, manual)

Completely replaces a field value, ignoring the `external` data. Useful when you need full control over a specific field.

**Example**: Provide a better description than GitHub's:
```yaml
override:
  description: A comprehensive data visualization system implementing the Grammar of Graphics
```

**Result**: The top-level `description` uses this value instead of `external.description`.

#### Processing Order

The `update-software-frontmatter.py` script computes top-level fields using this logic:

1. **Start** with values from `external`
2. **Include** - For list values (`people`, `languages`), add items from `include`
3. **Exclude** - For list values, remove items from `exclude`
4. **Override** - Apply `override`, which replaces the value completely

**Fields affected**: `title`, `people`, `description`, `website`, `latest_release`, `languages`

#### Practical Example

```yaml
---
# These top-level fields are computed automatically
title: air
description: R formatter and language server
languages:
  - Rust
  - R
people:
  - Lionel Henry
  - Davis Vaughan

# Manual override: we want to show R prominently even though it's primarily Rust
include:
  languages:
    - R

# External data from GitHub (auto-updated, do not edit)
external:
  repo: posit-dev/air
  stars: 389
  languages:
    - Rust
  people:
    - Lionel Henry
    - Davis Vaughan
---
```

**Result**: Even though GitHub detects only Rust, the final `languages` list includes both Rust and R.

### Writing Blog Posts

Blog posts can be written in three formats:

```bash
# Markdown
content/blog/my-post/index.md

# Quarto document (with executable code)
content/blog/my-post/index.qmd

# Jupyter notebook
content/blog/my-post/index.ipynb
```

Use the blog archetype to create new posts:
```bash
hugo new blog/my-post/index.md
```

### Adding Team Members

Create a new person profile:
```bash
hugo new people/firstname-lastname/_index.md
```

Edit the frontmatter to include:
```yaml
---
title: "Full Name"
role: "Software Engineer"
github: "github-username"
linkedin: "linkedin-username"
website: "https://..."
image: "photo.jpg"
---
```

The `github` field is crucial—it's used to link contributors to software projects automatically.

## Data Synchronization

### GitHub Metadata Sync

The site maintains a local cache of GitHub metadata in `data/github-repos.toml`. To update:

```bash
# Requires GH_TOKEN environment variable (GitHub personal access token)
export GH_TOKEN="ghp_..."

# Fetch latest data from GitHub API and update github-repos.toml
just update-github-repos

# Update all software frontmatter files from the updated data
just update-software-frontmatter
```

**What gets synced**:
- Repository metadata (stars, forks, license)
- Latest release date and version
- First commit date
- Primary programming language
- Contributors (top contributors by commit count)
- README image paths

### Environment Variables

Create a `.env` file in the project root (gitignored):

```bash
# GitHub personal access token (for update-github-repos.py)
# Get one at: https://github.com/settings/tokens
GH_TOKEN="ghp_your_token_here"

# Plausible Analytics API key (optional, for analytics integration)
PLAUSIBLE_KEY="your_key_here"
```

## Deployment

### Automatic Deployment

The site uses GitHub Actions for CI/CD (`.github/workflows/deploy.yml`):

1. **Pull Requests**: Automatically deploy preview builds with unique URLs
   - Preview URLs are posted as PR comments
   - Previews are cleaned up when PRs close

2. **Main Branch**: Automatically deploy to production on Netlify
   - Triggers on push to `main`
   - Full build + search index generation

### Deployment Pipeline

The complete build process:

```bash
# 1. Install dependencies
npm ci

# 2. Build Tailwind CSS (minified)
npm run build-tailwind

# 3. Build Hugo site (minified)
hugo --minify

# 4. Generate Pagefind search index
npm run build-search

# 5. Deploy to Netlify
# (automated by GitHub Actions)
```

### Manual Deployment

To deploy manually (requires Netlify CLI):

```bash
# Build the site
just build
just build-search

# Deploy to Netlify
netlify deploy --prod
```

### Netlify Configuration

Key settings in `netlify.toml`:

- **Hugo version**: 0.153.2
- **Node version**: 20
- **Build command**: Full pipeline (Tailwind + Hugo + Pagefind)
- **Security headers**: X-Frame-Options, X-XSS-Protection, Referrer-Policy
- **Cache headers**: 1-year cache for static assets
- **Publish directory**: `public/`

## Development Tips

### Hot Reload

The `just dev` command runs both Hugo and Tailwind in watch mode:
- Hugo rebuilds on content/template changes
- Tailwind rebuilds CSS on class usage changes
- Browser auto-refreshes via Hugo's LiveReload

### Searching Content

Use the search modal on the live site (powered by Pagefind). To rebuild the search index locally:

```bash
hugo
just build-search
# Then serve the public/ directory
```

### Theme Customization

The custom theme is in `themes/hugo-theme-tailwind/`. Override any template by creating the same path under `layouts/`:

```
themes/hugo-theme-tailwind/layouts/partials/header.html  # Theme default
layouts/partials/header.html                              # Project override (wins)
```

### Tailwind Classes

Tailwind scans these paths for class usage:
- `themes/hugo-theme-tailwind/layouts/**/*.html`
- `layouts/**/*.html`
- `content/**/*.md`
- `safelist.txt` (pre-defined classes for dynamic use)

### Debugging

```bash
# Start Hugo with verbose logging
hugo server --verbose --debug

# Check Hugo environment
hugo env

# Validate site structure
hugo config
```

## Content Formats

### Markdown (.md)

Standard Hugo markdown files with YAML frontmatter:

```markdown
---
title: "My Post"
date: 2026-02-17
---

Content here...
```

### Quarto Documents (.qmd)

Rich scientific documents with executable code:

```markdown
---
title: "My Analysis"
format: html
---

## Analysis

\```{r}
library(ggplot2)
ggplot(mtcars, aes(mpg, wt)) + geom_point()
\```
```

Preview Quarto documents:
```bash
just quarto-preview
```

### Jupyter Notebooks (.ipynb)

Interactive notebooks with Python/R code and visualizations. Place `.ipynb` files in blog post directories—Quarto will render them automatically during the Hugo build.

## Architecture Notes

### Static Site Generation

This is a **purely static site**—no server-side rendering or APIs. All content is pre-generated at build time:

1. Hugo processes Markdown and templates
2. Quarto renders .qmd and .ipynb files to HTML
3. Tailwind generates optimized CSS
4. Pagefind builds a static search index
5. Output is pure HTML/CSS/JS

### Data Flow

```
GitHub API
    ↓
data/github-repos.toml (via update-github-repos.py)
    ↓
content/software/*/_index.md frontmatter (via update-software-frontmatter.py)
    ↓
Hugo templates render pages
    ↓
Static HTML in public/
```

### People Cross-Referencing

1. People profiles in `content/people/` have `github` field
2. `update-software-frontmatter.py` maps GitHub usernames to people names
3. Software pages link to people via the `people` frontmatter field
4. Hugo templates create bidirectional links automatically

## Contributing

### Adding a New Software Project

1. Run the creation script:
   ```bash
   ./scripts/create-new-software.py
   ```

2. Edit `content/software/your-project/_index.md`:
   - Set `github` field to the repository (e.g., "posit-dev/positron")
   - Add a logo image if available
   - Optionally add `include`, `exclude`, or `override` fields

3. Sync metadata:
   ```bash
   just update-github-repos
   just update-software-frontmatter
   ```

4. Commit the changes:
   ```bash
   git add content/software/your-project/
   git commit -m "Add your-project to software catalog"
   ```

### Updating Software Metadata

To refresh all software metadata from GitHub:

```bash
# Fetch latest from GitHub (requires GH_TOKEN)
just update-github-repos

# Update all software frontmatter
just update-software-frontmatter

# Commit the changes
git add content/software/ data/github-repos.toml
git commit -m "Update software metadata from GitHub"
```

### Style Guide

- Use **sentence case** for titles (not Title Case)
- Write descriptions that explain **what** and **why**, not just feature lists
- Keep blog post descriptions under 160 characters (for SEO)
- Use relative links for internal content: `[link]({{< relref "path" >}})`

## Troubleshooting

### Build Failures

```bash
# Clear Hugo cache
hugo --gc

# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Check Hugo version
hugo version  # Should be v0.153.2 or higher

# Check Node version
node --version  # Should be v20 or higher
```

### Search Not Working

```bash
# Rebuild search index
hugo
just build-search

# Verify pagefind/ directory exists in public/
ls -la public/pagefind/
```

### Quarto Issues

```bash
# Check Quarto installation
quarto --version

# Reinstall Quarto (if needed)
# See: https://quarto.org/docs/get-started/

# Preview individual Quarto file
quarto preview path/to/file.qmd
```

### GitHub Rate Limiting

The `update-github-repos.py` script may hit GitHub API rate limits:

```bash
# Check your rate limit status
curl -H "Authorization: token $GH_TOKEN" https://api.github.com/rate_limit

# Wait for rate limit reset or use a token with higher limits
```

## License

MIT License - Copyright 2026 Posit PBC

## Questions or Issues?

- **GitHub Issues**: https://github.com/posit-dev/open-source-website/issues
- **Internal Wiki**: (link to internal documentation if applicable)
