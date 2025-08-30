# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a music recommendation tracking application called "whence-jam-python" that helps users remember who recommended specific songs or albums. The project follows a three-phase development approach:

- **Phase One**: Command line application
- **Phase Two**: Web application with Flask 
- **Phase Three**: REST API

## Architecture Guidelines

The project uses Python with Flask framework for web components and follows these principles:
- Code should be as simple as possible to achieve the Product Specifications
- Modern Python dependency management (pyproject.toml expected)
- Python version management should be configured
- Spotify API integration for music metadata

## Development Setup

Since this is an early-stage project with no implementation yet, standard Python development practices apply:

```bash
# Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies (when pyproject.toml exists)
pip install -e .

# Run tests (when implemented)
pytest

# Run linting (when configured)
ruff check
ruff format
```

## Testing Requirements

Based on TECH_SPEC.md:
- Unit tests are required for all functionality
- End-to-end testing should be implemented:
  - CLI app: Markdown test plan for manual testing
  - Web/API: Automated end-to-end tests

## Core Functionality

The application stores and retrieves music recommendations with:
- Song/album title and Spotify link
- Name of person who made the recommendation  
- Date of recommendation
- Chronological listing (newest first)

All phases integrate with Spotify's music database for metadata lookup.