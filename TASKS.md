# Development Task Plan

This document lists proposed tasks to align the repo with AGENTS.md and get a productive baseline without changing app behavior yet.

## Objectives
- Establish consistent Python/Poetry tooling and versions
- Set up project layout, tests, and quality gates
- Document E2E manual test flow per TECH_SPEC

## How To Work This Plan
- Complete one subtask at a time, run its Verify steps, then commit.
- When resuming, open this file and pick the first item marked [NEXT] or unchecked.

## Subtasks (in order)

1) Tooling: Poetry + linters [COMPLETED]
- Implement: Add `pyproject.toml` with Poetry metadata; configure Black/Ruff/isort.
- Verify:
  - `poetry install`
  - `poetry run python -V`
  - `poetry run black --version`
  - `poetry run ruff --version`

2) Versions: Pin Python with pyenv [COMPLETED]
- Implement: Add `.python-version` pinned to `3.11.9`.
- Verify:
  - Install Python: `pyenv install 3.11.9` and confirm with `pyenv versions`.
  - Local selection: `pyenv local 3.11.9` (or rely on `.python-version`).
  - Poetry interpreter: `poetry env use 3.11.9` (or `poetry env use $(pyenv which python)`).
  - Check: `pyenv version` shows 3.11.9; `poetry run python -V` prints `Python 3.11.9`.
  - Note (macOS): install via Homebrew `brew install pyenv`; if you use a different 3.11.x, update `.python-version` accordingly.

3) Environment: Example env vars [COMPLETED]
- Implement: Add `.env.example` with `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `WHENCEJAM_DB_URL=sqlite:///whencejam.db`; ignore `.env` and `whencejam.db`.
- Verify:
  - Inspect example: `rg 'WHENCEJAM_DB_URL' .env.example`
  - Copy local: `cp .env.example .env` and edit secrets
  - Load and print: `poetry run python -c 'import dotenv, os; dotenv.load_dotenv(); print(os.getenv("WHENCEJAM_DB_URL"))'` → expect `sqlite:///whencejam.db`
  - VCS safety: `.gitignore` includes `.env` and `whencejam.db`

4) Structure: Package and tests skeleton [NEXT]
- Implement: Create `src/whencejam/{core,cli,web,api}/__init__.py` and `tests/{core,test_cli,test_web,test_api}/` with a smoke test.
- Verify:
  - Imports: `poetry run python -c 'import whencejam, whencejam.core, whencejam.cli, whencejam.web, whencejam.api; print("imports ok")'`
  - Tests: `poetry run pytest -q` collects and passes at least the smoke test

5) Docs: Human E2E test plan [PENDING]
- Implement: Add `docs/test-plan.md` (CLI first, then web/API as they appear) and reference it from `README.md`.
- Verify:
  - `rg 'test-plan.md' README.md` shows a link
  - The doc contains step-by-step CLI test instructions

6) Database: SQLite-first, Postgres-ready [PENDING]
- Library: Ensure SQLAlchemy and Alembic present.
  - Verify: `poetry run python -c 'import sqlalchemy, alembic; print(sqlalchemy.__version__)'`
- URL default: Use `WHENCEJAM_DB_URL` with `sqlite:///whencejam.db` default.
  - Verify: `poetry run python -c 'import os, dotenv; dotenv.load_dotenv(); print(os.getenv("WHENCEJAM_DB_URL"))'`
- Models: Define jam entry model (spotify_url, recommender, created_at).
  - Verify: `alembic revision --autogenerate` shows expected table/columns; unit test inserts/selects a jam
- Abstraction: Storage interface in `core` with SQLAlchemy implementation.
  - Verify: unit tests use the interface; implementation is swappable
- Sessions: Centralized engine/session; context-managed in CLI; per-request in Flask.
  - Verify: CRUD commits; tests green without session warnings
- Migrations: Init Alembic; generate and apply initial migration.
  - Verify: `poetry run alembic upgrade head` creates `whencejam.db`; `sqlite3 whencejam.db '.schema'` shows tables
- Tests: Use in-memory SQLite or tmp file with fixtures.
  - Verify: `pytest -q -k db` passes using in-memory URL

7) CI: Lint/format/tests [PENDING]
- Implement: GitHub Actions workflow to run `ruff`, `black --check`, and `pytest` on push/PR; wire `make check`.
- Verify: CI green on PR; local `make check` passes

8) Developer UX: pre-commit (optional) [PENDING]
- Implement: Add `pre-commit` config for Black/Ruff and install hooks.
- Verify: `pre-commit run --all-files` passes; `pre-commit install` sets hooks

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
3) Project structure (src/…, tests/…)
4) Database setup (SQLAlchemy + Alembic, models)
5) Docs (test-plan.md)
6) CI and pre-commit

## Acceptance Criteria
- `poetry install` succeeds and pins Python 3.11
- `poetry run ruff`, `black --check`, and `pytest` pass in CI
- Repo contains `src/whencejam/...` and `tests/...` mirrors
- `.env.example` documents all required variables with SQLite default
- Alembic initialized; `alembic upgrade head` creates `whencejam.db`
- Core CRUD for jam entries works against SQLite (covered by tests)
- `docs/test-plan.md` enables a human to run an end-to-end check
