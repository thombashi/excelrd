PACKAGE := excelrd
PYTHON := python3


.PHONY: build
build: clean
	@$(PYTHON) -m tox -e build
	ls -lh dist/*

.PHONY: check
check:
	@$(PYTHON) -m tox -e lint

.PHONY: clean
clean:
	rm -rf docs/_build/
	$(PYTHON) -e clean

.PHONY: docs
docs:
	$(PYTHON) -m tox -e docs

.PHONY: fmt
fmt:
	tox -e fmt

.PHONY: setup-ci
setup-ci:
	@$(PYTHON) -m pip install -q --disable-pip-version-check --upgrade tox

.PHONY: setup
setup: setup-ci
	@$(PYTHON) -m pip install -q --disable-pip-version-check --upgrade .[dev]
