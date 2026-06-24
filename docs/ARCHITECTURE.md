# Architecture

This project separates the platform into two layers:

1. AWS foundation managed by Terraform.
2. Kubernetes platform services managed through GitOps.

## AWS Foundation

The Terraform layer creates a multi-AZ VPC, private and public subnets, NAT gateways, an EKS control plane, managed node groups, and IAM roles for platform services. The cluster is private-subnet first and exposes workloads through the AWS Load Balancer Controller path.

## Kubernetes Platform

The Kubernetes layer defines stable namespaces, RBAC, a sample service, ingress, autoscaling, and observability installation values. Argo CD is expected to reconcile this layer after the cluster exists.

## Operational Boundaries

- Terraform owns cloud primitives.
- Argo CD owns Kubernetes resources after bootstrap.
- Helm values define platform add-ons.
- Application teams own workload manifests inside their namespace.

## Scaling Path

- Replace the sample app with a real service.
- Enable Karpenter once node rightsizing is required.
- Add External Secrets for production secret delivery.
- Add cluster-level policy controls with Kyverno or OPA.
