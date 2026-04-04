# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Single-file Streamlit dashboard (`app.py`) tracking SEC546 course authoring progress. Deployed at https://sec546-status.streamlit.app/. The app displays module completion status across two course sections with styled dataframes.

## Running Locally

```bash
streamlit run app.py
```

The app runs on port 8501. Dependencies: `streamlit`, `pandas`. A devcontainer config (Python 3.11) is available for Codespaces.

## Deployment

Pushes to `main` auto-deploy to Streamlit Community Cloud. No build step or CI pipeline.

## Key Conventions

- **LAST_UPDATED**: When modifying `app.py`, always update the `LAST_UPDATED` variable to the current Central Time. Format: `"Month D, YYYY at HH:MM CT"`.
- Status icons: `✅` (done), `❌` (not done), `🔶 50%` (in progress), `N/A`. Use the constants `DONE`, `NOTDONE`, `HALF`, `NA` defined at the top of `app.py`.
- Course content is defined inline in the `sections` list — each section has a label, title, and rows of `[module_name, slides_status, notes_status, lab_status]`.
- Lab status entries include a description string prefixed with the status icon (e.g., `f"{DONE} Lab 1.0 Initial Setup"`).
- Styling is applied via `pandas.Styler` in `build_styled_dataframe()` — cell background colors map to status icons.
