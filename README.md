# whence-jam-python
An app for knowing who recommended a song or album.

## Prompts

> /init

We gave it the /init command and it did a lot. Wrote up a plan and offered to just start building things. We never managed to give the next prompt.

> ~~We are in planning mode for a new project. Read the product spec and tech spec documents in this repository and wait for more instructions.~~

> No, please write a new markdown file listing the tasks you want to do, the plan you just gave me

> I have updated the tech spec to explicitly require that we use SQLite database for initial development, with other important details. Please look at e54453fc5bf7adb3aa17b2e87f3954db8d28c2a7 and then update your dev plan accordingly if changes are needed.

> [codex]
> Would you also like me to reflect the SQLite default in AGENTS.md’s Security & Configuration section?

> Sure, go for it.

> For each task, add some notes about how we will verify that the task is complete. Verification does not have to be via a test, it can be from user action like running `ruby --version` to show the correct version is installed. Keep it terse and with an expected audience of an experienced software engineer.

> [codex]
> If you want, I can also wire up a minimal make check that runs lint/format/tests to standardize local verification.

> Sure, go for it.

> [codex]
> Want me to add a simple GitHub Actions workflow that uses make check?

> Hold your horses, partner.

> [codex]
> Got it—I’ll pause here. Ready when you want me to proceed or adjust anything.

> Do the first task, it is related to tooling

> [codex]
> Added pyproject.toml with Poetry and tool configs.
> What’s included
> - Poetry metadata: project name, version, license, readme, and src layout packages.
> - Python version: ^3.11.
> - Core deps: flask, sqlalchemy, alembic, python-dotenv.
> - Dev deps: pytest, black, ruff, isort.
> - Tooling config: Black (88 cols, py311), Ruff (py311, rules E/F/I/UP), isort (Black profile, first-party whencejam).
> Verification
> - Run: poetry install
> - Check versions: poetry run python -V, poetry run black --version, poetry run ruff --version
> - Optional: make check (will run once tests exist)
> Want me to proceed with the next task (add .python-version), or adjust dependencies/config?

> Nope...hang tight

> [codex]
> Understood. I’ll hold. Say the word when you want me to continue.
