import os
import shutil
import frontmatter
import markdown
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import json
from collections import Counter
import re
import string
from tissue_config import MARKDOWN_DIR, BUILD_DIR, TEMPLATE_DIR, STATIC_DIR

# Delete and recreate build directory
if BUILD_DIR.exists():
    shutil.rmtree(BUILD_DIR)
BUILD_DIR.mkdir(parents=True, exist_ok=True)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

# Collect markdown files and categorize
all_pages = []
category_pages = {}

for md_path in MARKDOWN_DIR.rglob("*.md"):
    rel_path = md_path.relative_to(MARKDOWN_DIR)
    subdir = rel_path.parent.name if rel_path.parent != Path('.') else 'root'
    page = frontmatter.load(md_path)

    if page.get('exclude'):
        continue  # skip this page if marked as excluded

    page['html'] = markdown.markdown(page.content)
    page['path'] = rel_path
    page['output_path'] = BUILD_DIR / rel_path.with_suffix(".html")
    
    all_pages.append(page)

    key = f"{subdir}_pages"
    if key not in category_pages:
        category_pages[key] = []
    category_pages[key].append(page)

# Render pages to build directory
for page in all_pages:
    output_path = page['output_path']
    output_path.parent.mkdir(parents=True, exist_ok=True)

    template_name = page.get('template', 'template_default.html')
    template = env.get_template(template_name)

    context = {
        'page': page,
        'all_pages': all_pages,
        **category_pages
    }

    html = template.render(**context)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

def tokenize(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    return re.findall(r"\b[a-zA-Z]{2,}\b", text.lower())

index = []
for page in all_pages:
    if page.get('exclude'):
        continue

    rel_path = page['path']
    if rel_path.parent == Path("."):
        continue  # ❌ skip root-level .md files

    tokens = tokenize(page.content)
    counts = Counter(tokens)
    keywords = [word for word, freq in counts.items() if freq == 1][:10]
    section = rel_path.parent.name

    index.append({
        "title": page.get("title", ""),
        "desc": page.get("desc", ""),
        "url": "/" + str(rel_path.with_suffix('.html')),
        "keywords": keywords,
        "category": section
    })

(BUILD_DIR / "search_index.json").write_text(json.dumps(index, indent=2), encoding='utf-8')

# Copy static assets
if STATIC_DIR.exists():
    shutil.copytree(STATIC_DIR, BUILD_DIR / "static", dirs_exist_ok=True)

print("Site built successfully.")
