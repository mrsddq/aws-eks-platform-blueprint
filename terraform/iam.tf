data "aws_iam_policy_document" "load_balancer_controller" {
  statement {
    effect = "Allow"

    actions = [
      "elasticloadbalancing:*",
      "ec2:Describe*",
      "ec2:AuthorizeSecurityGroupIngress",
      "ec2:RevokeSecurityGroupIngress",
      "iam:CreateServiceLinkedRole",
      "wafv2:GetWebACL",
      "wafv2:AssociateWebACL",
      "wafv2:DisassociateWebACL",
      "acm:ListCertificates",
      "acm:DescribeCertificate",
      "shield:GetSubscriptionState",
      "shield:DescribeProtection",
      "shield:CreateProtection",
      "shield:DeleteProtection"
    ]

    resources = ["*"]
  }
}

resource "aws_iam_policy" "load_balancer_controller" {
  name        = "${var.cluster_name}-aws-load-balancer-controller"
  description = "Policy used by the AWS Load Balancer Controller service account."
  policy      = data.aws_iam_policy_document.load_balancer_controller.json
  tags        = local.common_tags
}
