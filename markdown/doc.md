---
title: Doc
desc: Tissue Doc
image: /static/img/docs.png
template: template_default.html
permalink: /doc/
---
Tissue Doc

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

The pages of a static site are stored as Markdown files in the /markdown directory at the root of the project. Each file has a .md extension. For example, the Markdown file index.md will be rendered as index.html.

The file tissue.py is the site generator. To build the site, run the command `python3 tissue.py`.

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
