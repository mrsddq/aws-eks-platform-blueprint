# Runbook

## Bootstrap

1. Confirm AWS account access and region.
2. Create a remote state bucket and lock table.
3. Run `terraform init`.
4. Run `terraform plan -out tfplan`.
5. Apply only after reviewing networking, IAM, and EKS changes.

## Post-Deploy Checks

```bash
aws eks update-kubeconfig --name platform-blueprint --region us-east-1
kubectl get nodes
kubectl get pods -A
kubectl get ingress -A
```

## Common Issues

### Nodes do not join

- Check node group IAM role.
- Confirm private subnet routing and NAT gateway availability.
- Review EKS cluster security group rules.

### Ingress has no address

- Confirm AWS Load Balancer Controller is installed.
- Check service account IAM role annotation.
- Review subnet tags for Kubernetes load balancer discovery.

### Argo CD application is out of sync

- Confirm the target repo URL and path.
- Check namespace existence.
- Review Argo CD controller logs.

## Rollback

Rollback Kubernetes changes through Git revert and Argo CD sync. Roll back Terraform only through reviewed plans because cloud resource replacement can cause downtime.
