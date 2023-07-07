PACKAGE := excelrd
PYTHON := python3


.PHONY: build
build: clean
	@$(PYTHON) -m tox -e build
	ls -lh dist/*

.PHONY: check
check:
	python setup.py check
	pylama

.PHONY: clean
clean:
	@tox -e clean

.PHONY: fmt
fmt:
	tox -e fmt

.PHONY: setup-ci
setup-ci:
	@$(PYTHON) -m pip install -q --disable-pip-version-check --upgrade tox

.PHONY: setup
setup: setup-ci
	@$(PYTHON) -m pip install -q --disable-pip-version-check --upgrade .[dev]
