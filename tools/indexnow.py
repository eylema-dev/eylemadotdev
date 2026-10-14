"""Preview retained ownership data; submission is disabled by the search-removal policy."""
import argparse
import json
from urllib.parse import urlsplit

from build import INDEXNOW_KEY, ORIGIN

URLS = [ORIGIN + "/", ORIGIN + "/tr/"]


def payload():
    return {
        "host": urlsplit(ORIGIN).hostname,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{ORIGIN}/{INDEXNOW_KEY}.txt",
        "urlList": URLS.copy(),
    }


def submit():
    # Fail before any ownership lookup, page fetch or submission request.
    raise ValueError("IndexNow submission is disabled by the site's search-removal policy")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submit", action="store_true", help="Disabled: exits without network access")
    args = parser.parse_args()
    if args.submit:
        try:
            submit()
        except ValueError as error:
            parser.exit(2, str(error) + "\n")
    print(json.dumps({"mode": "preview_only", "submissionEnabled": False, "payload": payload()}, indent=2))
