# setup_nginx

## Usage

This role **configures an NGINX instance**.

## Variables

- `nginx_config_override` (string): path to file to replace the default `nginx.conf`.

## Example

```yml
- name: Install nginx
  roles:
    - role: nginx
      vars:
        nginx_config_override: "custom_nginx.conf"
```

The configuration override like the file `custom_nginx.conf` above should be
placed into `roles/nginx/files`
