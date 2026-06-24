# Runbook

## Prerequisites

- AWS sandbox account
- Terraform `>= 1.6`
- AWS CLI authenticated through SSO or an assumed role
- `kubectl`
- Remote state bucket and lock table before shared use

## Validate

```bash
make test
make lint
make local-demo
```

## Deploy

```bash
make deploy CONFIRM_DEPLOY=true
aws eks update-kubeconfig --name platform-blueprint --region us-east-1
kubectl get nodes
kubectl get pods -A
```

## Post-Deploy Checks

```bash
kubectl get nodes
kubectl get pods -A
kubectl get ingress -A
kubectl top nodes
```

## Destroy

```bash
make destroy CONFIRM_DEPLOY=true
```

## Rollback

- Kubernetes rollback: revert Git and let Argo CD reconcile.
- Terraform rollback: create a reviewed plan that restores the previous infrastructure state.
- Emergency rollback: scale down or remove the failing workload before touching shared infrastructure.

## Backup And Restore

- Store Terraform state in S3 with versioning and DynamoDB locking.
- Export critical Kubernetes manifests from Git, not from the cluster.
- Keep Grafana dashboards and alert rules in Git.
