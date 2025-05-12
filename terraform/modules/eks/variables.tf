variable "region" {}
variable "cluster_name" {}
variable "k8s_version" {}
variable "vpc_id" {}
variable "subnet_ids" {
  type = list(string)
}
variable "environment" {}
