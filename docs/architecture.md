# Architecture

## High-Level Platform

```mermaid
flowchart LR
    Engineer["Platform engineer"] --> GitHub["GitHub repository"]
    GitHub --> CI["CI validation"]
    CI --> Terraform["Terraform foundation"]
    Terraform --> VPC["Multi-AZ VPC"]
    Terraform --> EKS["Amazon EKS"]
    EKS --> Argo["Argo CD"]
    Argo --> Workloads["Namespaces and workloads"]
    Workloads --> ALB["AWS ALB ingress"]
    Workloads --> Observability["Prometheus, Grafana, Loki"]
```

## CI/CD Flow

```mermaid
flowchart LR
    PR["Pull request"] --> Tests["Unit and layout tests"]
    PR --> Fmt["Terraform fmt check"]
    PR --> Review["Human review"]
    Review --> Merge["Merge to main"]
    Merge --> Apply["Manual terraform apply"]
    Apply --> Argo["Argo CD sync"]
```

## Kubernetes Deployment Flow

```mermaid
flowchart LR
    Argo["Argo CD Application"] --> Namespace["sample-app namespace"]
    Namespace --> RBAC["ServiceAccount and Role"]
    Namespace --> Deployment["sample-api Deployment"]
    Deployment --> HPA["HorizontalPodAutoscaler"]
    Deployment --> PDB["PodDisruptionBudget"]
    Deployment --> Service["ClusterIP Service"]
    Service --> Ingress["ALB Ingress"]
```

## Observability Flow

```mermaid
flowchart LR
    Pods["Application pods"] --> Metrics["Prometheus scrape"]
    Pods --> Logs["Promtail logs"]
    Metrics --> Grafana["Grafana dashboards"]
    Logs --> Loki["Loki"]
    Grafana --> OnCall["On-call review"]
```

## Production Notes

- Terraform owns AWS networking, EKS and IAM foundation.
- Argo CD owns Kubernetes resources after bootstrap.
- Observability is part of the platform, not a later add-on.
- Production use should add remote state, AWS OIDC from CI, secret management and enforced admission policies.
