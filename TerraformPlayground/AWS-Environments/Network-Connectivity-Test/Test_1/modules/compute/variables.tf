variable "instance_type" {
    description = "Instance type"
    type = string
}


variable "ami" {
    description = "ami id"
    type = string
}


variable "key_name" {
  description = "the key pair for the instance"
  type        = string
}


variable "subnet_id" {
  description = "subnet_id"
  type        = string
}


variable "vpc_id" {
  description = "id of the public vpc for the security group"
  type        = string
}


variable "tags" {
    description = "Tags to set on Compute resources"
    type = map(string)
}

variable "public_ip" {
    description = "Public IP of the instance"
    type = string
}