# Variables

Core to Ansible are host and group variables. The hosts and groups are what you
declared in the hosts file.

## Host variables

These files declare what variables will be exclusive to each node. They live
under `host_vars/<host_name>.yml`.

Variables for the control node, the machine you're working on, is already there
as `host_vars/localhost.yml`.

For example, to configure two managed nodes, take the template from
`examplebox.yml`:

```sh
$ cp host_vars/examplebox.yml host_vars/mybox1.yml host_vars/mybox2.yml
```

They can declare the following variables (optional means depends if the
specific service is to be used):

```yml

# Base variables
base_hostname: examplebox # override the (decorative) hostname
base_user: cats
base_group: cats
base_user_id: "1000"
base_group_id: "1000"
base_timezone: "Gnu/Linux"
base_directory: "/path/homelab" # where compose and config files will be stored
base_tld: "example.cats"
base_tailip: "100.12.12.12" # headscale/tailscale ip of the box, fill in when asked to
base_lanip: "192.168.123.123" # local lan ip of the box, fill in in when asked to

sshd_port: "22" # The port for sshd

# These can be arbitrary, just make sure the networks are created
# in playbooks/traefik.yml and playbooks/unbound.yml have the same
# IPAM subnet.
traefik_bouncer_ip: "172.13.13.13" # traefik-bouncer ip
unbound_dns_ip: "172.12.12.12" # (OPTIONAL) unbound dns
unbound_dns_port: "1234" # (OPTIONAL) unbound dns port

# Core locations for storage and media
location:
  docker_data: "/my_data"
  cache: "/cache"
  films: "/my_films"
  music: "/my_music"
  books: "/my_books"
  repos: "/my_repos"
  downloads: "/my_downloads"

# Reverse proxy urls for our services
urls:
  # this format will give plex.example.cats
  jellyfin:
   sub: "plex"
   public: true # url is public (for DDNS auto configuration), defaults to false

  # this format will give admin.example.cats/pihole
  pihole:
    sub: "admin"
    path: "pihole"
    monitor: true # add to uptime monitoring, defaults to false

```

## Group variables

These files declare what variables will be shared between the nodes of each
group. They live under `group_vars/<group_name>.yml`.

So far, these variables can to be declare:

```yml
docker:
  compose_version: "3.8" # the current compose version
  traefik_network: "traefik" # the docker network for internal services
  expose_network: "expose" # the docker network for public services

# anything else for the group homelab goes here
```

## Service variables

Under `vars/` are variables specific to each service. They are stored here and
loaded in each playbook to keep the playbooks clean and easy to follow.
