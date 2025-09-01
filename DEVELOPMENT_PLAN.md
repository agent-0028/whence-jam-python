# Development Plan

This document outlines the implementation plan for the whence-jam-python music recommendation tracking application.

## Phase One: Command Line Application

### Setup Tasks
- [ ] Create `pyproject.toml` with project configuration and dependencies
  - *Verify*: `pip install -e .` succeeds, dependencies install correctly
- [ ] Set up Python project structure with appropriate modules
  - *Verify*: `python -c "import whence_jam"` succeeds
- [ ] Configure development dependencies (pytest, ruff, etc.)
  - *Verify*: `pytest --version`, `ruff --version` show correct versions
- [ ] Create virtual environment setup documentation
  - *Verify*: Follow README instructions from scratch, application runs

### Core Implementation
- [ ] Implement Spotify API integration for music search
  - *Verify*: Search for "Bohemian Rhapsody" returns Queen track with Spotify URL
- [ ] Design database abstraction layer for future PostgreSQL migration
  - *Verify*: Database interface can be swapped without changing business logic
- [ ] Create SQLite database schema and connection handling
  - *Verify*: `sqlite3 app.db ".schema"` shows correct tables
- [ ] Build command line interface for adding recommendations
  - *Verify*: `python -m whence_jam add "Song" "Friend"` succeeds
- [ ] Implement listing functionality (chronological, newest first)
  - *Verify*: `python -m whence_jam list` shows entries newest first
- [ ] Add error handling for API failures and invalid inputs
  - *Verify*: Invalid song name returns helpful error, no crash

### Testing & Documentation
- [ ] Write unit tests for core functionality
  - *Verify*: `pytest` passes with >80% coverage
- [ ] Create markdown test plan for manual end-to-end testing
  - *Verify*: Fresh user can follow plan and complete all scenarios
- [ ] Document CLI usage and commands
  - *Verify*: `python -m whence_jam --help` shows all options

## Phase Two: Web Application

### Web Framework Setup
- [ ] Integrate Flask framework
  - *Verify*: `flask run` starts development server
- [ ] Create HTML templates for forms and listing
  - *Verify*: Navigate to localhost shows form and list
- [ ] Set up static file handling for CSS/JS
  - *Verify*: CSS styles load, no 404s in browser dev tools
- [ ] Configure Flask application structure
  - *Verify*: `flask routes` shows all expected endpoints

### Web Features
- [ ] Build web form for song/person input
  - *Verify*: Form submission adds entry to database
- [ ] Implement form validation and error handling
  - *Verify*: Empty fields show validation errors
- [ ] Create web interface for displaying recommendation list
  - *Verify*: List shows all entries with person, song, date
- [ ] Add responsive design for mobile compatibility
  - *Verify*: Site usable on mobile browser/dev tools

### Testing
- [ ] Write integration tests for web routes
  - *Verify*: `pytest tests/integration/` passes
- [ ] Create automated end-to-end web tests
  - *Verify*: Selenium/Playwright tests pass in headless mode
- [ ] Test form submission and data persistence
  - *Verify*: Form data survives server restart

## Phase Three: REST API

### API Development
- [ ] Design REST API endpoints
  - *Verify*: OpenAPI spec covers all endpoints
- [ ] Implement POST endpoint for adding recommendations
  - *Verify*: `curl -X POST -d '{...}' /api/recommendations` returns 201
- [ ] Create GET endpoint for listing recommendations
  - *Verify*: `curl /api/recommendations` returns JSON list
- [ ] Add proper HTTP status codes and error responses
  - *Verify*: Invalid requests return 400 with error details
- [ ] Implement API authentication if needed
  - *Verify*: Requests without auth return 401

### API Testing & Documentation
- [ ] Write comprehensive API tests
  - *Verify*: `pytest tests/api/` covers all endpoints
- [ ] Create API documentation (OpenAPI/Swagger)
  - *Verify*: `/docs` endpoint shows interactive API docs
- [ ] Test API endpoints with various clients
  - *Verify*: Postman collection runs without errors

## Cross-Phase Requirements

### Quality Assurance
- [ ] Set up continuous linting with ruff
  - *Verify*: `ruff check .` passes without errors
- [ ] Configure type checking with mypy
  - *Verify*: `mypy .` passes without errors
- [ ] Ensure all tests pass in CI/CD pipeline
  - *Verify*: GitHub Actions/CI shows green build
- [ ] Code coverage reporting
  - *Verify*: Coverage report shows >80% line coverage

### Documentation
- [ ] Update README with installation and usage instructions
  - *Verify*: New developer can follow README and run application
- [ ] Document environment variables and configuration
  - *Verify*: `.env.example` file exists with all required vars
- [ ] Create troubleshooting guide for common issues
  - *Verify*: Guide addresses top 3 setup problems

## Technical Considerations

- Spotify API rate limiting and error handling
- Database abstraction design to support SQLite → PostgreSQL migration
- SQLite file location and backup strategies
- Configuration management for different environments
- Security considerations for web and API phases
- Performance optimization for large recommendation lists
- Database migration strategy from SQLite to PostgreSQL for production