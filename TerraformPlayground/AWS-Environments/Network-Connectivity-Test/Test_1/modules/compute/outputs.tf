output "public_ip" {
  description = "Public IP address of web_server instance"
  value       = aws_instance.web_server.public_ip
}


output "instance_id" {
  description = "ID of the EC2 instance"
  value = aws_instance.web_server.id
}