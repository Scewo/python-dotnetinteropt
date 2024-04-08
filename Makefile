ifeq ($(OS),Windows_NT)
	ON_WINDOWS = 1
else
	ON_WINDOWS = 0
endif

# Remove & move files
ifeq ($(ON_WINDOWS),1)
	RM = cmd /C "del /Q /F"
	RRM = cmd /C "rmdir /Q /S"
	MV = cmd /C "move"
else
	RM = rm -f
	RRM = rm -f -r
	MV = mv
endif

.PHONY: all
all: pre-commit

.PHONY: setup
setup: pyproject.toml
ifneq ("$(wildcard requirements.txt)","")
	python -m pip install -r requirements.txt
	python -m pip install --no-deps .
else
	python -m pip install .
endif

.PHONY: setup-dev
setup-dev: pyproject.toml
ifneq ("$(wildcard requirements-dev.txt)","")
	python -m pip install -r requirements-dev.txt
	python -m pip install --no-deps -e ".[dev]"
else
	python -m pip install -e ".[dev]"
endif
	pre-commit install

.PHONY: examples
examples: pyproject.toml
	python -m pip install -e .
	python -c "from dotnetinteropt.backend import install_nugets; install_nugets()"

.PHONY: pin-dev
pin-dev: pyproject.toml
	pip-compile --output-file=requirements.txt pyproject.toml
	pip-compile --extra=dev --output-file=requirements-dev.txt pyproject.toml

.PHONY: pin
pin: pyproject.toml
	pip-compile --resolver=backtracking --output-file=requirements.txt pyproject.toml

.PHONY: pin-upgrade-dev
pin-upgrade-dev: pyproject.toml
	pip-compile --resolver=backtracking --upgrade --output-file=requirements.txt pyproject.toml
	pip-compile --resolver=backtracking --upgrade --extra=dev --output-file=requirements-dev.txt pyproject.toml

.PHONY: precommit-update
precommit-update:
	pre-commit autoupdate

.PHONY: pin-upgrade
pin-upgrade: pyproject.toml
	pip-compile --resolver=backtracking --upgrade --output-file=requirements.txt pyproject.toml

.PHONY: sync-dev
sync-dev: requirements-dev.txt
	pip-sync requirements-dev.txt
	python -m pip install -e ".[dev]"

.PHONY: sync
sync: requirements.txt
	pip-sync requirements.txt
	python -m pip install .

.PHONY: pre-commit 
pre-commit:
	pre-commit run --all-files --show-diff-on-failure

.PHONY: format
format:
	pre-commit run --all-files isort 
	pre-commit run --all-files yapf

.PHONY: lint
lint:
	pre-commit run --all-files flake8
	pre-commit run --all-files pylint

.PHONY: lint-cached
lint-cached:
	pre-commit run flake8
	pre-commit run pylint

.PHONY: format-cached
format-cached:
	pre-commit run isort 
	pre-commit run yapf

.PHONY: test
test:
	pytest -s

.PHONY: profile
profile:
	pytest --profile --profile-svg

.PHONY: type-check
type-check:
	pre-commit run --all-files mypy

.PHONY: type-check-cached
type-check-cached:
	pre-commit run --all-files mypy

.PHONY: tox
tox:
	@echo "Be sure that python 3.8, 3.9, 3.10, 3.11 and 3.12 are installed."
	$(RRM) .tox
	tox -p auto

.PHONY: tox-serial
tox-serial:
	@echo "Be sure that python 3.8, 3.9, 3.10, 3.11 and 3.12 are installed."
	$(RRM) .tox
	tox

.PHONY: docs
docs: docs-html

.PHONY: docs-html
docs-html:
	$(MAKE) -C docs html

.PHONY: docs-pdf
docs-pdf:
	$(MAKE) -C docs latexpdf

.PHONY: docs-epub
docs-epub:
	$(MAKE) -C docs epub

.PHONY: docs-latex
docs-latex:
	$(MAKE) -C docs latex
