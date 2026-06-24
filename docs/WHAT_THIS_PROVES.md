# What This Proves

This repo is designed to show platform engineering judgment, not just YAML volume.

## Hiring Signals

- Can design AWS network boundaries for Kubernetes.
- Understands EKS cluster bootstrap and IAM constraints.
- Uses GitOps to separate infrastructure provisioning from workload reconciliation.
- Treats observability as part of the platform, not an afterthought.
- Documents operational checks, rollback paths, and cost risk.

## Interview Talking Points

- Why private subnets are the default for worker nodes.
- How IRSA reduces broad node-level AWS permissions.
- When managed node groups are enough and when Karpenter helps.
- Why Argo CD should own cluster resources after bootstrap.
- How Prometheus, Grafana, and Loki support incident response.
