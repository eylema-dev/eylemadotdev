"""Preview or explicitly submit the two canonical Eyleme URLs to IndexNow."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from build import INDEXNOW_KEY, ORIGIN
from check_live import require_indexable
from check_repository import Page

ENDPOINT = "https://api.indexnow.org/indexnow"
URLS = [ORIGIN + "/", ORIGIN + "/tr/"]
LIMIT = 65536


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def payload():
    return {"host": urlsplit(ORIGIN).hostname, "key": INDEXNOW_KEY,
            "keyLocation": f"{ORIGIN}/{INDEXNOW_KEY}.txt", "urlList": URLS.copy()}


def validate(data):
    if ORIGIN != "https://eyleme.dev" or data.get("host") != "eyleme.dev":
        raise ValueError("IndexNow is scoped to the current eyleme.dev host")
    key = data.get("key", "")
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key):
        raise ValueError("Invalid IndexNow key")
    if data.get("keyLocation") != f"{ORIGIN}/{key}.txt":
        raise ValueError("Ownership file must be at the canonical host root")
    if data.get("urlList") != [ORIGIN + "/", ORIGIN + "/tr/"]:
        raise ValueError("Submit exactly the two canonical URLs without duplicates")


def read(opener, request):
    try:
        response = opener.open(request, timeout=25)
    except HTTPError as error:
        response = error
    with response:
        body = response.read(LIMIT + 1)
        if len(body) > LIMIT:
            raise ValueError("Response exceeds the bounded read limit")
        return response.status, response.headers, body, response.geturl()


def preflight(opener, data):
    evidence = {"key": {}, "pages": {}}
    for url in [data["keyLocation"], *data["urlList"]]:
        status, headers, body, final = read(opener, Request(url, headers={"User-Agent": "Eyleme-IndexNow/1.0"}))
        if status != 200 or final != url:
            raise ValueError(f"Preflight requires HTTPS200 without redirects: {url}, HTTP {status}")
        require_indexable(headers, url)
        if url == data["keyLocation"]:
            if headers.get_content_type() != "text/plain" or body != data["key"].encode("utf-8"):
                raise ValueError("Ownership file must serve text/plain with exact UTF-8 key bytes")
            evidence["key"] = {"url": url, "httpStatus": status, "mime": "text/plain",
                               "sha256": hashlib.sha256(body).hexdigest()}
        else:
            if headers.get_content_type() != "text/html":
                raise ValueError(f"Landing page must be text/html: {url}")
            page = Page(body.decode("utf-8"))
            bots = [a for tag, a in page.tags if tag == "meta" and
                    a.get("name", "").lower() in {"robots", "googlebot", "bingbot"}]
            canonical = [a.get("href") for tag, a in page.tags if tag == "link" and a.get("rel") == "canonical"]
            if len(bots) != 1 or bots[0].get("name") != "robots" or bots[0].get("content") != "index,follow" or canonical != [url]:
                raise ValueError(f"Landing page is blocked or has incorrect canonical metadata: {url}")
            evidence["pages"][url] = {"httpStatus": status, "canonical": url, "robots": "index,follow"}
    return evidence


def submit():
    data = payload()
    validate(data)
    opener = build_opener(NoRedirect())
    evidence = preflight(opener, data)
    request = Request(ENDPOINT, data=json.dumps(data).encode("utf-8"), method="POST",
                      headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "Eyleme-IndexNow/1.0"})
    status, headers, body, final = read(opener, request)
    return {"checkedAt": datetime.now(timezone.utc).isoformat(), "endpoint": ENDPOINT,
            "httpStatus": status, "responseURL": final,
            "outcome": {200: "submitted", 202: "key_validation_pending"}.get(status, "rejected"),
            "responseBody": body.decode("utf-8", errors="replace")[:2048],
            "retryAfter": headers.get("Retry-After"), "payload": data, "preflight": evidence,
            "indexingConfirmed": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submit", action="store_true", help="Preflight then send one POST; no automatic retry")
    parser.add_argument("--receipt", type=Path, help="Save the actual protocol receipt as JSON")
    args = parser.parse_args(argv)
    if not args.submit:
        if args.receipt:
            parser.error("--receipt requires --submit")
        print(json.dumps({"mode": "preview_only", "submissionEnabled": True, "payload": payload()}, indent=2))
        return 0
    if args.receipt and args.receipt.exists():
        parser.error("Receipt already exists; no submission sent")
    try:
        receipt = submit()
    except (ValueError, URLError, TimeoutError) as error:
        parser.exit(2, str(error) + "\n")
    rendered = json.dumps(receipt, indent=2) + "\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        with args.receipt.open("x") as target:
            target.write(rendered)
    print(rendered, end="")
    return 0 if receipt["httpStatus"] in {200, 202} else 1


if __name__ == "__main__":
    raise SystemExit(main())
