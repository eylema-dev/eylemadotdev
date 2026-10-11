"""Negative release and hosting coverage; network evidence is checked on the live host."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build import ROOT
from check_live import verify_release
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


if __name__ == "__main__":
    unittest.main()
