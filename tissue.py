import os
import shutil
import frontmatter
import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from tissue_config import MARKDOWN_DIR, BUILD_DIR, TEMPLATE_DIR, STATIC_DIR

# Clean and recreate build directory
if BUILD_DIR.exists():
    shutil.rmtree(BUILD_DIR)
BUILD_DIR.mkdir(parents=True)

# Copy static files
if STATIC_DIR.exists():
    shutil.copytree(STATIC_DIR, BUILD_DIR / "static")

# Set up Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

# Gather pages
index = []

for md_path in MARKDOWN_DIR.rglob("*.md"):
    page = frontmatter.load(md_path)
    html = markdown.markdown(page.content)

    # Required metadata
    title = page.get("title", "")
    desc = page.get("desc", "")
    image = page.get("image", "")
    permalink = page.get("permalink", "")
    keywords = page.get("keywords", "")
    section = md_path.parent.name if md_path.parent != MARKDOWN_DIR else "root"

    # Select template
    template_name = page.get("template", "default") + ".html"
    template = env.get_template(template_name)

    # Render
    rendered = template.render(content=html, title=title, desc=desc, image=image)

    # Output path
    out_path = BUILD_DIR / permalink.strip("/")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(rendered, encoding="utf-8")

    # Append to index
    index.append({
        "title": title,
        "desc": desc,
        "image": image,
        "permalink": permalink,
        "keywords": keywords,
        "section": section
    })

# Optionally: Save index as JSON or inject into homepage, etc.
