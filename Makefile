# The first make statement is what runs when you run `make` in the shell.
# This sets up a shell and makes sure that the project dependencies are installed.
build:
	@poetry shell
	@poetry install

test:
	@poetry run mypy
	@poetry run pytest

# Run all pre-commit hooks on all files
verify-commit-hooks:
	@poetry run pre-commit run --all-files
