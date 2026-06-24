# Cost Estimate

This repo can create billable AWS resources. Treat all numbers as rough planning estimates and verify with the AWS Pricing Calculator before deployment.

## Main Cost Drivers

| Resource | Cost driver | Control |
|---|---|---|
| EKS control plane | Hourly cluster fee | Keep sandbox clusters short lived |
| Managed nodes | EC2 instance hours | Use small node groups and autoscaling |
| NAT gateways | Hourly plus data processing | Prefer one sandbox NAT only when acceptable |
| ALB | Hourly plus LCU usage | Delete test ingresses after demos |
| Logs and metrics | Retention and ingestion | Set retention and dashboard scope |

## Guardrails

- Use a sandbox AWS account.
- Apply cost allocation tags from Terraform.
- Set an AWS Budget before deployment.
- Run `make destroy CONFIRM_DEPLOY=true` after demos.
- Do not run production-sized node groups for portfolio screenshots.
