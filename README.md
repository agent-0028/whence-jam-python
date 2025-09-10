# whence-jam-python
An app for knowing who recommended a song or album.

## Prompts

**9/1/2025**

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

**9/9/2025**

This is a new session. Codex does not seem to have a `/resume` like Claude.

So, I am going to prompt it that we are in the resuming something...

> We are resuming a project. The goal is to use the product spec to write some new code. When we left off, you had implemented the fist Task. Do not do anything but read the files in this repo and wait while I verify that the first Task is actually complete.

Manual verification for first Task didn't work great, I have to install poetry with brew, then I'll try the steps again.

Installed poetry (added to my Brewfile) and tried to follow verification steps.


> I ran `poetry install` per the steps and got this error: `pyproject.toml is not a valid TOML file. TOMLDecodeError: Unescaped '\' in a string (at line 33, column 14)`. Please fix the error.

> I think that worked! The response was: `Installing the current project: whence-jam-python (0.1.0) whence-jam-python-codex/src/whencejam does not contain any element`, don't do anything more I am going to commit what we have.

> Go ahead and implement the next Task, it is related to versions. 

> [codex]
> Want me to proceed with the next task (env scaffolding with .env.example)?

> No, not yet, please run the verification steps yourself, then I will commit the results

Codex was unable to verify, since pyenv doesn't have the right version of Python available. So, I am gonna be a dick and make it correct the verification steps.

> [codex]
> The verification steps should cover everything a dev needs to do to
> bootstrap this project, so I think the pyenv instructions are missing.
> Update the Task verification steps. I can tell you I have installed
> pyenv via Brew, so you should be able to run it.

Codex updated the verification steps and I ran them myself. Things seem to be working as expected at this point.

