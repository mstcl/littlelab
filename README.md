# Homelab

**appropriately ansibled**

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Inventory](#inventory)
- [Variables](#variables)
- [Running](#running)
- [Other playbooks](#other-playbooks)
  - [Adding a new service](#adding-a-new-service)
  - [Update a docker container image](#update-a-docker-container-image)
  - [Creating new users for services](#creating-new-users-for-services)
    - [Authelia](#authelia)
    - [Headscale](#headscale)
  - [Generating API keys](#generating-api-keys)
    - [Headscale](#headscale-1)
- [Role documentation](#role-documentation)
  - [NGINX](#nginx)
    - [First usage](#first-usage)
    - [Second usage](#second-usage)

<!-- mdformat-toc end -->

## Inventory

Provided is an [example](./inventory/hosts_example) for our inventory under `inventory/hosts_example`.

## Variables

Provided is an [example](./host_vars/examplebox.yml) for our main box in under `host_vars/examplebox.yml`.
`group_vars` for `[homelab]` is provided as is. Most of these variables will need to
be filled in prior to running `main.yml`. Read through it first.

## Running

Read carefully the comments and notes inside `main.yml`. Go through each configuration
file (mostly as Jinja2 templates) and make sure they look good.

## Other playbooks

### Adding a new service

To add a new service playbook and template docker compose file:

```bash
ansible-playbook add_new_service.yml
```

It will prompt for a service name, and create a playbook
`playbooks/<service_name>.yml` and basic docker compose file under
`files/<service_name>/templates/docker-compose.yml`.

### Update a docker container image

The playbook `update_container.yml` will prompt for an image repo name. It will
pull the image with the latest tag. Rerun the playbooks for this particular
image with the tag `docker` to put the containers back up again.

Example:

```bash
ansible-playbook update_container.yml
#STDOUT: Enter the repository name
#STDIN: authelia/authelia
# [...]

ansible-playbook playbooks/authelia.yml --tags=docker
```

### Creating new users for services

The playbook `add_new_user.yml` can help with this.

#### Authelia

To make an authelia user:

```bash
ansible-playbook add_new_user.yml --tags=authelia -e username='user' -e display_name='User' \
    -e email='user@example.com' -e password='password' -e admin='false'
```

#### Headscale

To make a headscale user:

```bash
ansible-playbook add_new_user.yml --tags=headscale -e username='user'
```

### Generating API keys

The playbook `generate_api_key.yml` can help with this.

#### Headscale

```bash
ansible-playbook generate_api_key.yml --tags=headscale
```

## Role documentation

The playbook also reads from `vars/adguard-home.yml` to configure user rules,
upstream DNS, fallback DNS and blocklists. See the
[example](./vars/adguard-home_example.yml) provided.

### NGINX

**Location: `roles/nginx`**

#### First usage

When called _without_ `configs` or `mounts`, configures an NGINX
instance (that is, making default hardened `nginx.conf` and various files and
directories). We can also specify `nginx_config_override` to replace the
default `nginx.conf`.

Example:

```yaml
- name: Install nginx
  roles:
    - role: nginx
      vars:
        nginx_config_override: "custom_nginx.conf"
```

The configuration override like the file `custom_nginx.conf` above would be
found at `roles/nginx/files/custom_nginx.conf`

#### Second usage

To reverse proxy a service with NGINX, we call the `nginx` role with the
`configs` and/or `mounts` variables. This role should be called within the
service playbooks, and not the NGINX playbooks. Otherwise, it is very hard to
keep track of which service uses NGINX and the order of configuration.

We use the variable `nginx_flavour` to indicate the NGINX instance/container
name we wish to use for a certain service.

The `config` block lists all the server configurations to template into
`conf.d`. These templates should be found at
`roles/nginx/templates/<service>.conf.j2`.

The `mount` block will append bind mounts to the compose file found at
`files/<my-nginx-instance>/templates/docker-compose.yml.2`.

Example:

```yaml
- name: Install piped
  vars:
    nginx_flavour: "nginx-piped"
    # [...]
  roles:
    # [...]
    - role: nginx
      vars:
        configs:
          - config_name: "piped"
            server_url: "https://example1.com"
          - config_name: "piped-proxy"
            server_url: "https://example2.com"
          - config_name: "piped-frontend"
            server_url: "https://example3.com"
        mounts:
          - reference: "Piped socket"
            host_location: "/host/socket"
            container_location: "/remote/socket"
    # [...]
```

In this example, the `nginx-piped` container is configured. We add the server
configuration `{piped,piped-proxy,piped-frontend}.conf` to the usual NGINX's
`conf.d`, mounted appropriately onto the container.

We also bind mount the socket, which is equivalent `/host/socket:/remote/socket`.
