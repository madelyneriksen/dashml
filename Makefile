.ONESHELL:
SHELL := /bin/bash
.PHONY: build release format test bench all

test:
	pytest
	mypy --strict dashml
	black --check dashml
	exit ${STAT}

format:
	black dashml

bench:
	python bench.py

build: test
	python setup.py sdist bdist_wheel

release: build
	python -m twine upload dist/*


