---
title: Doc
desc: Tissue Doc
image: /static/img/docs.png
template: template_default.html
permalink: /doc/
---
Tissue Doc

Tissue is a static web site generator written in Python 3

# Lession 1 - hello, world! #

<span class="docheader">This is the directory tree for a minimal project</span>

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

### CONFIGURATION ###

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

