# The first make statement is what runs when you run `make` in the shell.
# This sets up a shell and makes sure that the project dependencies are installed.
build:
	@poetry shell
	@poetry install

test:
	@poetry run mypy
	@poetry run pytest

coverage:
	@poetry run pytest --cov=pom_elements tests

view-coverage-report
	@poetry run coverage report -m

atest:
	@poetry run pytest $(t)

# Run all pre-commit hooks on all files
verify-commit-hooks:
	@poetry run pre-commit run --all-files
