"""Website gates: crawlability, output integrity, translations and public assets."""
import argparse
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import ORIGIN, ROOT, outputs, schema


class CheckFailure(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise CheckFailure(message)


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags, self.ids, self.references, self.data = [], [], [], []
        self.ld, self.in_ld = [], False
        self.ancestors, self.images = [], []
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.tags.append((tag, attrs))
        if tag == "img":
            hidden = attrs.get("aria-hidden") == "true" or any(a.get("aria-hidden") == "true" for _, a in self.ancestors)
            self.images.append((attrs, hidden))
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.ancestors.append((tag, attrs))
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.references.append(attrs[key])
        if "srcset" in attrs:
            self.references.extend(item.strip().split()[0] for item in attrs["srcset"].split(","))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_ld = True

    def handle_endtag(self, tag):
        for i in range(len(self.ancestors) - 1, -1, -1):
            if self.ancestors[i][0] == tag:
                del self.ancestors[i:]
                break
        if tag == "script":
            self.in_ld = False

    def handle_data(self, text):
        self.data.append(text)
        if self.in_ld:
            self.ld.append(text)


def shape(value):
    if isinstance(value, dict):
        return {key: shape(val) for key, val in value.items()}
    if isinstance(value, list):
        return [shape(val) for val in value]
    return type(value).__name__


def check_content(en, tr):
    require(shape(en) == shape(tr), "English/Turkish content structure differs")
    require(en["lang"] == "en" and tr["lang"] == "tr", "Incorrect content locale")
    for data in (en, tr):
        require(40 <= len(data["title"]) <= 70, "Review title length")
        require(110 <= len(data["description"]) <= 170, "Review description length")
        for step in data["steps"]:
            require(step["source"] in {"architecture", "api", "teams", "learning"}, "Unknown source")
    for left, right in zip(en["steps"], tr["steps"]):
        require(left["id"] == right["id"] and left["source"] == right["source"], "Translated machine identifier drift")


def check_page(public, relative, data):
    path = public / relative
    page = Page(path.read_text())
    require(len(page.ids) == len(set(page.ids)), f"Duplicate HTML IDs: {relative}")
    require(sum(tag == "h1" for tag, _ in page.tags) == 1, f"Expected one H1: {relative}")
    require(sum(tag == "main" for tag, _ in page.tags) == 1, f"Expected main landmark: {relative}")
    html = next(attrs for tag, attrs in page.tags if tag == "html")
    require(html.get("lang") == data["lang"], "Incorrect document language")
    head_links = [attrs for tag, attrs in page.tags if tag == "link"]
    canonical = [attrs["href"] for attrs in head_links if attrs.get("rel") == "canonical"]
    expected = ORIGIN + ("/tr/" if data["lang"] == "tr" else "/")
    require(canonical == [expected], "Incorrect canonical URL")
    alternatives = {a.get("hreflang"): a.get("href") for a in head_links if a.get("rel") == "alternate"}
    require(alternatives == {"en": ORIGIN + "/", "tr": ORIGIN + "/tr/", "x-default": ORIGIN + "/"}, "Incorrect reciprocal hreflang")
    require(json.loads("".join(page.ld)) == schema(data), "Structured data differs from visible content source")
    meta = {a.get("name", a.get("property")): a.get("content") for tag, a in page.tags if tag == "meta"}
    require(meta.get("description") == data["description"], "Incorrect description")
    require(meta.get("og:url") == expected, "Incorrect social URL")
    require(meta.get("robots") == "index,follow,max-image-preview:large", "Page is not indexable")
    require(not any(tag == "meta" and a.get("http-equiv", "").lower() == "refresh" for tag, a in page.tags), "Language auto-redirect is forbidden")
    plain = " ".join(page.data)
    for question in data["questions"]:
        require(question["answer"] in plain, "FAQ answer missing from initial HTML")
    for step in data["steps"]:
        require(step["text"] in plain, "Architecture text missing from initial HTML")
    hero_images = [(attrs, hidden) for attrs, hidden in page.images if attrs.get("src") == "/assets/eylema-loop-1024.webp"]
    require(len(hero_images) == 1 and hero_images[0][1], "Decorative hero must remain hidden from assistive technology")
    require(bool(data["hero_art_alt"].strip()) and hero_images[0][0].get("alt") == data["hero_art_alt"], "Decorative hero needs the localized crawler alternative")
    for tag, attrs in page.tags:
        require(not any(key.startswith("on") for key in attrs), "Inline event handler found")
        if tag == "img":
            require(all(key in attrs for key in ("alt", "width", "height")), "Image lacks alternative text or stable dimensions")
        if tag in {"script", "img"} and "src" in attrs:
            require(attrs["src"].startswith("/assets/"), "Unexpected remote resource")
    for reference in page.references:
        parsed = urlsplit(reference)
        require(parsed.scheme in {"", "https"}, f"Unsafe reference: {reference}")
        if parsed.scheme:
            continue
        target = public / unquote(parsed.path.lstrip("/")) if parsed.path.startswith("/") else path.parent / unquote(parsed.path)
        if not parsed.path:
            target = path
        if target.is_dir():
            target /= "index.html"
        require(target.resolve().is_relative_to(public.resolve()), "Reference escapes public output")
        require(target.is_file(), f"Missing local link or asset: {reference}")
        if parsed.fragment:
            require(parsed.fragment in Page(target.read_text()).ids, f"Broken fragment: {reference}")


def translation_hashes(root, write=False):
    path = root / "tools/translation-pairs.json"
    manifest = json.loads(path.read_text())
    for pair in manifest["pairs"]:
        for lang in ("en", "tr"):
            digest = hashlib.sha256((root / pair[lang]).read_bytes()).hexdigest()
            if write:
                pair[lang + "_sha256"] = digest
            else:
                require(pair.get(lang + "_sha256") == digest, f"Stale reviewed translation: {pair[lang]}")
    if write:
        path.write_text(json.dumps(manifest, indent=2) + "\n")


def check_markdown(root, path, text):
    prose = re.sub(r"^```.*?^```\s*$", "", text, flags=re.M | re.S)
    for link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
        parsed = urlsplit(link.strip("<>"))
        if parsed.scheme in {"https", "http"} or link.startswith("#"):
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        require(not parsed.scheme and target.is_relative_to(root.resolve()) and target.is_file(), f"Broken documentation link: {path.name}: {link}")


def check_host_config(config):
    require(config.get("trailingSlash") == "auto", "Host must preserve asset URLs and directory slashes")
    require("navigationFallback" not in config, "SPA fallback would hide missing pages")
    require(config.get("responseOverrides", {}).get("404") == {"rewrite": "/404.html", "statusCode": 404}, "Host must return a real custom 404")
    require(config.get("globalHeaders", {}).get("Cache-Control") == "public, max-age=0, must-revalidate", "Unhashed assets must be revalidated")


def check(root=ROOT):
    check_host_config(json.loads((root / "public/staticwebapp.config.json").read_text()))
    content = {lang: json.loads((root / "content" / f"{lang}.json").read_text()) for lang in ("en", "tr")}
    check_content(content["en"], content["tr"])
    for name, generated in outputs(root).items():
        require((root / "public" / name).read_text() == generated, f"Stale generated file: {name}")
    for lang, path in [("en", "index.html"), ("tr", "tr/index.html")]:
        check_page(root / "public", path, content[lang])
    sitemap = ET.parse(root / "public/sitemap.xml")
    urls = [e.text for e in sitemap.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    require(urls == [ORIGIN + "/", ORIGIN + "/tr/"], "Sitemap contains unexpected or missing URLs")
    require("noindex" in (root / "public/404.html").read_text(), "404 page must be noindex")
    translation_hashes(root)
    paths = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "-z"], cwd=root, capture_output=True, check=True).stdout.decode().split("\0")
    for name in set(paths) - {""}:
        path = root / name
        require(not path.is_symlink(), f"Unexpected symlink: {name}")
        if path.suffix in {".md", ".json", ".html", ".css", ".js", ".yml", ".txt"}:
            text = path.read_text()
            require(not re.search(r"/Users/[^/\s]+/|/home/[^/\s]+/|file://|codex://", text), f"Private machine path: {name}")
            if path.suffix == ".md":
                check_markdown(root, path, text)
    total = sum(p.stat().st_size for p in (root / "public/assets").glob("*") if p.suffix in {".js", ".css"})
    require(total < 35000, "CSS/JS exceed the 35 KB raw budget")
    print("PASS: bilingual HTML, canonical/hreflang, JSON-LD, sitemap, assets, translation fingerprints and 35 KB CSS/JS budget")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-translation-hashes", action="store_true")
    args = parser.parse_args()
    if args.write_translation_hashes:
        translation_hashes(ROOT, write=True)
    else:
        check()
