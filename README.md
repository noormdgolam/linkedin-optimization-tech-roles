# LinkedIn Optimization Tech Hub

This is the static generator for the **LinkedIn Optimization Tech Hub** website. It is designed to be extremely lightweight, SEO-friendly, and optimized for high traffic and Google AdSense monetization.

## Project Structure

- `_src/`: Contains the site generator source code.
  - `_data/site.json`: Global site configuration.
  - `_data/articles.json`: The main database of articles.
  - `_data/generate_articles.py`: Script to seed or update articles.
  - `_templates/`: Jinja2 HTML templates.
  - `assets/`: Source CSS and JS files.
  - `generate.py`: The main build script that generates the static site.
- `/`: The root directory contains the generated static HTML files ready for deployment.

## How to Add New Articles

1. Open `_src/_data/articles.json`.
2. Add a new JSON object to the array with the following format:
   ```json
   {
     "title": "Your Article Title",
     "slug": "your-article-slug",
     "category": "Profile Optimization",
     "date": "YYYY-MM-DD",
     "description": "A short meta description.",
     "content_md": "## Introduction\n\nYour article content in markdown format..."
   }
   ```
3. Run the generator script to rebuild the site.

## How to Build the Site

Navigate to the `_src/` directory and run:

```bash
python generate.py
```

This will automatically compile all HTML pages, generate a new `sitemap.xml`, update the `rss.xml` feed, and rebuild the search index in the root directory.

## Inserting AdSense Code

The site is pre-configured with placeholder AdSense slots. To activate them:

1. Open the templates in `_src/_templates/`.
2. Search for `data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"` and `data-ad-slot="XXXXXXXXXX"`.
3. Replace the placeholder values with your actual AdSense Publisher ID and Ad Slot IDs.
4. **Global Script:** The main async AdSense script is located in the `<head>` of `_src/_templates/base.html`.
5. Run the build script (`python generate.py`) to apply changes.

## Connecting the Newsletter

The newsletter opt-in forms are currently placeholders. To connect them to a real provider (like Mailchimp, ConvertKit, etc.):

1. In `_src/_templates/base.html` (footer form), replace the `<form>` action URL and method.
2. In `_src/_templates/article.html` (mid-article form injected via JS), update the JS snippet at the bottom of the file that generates the inline form.

## Deployment

This repository is designed to be deployed directly via cPanel Git™ Version Control. 
Since the generated static files are output directly into the root directory, every `git push` to your main branch will automatically update the live site on your cPanel host without needing a `.cpanel.yml` file.
