"""Submission must stop before POST for invalid ownership or canonical routes."""
import json
import sys
import unittest
from email.message import Message
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import indexnow


def fetched(url, body=b"", content_type="text/html", status=200):
    headers = Message()
    headers["Content-Type"] = content_type
    return status, headers, body, url


class IndexNowTests(unittest.TestCase):
    def live(self):
        data = indexnow.payload()
        return [fetched(data["keyLocation"], data["key"].encode(), "text/plain"),
                *(fetched(url) for url in data["urlList"])]

    @patch("indexnow.urlopen")
    @patch("indexnow.fetch")
    def test_wrong_key_or_html_error_cannot_submit(self, fetch, post):
        location = indexnow.payload()["keyLocation"]
        for body, kind in [(b"different", "text/plain"), (b"not found", "text/html")]:
            fetch.return_value = fetched(location, body, kind)
            with self.assertRaisesRegex(ValueError, "Live IndexNow key"):
                indexnow.submit()
        post.assert_not_called()

    @patch("indexnow.urlopen")
    @patch("indexnow.fetch")
    def test_missing_or_redirected_locale_cannot_submit(self, fetch, post):
        for result in [fetched(indexnow.URLS[1], status=404), fetched(indexnow.URLS[0])]:
            fetch.side_effect = self.live()[:2] + [result]
            with self.assertRaisesRegex(ValueError, "Canonical page"):
                indexnow.submit()
        post.assert_not_called()

    @patch("indexnow.urlopen")
    @patch("indexnow.fetch")
    def test_receipt_distinguishes_validation_and_indexing(self, fetch, post):
        for status in (200, 202):
            fetch.side_effect = self.live()
            response = MagicMock()
            response.__enter__.return_value = response
            response.status = status
            response.read.return_value = b""
            post.return_value = response
            receipt = indexnow.submit()
            self.assertEqual(receipt["httpStatus"], status)
            self.assertIn("not established", receipt["indexing"])
            if status == 202:
                self.assertIn("pending", receipt["result"])
            request = post.call_args.args[0]
            self.assertEqual(request.full_url, indexnow.ENDPOINT)
            self.assertEqual(request.method, "POST")
            self.assertEqual(json.loads(request.data)["urlList"], indexnow.URLS)

    @patch("indexnow.urlopen")
    @patch("indexnow.fetch")
    def test_rejection_is_not_success_or_retried(self, fetch, post):
        fetch.side_effect = self.live()
        response = MagicMock()
        response.__enter__.return_value = response
        response.status = 429
        response.read.return_value = b"rate limited"
        post.return_value = response
        with self.assertRaisesRegex(ValueError, "HTTP 429"):
            indexnow.submit()
        post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
