.PHONY: help check lint format format-check test

# Runner for commands. Override to empty to run tools directly without Poetry.
# Example: make check RUN=""
RUN ?= poetry run

# Discover common code paths if present; fallback to repository root
PATHS := $(strip $(shell test -d src && echo src) $(shell test -d tests && echo tests))
DEFAULT_PATH := $(if $(PATHS),$(PATHS),.)

help:
	@echo "Targets:"
	@echo "  check         Run lint, format-check, and tests"
	@echo "  lint          Ruff static analysis"
	@echo "  format        Black auto-format (in-place)"
	@echo "  format-check  Black in check mode"
	@echo "  test          Run pytest"

lint:
	@echo "→ Ruff linting on $(DEFAULT_PATH)"
	@$(RUN) ruff check $(DEFAULT_PATH)

format:
	@echo "→ Black formatting $(DEFAULT_PATH)"
	@$(RUN) black $(DEFAULT_PATH)

format-check:
	@echo "→ Black check on $(DEFAULT_PATH)"
	@$(RUN) black --check $(DEFAULT_PATH)

test:
	@echo "→ Running tests"
	@$(RUN) pytest -q

check: lint format-check test
	@echo "✓ All checks passed"

