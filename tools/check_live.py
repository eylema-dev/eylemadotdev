"""Verify an HTTPS website's release, source hashes, MIME types and true 404."""
import argparse
import hashlib
import json
from urllib.error import HTTPError
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen

from build import ROOT
from release import manifest


def fetch(url):
    request = Request(url, headers={"User-Agent": "Eyleme-release-check/1.0", "Cache-Control": "no-cache"})
    try:
        response = urlopen(request, timeout=25)
    except HTTPError as error:
        response = error
    with response:
        return response.status, response.headers, response.read(), response.url


def verify_release(data, expected):
    if data.get("commit") != expected["commit"] or data.get("repository") != expected["repository"]:
        raise ValueError("Live release identity differs from source")
    if data.get("files") != expected["files"]:
        raise ValueError("Live release file inventory differs from source")


def require_indexable(headers, route):
    values = headers.get_all("X-Robots-Tag", [])
    if values and (len(values) != 1 or [value.strip().lower() for value in values[0].split(",")] != ["index", "follow"]):
        raise ValueError(f"Blocking or conflicting indexing header: {route}")


def check(origin, commit):
    parts = urlsplit(origin)
    if parts.scheme != "https" or not parts.netloc or parts.path not in {"", "/"} or parts.query or parts.fragment or parts.username:
        raise ValueError("Use a plain HTTPS origin")
    origin = origin.rstrip("/")
    expected = manifest(ROOT / "public", commit)
    status, headers, body, _ = fetch(origin + "/release.json")
    require_indexable(headers, "/release.json")
    if status != 200:
        raise ValueError(f"Release endpoint returned {status}")
    verify_release(json.loads(body), expected)
    types = {"html": "text/html", "css": "text/css", "js": ("text/javascript", "application/javascript"), "png": "image/png", "webp": "image/webp", "svg": "image/svg+xml", "xml": ("application/xml", "text/xml"), "txt": "text/plain"}
    for path, digest in expected["files"].items():
        route = "/" if path == "index.html" else "/tr/" if path == "tr/index.html" else "/" + quote(path)
        status, headers, body, final = fetch(origin + route)
        if path != "404.html":
            require_indexable(headers, route)
        if status != 200 or hashlib.sha256(body).hexdigest() != digest:
            raise ValueError(f"HTTP/source mismatch: {route}, status={status}")
        allowed = types.get(path.rsplit(".", 1)[-1])
        if isinstance(allowed, str):
            allowed = (allowed,)
        if allowed and headers.get_content_type() not in allowed:
            raise ValueError(f"Unexpected content type: {route}: {headers.get_content_type()}")
        if route.startswith("/assets/") and final != origin + route:
            raise ValueError(f"Unexpected asset redirect: {route}")
        if headers.get("X-Content-Type-Options") != "nosniff":
            raise ValueError(f"Host configuration missing: {route}")
    status, headers, body, _ = fetch(origin + "/not-a-page-" + commit[:12])
    if status != 404 or hashlib.sha256(body).hexdigest() != expected["files"]["404.html"]:
        raise ValueError("Missing route is not the genuine custom HTTP 404")
    for route, target in [("/index.html", "/"), ("/tr/index.html", "/tr/"), ("/tr", "/tr/")]:
        status, headers, _, final = fetch(origin + route)
        require_indexable(headers, route)
        if status != 200 or final != origin + target:
            raise ValueError(f"Canonical route normalization failed: {route}")
    print(f"PASS: {origin}, release {commit}, {len(expected['files'])} file hashes/MIME, indexable headers, true 404 and locale redirects")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()
    check(args.url, args.commit)
