# Website design specification

[Türkçe](design.tr.md). `WEB-001 / 0.1.0`. The implementation direction was selected by the author during the authorized build; user design approval is not claimed.

Four Image Gen UI concepts define the introduction, architecture, FAQ and roadmap at 1536 × 1024 each. One additional built-in Image Gen call isolates the orange ribbon sculpture. The image is illustrative artwork, never a product screenshot. Concepts remain conversation previews outside the production tree.

## System

- Paper background `#F7F6F2`; ink `#17252B`; action orange `#EE5638`; diagram surface `#EFEDE7`; rule `#CFD2CF`. Small orange text uses darker `#B63E28` for contrast.
- Helvetica Neue, Helvetica, Arial, sans-serif; no font download. Hero 120px at the concept width, weight 750, tight line height and tracking; section heading 76px, body 23px, navigation 18px. Responsive scales preserve hierarchy.
- Maximum content width 1392px with 72px desktop gutters; 24px mobile gutters. Open sections with 100–120px separation. Thin rules, 8px button/diagram corners, no repeating cards.
- Existing canonical Eylema SVG lockup replaces the generated concepts' inaccurate logo approximations. Preserve logo colors and proportions.
- Hero image: separate square asset on matching paper, no tint/overlay; blend only its outer edges into the page if necessary. Native text and links remain HTML.
- Icons: two simple SVG strokes for right and northeast arrows, 24px, 1.7px stroke, currentColor. No third-party icon library.
- Motion: brief color/underline transitions. No autoplay, scroll hijacking or continuous sculpture animation. Reduced-motion disables transitions and smooth scrolling.

## Surface and copy inventory

1. Header: Eylema logo; Architecture, Roadmap, GitHub; EN / TR. Hero: “From intent / to action. / By design.” Supporting text: “An agentic web platform for continuous development and operations. Built around explicit goals, local intelligence and human direction.” Actions: “Explore the architecture”, “Follow on GitHub”. Status: “Currently in design. Architecture and API drafts are public.” Principle strip: Explicit by design; Local at the core; Human in command, with the exact explanatory lines from the concept.
2. Architecture: “One contract. / A continuous loop.” Four numbered tabs: Define, Develop, Operate, Learn. Default: “Start with intent.” The diagram shows Goal connected to State, Actions, Authority and Budget, labeled as a proposed application contract and concept illustration. Other tabs reuse this exact component family, using source-bound copy to explain development, operation and permitted learning. Human-direction rule beneath.
3. Roadmap: “Built in the open. / Proven step by step.” Explicit architecture/API design status; three rows for foundation drafts, planned first application and planned learning loop. Dark invitation band and the real GitHub repository link. Footer: logo, design statement, architecture/API links and locale links.

The two lower sections share gutters, heading scale and open ruled layout. No new pricing, dashboards, account flows, waitlists or model interactions. The mobile header uses two simple rows rather than hiding links behind an extra menu. Mobile tabs form a 2 × 2 grid; diagrams and roadmap rows stack. Turkish copy is reviewed for meaning rather than forced into English line lengths.

## Generated production asset prompt

Built-in Image Gen, background-extraction, using the introduction concept as reference:

> The reference is a website mockup. Create a standalone production hero asset containing ONLY the orange sculptural folded ribbon on its right side. Remove ALL website UI, header, text, logo, columns and lines. Preserve the precise ribbon's E-like zigzag three-tier folded rectangular loop geometry, matte orange anodized metal, front/right 3/4 camera view, subtle highlights and realistic soft ground contact shadow. Render the sculpture fully, with no cropping, centered in a square 1024x1024 composition, 7% breathing space around it. Match exact solid paper background #F7F6F2, softly lit and uniform to the edges, no border. This art represents an abstract continuous development loop, not running software. No letters, symbols, logos, text or watermark. Do not reinvent the sculpture; isolate/recreate it faithfully as a separate asset with identical orientation and silhouette.

Concept prompts specify all copy above, semantic HTML/CSS, accessible progressive tabs, paper/ink/orange palette, open sections and no fabricated product evidence. Full prompts and generated previews are in the task conversation.

## Scope addition: international discovery

The maintainer requested SEO/GEO and English as the default. A fourth section concept adds a visible, source-linked FAQ between architecture and roadmap: “A clear idea. / An honest start.” Four native disclosures answer what Eylema is, whether it can be used today, human control and target platforms. The first answer is open. The roadmap label becomes 03. The four-concept set and asset total five Image Gen calls. The maintainer selected a separate website repository, then explicitly requested its final name `eylema-dev/eylemadotdev` and public visibility.
