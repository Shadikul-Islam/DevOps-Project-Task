module "eks" {
  source        = "../../modules/eks"
  region        = var.region
  cluster_name  = var.cluster_name
  k8s_version   = var.k8s_version
  vpc_id        = var.vpc_id
  subnet_ids    = var.subnet_ids
  environment   = var.environment
}
