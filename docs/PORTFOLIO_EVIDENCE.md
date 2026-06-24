# Portfolio Evidence

Use this repo as an EKS platform blueprint, not as a claim of a live production cluster unless it has been deployed in your AWS account.

## Verified Locally

```bash
python -m unittest discover -s tests
python scripts/validate_layout.py
terraform fmt -recursive -check terraform
```

## Reviewer Evidence

| Evidence | Location | What it proves |
|---|---|---|
| CI badge | `README.md` | Terraform formatting and static validation run on GitHub Actions. |
| Terraform foundation | `terraform/` | VPC, EKS, IAM and Karpenter-ready design. |
| GitOps application | `kubernetes/argocd/application.yaml` | Argo CD reconciliation model. |
| Workload controls | `kubernetes/app/` | Probes, HPA, PDB, resources and ingress path. |
| Observability values | `kubernetes/observability/` | Prometheus, Grafana and Loki installation inputs. |
| Runbook | `docs/runbook.md` | Bootstrap, troubleshooting and rollback discipline. |

## Interview Proof Points

- Explain private-subnet worker nodes and public ALB ingress.
- Explain IRSA and why AWS permissions should not live on broad node roles.
- Explain where Terraform ownership stops and Argo CD ownership begins.
- Explain how Prometheus, Grafana and Loki support incident response.

## Screenshots And Proof To Capture

- GitHub Actions CI run for this repo.
- `terraform plan` summary from a sandbox account.
- Argo CD Application sync screen after bootstrap.
- `kubectl get nodes` and `kubectl get pods -A` after deployment.
- Grafana EKS/platform dashboard after metrics ingestion.
- AWS Budget or cost estimate used for the demo.

Do not add screenshots from unrelated clusters or accounts.
