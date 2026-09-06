# Repository presentation verification · 2026-09-07

## Changes

- The hub and private risk repository now have matching English/Chinese landing pages, official logos, current architecture figures, clear demo entry points and evidence boundaries.
- Five overall project images were moved from the recognition repository to the hub. Their original bytes are verified by SHA-256 in `ASSET_MIGRATION.json`. Recognition-specific SVGs replace them on the component homepage.
- Recognition data-download links, model files and detailed experiment documentation remain accessible. Extended commands live in bilingual quick-start documents.
- Four README update summaries and changelogs now show current maintenance separately from historical software releases. Existing release dates were checked against GitHub release metadata, not rewritten.

## Checks performed

- English/Chinese SVG figures rendered in installed Microsoft Edge; node text bounds checked, with no remaining overflow.
- Interactive demo exercised in Chinese and English: stage switching, scenario selection, missing-observation wording and time cursor. No JavaScript errors; no horizontal overflow at 390px mobile width.
- Real component runner executed the recognition model demo and both decision evidence modules successfully. Recognition produced its documented 120 dense points; decision output explicitly retained `fusion_implemented: false`.
- Local Markdown/HTML file references and SVG syntax checked across all four repositories; historical annotator audit links were repaired.
- Original recognition-model hashes and imported decision runtime/package hashes remain unchanged.

The browser page is illustrative, not model inference. The component runner executes independent inputs, not an integrated warning service. No new training, field experiment or predictive-performance validation was performed.
