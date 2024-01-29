resource "aws_instance" "web_server" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  key_name      = var.key_name
  tags          = var.tags
  public_ip     = var.public_ip

  user_data = <<-EOF
  #!/bin/bash
  ping -c 10 8.8.8.8
  EOF
}