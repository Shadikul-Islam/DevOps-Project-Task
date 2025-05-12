provider "aws" {
  region = var.region
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.8.3" 

  cluster_name    = var.cluster_name
  cluster_version = var.k8s_version
  subnet_ids      = var.subnet_ids
  vpc_id          = var.vpc_id

  eks_managed_node_groups = {
    default = {
      min_size       = 1
      max_size       = 3
      desired_size   = 2
      instance_types = ["t3.medium"]
    }
  }

  tags = {
    Environment = var.environment
    Terraform   = "true"
  }
}
