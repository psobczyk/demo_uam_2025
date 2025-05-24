
say_hello:
	echo "Hello World"

# phony
.PHONY: venv
venv:
	uv init

dev_env:
	uv sync --dev

.PHONY: lint
lint: dev_env
	uv run ruff check --fix

01_ps_first_notebook.html: notebooks/01_ps_first_notebook.ipynb
	uv run jupyter nbconvert --to html notebooks/01_ps_first_notebook.ipynb

.PHONY: mypy
mypy: dev_env
	uv run mypy src

.PHONY: format-check
format-check: dev_env
	uv run ruff check

.PHONY: format-fix
format-fix: dev_env
	uv run ruff check --fix

clean:
	rm -rf src/__pycache__/
	rm -rf src/.pytest_cache/
	rm -rf src/.coverage
	rm -rf src/htmlcov/
	rm -rf notebooks/.ipynb_checkpoints/
	rm -rf notebooks/*.html