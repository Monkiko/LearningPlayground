resource "digitalocean_database_cluster" "mysql-Monkiko" {
  name       = "Monkiko-mysql-cluster"
  engine     = "mysql"
  version    = "8"
  size       = "db-s-1vcpu-1gb"
  region     = "nyc1"
  node_count = 1
}
