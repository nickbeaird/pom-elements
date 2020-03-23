# This file is part of Selenium-XPath

build:
	@poetry shell
	@poetry install

test:
	@poetry run pytest

# Run all pre-commit hooks
commit-hooks:
	@poetry run pre-commit run --all-files
