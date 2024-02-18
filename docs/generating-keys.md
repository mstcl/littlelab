# Generating keys

The playbook `generate_keys.yml` can help with this.

To generate a key:

```sh
$ ansible-playbook generate_keys.yml -e service='<service-name>'
```

## Implemented services

- `headscale_api`: Headscale API
- `headscale_pak`: Headscale preauthkey
- `authelia`: Authelia hash pair for OIDC
