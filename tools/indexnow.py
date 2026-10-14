"""Preview or submit the two canonical pages after checking their live ownership file."""
import argparse
import json
from datetime import datetime, timezone
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from build import INDEXNOW_KEY, ORIGIN
from check_live import fetch

ENDPOINT = "https://api.indexnow.org/indexnow"
URLS = [ORIGIN + "/", ORIGIN + "/tr/"]


def payload():
    return {
        "host": urlsplit(ORIGIN).hostname,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{ORIGIN}/{INDEXNOW_KEY}.txt",
        "urlList": URLS.copy(),
    }


def preflight(data):
    location = data["keyLocation"]
    status, headers, body, final = fetch(location)
    if (status != 200 or final != location or
            headers.get_content_type() != "text/plain" or
            body != data["key"].encode("utf-8")):
        raise ValueError("Live IndexNow key must return exact UTF-8 text/plain bytes without redirects")
    for url in data["urlList"]:
        status, headers, _, final = fetch(url)
        if status != 200 or final != url or headers.get_content_type() != "text/html":
            raise ValueError(f"Canonical page is unavailable or redirected: {url}")


def submit():
    data = payload()
    preflight(data)  # No POST if ownership or canonical routes fail.
    request = Request(ENDPOINT, data=json.dumps(data).encode("utf-8"), method="POST",
                      headers={"Content-Type": "application/json; charset=utf-8",
                               "User-Agent": "Eyleme-IndexNow/1.0"})
    try:
        response = urlopen(request, timeout=30)
    except HTTPError as error:
        response = error
    with response:
        status = response.status
        body = response.read(4096).decode("utf-8", errors="replace")
    if status not in {200, 202}:
        raise ValueError(f"IndexNow rejected submission: HTTP {status}: {body}")
    return {
        "submittedAt": datetime.now(timezone.utc).isoformat(),
        "endpoint": ENDPOINT,
        "urls": data["urlList"],
        "httpStatus": status,
        "result": "submitted" if status == 200 else "received; key validation pending",
        "indexing": "not established by this receipt",
        "response": body,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submit", action="store_true", help="Check live pages and send one POST; no retries")
    args = parser.parse_args()
    print(json.dumps(submit() if args.submit else payload(), indent=2))
