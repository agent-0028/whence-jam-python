# whence-jam-python
An app for knowing who recommended a song or album.

## Prompts

**9/1/2025**

> /init

It generated a CLAUDE.md and in the terminal gave me a summary of a plan.

> [CLAUDE]
> I've created a CLAUDE.md file for your repository. The file provides essential information about your music recommendation tracking project, including:
> - Project overview and three-phase development plan
> - Architecture guidelines emphasizing Flask and Python best practices
> - Development setup commands for virtual environments and dependencies
> - Testing requirements from your technical specification
> - Core functionality description
>
> Since this is an early-stage project with no code implementation yet, the file focuses on the architectural foundation from your product and technical specifications rather than specific build commands or detailed code structure.

> Please write a new markdown file listing the tasks you want to do, the plan you just gave me

> I see you have already specified SQLite database. I have updated the tech spec to make this choice explicit and add some details. Please look at 4d2d60b2e6c32ca5575ccf52900a54cfc8e41fd5 and then update your dev plan accordingly if changes are needed.

> For each task in the dev plan, add some notes about how we will verify that the task is complete. Verification does not have to be via a test, it can be from user action like running `ruby --version` to show the correct version is installed. Keep it terse and with an expected audience of an experienced siftware engineer.

> Do the first task in "Setup Tasks"

Claude got confused and was having a hard time with installs.

> What are we using to manage our version of Python? The tech spec says we should have a tool for that. I see you installing pip, that should not be needed.

> [Claude]
> You're absolutely right. The tech spec requires "facility to manage what version of Python is used" and I jumped ahead to pip installation without setting that up first.
> Looking at the .gitignore, I can see it mentions several Python version management tools:
> - pyenv (line 88)
> - pipenv (line 95)
> - UV (line 98)
> - poetry (line 108)
> - pdm (line 115)
> - pixi (line 122)
> Which Python version management tool would you like to use for this project? Common choices are:
> - pyenv for Python version management
> - uv for modern fast dependency management
> - poetry for dependency + version management
> - pdm for PEP 582 compliant dependency management

It did all the things, tried to verify and then actually seemed to give up on verifying. The output was:

> [Claude]
> I've completed the first setup task:
>  ✅ Created pyproject.toml with Poetry configuration
>  - Set up Poetry-based dependency management
>  - Added .python-version file specifying Python 3.12.0 for pyenv
>  - Configured all required dependencies (click, requests, flask, python-dotenv)
>  - Added development dependencies (pytest, ruff, mypy, etc.)
>  - Set up tool configurations for ruff, mypy, pytest
>    To verify: The user will need to:
>  1. Install Python 3.12.0 with pyenv: pyenv install 3.12.0
>  2. Install Poetry if not present
>  3. Run poetry install to install dependencies
> The pyproject.toml is ready and follows Poetry conventions with proper Python version management via pyenv.

**9/9/2025**

This is a new session.

I used the `/resume` command in Claude.

Sigh...the verification steps in DEVELOPMENT_PLAN.md do not match what Claude told me in the console.

> The verification steps in the dev plan do not match what you told me here during the last session. Please update the plan.

