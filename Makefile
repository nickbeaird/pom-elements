# This file is part of Selenium-XPath

build:
	@poetry shell
	@poetry install

test:
	@poetry run pytest