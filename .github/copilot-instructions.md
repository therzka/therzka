# Copilot Instructions

## Repository Overview

This is a GitHub profile README repository (`therzka/therzka`). It displays a personal profile page with social links and auto-generated GitHub metrics SVGs.

## Architecture

- **README.md** — The profile page content (rendered on github.com/therzka)
- **`.github/workflows/`** — GitHub Actions that auto-generate metrics SVGs using [lowlighter/metrics](https://github.com/lowlighter/metrics)
  - `metrics-action.yml` — Generates `github-metrics.svg` weekly (Mondays 1:00 UTC) with starred repos and custom purple theming
  - `terminal-template.yml` — Generates `metrics.terminal.svg` on manual dispatch
- **`img/`** — Static icons for social links

## Conventions

- Metrics SVGs are committed to the repo root and referenced directly in the README
- The `METRICS_TOKEN` secret powers the lowlighter/metrics action
- Brand color is `#A654FF` (purple), applied via `extras_css` in the metrics workflow
