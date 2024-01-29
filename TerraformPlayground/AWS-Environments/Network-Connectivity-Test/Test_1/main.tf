module "web_server" {
  source = "./modules/compute"

  instance_type = "t2.micro"
  ami           = "ami-06aa3f7caf3a30282"
  subnet_id     = "subnet-01bd6dc7d5c31f7d6"
  key_name      = "MonKeyPair"
  vpc_id        = "vpc-0d0f54dd3faeceb2e"
  #count         = 4
  #public_ip     = aws_instance.web_server.public_ip
  tags = {
    Name = "web_server-NCT"
  }
}