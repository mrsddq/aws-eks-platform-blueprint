from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    ".github/workflows/ci.yml",
    "terraform/main.tf",
    "terraform/iam.tf",
    "terraform/karpenter.tf",
    "kubernetes/namespaces.yaml",
    "kubernetes/rbac.yaml",
    "kubernetes/app/deployment.yaml",
    "kubernetes/app/service.yaml",
    "kubernetes/app/ingress.yaml",
    "kubernetes/app/autoscaling.yaml",
    "kubernetes/argocd/application.yaml",
    "kubernetes/observability/prometheus-values.yaml",
    "docs/RUNBOOK.md",
]


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_phrases = ["EKS", "Argo CD", "Prometheus", "What This Proves"]
    missing_phrases = [phrase for phrase in required_phrases if phrase not in readme]
    if missing_phrases:
        raise SystemExit(f"README missing phrases: {', '.join(missing_phrases)}")

    print("layout validation passed")


if __name__ == "__main__":
    main()
