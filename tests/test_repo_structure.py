import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepoStructureTest(unittest.TestCase):
    def test_terraform_layer_mentions_eks_and_vpc(self):
        main_tf = (ROOT / "terraform" / "main.tf").read_text(encoding="utf-8")
        self.assertIn('module "vpc"', main_tf)
        self.assertIn('module "eks"', main_tf)

    def test_kubernetes_workload_has_limits_and_probes(self):
        deployment = (ROOT / "kubernetes" / "app" / "deployment.yaml").read_text(encoding="utf-8")
        self.assertIn("resources:", deployment)
        self.assertIn("readinessProbe:", deployment)
        self.assertIn("livenessProbe:", deployment)

    def test_docs_include_operational_runbook(self):
        runbook = (ROOT / "docs" / "RUNBOOK.md").read_text(encoding="utf-8")
        self.assertIn("Rollback", runbook)
        self.assertIn("Post-Deploy Checks", runbook)


if __name__ == "__main__":
    unittest.main()
