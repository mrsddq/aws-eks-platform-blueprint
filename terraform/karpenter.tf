resource "aws_iam_instance_profile" "karpenter_node" {
  name = "${var.cluster_name}-karpenter-node"
  role = module.eks.eks_managed_node_groups["system"].iam_role_name
}

locals {
  karpenter_discovery_tag = {
    "karpenter.sh/discovery" = var.cluster_name
  }
}

# Karpenter installation is intentionally left as a GitOps step so the cluster
# can be bootstrapped first and reconciled afterward by Argo CD.
