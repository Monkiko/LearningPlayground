output "instance_public_ip" {
    description = "Public IP address of web_server instance"
    value = join(", ", aws_instance.web_server.*.public_ip)
}