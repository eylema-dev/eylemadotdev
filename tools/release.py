"""Create a public website release manifest; no credentials or machine metadata."""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone

from build import ROOT


def file_hashes(public):
    result = {}
    for path in sorted(public.rglob("*")):
        if path.is_symlink():
            raise ValueError("Symlinks are not release artifacts")
        if path.is_file() and path.name not in {"release.json", "staticwebapp.config.json"}:
            result[path.relative_to(public).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if not {"index.html", "tr/index.html", "404.html", "robots.txt", "sitemap.xml"} <= result.keys():
        raise ValueError("Incomplete website artifact")
    return result


def manifest(public, commit):
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Expected a full lowercase Git commit SHA")
    return {
        "commit": commit,
        "builtAt": datetime.now(timezone.utc).isoformat(),
        "repository": "https://github.com/eyleme-dev/eylemedotdev",
        "scope": "Eyleme promotional website only; not a platform runtime release",
        "files": file_hashes(public),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()
    current = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    if current != args.commit:
        parser.error("Release commit does not match the checked-out source")
    data = manifest(ROOT / "public", args.commit)
    (ROOT / "public/release.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f"PASS: release {args.commit}, {len(data['files'])} public files")
