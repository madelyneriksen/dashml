.ONESHELL:
SHELL := /bin/bash
.PHONY: build release format test bench all docs

test:
	pytest
	MYPYPATH=${PWD}/dashml/stubs mypy --strict dashml
	black --check dashml
	exit ${STAT}

format:
	black dashml

bench:
	python bench.py

build: test
	rm -rf dist
	python setup.py sdist bdist_wheel

release: build
	python -m twine upload dist/*

docs:
	mkdir -p dist
	mkdir -p dist/docs
	sphinx-build -b html docs dist/docs 
