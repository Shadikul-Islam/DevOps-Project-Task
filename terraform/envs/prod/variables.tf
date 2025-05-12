variable "region" {
  default = "us-west-2"
}
variable "cluster_name" {
  default = "my-cluster"
}
variable "k8s_version" {
  default = "1.29"
}
variable "vpc_id" {}
variable "subnet_ids" {
  type = list(string)
}
variable "environment" {
  default = "prod"
}
