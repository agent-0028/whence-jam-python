# Repository Guidelines

## Project Structure & Module Organization

Use a src layout and keep concerns separated:

- `src/whencejam/core/`: domain models, storage, Spotify search client
- `src/whencejam/cli/`: command-line entrypoint and helpers
- `src/whencejam/web/`: Flask app (views, templates, static)
- `src/whencejam/api/`: Flask blueprints for REST endpoints
- `tests/`: unit/integration tests mirroring package structure
- `scripts/`: one-off maintenance or data scripts
- `docs/`: usage notes and the end-to-end test plan

Example tree:

```
src/whencejam/{core,cli,web,api}/__init__.py
tests/{core,test_cli,test_web,test_api}/test_*.py
```

## Build, Test, and Development Commands

Prefer Poetry for dependency and Python version management.

- Install: `poetry install` — create venv and install deps
- Run CLI: `poetry run python -m whencejam.cli` — local usage
- Run Web: `poetry run flask --app whencejam.web.app run --debug` — dev server
- Tests: `poetry run pytest -q` — run unit/integration tests
- Lint: `poetry run ruff check src tests` — static analysis
- Format: `poetry run black src tests` — auto-format

If using pyenv, include `.python-version` (e.g., 3.11) and align Poetry.

## Coding Style & Naming Conventions

- Python 3.11+, 4-space indents, UTF-8
- Names: modules/functions `snake_case`, classes `PascalCase`, constants `UPPER_CASE`
- Formatting: Black (line length 88), isort for imports
- Linting: Ruff; keep CI green before merging
- Keep functions small; separate I/O (Flask/CLI) from core logic

## Testing Guidelines

- Framework: pytest; name files `test_*.py`, functions `test_*`
- Aim for ≥80% coverage in `core` and request-focused tests for `cli/web/api`
- Add fixtures for Spotify client/storage; prefer fakes over network calls
- Provide a human E2E test plan in `docs/test-plan.md` per TECH_SPEC

## Commit & Pull Request Guidelines

- Use Conventional Commits: `feat:`, `fix:`, `chore:`, `docs:`, `test:` (scope examples: `core`, `cli`, `web`, `api`)
- Commits: small, focused; include rationale when non-obvious
- PRs: clear description, linked issue, test coverage, and screenshots for UI
- Pass CI (lint, format, tests) before requesting review

## Security & Configuration Tips

- Configure Spotify: `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` (env vars)
- Storage config via env (e.g., `WHENCEJAM_DB_URL=sqlite:///whencejam.db`)
- Never commit secrets; use `.env.example` and `python-dotenv` if helpful
