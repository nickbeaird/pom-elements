build:
	# The first make statement is what runs when you run `make` in the shell.
	# This sets up a shell and makes sure that the project dependencies are installed.
	@poetry shell
	@poetry install

test-speed:
	# Check the speed of the tests and return the slowest tests by the --durations flag
	# Run with `make test-speed top=NUMBER_OF_TESTS
	@poetry run pytest --durations=${top}

test:
	# Run all tests
	@poetry run mypy
	@poetry run pytest

coverage:
	@poetry run pytest --cov=pom_elements tests

view-coverage-report:
	@poetry run coverage report -m

atest:
	@poetry run pytest tests/test_$(t)

verify-commit-hooks:
	# Run all pre-commit hooks on all files
	@poetry run pre-commit run --all-files
