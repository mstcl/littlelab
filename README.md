# Homelab ansible repo

## Setting up the nodes

Run the [main](./main.yml) playbook to set up our control and remote nodes.

## Automation

To add a new service playbook and template docker compose file:

```bash
ansible-playbook add_new_control.yml
```

It will prompt you for a service name, and create a playbook
`<service_name>.yml` and basic docker compose file under
`files/<service_name>/templates/docker-compose.yml`

## Inventory

Provided is an [example](./inventory/hosts_example) for our inventory under `inventory/hosts_example`.

## Variables

Provided is an [example](./host_vars/examplebox.yml) for our main box in under `host_vars/examplebox.yml`.
`group_vars` for `[homelab]` is provided as is.

## Playbook notes

### Adguard Home

At the start, we might not have persistent clients. Therefore, we set
`add_persistent_config: false` in the [playbook](./adguard-home.yml). After setting up the clients to
our liking, we can then extract everything under `clients.persistent` from the
overwritten remote configuration to
`files/adguard-home/files/persistent_clients.yml` on the control node. Once
this is done, we can set `add_persistent_config: true`. This file is ignored in
git as it is somewhat sensitive so we must store our own configuration
elsewhere.

The playbook also reads from `vars/adguard-home.yml` to configure user rules,
upstream DNS, fallback DNS and blocklists. See the
[example](./vars/adguard-home_example.yml) provided.

### Authelia

We must bring our own `users.yml`, which should be placed in
`files/authelia/files/users.yml`.

### NGINX

To get NGINX to work, we consider a few things:

* The `nginx` role, if called without `configs` or `mounts`, configures an
NGINX instance (that is, making default hardened `nginx.conf` and various files
and directories).
* To reverse proxy a service, we call the `nginx` roll with with `configs`
and/or `mounts`. This should be called within the service playbooks, not the
corresponding nginx playbooks.
    * The `config` block lists all the server configurations to
template into `conf.d`. These templates should be found at
`roles/nginx/templates/<service>.conf.j2`.
    * The `mount` block will append bind mounts to the compose file found at
    `files/<my-nginx-instance>/templates/docker-compose.yml.2`.
* For example, the `nginx-lemmy` [playbook](./nginx-lemmy.yml) configures an
NGINX container specifically for Lemmy (with a special `nginx.conf` to override
the default one, as the default one is too hardened and breaks federation. Then
inside the `lemmy` [playbook](./lemmy.yml) we call the role `nginx` with a
`config` block to add the NGINX configuration.
