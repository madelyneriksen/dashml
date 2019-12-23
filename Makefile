SHELL := /bin/bash
.PHONY: build release format test bench all docs serve-docs

test:
	pytest
	python -m doctest dashml/*.py
	MYPYPATH=${PWD}/dashml/stubs mypy --strict dashml
	black --check dashml

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

serve-docs: docs
	cd dist/docs && python -m http.server
