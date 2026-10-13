"""Build crawlable bilingual HTML using only the Python standard library."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://eylema.dev"
INDEXNOW_KEY = "1e76b9883a4f4a64a2ceffbbc439a640"
PROJECT = "https://github.com/eylema-dev/eylema"
UPDATED = "2026-10-13"
# Actual page changes, independent of the reviewed design date and build time.
PAGE_MODIFIED = {"en": "2026-10-13", "tr": "2026-10-13"}
SOURCES = {
    "en": {"architecture": "docs/architecture.md", "api": "docs/api-reference.md", "teams": "docs/development-and-operations.md", "learning": "docs/learning-and-training.md", "project": "README.md", "project_structure": "docs/project-structure.md", "core_browser": "docs/en/local-browser.md", "license": "LICENSE"},
    "tr": {"architecture": "docs/architecture.md", "api": "docs/api-reference.md", "teams": "docs/development-and-operations.md", "learning": "docs/learning-and-training.md", "project": "README.tr.md", "project_structure": "docs/project-structure.md", "core_browser": "docs/tr/local-browser.md", "license": "LICENSE"},
}


def esc(value):
    return html.escape(str(value), quote=True)


def arrow(external=False):
    path = "M6 18 18 6M6 6h12v12" if external else "M4 12h16m-7-7 7 7-7 7"
    return f'<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="{path}"/></svg>'


def source(lang, name):
    repository = PROJECT if name in {"project", "core_browser", "license"} else f"https://github.com/eylema-dev/eylema-docs-{lang}"
    return f"{repository}/blob/main/{SOURCES[lang][name]}"


def schema(data):
    url = ORIGIN + ("/tr/" if data["lang"] == "tr" else "/")
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": ORIGIN + "/#organization", "name": "Eylema", "url": ORIGIN + "/", "logo": ORIGIN + "/assets/apple-touch-icon.png", "sameAs": ["https://github.com/eylema-dev", PROJECT]},
            {"@type": "WebSite", "@id": ORIGIN + "/#website", "name": "Eylema", "url": ORIGIN + "/", "inLanguage": ["en", "tr"], "publisher": {"@id": ORIGIN + "/#organization"}},
            {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": data["title"], "description": data["description"], "inLanguage": data["lang"], "dateModified": PAGE_MODIFIED[data["lang"]], "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@type": "Thing", "name": "Eylema", "description": data["questions"][0]["answer"]}, "citation": [source(data["lang"], key) for key in ("architecture", "api", "teams", "learning")]},
        ],
    }


def language_links(data):
    links = []
    for lang, path, label in [("en", "/", "English"), ("tr", "/tr/", "Türkçe")]:
        current = ' aria-current="page"' if data["lang"] == lang else ""
        links.append(f'<a href="{path}" lang="{lang}" hreflang="{lang}" aria-label="{label}"{current}>{lang.upper()}</a>')
    return f'<nav class="languages" aria-label="{esc(data["language"])}">' + '<span aria-hidden="true">/</span>'.join(links) + '</nav>'


def render(data):
    lang = data["lang"]
    url = ORIGIN + ("/tr/" if lang == "tr" else "/")
    e = lambda key: esc(data[key])
    heading = lambda key: "<br>".join(esc(line) for line in data[key])
    logo = '<img src="/assets/eylema-wordmark.webp" alt="EylemA" width="960" height="320" decoding="async">'
    languages = language_links(data)
    principles = "".join(f'<li><span class="index">{i:02d} /</span><h2>{esc(p["title"])}</h2><p>{esc(p["text"])}</p></li>' for i, p in enumerate(data["principles"], 1))
    foundation = "".join(f'<article><p class="scope-label">{esc(card["label"])}</p><h3>{esc(card["title"])}</h3><p>{esc(card["text"])}</p><a class="text-link" href="{source(lang, card["source"])}">{esc(card["link"])}{arrow(True)}</a></article>' for card in data["foundation_cards"])
    tabs = "".join(f'<a id="step-{s["id"]}" href="#panel-{s["id"]}"><span>{i:02d}</span> {esc(s["name"])}</a>' for i, s in enumerate(data["steps"], 1))
    panels = []
    for step in data["steps"]:
        nodes = "".join(f'<li>{esc(node)}</li>' for node in step["nodes"])
        panels.append(f'''<section class="step-panel" id="panel-{step['id']}" aria-labelledby="step-{step['id']}">
          <div class="step-copy"><h3>{esc(step['title'])}</h3><p>{esc(step['text'])}</p><a class="text-link" href="{source(lang, step['source'])}">{esc(step['link'])}{arrow(True)}</a></div>
          <figure class="contract"><figcaption>{esc(step['diagram'])}</figcaption><div class="contract-tree"><div class="contract-root">{esc(step['root'])}</div><ul>{nodes}</ul></div><p class="concept-note">{e('concept_note')}</p></figure>
        </section>''')
    questions = "".join(f'''<details {'open' if i == 0 else ''}><summary>{esc(q['question'])}<svg class="disclosure-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12h18"/><path class="vertical" d="M12 3v18"/></svg></summary><div class="answer"><p>{esc(q['answer'])}</p><a class="text-link" href="{source(lang, q['source'])}">{esc(q['link'])}{arrow(True)}</a></div></details>''' for i, q in enumerate(data["questions"]))
    milestones = "".join(f'<li><span class="milestone-index">{i:02d}</span><h3>{esc(m["title"])}</h3><p>{esc(m["text"])}</p><span class="milestone-status">{esc(m["status"])}</span></li>' for i, m in enumerate(data["milestones"], 1))
    # Escape '<' so even future untrusted copy cannot close the JSON-LD script.
    ld = json.dumps(schema(data), ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e('title')}</title>
  <meta name="description" content="{e('description')}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="theme-color" content="#F7F6F2">
  <meta name="color-scheme" content="light">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="en" href="{ORIGIN}/">
  <link rel="alternate" hreflang="tr" href="{ORIGIN}/tr/">
  <link rel="alternate" hreflang="x-default" href="{ORIGIN}/">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Eylema">
  <meta property="og:title" content="{e('title')}">
  <meta property="og:description" content="{e('description')}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{e('locale')}">
  <meta property="og:locale:alternate" content="{'tr_TR' if lang == 'en' else 'en_US'}">
  <meta property="og:image" content="{ORIGIN}/assets/social.png">
  <meta property="og:image:width" content="1280">
  <meta property="og:image:height" content="640">
  <meta property="og:image:alt" content="Eylema — Continuous development. Continuous operations.">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e('title')}">
  <meta name="twitter:description" content="{e('description')}">
  <meta name="twitter:image" content="{ORIGIN}/assets/social.png">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="stylesheet" href="/assets/site.css">
  <script type="application/ld+json">{ld}</script>
  <script src="/assets/site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">{e('skip')}</a>
  <header class="site-header"><div class="shell header-inner">
    <a class="brand" href="{'/tr/' if lang == 'tr' else '/'}" aria-label="EylemA">{logo}</a>
    <nav class="main-nav" aria-label="{e('navigation')}"><a href="#architecture">{e('nav_architecture')}</a><a href="#roadmap">{e('nav_roadmap')}</a><a href="{PROJECT}">GitHub {arrow(True)}</a></nav>
    {languages}
  </div></header>
  <main id="main" tabindex="-1">
    <section class="hero shell" aria-labelledby="hero-title">
      <div class="hero-copy"><h1 id="hero-title">{esc(data['headline'][0])}<br>{esc(data['headline'][1])}<br><span>{esc(data['headline'][2])}</span></h1>
        <p class="hero-intro">{e('intro')}</p>
        <div class="hero-actions"><a class="button" href="#architecture">{e('explore')}{arrow()}</a><a class="text-link" href="{PROJECT}">{e('follow')}{arrow(True)}</a></div>
        <p class="project-status">{e('status')}</p>
      </div>
      <div class="hero-art" aria-hidden="true"><img src="/assets/eylema-loop-1024.webp" srcset="/assets/eylema-loop-640.webp 640w, /assets/eylema-loop-1024.webp 1024w" sizes="(max-width: 720px) 100vw, 52vw" width="1024" height="1024" alt="{e('hero_art_alt')}" fetchpriority="high" decoding="async"></div>
    </section>
    <div class="shell"><ul class="principles">{principles}</ul></div>
    <section class="architecture section shell" id="architecture" aria-labelledby="architecture-title">
      <p class="section-label">{e('architecture_label')}</p>
      <div class="section-heading"><h2 id="architecture-title">{heading('architecture_title')}</h2><p>{e('architecture_intro')}</p></div>
      <div class="foundation-scope" aria-label="{e('foundation_label')}">{foundation}</div>
      <figure class="technology-overview" id="technology">
        <p class="technology-notice">{e('technology_notice')}</p>
        <a class="technology-image" href="/assets/eylema-technology-{lang}.png" target="_blank" rel="noopener" aria-label="{e('technology_open')}">
          <img src="/assets/eylema-technology-{lang}.webp" alt="{e('technology_alt')}" width="1672" height="941" loading="lazy" decoding="async">
        </a>
        <figcaption><p>{e('technology_caption')}</p><a class="text-link" href="/assets/eylema-technology-{lang}.png" target="_blank" rel="noopener">{e('technology_open')}{arrow(True)}</a></figcaption>
      </figure>
      <nav class="steps" aria-label="{e('steps_label')}">{tabs}</nav>
      {''.join(panels)}
      <div class="section-note"><p>{e('human_title')}</p><p>{e('human_text')}</p></div>
    </section>
    <section class="faq section shell" id="questions" aria-labelledby="faq-title">
      <p class="section-label">{e('faq_label')}</p><div class="faq-layout"><div class="faq-intro"><h2 id="faq-title">{heading('faq_title')}</h2><p>{e('faq_intro')}</p></div><div class="questions">{questions}</div></div>
      <div class="section-note"><p><time datetime="{UPDATED}">{e('updated')}</time></p><p>{e('language_note')}</p></div>
    </section>
    <section class="roadmap section shell" id="roadmap" aria-labelledby="roadmap-title">
      <p class="section-label">{e('roadmap_label')}</p><div class="section-heading"><h2 id="roadmap-title">{heading('roadmap_title')}</h2><p>{e('roadmap_intro')}</p></div>
      <ol class="milestones">{milestones}</ol>
    </section>
    <section class="invitation" aria-labelledby="join-title"><div class="shell invitation-inner"><div><h2 id="join-title">{e('join_title')}</h2><p>{e('join_text')}</p></div><a class="button button-light" href="{PROJECT}">{e('join_link')}{arrow(True)}</a></div></section>
  </main>
  <footer class="site-footer shell"><a class="brand" href="{'/tr/' if lang == 'tr' else '/'}" aria-label="EylemA">{logo}</a><p>{e('footer')}</p><nav aria-label="{e('nav_architecture')}"><a href="{source(lang, 'architecture')}">{e('nav_architecture')}</a><a href="{source(lang, 'api')}">{e('api_link')}</a></nav>{languages}</footer>
</body>
</html>
'''


def outputs(root=ROOT):
    result = {}
    for lang, path in [("en", "index.html"), ("tr", "tr/index.html")]:
        data = json.loads((root / "content" / f"{lang}.json").read_text())
        result[path] = render(data)
    result["sitemap.xml"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{ORIGIN}/</loc><lastmod>{PAGE_MODIFIED['en']}</lastmod></url>
  <url><loc>{ORIGIN}/tr/</loc><lastmod>{PAGE_MODIFIED['tr']}</lastmod></url>
</urlset>
'''
    result["robots.txt"] = f"User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n"
    result[f"{INDEXNOW_KEY}.txt"] = INDEXNOW_KEY
    result["404.html"] = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found — Eylema</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/assets/site.css"><link rel="icon" href="/assets/favicon.svg"></head><body><main class="not-found shell"><img src="/assets/eylema.svg" alt="Eylema" width="190" height="70"><p class="section-label">404</p><h1>This page is not here.</h1><p>The address may have changed.</p><a class="button" href="/">Back to Eylema</a><p lang="tr">Bu sayfa bulunamadı. <a class="text-link" href="/tr/">Türkçe ana sayfaya dön</a></p></main></body></html>
'''
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed outputs differ from sources")
    args = parser.parse_args()
    stale = []
    for name, value in outputs().items():
        path = ROOT / "public" / name
        if args.check:
            if not path.is_file() or path.read_text() != value:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8")
    if stale:
        parser.exit(1, "Stale generated files: " + ", ".join(stale) + "\n")
    print("PASS: generated pages are current" if args.check else "Built English, Turkish, sitemap, robots and 404 pages")


if __name__ == "__main__":
    main()
