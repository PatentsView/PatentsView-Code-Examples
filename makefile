.PHONY: format test

format:
	ruff format --line-length 120

test:
	conda run -v --no-capture-output -n pv-code-examples pytest