"""Regression and failure coverage for the website build and SEO gates."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build import ROOT, render
from check_repository import CheckFailure, Page, check_content, check_markdown, check_page, translation_hashes
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
        text = render(self.en).replace('rel="canonical" href="https://eylema.dev/"', 'rel="canonical" href="https://eylema.dev/tr/"')
        with self.assertRaisesRegex(CheckFailure, "canonical"):
            self.check_modified(text)

    def test_missing_reciprocal_locale_fails(self):
        text = render(self.en).replace('hreflang="tr"', 'hreflang="de"')
        with self.assertRaisesRegex(CheckFailure, "hreflang"):
            self.check_modified(text)

    def test_noindex_on_landing_page_fails(self):
        text = render(self.en).replace('content="index,follow,max-image-preview:large"', 'content="noindex"')
        with self.assertRaisesRegex(CheckFailure, "indexable"):
            self.check_modified(text)

    def test_structured_claim_drift_fails(self):
        text = render(self.en).replace('"name":"Eylema"', '"name":"Different project"', 1)
        with self.assertRaisesRegex(CheckFailure, "Structured data"):
            self.check_modified(text)

    def test_duplicate_heading_id_fails(self):
        text = render(self.en).replace('id="architecture-title"', 'id="hero-title"')
        with self.assertRaisesRegex(CheckFailure, "Duplicate HTML"):
            self.check_modified(text)

    def test_missing_local_asset_fails(self):
        with self.assertRaisesRegex(CheckFailure, "Missing local"):
            self.check_modified(render(self.en))

    def test_all_answers_exist_without_javascript(self):
        page = Page(render(self.en))
        text = " ".join(page.data)
        for row in self.en["questions"]:
            self.assertIn(row["answer"], text)
        for step in self.en["steps"]:
            self.assertIn(step["text"], text)

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
