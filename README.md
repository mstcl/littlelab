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
    - [Filebrowser](#filebrowser)
  - [Generating keys](#generating-keys)
    - [Implemented services](#implemented-services)
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
ansible-playbook create_service.yml
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

The playbook `create_user.yml` can help with this.

To make an user:

```bash
ansible-playbook create_user.yml --tags='<service-name>' -e variable1='<variable1>' -e variable2='<variable2>' # etc.
```

The variables are specific for each service. Use single quotes on the variables, especially on the password.

#### Authelia

- `username`: the username to login (string).
- `display_name`: the display name that is shown on the login page (string).
- `password`: the password (string).
- `email`: the email that Authelia will use for confirmation of certain things (string).
- `admin`: whether or not the user is in the admin group, true/false/yes/no accepted (boolean).

#### Headscale

- `username`: the username to login (string).

#### Filebrowser

- `username`: the username to login (string).
- `password`: the password (string).

### Generating keys

The playbook `generate_keys.yml` can help with this.

To generate a key:

```bash
ansible-playbook generate_keys.yml -e service='<service-name>'
```

#### Implemented services

- `headscale_api`: Headscale API
- `headscale_pak`: Headscale preauthkey
- `authelia`: Authelia hash pair for OIDC

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
