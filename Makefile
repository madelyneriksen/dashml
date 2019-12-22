.PHONY: build upload

build:
	python setup.py sdist bdist_wheel

upload:
	python -m twine upload dist/*
