# Development Task Plan

This document lists proposed tasks to align the repo with AGENTS.md and get a productive baseline without changing app behavior yet.

## Objectives
- Establish consistent Python/Poetry tooling and versions
- Set up project layout, tests, and quality gates
- Document E2E manual test flow per TECH_SPEC

## Tasks
- Tooling: Add `pyproject.toml` (Poetry), configure Python `3.11`, and set Black/Ruff/isort in `tool.*` sections.
- Versions: Add `.python-version` pinned to `3.11.x` (pyenv-compatible).
- Environment: Add `.env.example` with `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `WHENCEJAM_DB_URL`.
- Structure: Create `src/whencejam/{core,cli,web,api}/__init__.py` and a minimal module skeleton.
- Testing: Add `tests/` layout and a smoke test to validate env and import paths.
- Docs: Add `docs/test-plan.md` human E2E plan (CLI first, then Web/API as they appear).
- CI: Add GitHub Actions workflow to run `ruff`, `black --check`, and `pytest` on pushes/PRs.
- Developer UX: Optional `pre-commit` with Black/Ruff hooks.

## Order of Execution
1) Tooling and versions (pyproject, .python-version)
2) Env scaffolding (.env.example)
3) Project structure (src/…, tests/…)
4) Docs (test-plan.md)
5) CI and pre-commit

## Acceptance Criteria
- `poetry install` succeeds and pins Python 3.11
- `poetry run ruff`, `black --check`, and `pytest` pass in CI
- Repo contains `src/whencejam/...` and `tests/...` mirrors
- `.env.example` documents all required variables
- `docs/test-plan.md` enables a human to run an end-to-end check
