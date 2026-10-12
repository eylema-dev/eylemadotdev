# IndexNow enablement

[Türkçe](indexnow.tr.md). Task `WEB-005`, revision `0.1.0`, 12 October 2026.

Authority: the maintainer's current request to enable IndexNow for `eylema.dev` and submit English and Turkish pages, together with the existing authorization to publish this website to `rg-eylema-dev / swa-eylema-dev`, Free, in the umayos subscription. No DNS, account, subscription or hosting-tier changes are needed.

Base: `425834d978160f8e0f1b6f5cbc049b3add3e0164` on current `origin/main`. Branch: `codex/indexnow`. Allowed paths: `tools/build.py`, `tools/indexnow.py`, `tools/tests/test_indexnow.py`, `public/<IndexNow-key>.txt`, both discovery guides, this bilingual record and `tools/translation-pairs.json`. Existing page copy and platform checkout are outside scope.

Acceptance: generate a root UTF-8 key file; verify deterministic output and failure tests; include the file in the existing release inventory; publish through a draft PR and existing main deployment; verify the deployed revision and public key over normal HTTPS; submit exactly `https://eylema.dev/` and `https://eylema.dev/tr/` and record the actual HTTP receipt. HTTP 200 is a submission receipt; 202 means key validation is pending. Neither proves indexing.

Architect, implementer, verifier and self-reviewer: this Codex session (specific model identifier not exposed). Tools: Python standard library, Git, GitHub CLI, official protocol documentation and existing Azure/GitHub publication checks. No independent reviewer is claimed. Maintainer authorization is distinct from CI and self-review.

Risks: key/file mismatch, stale deployment, submission without acceptance, and confusing submission with indexing. The ownership key and file are intentionally public; they are not account or deployment credentials. Commands default to a preview and perform one bounded submission only with `--submit`. No automatic resubmission on unrelated deployments. Budget: 60 minutes, at most three repair rounds per failing gate and three submission attempts after resolving an observed failure; no paid services.

Local verification passed on this PR head, macOS, Python 3.14.8: virtual environment and hash-locked dependency setup; all 31 unit tests; repository checks; blank PR-template structure; generated-output freshness; diff whitespace check and payload preview. English/Turkish guides and task records were reviewed before refreshing fingerprints. Self-review found only the scoped public ownership file, standard-library tooling and documentation. PR CI, production publication and actual protocol receipt remain pending until executed. UI checks are not applicable because page presentation and interactions are unchanged. Existing Google and Bing monitors remain responsible for authoritative indexing status.
