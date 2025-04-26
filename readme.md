<span align="left">
  <img src="logo.png" width="400" alt="parabin logo">
</span>

Tissue is a static web site generator written in Python 3

# T U T O R I A L #

## Lession 1 - hello, world! ##

### This is the directory tree for a minimal project ###

    .
    ├── markdown
    │   └── index.md
    ├── static
    ├── templates
    │   └── template_default.html
    ├── tissue_config.py
    └── tissue.py

- **markdown/**  
  This directory holds all the source content for the site.  
  Each file is written in Markdown (`.md`) and must include a YAML frontmatter section specifying metadata like `title`, `desc`, and `template`.

  Example:  
  - `index.md` → will be rendered into `public/index.html` (or another permalink if specified).

- **static/**  
  This directory contains static assets such as:
  - Stylesheets (`.css`)
  - JavaScript files (`.js`)
  - Images (`.png`, `.jpg`, etc.)

  During the build process, the entire `static/` directory is copied into `public/static/`.

- **templates/**  
  This folder stores HTML templates (`.html`) used to render the site.
  Templates are powered by the Jinja2 templating engine, and they receive variables from the Markdown frontmatter (like `title`, `desc`, and `content`).

  Example:
  - `template_default.html` — the main default layout for rendered pages.

- **tissue_config.py**  
  This file defines the directory structure and build settings for the project:
  - Root project directory
  - Markdown source directory
  - Build output directory
  - Templates directory
  - Static assets directory
  - Sitemap base URL

  Update `sitemap_base_url` here to reflect your production domain (e.g., `https://example.com`).

- **tissue.py**  
  The core site generator script.
  Running `python3 tissue.py` will:
  - Clear and rebuild the `public/` output directory
  - Render each Markdown file into an HTML page
  - Copy static files
  - Render partials
  - Generate a `search_index.json` for client-side search
  - Generate a `sitemap.xml` for SEO and crawler support

---

## 🚀 To Build the Site

In the project root, run:

```bash
python3 tissue.py
```

After building, the output is ready inside the `public/` directory, structured for easy deployment to any static web host (Vercel, Netlify, GitHub Pages, etc).

---



### tissue_config.py — Configuration for Tissue Static Site Generator ###

    from pathlib import Path

    # Directory paths
    ROOT_DIR = Path(__file__).resolve().parent
    MARKDOWN_DIR = ROOT_DIR / "markdown"
    BUILD_DIR = ROOT_DIR / "public"
    TEMPLATE_DIR = ROOT_DIR / "templates"
    STATIC_DIR = ROOT_DIR / "static"
    
    # sitemap.xml config
    sitemap_path = BUILD_DIR / "sitemap.xml"
    sitemap_base_url = "https://domain.io"  # CHANGE THIS!

This file defines key directory paths and settings used throughout the Tissue build process.

    ROOT_DIR — The directory where the project’s Python files are located.

    MARKDOWN_DIR — Location of source markdown files (.md) that Tissue processes into HTML.

    BUILD_DIR — Destination folder for all generated output (ready for deployment). Typically called public/.

    TEMPLATE_DIR — Folder containing Jinja2 templates (.html) used to render pages.

    STATIC_DIR — Folder containing static assets like CSS, JavaScript, and images. Copied into the build automatically.

Additionally, sitemap settings are defined:

    sitemap_path — The path where sitemap.xml will be written inside the BUILD_DIR.

    sitemap_base_url — The base URL of the final website.
    ➔ Important: Update this value to match your deployed domain (e.g., https://example.com).

This file keeps all path and domain configurations in one place, making Tissue easy to adapt for any project structure.
