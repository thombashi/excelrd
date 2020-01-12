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
	@python setup.py clean
	@rm -rf $(PACKAGE)-*.*.*/ \
		build/ \
		dist/ \
		pip-wheel-metadata/ \
		.eggs/ \
		.pytest_cache/ \
		.tox/ \
		*.egg-info/
	@find . -name "__pycache__" -type d -exec rm -rf "{}" \;
	@find . -name "*.pyc" -delete

.PHONY: fmt
fmt:
	tox -e fmt

.PHONY: setup
setup:
	@pip install --upgrade .[dev] tox
