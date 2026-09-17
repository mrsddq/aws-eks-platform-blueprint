.PHONY: prerequisites validate fmt lint security-scan deploy destroy local-demo test

CONFIRM_DEPLOY ?= false

validate: test
	python scripts/validate_layout.py
	python scripts/validate_manifests.py

fmt:
	terraform fmt -recursive terraform

terraform-validate:
	terraform -chdir=terraform init -backend=false
	terraform -chdir=terraform validate

lint: validate
	terraform fmt -recursive -check terraform

security-scan:
	checkov -d terraform -d kubernetes --quiet

prerequisites:
	@command -v terraform >/dev/null || (echo "terraform is required" && exit 1)
	@command -v kubectl >/dev/null || (echo "kubectl is required" && exit 1)

deploy: prerequisites
	@if [ "$(CONFIRM_DEPLOY)" != "true" ]; then echo "Set CONFIRM_DEPLOY=true to create billable AWS resources."; exit 2; fi
	terraform -chdir=terraform init
	terraform -chdir=terraform apply

destroy: prerequisites
	@if [ "$(CONFIRM_DEPLOY)" != "true" ]; then echo "Set CONFIRM_DEPLOY=true to destroy AWS resources."; exit 2; fi
	terraform -chdir=terraform destroy

local-demo:
	kubectl kustomize kubernetes

test:
	python -m unittest discover -s tests
