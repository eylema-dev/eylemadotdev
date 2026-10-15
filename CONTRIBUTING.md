# Contributing to the website

[Türkçe](CONTRIBUTING.tr.md). Follow [AGENTS.md](AGENTS.md) and the [quality gates](docs/en/quality-gates.md).

This is the separate, public marketing-site repository authorized by the maintainer. The public platform design remains in [eyleme-dev/eyleme](https://github.com/eyleme-dev/eyleme). No public source license is selected for this website repository; the open-source Apache-2.0 statement refers to first-party Eyleme core code/docs. Keep the single Eyleme brand and the standalone community tool visible. Present Derleme and Onama as private-source subscription products in development; public website links must not send visitors to private repositories. Do not add prices, checkout, customer testimonials or production-service claims without actual evidence and authority.

Use a scoped branch from current main. Link the issue or explicit maintainer request, record a bounded plan, and keep changes reviewable. Source copy belongs in `content/en.json` and `content/tr.json`; edit `tools/build.py` for shared HTML and metadata, and `public/assets/site.css` or `site.js` for presentation. Regenerate with `.venv/bin/python tools/build.py`.

After reviewing both languages, run `.venv/bin/python tools/check_repository.py --write-translation-hashes`, then all commands in AGENTS.md. The checker must reject negative fixtures. Add meaningful tests when changing it. Report static checks separately from browser interaction, visual review, CI and live deployment.

Use the PR template and `.venv/bin/python tools/check_pr.py --body-file <body-file>` for the filled description. Name actual tools/roles, distinguish self-review from independent review, and report pending gates. Do not submit private reasoning, credentials or operational records. A maintainer owns review, merge and publication decisions. PR checks are read-only and do not deploy. The separately authorized production workflow deploys main using only its scoped Azure secret and verifies the live release.
