# .PHONY: run
run:
	poetry run clickpy

test:
	pytest tests/ --cov=clickpy -v


coverage:
	coverage html && open htmlcov/index.html
