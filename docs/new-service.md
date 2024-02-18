# Creating new services

To create a service playbook and a template docker compose file on the control
node:

```sh
$ ansible-playbook create_service.yml
```

It will prompt for a service name, and create a playbook
`playbooks/<service_name>.yml` and basic docker compose file under
`files/<service_name>/templates/docker-compose.yml`.

If the service does not require a docker compose file, run instead:

```sh
$ ansible-playbook create_service.yml -e use_docker=false
```
