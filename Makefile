SHELL = /bin/bash

default: help
.PHONY: help

test: ## Run tests
	tox -e py35,py38

coverage: ## Test coverage report
	tox -e coverage

lint: check-format flake8 bandit ## Lint code

flake8:
	tox -e flake8

bandit:
	tox -e bandit

extra-lint: pylint mypy  ## Extra, optional linting.

pylint:
	tox -e pylint

mypy:
	tox -e mypy

check-format:
	tox -e check-format

format: ## Format code
	tox -e format

piprot: ## Check for outdated dependencies
	tox -e piprot

.PHONY: docs
docs:  ## Generate documentation
	tox -e docs

precommit: test lint coverage docs ## Pre-commit targets
	@ python -m this

recreate: ## Recreate tox environments
	tox --recreate --notest -e py35,py36,py37,format,flake8,bandit,piprot,pylint

clean: ## Clean generated files
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	rm -rf build/ dist/ *.egg-info/ .cache .coverage .pytest_cache
	find . -name "__pycache__" -type d -print | xargs -t rm -r
	find . -name "test-output" -type d -print | xargs -t rm -r

repl: ## Python REPL
	tox -e py38 -- python

outdated: ## List outdated dependancies
	tox -e py38 -- pip list --outdated

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1,$$2}'
