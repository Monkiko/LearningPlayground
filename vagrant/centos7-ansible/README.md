# Ansible Playground

### Setup Recommendation
It is recommended that a shared SSH key be created as the ansible user on the ansible server and then copied over to server1. This can be executed in the following manner:

```
$ ssh-keygen
```

Accept the default file location and skip the passphrase (so you don't have to enter a password when running a playbook)

```
$ ssh-copy-id test
```

You will have to provide the password for the ansible user on server1 ('P@$$w0rd123') the first time to establish a connection to copy the ssh key over.


Test connecting using sshkey:
```
$ ssh test
```