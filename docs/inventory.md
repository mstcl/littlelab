# Inventory

Ansible acts on an inventory 'hosts' file to know what nodes are available to
run tasks on. It normally defaults to a file elsewhere on the system, we want
to use one local to our project only.

Inside `inventory/`, copy `hosts_example` to `hosts`, which is the actual hosts
file the project will reference:

```sh
$ cp inventory/hosts_example inventory/hosts
```

It should look something like:

```ini
# This is the machine you're on, can leave as is
localhost ansible_connection=local

# The homelab group, consisting of hosts (1) mybox and (2) mybox2
[homelab]
mybox1 ansible_user=cat ansible_host=192.168.4.87 ansible_port=22
mybox2 ansible_user=dog ansible_host=192.168.4.17 ansible_port=22
```

The `ansible_user` of each host should be the name of the non-root user you
intend to create on each host.
