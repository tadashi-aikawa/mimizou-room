PHONY: serve

serve:
	poetry run mkdocs serve -a localhost:3300 --dirtyreload

build:
	poetry run mkdocs build
