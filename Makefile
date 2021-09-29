.PHONY: run
run:
	poetry run clickpy

.PHONY: test
test:
	poetry run pytest tests/ --cov=clickpy -v

.PHONY: coverage
coverage:
	poetry run coverage html && open htmlcov/index.html
