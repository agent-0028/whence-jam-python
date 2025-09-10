# Development Task Plan

This document lists proposed tasks to align the repo with AGENTS.md and get a productive baseline without changing app behavior yet.

## Objectives
- Establish consistent Python/Poetry tooling and versions
- Set up project layout, tests, and quality gates
- Document E2E manual test flow per TECH_SPEC

## Tasks
- Tooling: Add `pyproject.toml` (Poetry), configure Python `3.11`, and set Black/Ruff/isort in `tool.*` sections.
  - Verify: `poetry install`; `poetry run python -V` shows 3.11; `poetry run black --version`; `poetry run ruff --version`.
- Versions: Add `.python-version` pinned to `3.11.9` (pyenv-compatible).
  - Verify:
    - Install Python: `pyenv install 3.11.9` (one-time) and confirm with `pyenv versions`.
    - Set local: `pyenv local 3.11.9` at repo root (or rely on the committed `.python-version`).
    - Point Poetry at 3.11: `poetry env use 3.11.9` (or `poetry env use $(pyenv which python)`).
    - Check: `pyenv version` shows 3.11.9; `poetry run python -V` prints `Python 3.11.9`.
    - Note (macOS): install pyenv via Homebrew `brew install pyenv`; if 3.11.9 isn’t available, use the latest 3.11.x and update `.python-version` accordingly.
- Environment: Add `.env.example` with `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `WHENCEJAM_DB_URL` (default `sqlite:///whencejam.db`).
  - Verify: `rg 'WHENCEJAM_DB_URL' .env.example`; load via `poetry run python -c 'import dotenv; dotenv.load_dotenv(); import os; print(os.getenv("WHENCEJAM_DB_URL"))'`.
- Structure: Create `src/whencejam/{core,cli,web,api}/__init__.py` and a minimal module skeleton.
  - Verify: `python -c 'import whencejam, whencejam.core, whencejam.cli, whencejam.web, whencejam.api'` imports cleanly.
- Testing: Add `tests/` layout and a smoke test to validate env and import paths.
  - Verify: `poetry run pytest -q` passes with at least one test collected.
- Docs: Add `docs/test-plan.md` human E2E plan (CLI first, then Web/API as they appear).
  - Verify: `test-plan.md` exists and is referenced from `README.md`.
- CI: Add GitHub Actions workflow to run `ruff`, `black --check`, and `pytest` on pushes/PRs.
  - Verify: first PR/commit shows green checks; local `make check` passes; optional local dry-run via `act`.
- Developer UX: Optional `pre-commit` with Black/Ruff hooks.
  - Verify: `pre-commit run --all-files` passes; hooks installed (`pre-commit install`).

## Database (SQLite-first, Postgres-ready)
- Library: Add SQLAlchemy (ORM) and Alembic (migrations).
  - Verify: `poetry run python -c 'import sqlalchemy, alembic; print(sqlalchemy.__version__)'`.
- URL: Default DB URL to `sqlite:///whencejam.db`; allow override via env for future Postgres (e.g., `postgresql+psycopg://...`).
  - Verify: default `.env.example` value set; `poetry run python -c 'from whencejam.core.db import make_engine; print(make_engine().url)'` prints sqlite URL.
- Models: Define minimal domain tables (jam entries with spotify_url, recommender, created_at).
  - Verify: `alembic revision --autogenerate` shows expected tables/columns; tests can insert/select a jam.
- Abstraction: Introduce a storage interface in `core` with a SQLAlchemy implementation to ease future swaps.
  - Verify: unit tests exercise storage via interface; implementation swap behind interface requires no call-site changes.
- Sessions: Centralize engine/session creation; use per-request scoped session in Flask and context-managed sessions in CLI.
  - Verify: CRUD in CLI/web commits; no dangling sessions in tests (all green, no warnings).
- Migrations: Initialize Alembic, autogenerate initial migration, and document commands (`alembic upgrade head`).
  - Verify: `poetry run alembic upgrade head` creates `whencejam.db`; `sqlite3 whencejam.db '.schema'` shows tables.
- Tests: Use in-memory SQLite (`sqlite+pysqlite:///:memory:`) or tmp file; provide fixtures to create/drop schema.
  - Verify: `pytest -q -k db` passes using in-memory URL; no external services required.

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
