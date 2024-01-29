output "instance_id" {
  description = "ID of the EC2 instance"
  value       = module.web_server.instance_id
}


output "public_ip" {
  description = "Public IP of EC2 instance"
  value       = module.web_server.public_ip
}