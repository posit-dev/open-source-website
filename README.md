# Posit Open Source Website

A static website showcasing Posit's open-source projects, packages, people, events, and blog posts.

## Overview

This website is built using a modern static site generation stack that combines Hugo for fast site building with Quarto for scientific computing content. The site supports multiple content formats including standard Markdown, Quarto documents, and executable Jupyter notebooks.

**Live Site**: https://positopensource.netlify.app

## Tech Stack

- **Hugo** (v0.153.2) - Static site generator
- **Quarto** - Renders scientific documents (.qmd and .ipynb files)
- **Tailwind CSS** (v4.0.17) - Utility-first CSS framework
- **Node.js** (v20) - Build tooling and package management
- **Netlify** - Hosting and deployment

## Project Structure

```
open-source-website/
├── content/                    # Website content (markdown, Quarto, notebooks)
│   ├── blog/                   # Blog posts (.md, .qmd, .ipynb)
│   └── _index.md              # Home page content
├── themes/                    # Hugo themes
│   └── hugo-theme-tailwind/   # Custom Tailwind CSS theme
├── assets/css/                # Stylesheet source files
├── static/                    # Static assets (images, videos)
├── public/                    # Generated site output (build artifact)
├── .github/workflows/         # CI/CD automation
├── hugo.toml                  # Hugo configuration
├── _quarto.yml               # Quarto configuration
├── tailwind.config.js        # Tailwind CSS configuration
└── netlify.toml              # Netlify deployment settings
```

## Getting Started

### Prerequisites

- [just](https://github.com/casey/just) - Command runner
- Node.js v20 or higher
- Hugo Extended v0.153.2 or higher
- Quarto (for rendering .qmd and .ipynb files)

### Installation

```bash
# Install dependencies
just install
```

### Development

```bash
# Start local development server
just dev
```

This command runs Hugo server and Tailwind watcher in parallel. The site will be available at `http://localhost:1313` with live reload enabled.

### Building

```bash
# Build the site (compiles Tailwind CSS and runs Hugo)
just build
```

The generated site will be in the `public/` directory.

### Available Commands

Run `just` to see all available commands:

```bash
just
```

## Content Formats

The site supports three content formats:

- **Markdown (.md)** - Standard Hugo markdown files
- **Quarto documents (.qmd)** - Rich scientific documents with code execution
- **Jupyter notebooks (.ipynb)** - Interactive notebooks with visualizations

Blog posts can be written in any of these formats and placed in `content/blog/`.

## Deployment

The site uses GitHub Actions for CI/CD:

- **Pull Requests**: Automatically deploy preview builds with unique URLs
- **Main Branch**: Automatically deploy to production on Netlify

The deployment pipeline:
1. Install Node.js dependencies
2. Build Tailwind CSS
3. Render Quarto documents
4. Generate static site with Hugo
5. Deploy to Netlify

## License

MIT License - Copyright 2026 posit-dev
