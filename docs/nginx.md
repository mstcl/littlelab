# nginx

## Usage

This role **configures a service to use NGINX**.

## Variables

- `nginx_flavour` (string): indicate the NGINX instance/container name we wish to use for
  a certain service.
- `config` (list): lists all the server configurations to template into the
  `/etc/nginx/conf.d`. These templates should be found at
  `roles/nginx/templates/<service>.conf.j2`.
- `mounts` (list): Append bind mounts to the compose file found at
  `files/<nginx-flavour>/templates/docker-compose.yml.2`.

## Example

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

We also bind mount the socket as `/host/socket:/remote/socket`.
