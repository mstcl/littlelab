# Deploying specific services

Services are deployed from playbooks that live under the subdirectory
`playbooks/<service_name>.yml`. This is a bit unorthodox but it keeps the top
directory nice and clean. To deploy a service:

```sh
$ ansible-playbook playbooks/service_name.yml
```
