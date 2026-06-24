.PHONY: validate fmt test

validate: test
	python scripts/validate_layout.py

fmt:
	terraform fmt -recursive terraform

test:
	python -m unittest discover -s tests
