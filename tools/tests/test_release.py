"""Negative release and hosting coverage; network evidence is checked on the live host."""
import copy
import json
import io
from email.message import Message
from unittest.mock import patch
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build import ROOT
from check_live import verify_release, check, require_noindex
from check_repository import CheckFailure, check_host_config
from release import file_hashes, manifest


class ReleaseTests(unittest.TestCase):
    def test_short_commit_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "full lowercase"):
            manifest(ROOT / "public", "123abc")

    def test_missing_site_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "Incomplete"):
                file_hashes(Path(directory))

    def test_symlink_cannot_publish_outside_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "escape").symlink_to(ROOT / "README.md")
            with self.assertRaisesRegex(ValueError, "Symlinks"):
                file_hashes(root)

    def test_wrong_live_commit_is_rejected(self):
        expected = manifest(ROOT / "public", "a" * 40)
        remote = copy.deepcopy(expected)
        remote["commit"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "identity"):
            verify_release(remote, expected)

    def test_changed_live_inventory_is_rejected(self):
        expected = manifest(ROOT / "public", "a" * 40)
        remote = copy.deepcopy(expected)
        remote["files"]["index.html"] = "wrong"
        with self.assertRaisesRegex(ValueError, "inventory"):
            verify_release(remote, expected)

    def test_host_rejects_spa_fallback(self):
        config = json.loads((ROOT / "public/staticwebapp.config.json").read_text())
        config["navigationFallback"] = {"rewrite": "/index.html"}
        with self.assertRaisesRegex(CheckFailure, "SPA fallback"):
            check_host_config(config)

    def test_host_rejects_soft_404(self):
        config = json.loads((ROOT / "public/staticwebapp.config.json").read_text())
        config["responseOverrides"]["404"]["statusCode"] = 200
        with self.assertRaisesRegex(CheckFailure, "real custom 404"):
            check_host_config(config)

    def test_host_rejects_redirected_assets(self):
        config = json.loads((ROOT / "public/staticwebapp.config.json").read_text())
        config["trailingSlash"] = "always"
        with self.assertRaisesRegex(CheckFailure, "asset URLs"):
            check_host_config(config)

    def test_global_noindex_is_required_and_cannot_be_overridden(self):
        original = json.loads((ROOT / "public/staticwebapp.config.json").read_text())
        for value in [None, "index,follow", "", "noindex"]:
            config = copy.deepcopy(original)
            if value is None:
                del config["globalHeaders"]["X-Robots-Tag"]
            else:
                config["globalHeaders"]["X-Robots-Tag"] = value
            with self.subTest(value=value), self.assertRaisesRegex(CheckFailure, "Global X-Robots"):
                check_host_config(config)
        config = copy.deepcopy(original)
        config["routes"].append({"route": "/assets/*", "headers": {"x-robots-tag": ""}})
        with self.assertRaisesRegex(CheckFailure, "Route must not override"):
            check_host_config(config)
        config = copy.deepcopy(original)
        config["globalHeaders"]["x-robots-tag"] = "index"
        with self.assertRaisesRegex(CheckFailure, "Global X-Robots"):
            check_host_config(config)

    def test_live_noindex_rejects_missing_conflicting_or_duplicate_headers(self):
        for values in [[], ["index,follow"], ["noindex"], ["noindex,follow", "googlebot: index"]]:
            headers = Message()
            for value in values:
                headers["X-Robots-Tag"] = value
            with self.subTest(values=values), self.assertRaisesRegex(ValueError, "noindex header"):
                require_noindex(headers, "/sample")

    def test_live_policy_covers_release_assets_pages_normalized_routes_and_404(self):
        origin, commit = "https://eyleme.dev", "a" * 40
        expected = manifest(ROOT / "public", commit)
        types = {"html": "text/html", "css": "text/css", "js": "application/javascript",
                 "png": "image/png", "webp": "image/webp", "svg": "image/svg+xml",
                 "xml": "application/xml", "txt": "text/plain"}
        def response(url, missing):
            route = url.removeprefix(origin)
            headers = Message()
            headers["X-Content-Type-Options"] = "nosniff"
            if route != missing:
                headers["X-Robots-Tag"] = "noindex,follow"
            if route == "/release.json":
                return 200, headers, json.dumps(expected).encode(), url
            normalized = {"/index.html": "/", "/tr/index.html": "/tr/", "/tr": "/tr/"}
            final = origin + normalized.get(route, route)
            path = {"/": "index.html", "/tr/": "tr/index.html", "/tr": "tr/index.html"}.get(route, route.lstrip("/"))
            status = 200
            if route.startswith("/not-a-page-"):
                path, status = "404.html", 404
            headers["Content-Type"] = types[path.rsplit(".", 1)[-1]]
            return status, headers, (ROOT / "public" / path).read_bytes(), final
        missing_routes = ["/release.json", "/", "/tr/", "/assets/eyleme-wordmark.webp",
                          "/not-a-page-" + commit[:12], "/index.html", "/tr/index.html", "/tr"]
        for missing in missing_routes:
            with self.subTest(missing=missing), patch("check_live.fetch", side_effect=lambda url: response(url, missing)):
                with self.assertRaisesRegex(ValueError, "noindex header"):
                    check(origin, commit)
        with patch("check_live.fetch", side_effect=lambda url: response(url, None)), patch("sys.stdout", new=io.StringIO()):
            check(origin, commit)


if __name__ == "__main__":
    unittest.main()
