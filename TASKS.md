# Development Task Plan

This document lists proposed tasks to align the repo with AGENTS.md and get a productive baseline without changing app behavior yet.

## Objectives
- Establish consistent Python/Poetry tooling and versions
- Set up project layout, tests, and quality gates
- Document E2E manual test flow per TECH_SPEC

## Tasks
- Tooling: Add `pyproject.toml` (Poetry), configure Python `3.11`, and set Black/Ruff/isort in `tool.*` sections.
- Versions: Add `.python-version` pinned to `3.11.x` (pyenv-compatible).
 - Environment: Add `.env.example` with `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `WHENCEJAM_DB_URL` (default `sqlite:///whencejam.db`).
- Structure: Create `src/whencejam/{core,cli,web,api}/__init__.py` and a minimal module skeleton.
- Testing: Add `tests/` layout and a smoke test to validate env and import paths.
- Docs: Add `docs/test-plan.md` human E2E plan (CLI first, then Web/API as they appear).
- CI: Add GitHub Actions workflow to run `ruff`, `black --check`, and `pytest` on pushes/PRs.
- Developer UX: Optional `pre-commit` with Black/Ruff hooks.

## Database (SQLite-first, Postgres-ready)
- Library: Add SQLAlchemy (ORM) and Alembic (migrations).
- URL: Default DB URL to `sqlite:///whencejam.db`; allow override via env for future Postgres (e.g., `postgresql+psycopg://...`).
- Models: Define minimal domain tables (jam entries with spotify_url, recommender, created_at).
- Abstraction: Introduce a storage interface in `core` with a SQLAlchemy implementation to ease future swaps.
- Sessions: Centralize engine/session creation; use per-request scoped session in Flask and context-managed sessions in CLI.
- Migrations: Initialize Alembic, autogenerate initial migration, and document commands (`alembic upgrade head`).
- Tests: Use in-memory SQLite (`sqlite+pysqlite:///:memory:`) or tmp file; provide fixtures to create/drop schema.

## Order of Execution
1) Tooling and versions (pyproject, .python-version)
2) Env scaffolding (.env.example)
3) Database setup (SQLAlchemy + Alembic, models)
4) Project structure (src/…, tests/…)
5) Docs (test-plan.md) including DB setup/run notes
6) CI and pre-commit

## Acceptance Criteria
- `poetry install` succeeds and pins Python 3.11
- `poetry run ruff`, `black --check`, and `pytest` pass in CI
- Repo contains `src/whencejam/...` and `tests/...` mirrors
- `.env.example` documents all required variables with SQLite default
- Alembic initialized; `alembic upgrade head` creates `whencejam.db`
- Core CRUD for jam entries works against SQLite (covered by tests)
- `docs/test-plan.md` enables a human to run an end-to-end check
