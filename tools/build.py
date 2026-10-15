"""Build crawlable bilingual HTML using only the Python standard library."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://eyleme.dev"
INDEXNOW_KEY = "1e76b9883a4f4a64a2ceffbbc439a640"
PROJECT = "https://github.com/eyleme-dev/eyleme"
UPDATED = "2026-10-15"
# Actual page changes, independent of the reviewed design date and build time.
PAGE_MODIFIED = {"en": "2026-10-15", "tr": "2026-10-15"}
SOURCES = {
    "en": {"architecture": "docs/architecture.md", "api": "docs/api-reference.md", "teams": "docs/development-and-operations.md", "learning": "docs/learning-and-training.md", "project": "README.md", "project_structure": "docs/project-structure.md", "core_browser": "docs/en/local-browser.md", "core_authority": "docs/en/real-human.md", "core_contracts": "docs/en/platform-contracts.md", "core_models": "docs/en/model-contract.md", "core_memory": "docs/en/memory-contracts.md", "core_evidence": "docs/en/decision-evidence.md", "core_data": "docs/en/project-data.md", "license": "LICENSE"},
    "tr": {"architecture": "docs/architecture.md", "api": "docs/api-reference.md", "teams": "docs/development-and-operations.md", "learning": "docs/learning-and-training.md", "project": "README.tr.md", "project_structure": "docs/project-structure.md", "core_browser": "docs/tr/local-browser.md", "core_authority": "docs/tr/real-human.md", "core_contracts": "docs/tr/platform-contracts.md", "core_models": "docs/tr/model-contract.md", "core_memory": "docs/tr/memory-contracts.md", "core_evidence": "docs/tr/decision-evidence.md", "core_data": "docs/tr/project-data.md", "license": "LICENSE"},
}


def esc(value):
    return html.escape(str(value), quote=True)


def arrow(external=False):
    path = "M6 18 18 6M6 6h12v12" if external else "M4 12h16m-7-7 7 7-7 7"
    return f'<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="{path}"/></svg>'


def source(lang, name):
    if name == "contributing":
        return f"{PROJECT}/blob/main/CONTRIBUTING{'.tr' if lang == 'tr' else ''}.md"
    repository = PROJECT if name in {"project", "license"} or name.startswith("core_") else f"https://github.com/eyleme-dev/eyleme-docs-{lang}"
    return f"{repository}/blob/main/{SOURCES[lang][name]}"


def schema(data):
    url = ORIGIN + ("/tr/" if data["lang"] == "tr" else "/")
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": ORIGIN + "/#organization", "name": "Eyleme", "url": ORIGIN + "/", "logo": ORIGIN + "/assets/apple-touch-icon.png", "sameAs": ["https://github.com/eyleme-dev", PROJECT]},
            {"@type": "WebSite", "@id": ORIGIN + "/#website", "name": "Eyleme", "url": ORIGIN + "/", "inLanguage": ["en", "tr"], "publisher": {"@id": ORIGIN + "/#organization"}},
            {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": data["title"], "description": data["description"], "inLanguage": data["lang"], "dateModified": PAGE_MODIFIED[data["lang"]], "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@type": "Thing", "name": "Eyleme", "description": data["questions"][0]["answer"]}, "citation": [source(data["lang"], key) for key in ("architecture", "api", "teams", "learning")]},
        ],
    }


def language_links(data):
    links = []
    for lang, path, label in [("en", "/", "English"), ("tr", "/tr/", "Türkçe")]:
        current = ' aria-current="page"' if data["lang"] == lang else ""
        links.append(f'<a href="{path}" lang="{lang}" hreflang="{lang}" aria-label="{label}"{current}>{lang.upper()}</a>')
    return f'<nav class="languages" aria-label="{esc(data["language"])}">' + '<span aria-hidden="true">/</span>'.join(links) + '</nav>'


def product_art(product_id):
    """Small original line illustrations reinforce the adjacent product copy."""
    paths = {
        "derleme": '<path d="M24 106h192M40 106V66h40v40m-30-56v16m20-16v16M50 82h20m-20 12h20M160 106V70h40v36m-30-24h20m-20 12h20"/><path class="art-accent" d="M80 83h38V40h40" stroke-dasharray="3 5"/><path d="M158 40h42a16 16 0 0 0 0-32 24 24 0 0 0-45 7 13 13 0 0 0 3 25Z"/><circle cx="60" cy="38" r="5"/><path d="M45 26a21 21 0 0 1 30 0m-38-8a33 33 0 0 1 46 0"/>',
        "onama": '<path class="art-accent" d="M120 9 162 27v31c0 27-19 46-42 57-23-11-42-30-42-57V27Z"/><circle cx="120" cy="45" r="12"/><path d="M100 80v-6a20 20 0 0 1 40 0v6Z M24 42h30v44H24Zm7 11h16m-16 10h16m-16 10h9M186 54h30v27h-30Zm6 0v-9a9 9 0 0 1 18 0v9M54 64h24m84 0h24"/>',
        "eyleme": '<path d="m120 14 91 31-91 31-91-31Z m-91 52 91 31 91-31m-182 22 91 31 91-31"/><path class="art-accent" d="m29 67 91 31 91-31"/><path stroke-dasharray="3 5" d="M29 45H12v64h52m147-64h17v64h-52"/><circle cx="12" cy="45" r="3"/><circle cx="228" cy="45" r="3"/>',
    }
    return f'<svg class="product-art" viewBox="0 0 240 132" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true">{paths[product_id]}</svg>'


def ecosystem_svg(data):
    """Original vector diagram; localized text remains sharp at every viewport."""
    d = {key: esc(value) for key, value in data["hero_diagram"].items()}
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 600" width="640" height="600" role="img" aria-labelledby="ecosystem-title ecosystem-desc" xml:lang="{data['lang']}">
  <title id="ecosystem-title">{d['title']}</title><desc id="ecosystem-desc">{d['alt']}</desc>
  <style>
    :root {{ --ink:#10252e; --muted:#526875; --accent:#ce492c; --cyan:#167685; --rule:#cedae1; --paper:#f5f8fa; }}
    @media (prefers-color-scheme:dark) {{ :root {{ --ink:#edf3f7; --muted:#a4b5bf; --accent:#ff714e; --cyan:#84d8e2; --rule:#293740; --paper:#0b1116; }} }}
    .node {{ fill:var(--paper); stroke:var(--cyan); stroke-width:1.5; }}
    .guide {{ fill:none; stroke:var(--rule); stroke-width:1; }}
    .link {{ fill:none; stroke:var(--accent); stroke-width:2.5; marker-end:url(#tip); }}
    @media (max-width:400px) {{ .roles, .details {{ display:none; }} .names {{ font-size:34px; }} .edges {{ font-size:27px; }} .center {{ font-size:32px; }} }}
  </style>
  <defs><marker id="tip" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M1 1 9 5 1 9Z" fill="var(--accent)"/></marker></defs>
  <circle class="guide" cx="320" cy="318" r="248" stroke-dasharray="3 6"/>
  <path class="guide" d="M320 2v596M4 440h632M226 100h188M16 532h36m-18-18v36m554-18h36m-18-18v36"/>
  <path class="link" d="M280 165 151 374"/><path class="link" d="M190 440H448"/><path class="link" d="M489 374 360 165"/>
  <g class="guide" stroke-dasharray="3 5"><path d="M320 180v60m-40 125-100 48m180-48 100 48"/><circle cx="320" cy="315" r="70"/></g>
  <g class="node"><circle cx="320" cy="100" r="80"/><circle cx="110" cy="440" r="80"/><circle cx="530" cy="440" r="80"/></g>
  <g fill="none" stroke="var(--accent)" stroke-width="1.5"><circle cx="320" cy="100" r="70"/><circle cx="110" cy="440" r="70"/><circle cx="530" cy="440" r="70"/></g>
  <g font-family="Helvetica Neue, Helvetica, Arial, sans-serif" text-anchor="middle" fill="var(--ink)">
    <g class="names" font-size="29" font-weight="700" letter-spacing="-1"><text x="320" y="98" fill="var(--accent)">Eyleme</text><text x="110" y="437">Derleme</text><text x="530" y="437">Onama</text></g>
    <g class="roles" font-size="17" fill="var(--muted)"><text x="320" y="126">{d['eyleme_role']}</text><text x="110" y="464">{d['derleme_role']}</text><text x="530" y="464">{d['onama_role']}</text></g>
    <g class="details" font-size="16" fill="var(--muted)"><text x="110" y="550">{d['derleme_deployment']}</text><text x="530" y="550">{d['onama_scope']}</text></g>
    <g class="edges" font-size="19" fill="var(--ink)"><text x="178" y="266" transform="rotate(-58 178 266)">{d['feedback']}</text><text x="468" y="266" transform="rotate(58 468 266)">{d['authority']}</text><text x="320" y="420">{d['data']}</text></g>
    <text class="center" x="320" y="308" font-size="29" font-weight="650" letter-spacing="-.8">{d['center']}</text><text class="center" x="320" y="339" font-size="26" fill="var(--muted)">{d['center_subtitle']}</text>
  </g>
</svg>
'''



def render(data):
    lang = data["lang"]
    url = ORIGIN + ("/tr/" if lang == "tr" else "/")
    e = lambda key: esc(data[key])
    heading = lambda key: "<br>".join(f'<span>{esc(line)}</span>' if i == len(data[key]) - 1 else esc(line) for i, line in enumerate(data[key]))
    logo = '<img src="/assets/eyleme-wordmark.webp" alt="Eyleme" width="960" height="320" decoding="async">'
    languages = language_links(data)
    principles = "".join(f'<li><span class="index">{i:02d} /</span><h2>{esc(p["title"])}</h2><p>{esc(p["text"])}</p></li>' for i, p in enumerate(data["principles"], 1))
    foundation = "".join(f'<article><p class="scope-label">{esc(card["label"])}</p><h3>{esc(card["title"])}</h3><p>{esc(card["text"])}</p><a class="text-link" href="{source(lang, card["source"])}">{esc(card["link"])}{arrow(True)}</a></article>' for card in data["foundation_cards"])
    products = "".join(f'<li id="product-{p["id"]}"><p class="scope-label">{esc(p["model"])}</p><h3>{esc(p["name"])}</h3><p class="product-purpose">{esc(p["title"])}</p><p>{esc(p["text"])}</p>{product_art(p["id"])}<p class="product-status">{esc(p["status"])}</p></li>' for p in data["products"])
    subscriptions = "".join(f'<article><p class="scope-label">{esc(card["label"])}</p><h3>{esc(card["title"])}</h3><p>{esc(card["text"])}</p></article>' for card in data["subscription_cards"])
    community = "".join(f'<article><h3>{esc(card["title"])}</h3><p>{esc(card["text"])}</p><a class="text-link" href="{source(lang, card["source"])}">{esc(card["link"])}{arrow(True)}</a></article>' for card in data["community_links"])
    model_rows = "".join(f'<li><span>{i:02d}</span><div><h3>{esc(row["title"])}</h3><p>{esc(row["text"])}</p></div></li>' for i, row in enumerate(data["model_rows"], 1))
    oversight = "".join(f'<article><p class="control-name">{esc(card["name"])}</p><h3>{esc(card["title"])}</h3><p>{esc(card["text"])}</p></article>' for card in data["oversight_cards"])
    delivery = "".join(f'<li><span>{i:02d}</span><h3>{esc(step["title"])}</h3><p>{esc(step["text"])}</p></li>' for i, step in enumerate(data["delivery_steps"], 1))
    loop = "".join(f'<li>{esc(step)}</li>' for step in data["loop_steps"])
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
  <meta name="robots" content="index,follow">
  <meta name="theme-color" content="#f5f8fa">
  <meta name="color-scheme" content="light dark">
  <script src="/assets/theme.js"></script>
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="en" href="{ORIGIN}/">
  <link rel="alternate" hreflang="tr" href="{ORIGIN}/tr/">
  <link rel="alternate" hreflang="x-default" href="{ORIGIN}/">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Eyleme">
  <meta property="og:title" content="{e('title')}">
  <meta property="og:description" content="{e('description')}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{e('locale')}">
  <meta property="og:locale:alternate" content="{'tr_TR' if lang == 'en' else 'en_US'}">
  <meta property="og:image" content="{ORIGIN}/assets/social.png">
  <meta property="og:image:width" content="1280">
  <meta property="og:image:height" content="640">
  <meta property="og:image:alt" content="Eyleme — Continuous development. Continuous operations.">
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
    <a class="brand" href="{'/tr/' if lang == 'tr' else '/'}" aria-label="Eyleme">{logo}</a>
    <nav class="main-nav" aria-label="{e('navigation')}"><a href="#products">{e('nav_products')}</a><a href="#oversight">{e('nav_oversight')}</a><a href="#community">{e('nav_community')}</a></nav>
    <button class="theme-toggle" type="button" aria-label="{e('theme_label')}" aria-pressed="false" data-light-label="{e('theme_light')}" data-dark-label="{e('theme_dark')}" hidden><svg class="theme-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></svg><span class="theme-track" aria-hidden="true"><span></span></span><svg class="theme-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.4 13.3A8.5 8.5 0 0 1 10.7 3.6 8.5 8.5 0 1 0 20.4 13.3Z"/></svg></button>
    {languages}
  </div></header>
  <main id="main" tabindex="-1">
    <section class="hero shell" aria-labelledby="hero-title">
      <div class="hero-heading"><p class="scope-label development-status">{e('development_status')}</p><h1 id="hero-title">{esc(data['headline'][0])}<br>{esc(data['headline'][1])}<br><span>{esc(data['headline'][2])}</span></h1></div>
      <figure class="hero-art"><img src="/assets/eyleme-ecosystem-{lang}.svg" width="640" height="600" alt="{esc(data['hero_diagram']['alt'])}" fetchpriority="high" decoding="async"><figcaption>{esc(data['hero_diagram']['caption'])}</figcaption></figure>
      <div class="hero-copy">
        <p class="hero-intro">{e('intro')}</p>
        <div class="hero-actions"><a class="button" href="#products">{e('explore')}{arrow()}</a><a class="text-link" href="{PROJECT}">{e('follow')}{arrow(True)}</a></div>
        <p class="project-status">{e('status')}</p>
      </div>
    </section>
    <div class="shell"><ul class="principles">{principles}</ul></div>
    <section class="models section shell" id="models" aria-labelledby="models-title">
      <div class="model-layout"><div><h2 id="models-title">{heading('models_title')}</h2><p class="section-intro">{e('models_intro')}</p></div><ol class="model-ledger">{model_rows}</ol></div>
      <ol class="agent-loop" aria-label="{e('loop_label')}">{loop}</ol>
      <p class="scope-note">{e('models_note')}</p>
    </section>
    <section class="oversight section" id="oversight" aria-labelledby="oversight-title"><div class="shell">
      <h2 id="oversight-title">{heading('oversight_title')}</h2><p class="section-intro">{e('oversight_intro')}</p>
      <div class="control-grid">{oversight}</div><p class="scope-note">{e('oversight_note')}</p>
    </div></section>
    <section class="delivery section shell" id="field-support" aria-labelledby="delivery-title">
      <div class="section-heading"><h2 id="delivery-title">{heading('delivery_title')}</h2><p>{e('delivery_intro')}</p></div>
      <ol class="delivery-rail">{delivery}</ol><p class="scope-note team-status">{e('delivery_note')}</p>
    </section>
    <section class="products section shell" id="products" aria-labelledby="products-title">
      <p class="section-label">{e('products_label')}</p>
      <div class="section-heading"><h2 id="products-title">{heading('products_title')}</h2><p>{e('products_intro')}</p></div>
      <ol class="product-cards">{products}</ol>
      <p class="product-note">{e('products_note')}</p>
    </section>
    <section class="subscriptions section shell" id="subscriptions" aria-labelledby="subscriptions-title">
      <p class="section-label">{e('subscriptions_label')}</p>
      <div class="section-heading"><h2 id="subscriptions-title">{heading('subscriptions_title')}</h2><p>{e('subscriptions_intro')}</p></div>
      <div class="foundation-scope">{subscriptions}</div>
      <p class="product-note">{e('subscriptions_note')}</p>
    </section>
    <section class="community section shell" id="community" aria-labelledby="community-title">
      <p class="section-label">{e('community_label')}</p>
      <div class="section-heading"><h2 id="community-title">{heading('community_title')}</h2><p>{e('community_intro')}</p></div>
      <div class="community-cards">{community}</div>
      <p class="community-issues"><a class="text-link" href="{PROJECT}/discussions">{e('community_discussions')}{arrow(True)}</a></p>
      <p class="community-issues"><a class="text-link" href="{PROJECT}/issues">{e('community_issues')}{arrow(True)}</a></p>
    </section>
    <section class="architecture section shell" id="architecture" aria-labelledby="architecture-title">
      <p class="section-label">{e('architecture_label')}</p>
      <div class="section-heading"><h2 id="architecture-title">{heading('architecture_title')}</h2><p>{e('architecture_intro')}</p></div>
      <div class="foundation-scope" aria-label="{e('foundation_label')}">{foundation}</div>
      <figure class="technology-overview" id="technology">
        <p class="technology-notice">{e('technology_notice')}</p>
        <a class="technology-image" href="/assets/eyleme-technology-{lang}.png" target="_blank" rel="noopener" aria-label="{e('technology_open')}">
          <img src="/assets/eyleme-technology-{lang}.webp" alt="{e('technology_alt')}" width="1672" height="941" loading="lazy" decoding="async">
        </a>
        <figcaption><p>{e('technology_caption')}</p><a class="text-link" href="/assets/eyleme-technology-{lang}.png" target="_blank" rel="noopener">{e('technology_open')}{arrow(True)}</a></figcaption>
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
    <section class="invitation" aria-labelledby="join-title"><div class="shell invitation-inner"><div><h2 id="join-title">{e('join_title')}</h2><p>{e('join_text')}</p></div><a class="button button-light" href="{PROJECT}/discussions">{e('join_link')}{arrow(True)}</a></div></section>
  </main>
  <footer class="site-footer shell"><a class="brand" href="{'/tr/' if lang == 'tr' else '/'}" aria-label="Eyleme">{logo}</a><p>{e('footer')}</p><nav aria-label="{e('nav_architecture')}"><a href="{source(lang, 'architecture')}">{e('nav_architecture')}</a><a href="{source(lang, 'api')}">{e('api_link')}</a></nav>{languages}</footer>
</body>
</html>
'''


def outputs(root=ROOT):
    result = {}
    for lang, path in [("en", "index.html"), ("tr", "tr/index.html")]:
        data = json.loads((root / "content" / f"{lang}.json").read_text())
        result[path] = render(data)
        result[f"assets/eyleme-ecosystem-{lang}.svg"] = ecosystem_svg(data)
    result["sitemap.xml"] = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'  <url><loc>{ORIGIN}{route}</loc><lastmod>{PAGE_MODIFIED[lang]}</lastmod></url>\n'
                  for lang, route in (("en", "/"), ("tr", "/tr/")))
        + '</urlset>\n')
    result["robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n"
    result[f"{INDEXNOW_KEY}.txt"] = INDEXNOW_KEY
    result["404.html"] = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found — Eyleme</title><meta name="robots" content="noindex"><meta name="color-scheme" content="light dark"><script src="/assets/theme.js"></script><link rel="stylesheet" href="/assets/site.css"><link rel="icon" href="/assets/favicon.svg"></head><body><main class="not-found shell"><a class="brand" href="/"><img src="/assets/eyleme-wordmark.webp" alt="Eyleme" width="190" height="63"></a><p class="section-label">404</p><h1>This page is not here.</h1><p>The address may have changed.</p><a class="button" href="/">Back to Eyleme</a><p lang="tr">Bu sayfa bulunamadı. <a class="text-link" href="/tr/">Türkçe ana sayfaya dön</a></p></main></body></html>
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
