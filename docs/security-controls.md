# Security Controls

## Implemented

- EKS worker nodes in private subnets.
- IAM policy boundary example for AWS Load Balancer Controller.
- Kubernetes namespaces and RBAC.
- Resource limits, probes, HPA and PodDisruptionBudget.
- GitHub Actions validation.
- Optional Checkov scan through `make security-scan`.

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
