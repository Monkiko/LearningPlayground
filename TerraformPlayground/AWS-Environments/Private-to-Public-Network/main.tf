data "aws_security_group" "forssh" {
  id = "sg-006ff5db7508acdeb"
}

resource "aws_instance" "web_server" {
  count           = 4
  instance_type   = "t2.micro"
  ami             = "ami-00c39f71452c08778"
  key_name        = "MonKeyPair"
  subnet_id       = "subnet-02496d4df3bc85771"
  security_groups = [data.aws_security_group.forssh.id]
  tags = {
    Name = "web_server_${count.index}"
  }
}