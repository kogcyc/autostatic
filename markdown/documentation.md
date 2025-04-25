---
title: Documentation
desc: How Tissue Works and How to Use It
image: /static/img/docs.png
template: template_default.html
permalink: /documentation/
---

# Tissue Static Site Generator Documentation

Tissue is a minimal, fast, and elegant static website site generator (SWSG).  
It is designed to be **light**, **understandable**, and **pleasant** to use.

---

## 📦 Project Structure

```plaintext
markdown/          → Source markdown files (.md)
templates/         → HTML templates (.html)
templates/partialsource/ → Partial markdown files (.md) compiled into HTML
static/            → Static assets (CSS, JS, images)
public/            → Build output (ready to deploy)
```

---

## 🛠 How Tissue Works

1. Markdown files are processed.
2. Frontmatter defines metadata like `title`, `desc`, `permalink`, `template`.
3. Permalinks are either:
   - **Manually** specified in frontmatter, or
   - **Auto-generated** based on the file path.
4. Templates use top-level variables like `{{ title }}`, `{{ desc }}`, `{{ content|safe }}`.
5. Static files are copied into `/static/`.
6. `search_index.json` and `sitemap.xml` are generated automatically.

---

## ✍️ Frontmatter Reference

Each `.md` file requires:

| Key             | Required | Purpose                                     |
|-----------------|----------|---------------------------------------------|
| `title`         | Yes      | Page title                                  |
| `desc`          | Yes      | Short description for SEO/meta              |
| `image`         | Yes      | URL to a preview image (optional for OG)     |
| `template`      | Yes      | Template file to use, e.g. `template_default.html` |
| `permalink`     | Optional | URL path; if missing, generated automatically |
| `pages_exclude` | Optional | Boolean; if true, page is hidden from search and indexes |

Example frontmatter:

```yaml
---
title: About
desc: Learn about our project
image: /static/img/about.png
template: template_default.html
permalink: /about/
---
```

---

## 🔗 Permalink Behavior

- `/about.md` → `/about/`
- `/blog/first-post.md` → `/blog/first-post/`
- If `permalink` ends with `.html`, the page is rendered as a flat file (e.g., `/about.html`).

---

## 🔎 Search System

- `search_index.json` is built from all non-excluded pages.
- Searches titles and descriptions.
- The search page uses lightweight JavaScript embedded into the template.

---

## 🧩 Partials System

- Markdown partials placed in `templates/partialsource/` are rendered to `/partial_*.html`.
- Can be included inside templates via `{% include %}` or client-side fetch.

---

## 🌐 Sitemap.xml

- Tissue generates `sitemap.xml` automatically at build time.
- Only includes published (non-excluded) pages.
- Helps search engines discover your site.

---

## 🚀 Deployment

- Output in `public/` can be hosted anywhere:
  - Vercel
  - Netlify
  - Cloudflare Pages
  - GitHub Pages
- Ensure your root `index.md` has:
  ```yaml
  permalink: /index.html
  ```

---

## 🧠 Philosophy

> **"If a page is heavy, then a tissue is light."**

Tissue is designed to be:
- Lightweight
- Understandable
- Predictable
- Fast

No bloat. No mystery. Just a clean website, built with care.

---

## 🛎 Tips

- **Use `VERBOSE = True`** to see build-time info about what Tissue is generating.
- **Use `pages_exclude: true`** on draft or private pages to hide them from search and sitemaps.
- **Use meaningful permalinks** to control URLs exactly.
- **Keep templates simple** — let Markdown do the heavy lifting.

---

# 🎉 Congratulations

You're now ready to build beautiful, light websites with Tissue.

Happy building!  
*– The Tissue Project*
