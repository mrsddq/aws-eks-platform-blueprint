variable "region" {
  description = "AWS region for the platform."
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "EKS cluster name."
  type        = string
  default     = "platform-blueprint"
}

variable "environment" {
  description = "Environment label."
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for the platform VPC."
  type        = string
  default     = "10.40.0.0/16"
}

variable "node_instance_types" {
  description = "Managed node group instance types."
  type        = list(string)
  default     = ["t3.large"]
}

variable "cluster_version" {
  description = "Supported EKS Kubernetes minor version, chosen explicitly before planning."
  type        = string

  validation {
    condition     = can(regex("^1\\.[0-9]+$", var.cluster_version))
    error_message = "Specify a Kubernetes minor version such as 1.XX, verified against current EKS support."
  }
}

variable "cluster_endpoint_public_access" {
  description = "Expose the Kubernetes API publicly only when trusted CIDRs are set."
  type        = bool
  default     = false
}

variable "cluster_endpoint_public_access_cidrs" {
  description = "Trusted IPv4 CIDRs allowed to reach an enabled public API endpoint."
  type        = list(string)
  default     = []

  validation {
    condition = alltrue([
      for cidr in var.cluster_endpoint_public_access_cidrs :
      try(cidrnetmask(cidr) != "0.0.0.0", false)
    ])
    error_message = "Use valid IPv4 CIDRs and never allow 0.0.0.0/0."
  }
}
