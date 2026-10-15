"""Regression and failure coverage for the website build and SEO gates."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build import ROOT, render, outputs
from check_repository import CheckFailure, Page, check_content, check_markdown, check_page, check_search_files, translation_hashes
from check_pr import validate_body


class WebsiteTests(unittest.TestCase):
    def setUp(self):
        self.en = json.loads((ROOT / "content/en.json").read_text())
        self.tr = json.loads((ROOT / "content/tr.json").read_text())

    def check_modified(self, text):
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            (public / "index.html").write_text(text)
            check_page(public, "index.html", self.en)

    def test_translation_rejects_missing_answer(self):
        del self.tr["questions"][0]["answer"]
        with self.assertRaisesRegex(CheckFailure, "structure differs"):
            check_content(self.en, self.tr)

    def test_translation_rejects_machine_identifier_change(self):
        self.tr["steps"][0]["id"] = "tanimla"
        with self.assertRaisesRegex(CheckFailure, "identifier drift"):
            check_content(self.en, self.tr)

    def test_translation_rejects_wrong_locale(self):
        self.tr["lang"] = "en"
        with self.assertRaisesRegex(CheckFailure, "content locale"):
            check_content(self.en, self.tr)

    def test_product_order_is_explicit_in_each_language(self):
        check_content(self.en, self.tr)
        for data in (self.en, self.tr):
            data["products"][0], data["products"][1] = data["products"][1], data["products"][0]
            with self.assertRaisesRegex(CheckFailure, "Product family must preserve"):
                check_content(self.en, self.tr)
            data["products"][0], data["products"][1] = data["products"][1], data["products"][0]

    def test_subscription_terms_cannot_disappear_from_static_html(self):
        text = render(self.en).replace(self.en["products_note"], "")
        with self.assertRaisesRegex(CheckFailure, "Subscription availability notice"):
            self.check_modified(text)

    def test_product_availability_cannot_disappear_from_static_html(self):
        text = render(self.en).replace(self.en["products"][0]["status"], "")
        with self.assertRaisesRegex(CheckFailure, "Product model or availability"):
            self.check_modified(text)

    def test_private_product_links_are_rejected(self):
        for target in ("https://github.com/derleme-dev/derleme", "https://github.com/eyleme-dev/onama"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as directory:
                # Existing local assets remain available so this exercises the new link gate.
                public = Path(directory)
                import shutil
                shutil.copytree(ROOT / "public", public, dirs_exist_ok=True)
                text = render(self.en).replace('</body>', f'<a href="{target}">Private source</a></body>')
                (public / "index.html").write_text(text)
                with self.assertRaisesRegex(CheckFailure, "private product repositories"):
                    check_page(public, "index.html", self.en)

    def test_missing_documentation_target_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(CheckFailure, "Broken documentation"):
                check_markdown(root, root / "README.md", "[Guide](missing.md)")

    def test_escaping_documentation_target_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(CheckFailure, "Broken documentation"):
                check_markdown(root, root / "README.md", "[Guide](../outside.md)")

    def test_documentation_anchors_and_https_are_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            check_markdown(root, root / "README.md", "[Guide](https://example.com/guide) [Here](#section)")

    def test_real_pr_rejects_blank_template(self):
        template = (ROOT / ".github/PULL_REQUEST_TEMPLATE.md").read_text()
        self.assertTrue(validate_body(template))
        self.assertEqual(validate_body(template, allow_template=True), [])

    def test_html_and_jsonld_cannot_be_closed_by_content(self):
        malicious = '</script><img src=x onerror="alert(1)">'
        self.en["description"] = malicious
        text = render(self.en)
        page = Page(text)
        self.assertNotIn(malicious, text)
        self.assertEqual(json.loads("".join(page.ld))["@graph"][2]["description"], malicious)
        self.assertEqual(sum(tag == "script" for tag, _ in page.tags), 2)

    def test_wrong_turkish_canonical_fails(self):
        text = render(self.en).replace('rel="canonical" href="https://eyleme.dev/"', 'rel="canonical" href="https://eyleme.dev/tr/"')
        with self.assertRaisesRegex(CheckFailure, "canonical"):
            self.check_modified(text)

    def test_missing_reciprocal_locale_fails(self):
        text = render(self.en).replace('hreflang="tr"', 'hreflang="de"')
        with self.assertRaisesRegex(CheckFailure, "hreflang"):
            self.check_modified(text)

    def test_noindex_on_landing_page_fails(self):
        text = render(self.en).replace('content="index,follow"', 'content="noindex,follow"')
        with self.assertRaisesRegex(CheckFailure, "index,follow"):
            self.check_modified(text)

    def test_duplicate_or_bot_specific_directives_fail(self):
        for extra in ['<meta name="robots" content="noindex,follow">',
                      '<meta name="googlebot" content="index">',
                      '<meta name="bingbot" content="index">']:
            with self.subTest(extra=extra):
                text = render(self.en).replace('</head>', extra + '</head>')
                with self.assertRaisesRegex(CheckFailure, "index,follow"):
                    self.check_modified(text)

    def test_crawl_blocks_and_wrong_sitemap_advertisement_fail(self):
        generated = outputs()
        for robots in ['User-agent: *\nDisallow: /\n',
                       generated['robots.txt'].replace('eyleme.dev', 'eylema.dev')]:
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / 'robots.txt').write_text(robots)
                (root / 'sitemap.xml').write_text(generated['sitemap.xml'])
                with self.assertRaisesRegex(CheckFailure, "Robots must allow"):
                    check_search_files(root)

    def test_incomplete_duplicate_foreign_or_stale_sitemap_fails(self):
        correct = outputs()['sitemap.xml']
        from build import PAGE_MODIFIED
        tr_node = f'<url><loc>https://eyleme.dev/tr/</loc><lastmod>{PAGE_MODIFIED["tr"]}</lastmod></url>'
        mutations = [
            correct.replace(tr_node, ''),
            correct.replace('https://eyleme.dev/tr/', 'https://eyleme.dev/'),
            correct.replace('https://eyleme.dev/tr/', 'https://eylema.dev/tr/'),
            correct.replace(PAGE_MODIFIED['en'], '2020-01-01'),
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>',
        ]
        for xml in mutations:
            with self.subTest(xml=xml), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / 'robots.txt').write_text(outputs()['robots.txt'])
                (root / 'sitemap.xml').write_text(xml)
                with self.assertRaisesRegex(CheckFailure, "both canonical URLs"):
                    check_search_files(root)

    def test_structured_claim_drift_fails(self):
        text = render(self.en).replace('"name":"Eyleme"', '"name":"Different project"', 1)
        with self.assertRaisesRegex(CheckFailure, "Structured data"):
            self.check_modified(text)

    def test_duplicate_heading_id_fails(self):
        text = render(self.en).replace('id="architecture-title"', 'id="hero-title"')
        with self.assertRaisesRegex(CheckFailure, "Duplicate HTML"):
            self.check_modified(text)

    def test_missing_local_asset_fails(self):
        with self.assertRaisesRegex(CheckFailure, "Missing local"):
            self.check_modified(render(self.en))

    def test_decorative_hero_cannot_be_exposed(self):
        text = render(self.en).replace('<div class="hero-art" aria-hidden="true">', '<div class="hero-art">')
        with self.assertRaisesRegex(CheckFailure, "hidden from assistive"):
            self.check_modified(text)

    def test_decorative_hero_cannot_have_blank_alternative(self):
        self.en["hero_art_alt"] = ""
        with self.assertRaisesRegex(CheckFailure, "localized crawler alternative"):
            self.check_modified(render(self.en))

    def test_hiding_does_not_leak_into_informative_images(self):
        for data in (self.en, self.tr):
            page = Page(render(data))
            images = {attrs["src"]: (attrs, hidden) for attrs, hidden in page.images}
            hero, hidden = images["/assets/eyleme-loop-1024.webp"]
            self.assertTrue(hidden)
            self.assertEqual(hero["alt"], data["hero_art_alt"])
            _, hidden = images[f'/assets/eyleme-technology-{data["lang"]}.webp']
            self.assertFalse(hidden)

    def test_all_answers_exist_without_javascript(self):
        page = Page(render(self.en))
        text = " ".join(page.data)
        for row in self.en["questions"]:
            self.assertIn(row["answer"], text)
        for step in self.en["steps"]:
            self.assertIn(step["text"], text)

    def test_missing_foundation_scope_fails(self):
        text = render(self.en).replace(self.en["foundation_cards"][0]["text"], "")
        with self.assertRaisesRegex(CheckFailure, "Foundation scope missing"):
            self.check_modified(text)

    def test_component_evidence_links_target_core_in_both_languages(self):
        # Component execution evidence belongs in core, not the product-prose repo.
        for data in (self.en, self.tr):
            page = Page(render(data))
            hrefs = {attrs.get("href") for tag, attrs in page.tags if tag == "a"}
            for filename in ("real-human", "platform-contracts", "model-contract",
                             "memory-contracts", "decision-evidence", "project-data"):
                with self.subTest(lang=data["lang"], component=filename):
                    tail = f'docs/{data["lang"]}/{filename}.md'
                    self.assertIn(f"https://github.com/eyleme-dev/eyleme/blob/main/{tail}", hrefs)
                    self.assertNotIn(f'https://github.com/eyleme-dev/eyleme-docs-{data["lang"]}/blob/main/{tail}', hrefs)

    def test_architecture_illustration_requires_visible_notice(self):
        text = render(self.en).replace(self.en["technology_notice"], "")
        with self.assertRaisesRegex(CheckFailure, "Architecture illustration"):
            self.check_modified(text)

    def test_stale_translation_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tools").mkdir()
            (root / "en.md").write_text("Source")
            (root / "tr.md").write_text("Kaynak")
            (root / "tools/translation-pairs.json").write_text(json.dumps({"pairs": [{"en": "en.md", "tr": "tr.md"}]}))
            translation_hashes(root, write=True)
            (root / "tr.md").write_text("Değişti")
            with self.assertRaisesRegex(CheckFailure, "Stale reviewed"):
                translation_hashes(root)


if __name__ == "__main__":
    unittest.main()
