# banglallm.github.io

The BanglaLLM research lab landing page. Bangla-default, English toggle.

## Editing content

All text lives in `_data/*.yml`:

- `site_content.yml` — hero, about, research themes, Drishtikon, join/contact copy
- `publications.yml` — published papers + in-progress research
- `people.yml` — team roster
- `models.yml` — HuggingFace model families and datasets
- `repos.yml` — featured GitHub repos

Every human-readable field has `_bn` (Bengali) and `_en` (English) variants. Both render into the page; a CSS rule shows only the active language.

## Local preview

Requires Ruby 3.x and Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000.

## Deploy

Push `main` to `github.com/banglallm/banglallm.github.io`. GitHub Pages builds automatically. No CI needed.

```bash
git init
git add -A
git commit -m "Initial landing page"
git branch -M main
git remote add origin git@github.com:banglallm/banglallm.github.io.git
git push -u origin main
```

The site is live at <https://banglallm.github.io> within a minute or two.

## Structure

```
├── _config.yml            # site settings
├── _data/                 # bilingual content (edit here)
├── _layouts/default.html  # single page layout
├── _includes/             # header, footer
├── assets/
│   ├── css/style.css      # Anthropic-minimal styling
│   ├── js/lang-toggle.js  # bn/en toggle with localStorage
│   └── favicon.svg
└── index.html             # the one page
```
