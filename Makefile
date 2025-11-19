.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@grep -E '^\.PHONY: [a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: dev-setup ## Install development dependencies
dev-setup:
	pip install --use-pep517 -e ".[dev]"
	pre-commit install

.PHONY: tests ## Run unit tests
tests:
	PYTHONPATH=. pytest tests --cov=graphene_django_cruddals -vv --cov-report=term-missing

.PHONY: format ## Format code
format:
	pre-commit run ruff-format --all-files

.PHONY: lint ## Lint code
lint:
	pre-commit run ruff --all-files
