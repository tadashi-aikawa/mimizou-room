PHONY: serve

serve:
	pipenv run mkdocs serve

init:
	pipenv install

build:
	pipenv run mkdocs build
