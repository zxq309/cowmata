# COWMATA repository visual system

The user requested the established COWMATA repository style. Official logo green `#92C142` comes from the existing SVG; teal `#0A7EA4` follows the existing repository badges. Architecture figures use paper `#F7FAF8`, ink `#17352E`, secondary text `#59716B` and pale borders `#B8CCC4`.

Typography uses local Segoe UI / Microsoft YaHei / Noto Sans CJK SC fallbacks; no remote font is required. These are repository-document fonts, not a claim to reproduce the company website's exact font stack.

The new diagrams are 1200 × 680 document-wide SVGs with English and Simplified Chinese variants. Solid edges denote current component flow; dashed edges denote planned integration. Original concept art remains explicitly conceptual. The diagram-design architecture layout principles are adapted to the existing project brand at the user's request.

Rebuild from the hub root:

```sh
python scripts/build_diagrams.py --kind system --out assets/figures
python scripts/build_diagrams.py --kind recognition --out ../cowmata-tailring/assets/figures
python scripts/build_diagrams.py --kind risk --out ../cowmata-risk/assets/figures
```
