"""Offline cross-resource checks for the manifests Argo CD actually selects."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_resources(root=ROOT):
    directory = root / "kubernetes"
    kustomization = yaml.safe_load((directory / "kustomization.yaml").read_text())
    resources = []
    for entry in kustomization["resources"]:
        path = (directory / entry).resolve()
        if not path.is_relative_to(directory.resolve()):
            raise ValueError("resources must stay within kubernetes/")
        for resource in yaml.safe_load_all(path.read_text()):
            if not isinstance(resource, dict) or not resource.get("apiVersion") or not resource.get("kind"):
                raise ValueError(f"{entry} is not a Kubernetes resource")
            resources.append(resource)
    return resources


def validate(resources):
    errors = []
    identities = [(r["kind"], r["metadata"].get("namespace"), r["metadata"]["name"]) for r in resources]
    if len(set(identities)) != len(identities):
        errors.append("duplicate Kubernetes resource identity")
    deployments = {(r["metadata"].get("namespace"), r["metadata"]["name"]): r for r in resources if r["kind"] == "Deployment"}
    if not deployments:
        errors.append("GitOps resource set contains no Deployment")
    service_accounts = {(ns, name) for kind, ns, name in identities if kind == "ServiceAccount"}
    for (namespace, name), deployment in deployments.items():
        spec = deployment["spec"]
        pod = spec["template"]
        labels = pod["metadata"]["labels"]
        selector = spec["selector"]["matchLabels"]
        if not selector or not selector.items() <= labels.items():
            errors.append(f"{name}: deployment selector does not match pod")
        if (namespace, pod["spec"].get("serviceAccountName")) not in service_accounts:
            errors.append(f"{name}: referenced service account is absent")
    for resource in resources:
        kind = resource["kind"]
        namespace = resource["metadata"].get("namespace")
        spec = resource.get("spec", {})
        if kind == "Service":
            selector = spec["selector"]
            matched = [d for (ns, _), d in deployments.items() if ns == namespace and selector and selector.items() <= d["spec"]["template"]["metadata"]["labels"].items()]
            if not matched:
                errors.append("service selector has no workload")
            for deployment in matched:
                ports = [port for c in deployment["spec"]["template"]["spec"]["containers"] for port in c.get("ports", [])]
                for port in spec["ports"]:
                    target = port.get("targetPort", port["port"])
                    if not any(target == p.get("containerPort") or target == p.get("name") for p in ports):
                        errors.append("service targetPort has no container port")
        if kind == "HorizontalPodAutoscaler" and (namespace, spec["scaleTargetRef"]["name"]) not in deployments:
            errors.append("autoscaler target has no Deployment")
    return errors


def main():
    resources = load_resources()
    errors = validate(resources)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"validated {len(resources)} selected Kubernetes resources and workload references")


if __name__ == "__main__":
    main()
