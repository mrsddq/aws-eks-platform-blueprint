# Incident Response

## Example Incidents

| Symptom | First check | Likely mitigation |
|---|---|---|
| Nodes not joining | Node IAM role, subnet routes, security groups | Fix IAM or private subnet routing |
| Ingress has no address | AWS Load Balancer Controller, subnet tags | Restore controller or subnet discovery tags |
| Pods crash looping | Events, logs, probes, resource limits | Roll back workload or tune resources |
| High error rate | App logs, recent deploys, ALB target health | Revert app change or isolate failing dependency |

## RCA Template

1. What happened?
2. Who was affected?
3. When did detection happen?
4. What changed recently?
5. What mitigated the issue?
6. What control would prevent recurrence?

## Production Improvements

- Add Alertmanager routing.
- Add synthetic checks for ingress endpoints.
- Add cluster backup strategy for critical namespaces.
- Add game-day failure scenarios for node drain, ingress failure and bad deploy rollback.
