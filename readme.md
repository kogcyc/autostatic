
<span align="left">
  <img src="./tissue_logo.png" width="400" alt="Tissue logo">
</span>

Tissue is a static web site generator written in Python 3

# A Step-by-Step Guide To Setup

This guide walks you through setting up a minimal Tissue-based static site project.

---

## 1. Place Core Files in Your Project Root

Put the following files in your project root directory:

- `tissue.py`
- `tissue_config.py`

---

## 2. Create the Source Directory

Create a directory in the root named:

```plaintext
markdown/
```

This is where your site's pages will live.

---

## 3. Add a Starter Page

Inside `markdown/`, create a file named `index.md` with the following content:

```markdown
---
title: Home
desc: Welcome to the site
image: /static/images/home.png
template: template_default.html
permalink: /index.html
---

# Welcome

This is the homepage of your Tissue-generated site.
```

---

## 4. Add an Image

Notice that `index.md` references an image.  
Create these directories inside your project:

```plaintext
static/
└── images/
```

Place an image file inside `static/images/`, such as `home.png`.

---

## 5. Create the Templates Directory

Notice that `index.md` also references a template.  
Create this directory inside your project:

```plaintext
templates/
```

Add a file called `template_default.html` containing:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ title }}</title>
  <meta name="description" content="{{ desc }}">
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <header><h1>{{ title }}</h1></header>
  <main>{{ content|safe }}</main>
  <footer><p>Section: {{ section }}</p></footer>
</body>
</html>
```

---

## 6. Understand Permalinks

Look at `index.md` again.  
Note that the `permalink` is set to `/index.html`.

> **IMPORTANT:**  
> For most other pages, you can leave `permalink` **blank** or omit it, and Tissue will generate a clean URL automatically.

---

## 7. Review `tissue_config.py`

Open `tissue_config.py` and confirm:

- `BUILD_DIR` is set to `public`
- `MARKDOWN_DIR` is `markdown`
- `STATIC_DIR` is `static`
- `TEMPLATE_DIR` is `templates`

You can adjust these later if needed.

---

## 8. Install Python Requirements

Create a `requirements.txt` in your root directory containing:

```plaintext
markdown
frontmatter
jinja2
```

Then install them:

```bash
pip3 install -r requirements.txt
```

---

## 9. Project Dir Tree

Your project should look like this now:

    .
    ├── markdown
    │   └── index.md
    ├── requirements.txt
    ├── static
    │   └── images
    │       └── home.png
    ├── templates
    │   └── template_default.html
    ├── tissue_config.py
    └── tissue.py

---

## 10. Build Your Site

In the root directory, run:

```bash
python3 tissue.py
```

You should see:

- A new `public/` directory
- Your static files copied into `public/static/`
- Your `index.html` generated at `public/index.html`

> **IMPORTANT:**  
> Every time you run `python3 tissue.py`, the `public/` directory is completely cleared and rebuilt from scratch.

---

# 🎉 Congratulations!

You now have a fully working minimal Tissue site.

Happy building!
