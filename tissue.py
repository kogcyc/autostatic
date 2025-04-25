import shutil
import frontmatter
import markdown
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from tissue_config import MARKDOWN_DIR, BUILD_DIR, TEMPLATE_DIR, STATIC_DIR

VERBOSE = True

REQUIRED_KEYS = {"title", "desc", "image", "template"}
OPTIONAL_KEYS = {"permalink", "pages_exclude"}
KNOWN_KEYS = REQUIRED_KEYS | OPTIONAL_KEYS

def validate_frontmatter(metadata, filepath):
    missing = REQUIRED_KEYS - metadata.keys()
    unknown = set(metadata.keys()) - KNOWN_KEYS

    if missing:
        print(f"❌ {filepath} is missing required keys: {', '.join(missing)}")
    if unknown:
        print(f"⚠️ {filepath} has unknown keys: {', '.join(unknown)}")

    return not missing  # Only skip file if required keys are missing

def generate_permalink(md_path):
    rel = md_path.relative_to(MARKDOWN_DIR)
    return "/" + rel.with_suffix("").as_posix() + "/"

# Clean and recreate build directory
if BUILD_DIR.exists():
    shutil.rmtree(BUILD_DIR)
BUILD_DIR.mkdir(parents=True)

# Copy static files
if STATIC_DIR.exists():
    # shutil.copytree(STATIC_DIR, BUILD_DIR / "static")
    shutil.copytree(STATIC_DIR, BUILD_DIR / "static", dirs_exist_ok=True)


# Set up Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

# Collect pages
index = []

for md_path in MARKDOWN_DIR.rglob("*.md"):
    page = frontmatter.load(md_path)
    if not validate_frontmatter(page.metadata, md_path):
        continue

    html = markdown.markdown(page.content)

    title = page.get("title", "")
    desc = page.get("desc", "")
    image = page.get("image", "")
    permalink = page.get("permalink") or generate_permalink(md_path)
    template_file = page.get("template", "template_default.html")
    section = md_path.relative_to(MARKDOWN_DIR).parent.name or "root"

    index.append({
        "title": title,
        "desc": desc,
        "image": image,
        "permalink": permalink,
        "section": section,
        "pages_exclude": page.get("pages_exclude", False)
    })

# Build page groups
all_pages = index
root_pages = [p for p in index if p["section"] == "root"]
sections = set(p["section"] for p in index if p["section"] != "root")
section_pages = {
    section: [p for p in index if p["section"] == section]
    for section in sections
}

if VERBOSE:
    print("🔧 Injected into templates:")
    print("  - all_pages")
    print("  - root_pages")
    for section in section_pages:
        print(f"  - section_pages['{section}']")

# Render all pages
for md_path in MARKDOWN_DIR.rglob("*.md"):
    page = frontmatter.load(md_path)
    if not validate_frontmatter(page.metadata, md_path):
        continue

    html = markdown.markdown(page.content)

    title = page.get("title", "")
    desc = page.get("desc", "")
    image = page.get("image", "")
    permalink = page.get("permalink") or generate_permalink(md_path)
    template_file = page.get("template", "template_default.html")
    section = md_path.relative_to(MARKDOWN_DIR).parent.name or "root"

    template = env.get_template(template_file)
    render_context = {
        "content": html,
        "title": title,
        "desc": desc,
        "image": image,
        "permalink": permalink,
        "section": section,
        "all_pages": all_pages,
        "root_pages": root_pages,
        "section_pages": section_pages
    }
    rendered = template.render(**render_context)

    out_path = BUILD_DIR / permalink.strip("/")
    if out_path.suffix == "":
        out_path /= "index.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(rendered, encoding="utf-8")

# Render partials
PARTIAL_SOURCE_DIR = TEMPLATE_DIR / "partialsource"
if PARTIAL_SOURCE_DIR.exists():
    for md_path in PARTIAL_SOURCE_DIR.glob("*.md"):
        name = md_path.stem
        html = markdown.markdown(md_path.read_text(encoding="utf-8"))
        out_path = BUILD_DIR / f"partial_{name}.html"
        out_path.write_text(html, encoding="utf-8")
        if VERBOSE:
            print(f"🧹 Partial rendered: {out_path.relative_to(BUILD_DIR)}")

# Generate search index
searchable_pages = [p for p in index if not p.get("pages_exclude")]
search_index_path = BUILD_DIR / "search_index.json"
with search_index_path.open("w", encoding="utf-8") as f:
    json.dump(searchable_pages, f, indent=2)

if VERBOSE:
    print(f"🔍 search_index.json written with {len(searchable_pages)} pages.")
