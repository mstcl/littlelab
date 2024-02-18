# NGINX

Located in `roles/nginx`.

## Configuring an NGINX instance

When called _without_ `configs` or `mounts`, the role configures an NGINX
instance (that is, making default hardened `nginx.conf` and various files and
directories). We can also specify `nginx_config_override` to replace the
default `nginx.conf`.

Example:

```yml
- name: Install nginx
  roles:
    - role: nginx
      vars:
        nginx_config_override: "custom_nginx.conf"
```

The configuration override like the file `custom_nginx.conf` above would be
found at `roles/nginx/files/custom_nginx.conf`

## Configuring a service to use NGINX

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

```yml
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
