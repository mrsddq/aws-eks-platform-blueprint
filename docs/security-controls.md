# Security Controls

## Implemented

- EKS worker nodes in private subnets.
- IRSA role restricted to kube-system/aws-load-balancer-controller, using the maintained controller policy.
- Private EKS API by default; public access requires an explicit trusted CIDR list.
- Grafana admin credentials are loaded from an existing Secret.
- Kubernetes namespaces and RBAC.
- Resource limits, probes, HPA and PodDisruptionBudget.
- GitHub Actions validation.
- Advisory Checkov scan in CI; `make security-scan` fails on findings.

## Recommended Production Additions

- GitHub OIDC to AWS instead of long-lived access keys.
- External Secrets or Secrets Manager integration.
- Kyverno or OPA admission policies.
- Trivy image scanning.
- Kubernetes audit logging export and retention.
- KMS-encrypted secrets and least-privilege IRSA per workload.

## Security Review Questions

- Which IAM role can create load balancers?
- Which service account can read Kubernetes resources?
- What happens if a pod is compromised?
- How are secrets delivered without committing values?
- Which CI checks block unsafe infrastructure changes?
