# Website verification

[Türkçe](verification.tr.md). `WEB-001 / 0.2.0`, 11 October 2026. Applies to the introducing PR head; the exact commit and CI run are reported in that PR. Base: `a08b78d9210035aafdd2db35958f0c2d854c94c2`.

## Environment and roles

Local macOS, Python 3.14.8, Codex in-app browser through CUA, Git/GitHub CLI. Supplemental bundled Playwright Chromium 151.0.7922.34 was used only for JavaScript-disabled and reduced-motion overrides not exposed by IAB. Sharp 0.35.5 encoded the original generated asset. No website runtime packages were installed. Architect, implementer, verifier and self-reviewer were the same Codex GPT-6-family session; no independent reviewer is claimed.

## Results and limits

| Check | Status | Evidence |
|---|---|---|
| Exact AGENTS.md command sequence | passed | Virtual environment, hash-required empty dependency install, 16 regression tests, repository validator, blank PR-template validator and diff whitespace check |
| Generated output | passed | `tools/build.py --check`; English root and Turkish `/tr/`, current sitemap/robots/404 |
| Content and discovery | passed | Complete HTML without JavaScript; self-canonical, reciprocal en/tr/x-default, JSON-LD matched to source copy, dimensions/alt, links, reviewed translation fingerprints and 35 KB CSS/JS budget |
| Public source references | passed | All 10 English/Turkish source document paths confirmed on the platform repository main tree |
| Repository change | passed | GitHub reports `eylema-dev/eylemadotdev` as PUBLIC; origin uses the renamed repository, following explicit maintainer requests |
| IAB interactions | passed | English/Turkish links, architecture CTA, all four tabs, selected/panel states, Home/End/arrow keys, native FAQ expansion, Turkish mobile learning panel |
| Responsive behavior | passed | EN: 320, 390, 768, 1024, 1536px; TR: 320, 390, 768, 1024px; no horizontal overflow; 1536 × 1024 concept-size viewport checked |
| Supplemental browser modes | passed | Both languages retain all four architecture panels with JavaScript disabled; native FAQ and language links work; reduced motion uses no transitions or smooth scrolling; no third-party requests or page errors |
| Browser console | passed | No warnings/errors in the observed IAB flow |
| Visual fidelity | passed | Four section concepts and browser captures inspected directly with `view_image`; ledger below; no unresolved material mismatch |
| Independent/maintainer review | not_run | Separate human review remains required; self-review and CI are not substitutes |
| Production hosting, DNS/TLS, indexing, field performance | not_run | No host is provisioned or deployment claimed; follow the launch checklist |
| Rust/GPU/model runtime tests | not_applicable | This repository implements a static promotional website only |

GitHub CI and the filled PR-body check are separate evidence on the associated pull request. The blank-template result above does not validate a filled PR description. Screenshot evidence is attached to the task outside the source repository; temporary QA scripts are not shipped.

## Fidelity ledger

| Comparison | Concept evidence | Browser evidence and resolution |
|---|---|---|
| Copy and hierarchy | Three-line “From intent / to action. / By design.”, two actions, visible design-stage status | Exact English above-the-fold copy checked; no invented eyebrow, statistics or proof claims; Turkish preserves meaning |
| Hero layout and image | Left editorial copy, right orange ribbon, principle strip below | Corrected intrinsic image height and negative placement so the asset does not cover the principle strip; header now sits above image edges |
| Typography | Large tight headings, deliberate body/control sizing | System Helvetica hierarchy checked at desktop/mobile; natural font metrics and Turkish line breaks are an intentional adaptation |
| Palette and asset | Paper/ink/orange, unfiltered sculptural asset | Computed paper `#F7F6F2`, ink `#17252B`, accent `#EE5638`; no tint or overlay; only edge blending; small accent text is deliberately darker for contrast |
| Brand and icons | Generated logo approximation, thin directional arrows and disclosures | Maintainer's canonical logo deliberately replaces the approximation; code-native SVG arrows; corrected open FAQ indicator to a minus |
| Architecture | Open heading, four numbered tabs and a contract diagram | Same component family in all four working states; explicit conceptual/non-runtime note; source links remain real |
| FAQ | Open two-column layout, four ruled disclosures, first answer open | Native disclosure controls, complete source-bound answers in HTML; requested SEO/GEO addition has its own fourth concept |
| Roadmap and footer | Three status rows, dark contribution band and restrained footer | Design/planned status preserved, no progress metrics invented; continuous-page spacing follows the section system |
| Responsive composition | Shared gutters, open section rhythm and hierarchy | Two-row mobile navigation, stacked content and 2 × 2 tabs; image/text stay legible without horizontal overflow |

The implementation was faithfully verified against the author-selected four-concept specification. Remaining intentional differences are the canonical brand mark, accessible small-text orange, real system-font/locale wrapping, and the standalone generated sculpture's subtle geometry variation. These do not change the page structure, claims or interactions. User design approval is not implied.
