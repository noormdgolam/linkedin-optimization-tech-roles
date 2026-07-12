import os
import json
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import markdown

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(SRC_DIR, '_data')
TEMPLATES_DIR = os.path.join(SRC_DIR, '_templates')
ASSETS_DIR = os.path.join(SRC_DIR, 'assets')

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def setup_jinja(site_data):
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    env.globals['site'] = site_data
    env.globals['now'] = datetime.now()
    env.filters['markdown'] = lambda text: markdown.markdown(text, extensions=['fenced_code', 'tables'])
    return env

def render_page(env, template_name, output_filename, **context):
    template = env.get_template(template_name)
    html = template.render(**context)
    
    output_path = os.path.join(ROOT_DIR, output_filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {output_filename}")

def copy_assets():
    dest_assets = os.path.join(ROOT_DIR, 'assets')
    if os.path.exists(dest_assets):
        shutil.rmtree(dest_assets)
    shutil.copytree(ASSETS_DIR, dest_assets)
    print("Copied assets to root.")

    for f in ['manifest.json', 'sw.js']:
        src_f = os.path.join(SRC_DIR, f)
        if os.path.exists(src_f):
            shutil.copy2(src_f, os.path.join(ROOT_DIR, f))
            print(f"Copied {f}")

def main():
    print("Starting site generation...")
    site_data = load_json('site.json')
    articles_data = load_json('articles.json')
    
    env = setup_jinja(site_data)
    
    categories = {}
    for article in articles_data:
        cat = article.get('category', 'Uncategorized')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(article)
        
    site_data['categories'] = categories
    
    pages = ['index', 'about-us', 'contact', 'privacy-policy', 'terms-of-service', 'disclaimer', '404', 'search']
    for p in pages:
        render_page(env, f'{p}.html', f'{p}.html', articles=articles_data)
        
    for article in articles_data:
        output_name = f"{article['slug']}/index.html"
        render_page(env, 'article.html', output_name, article=article, articles=articles_data)
        
    for cat_name, cat_articles in categories.items():
        slug = cat_name.lower().replace(' ', '-')
        output_name = f"{slug}/index.html"
        render_page(env, 'category.html', output_name, category_name=cat_name, category_slug=slug, articles=cat_articles)
        
    render_page(env, 'sitemap.xml', 'sitemap.xml', articles=articles_data, categories=categories, pages=pages)
    render_page(env, 'rss.xml', 'rss.xml', articles=articles_data)
    render_page(env, 'robots.txt', 'robots.txt')
    
    search_index = []
    for a in articles_data:
        search_index.append({
            'title': a['title'],
            'url': f"/{a['slug']}/",
            'description': a['description'],
            'category': a.get('category', '')
        })
    with open(os.path.join(ROOT_DIR, 'search_index.json'), 'w', encoding='utf-8') as f:
        json.dump(search_index, f)
    
    copy_assets()
    print("Site generation complete!")

if __name__ == '__main__':
    main()
