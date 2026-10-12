# Bilingual technology visual

Task WEB-003, revision 1, 12 October 2026. [Türkçe](technology-visual.tr.md).

Authority: the maintainer explicitly requested publishing the latest English explanatory image and its Turkish counterpart on eylema.dev, and using the image's EylemA wordmark in the site's upper-left banner. This request authorizes the scoped PR, merge to the existing production branch, and publication through the existing workflow.

Base: `878d785242fe75065e255c0fa44630aa4886ff8f`. Branch: `feat/bilingual-technology-visual`.
Allowed paths: `content/en.json`, `content/tr.json`, `tools/build.py`, generated `public/` pages and sitemap, `public/assets/` image assets and CSS, this bilingual task record, asset provenance/tooling documentation, and translation fingerprints. No runtime, policy, workflow, DNS or cloud-resource changes.

Acceptance:
- Both locale pages show the matching explanatory image with descriptive alternative text and a full-size image link.
- The upper-left brand matches the approved image: the orange E/action icon followed by dark `ylemA`, with uppercase A.
- The Turkish poster has the same wordmark and retains its reviewed Turkish explanation.
- The image's design-stage status remains visible; publication is not runtime/model/GPU evidence.
- Exact local contributor commands and generated-output check pass; browser checks cover English/Turkish, desktop/mobile, language navigation, full-size image access, existing tabs and FAQ, console and overflow.
- Publication is verified by production commit, successful GitHub workflow, Azure environment state, live release/file hashes and browser behavior on eylema.dev.

Risks: image text fidelity, distorted brand proportions, unreadable mobile detail, and stale assets. Use the approved PNG as source, lossless web encodings, a full-size link, natural aspect ratios and release hashes. Rollback is a scoped revert and a normal production workflow run.

Budget: 60 minutes; at most 3 image generation calls including one repair; at most 3 targeted repairs per failing check; bounded CI/cloud polling. No new paid resource or runtime dependency.
Roles: the same Codex assistant is architect, implementer, verifier and self-reviewer. Tools: built-in Image Gen, Python standard library, Git/GitHub CLI, Azure CLI, bundled sharp and Playwright. No separate reviewer is claimed. The Browser plugin skill is unavailable in this session; use bundled Playwright for responsive interaction verification.

Local verification passed on the final WEB-003 source tree: macOS 27.0.1 arm64, Python 3.14.8, Chromium 151.0.7922.34. The exact contributor commands passed, including 24 existing regression tests, repository validation, generated-output verification, blank-template validation and whitespace checking. English/Turkish meaning was reviewed before refreshing translation fingerprints.

Browser verification passed for both languages at 1440 × 1000, 390 × 844 and 320 × 844: page identity, EylemA header image and aspect ratio, matching locale poster, full-size PNG popup, language navigation, tabs and keyboard, FAQ and horizontal overflow. Both languages retained all four architecture panels without JavaScript. No relevant console warnings, page errors or failed asset requests were observed. Desktop, mobile and image-section screenshots were visually inspected; the rendered header matches the selected orange-E/ylemA appearance. Screenshots and temporary QA scripts are not shipped.

Independent review: not_run; self-review only. Runtime/GPU/model/training execution: not_applicable to this static website change. CI, merge and live publication are pending at authoring time; actual final commit, workflow and live-release evidence will be recorded in the PR and task delivery.

