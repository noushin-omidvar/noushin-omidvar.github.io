# Noushin Omidvar — Personal Portfolio

Personal website for **Noushin Omidvar**, an applied machine learning scientist working at the intersection of **scientific machine learning, materials informatics, molecular ML, experimental decision support, and optimization**.

**Live site:** https://noushin-omidvar.github.io

---

## About the site

This site is designed as a compact scientific portfolio rather than a traditional academic CV page. It brings together:

- selected work in applied ML for science and engineering
- publications and research background
- technical writing and notes
- professional experience and education
- links to CV and professional profiles

The current visual system uses an editorial, research-focused design with serif display typography, restrained scientific accents, and a custom portrait/orbit motif.

## Site structure

- **About** — introduction, research focus, and selected work
- **Work** — applied scientific ML projects and problem areas
- **Publications** — peer-reviewed research and publication history
- **Writing** — technical notes and long-form posts
- **CV** — experience, education, tools, and methods

## Tech stack

The site is built with:

- [Jekyll](https://jekyllrb.com/)
- [GitHub Pages](https://pages.github.com/)
- Liquid templates
- Sass / CSS
- JavaScript

It originated from the [al-folio](https://github.com/alshedivat/al-folio) academic Jekyll theme and has since been substantially customized with new layouts, styling, navigation, article presentation, and portfolio-specific components.

## Custom portfolio architecture

The redesign introduces dedicated portfolio layouts and assets, including:

```text
_layouts/
  portfolio_base.html
  portfolio_home.html
  portfolio_page.html
  portfolio_publications.html
  portfolio_writing.html
  portfolio_cv.html
  portfolio_post.liquid

assets/css/
  portfolio-site.css
  portfolio-redesign.css

assets/js/
  portfolio-site.js
  portfolio-redesign.js
```

The main profile image is stored at:

```text
assets/img/noushin-profile.jpg
```

## Local development

Install the Ruby dependencies:

```bash
bundle install
```

Run the site locally:

```bash
bundle exec jekyll serve
```

Then open:

```text
http://127.0.0.1:4000
```

For a clean rebuild:

```bash
rm -rf _site .jekyll-cache
bundle exec jekyll serve
```

## Build

To verify the site before pushing:

```bash
rm -rf _site .jekyll-cache
bundle exec jekyll build
```

The site is deployed from the `main` branch through GitHub Pages / the repository's configured deployment workflow.

## Content

Blog posts live in:

```text
_posts/
```

Publications are managed through the site's bibliography data and publication layouts.

Page-level content lives primarily in:

```text
_pages/
```

## Notes

Local ImageMagick warnings may appear if the `convert` executable is not installed. These warnings do not necessarily prevent Jekyll from completing a build, but installing ImageMagick is recommended if responsive image generation is needed locally.

## Credits

Built on top of [al-folio](https://github.com/alshedivat/al-folio), with a custom editorial/scientific redesign for this portfolio.

---

© Noushin Omidvar
