.ONESHELL:
SHELL := /bin/bash
.PHONY: build upload format test

test:
	pytest
	mypy --strict dashml
	black --check dashml
	exit ${STAT}

build:
	python setup.py sdist bdist_wheel

upload:
	python -m twine upload dist/*

format:
	black dashml

