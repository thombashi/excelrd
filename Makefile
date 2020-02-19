PACKAGE := excelrd


.PHONY: build
build:
	@make clean
	@python setup.py sdist bdist_wheel
	@twine check dist/*
	@python setup.py clean
	ls -lh dist/*

.PHONY: check
check:
	python setup.py check
	travis lint
	pylama

.PHONY: clean
clean:
	@tox -e clean

.PHONY: fmt
fmt:
	tox -e fmt

.PHONY: setup
setup:
	@pip install --upgrade .[dev] tox
