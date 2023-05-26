PACKAGE := excelrd
PYTHON := python3


.PHONY: build
build: clean
	@$(PYTHON) -m tox -e build
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
