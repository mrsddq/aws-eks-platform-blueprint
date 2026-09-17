import copy
import importlib.util
from pathlib import Path
import unittest

import hcl2
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate_manifests.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ManifestContractTest(unittest.TestCase):
    def setUp(self):
        self.resources = VALIDATOR.load_resources()

    def test_gitops_selects_workloads_without_helm_values_or_self_reference(self):
        self.assertEqual(VALIDATOR.validate(self.resources), [])
        kinds = {r["kind"] for r in self.resources}
        self.assertTrue({"Deployment", "Service", "Ingress", "HorizontalPodAutoscaler", "PodDisruptionBudget"} <= kinds)
        self.assertNotIn("Application", kinds)

    def test_missing_workload_is_detected(self):
        resources = [r for r in self.resources if r["kind"] != "Deployment"]
        self.assertIn("GitOps resource set contains no Deployment", VALIDATOR.validate(resources))

    def test_broken_selector_or_port_is_detected(self):
        for key, value, message in (("selector", {"app": "wrong"}, "service selector has no workload"), ("ports", [{"port": 80, "targetPort": 9999}], "service targetPort has no container port")):
            with self.subTest(key=key):
                resources = copy.deepcopy(self.resources)
                service = next(r for r in resources if r["kind"] == "Service")
                service["spec"][key] = value
                self.assertIn(message, VALIDATOR.validate(resources))

    def test_duplicate_resources_are_detected(self):
        self.assertIn("duplicate Kubernetes resource identity", VALIDATOR.validate(self.resources + [self.resources[0]]))

    def test_grafana_requires_external_credentials(self):
        values = yaml.safe_load((ROOT / "kubernetes/observability/prometheus-values.yaml").read_text())
        self.assertNotIn("adminPassword", values["grafana"])
        self.assertTrue(values["grafana"]["admin"]["existingSecret"])

    def test_terraform_parses_and_endpoint_is_private_by_default(self):
        documents = [hcl2.loads(path.read_text()) for path in (ROOT / "terraform").glob("*.tf")]
        variables = {name.strip('"'): body for doc in documents for entry in doc.get("variable", []) for name, body in entry.items()}
        self.assertIs(variables["cluster_endpoint_public_access"]["default"], False)
        self.assertEqual(variables["cluster_endpoint_public_access_cidrs"]["default"], [])
        self.assertNotIn("default", variables["cluster_version"])


if __name__ == "__main__":
    unittest.main()
