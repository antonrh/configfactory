.PHONY: help docs
.DEFAULT_GOAL := help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install

lint: ## Run code linters
	isort --check configfactory tests
	black --check configfactory tests
	flake8 configfactory tests
	mypy configfactory tests

fmt format: ## Run code formatters
	isort configfactory tests
	black configfactory tests

i18n-make:
	cd configfactory/ && django-admin makemessages -l en --settings=configfactory.conf.settings
