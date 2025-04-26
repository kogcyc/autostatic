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

The pages that make up a static site are stored as Markdown files in the /markdown directory at the root of a project. Those files has an extension of .md. In this example is the Markdown file for the index.html file.

The file named tissue.py is the generator. You run the command `python3 tissue.py` to 'build' the site.

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

