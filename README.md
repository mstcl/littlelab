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
