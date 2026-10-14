"""The search-removal policy must prevent every submission network request."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import indexnow
from build import ROOT


class IndexNowTests(unittest.TestCase):
    @patch("urllib.request.urlopen")
    @patch("socket.create_connection")
    def test_submission_refuses_before_network(self, connect, request):
        with self.assertRaisesRegex(ValueError, "disabled.*search-removal"):
            indexnow.submit()
        request.assert_not_called()
        connect.assert_not_called()

    def test_cli_submission_is_nonzero_and_explicit(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools/indexnow.py"), "--submit"],
                                capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 2)
        self.assertIn("disabled", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_preview_is_explicitly_non_submitting(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools/indexnow.py")],
                                capture_output=True, text=True, timeout=5, check=True)
        preview = json.loads(result.stdout)
        self.assertEqual(preview["mode"], "preview_only")
        self.assertIs(preview["submissionEnabled"], False)
        self.assertEqual(preview["payload"], indexnow.payload())

    def test_existing_public_ownership_bytes_are_retained(self):
        data = indexnow.payload()
        self.assertEqual((ROOT / "public" / f'{data["key"]}.txt').read_bytes(), data["key"].encode())


if __name__ == "__main__":
    unittest.main()
