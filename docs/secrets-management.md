# Secrets management

There are a variety of services that can be used to manage secrets: Hashicorp
Vault, Ansible Vault, Bitwarden Secrets Manager *etc*.

Of course, you can also write the secrets in directly, that is also an option.

LittleLab uses [Infisical](https://infisical.com/), which is open-source and
comes with a very generous free-tier (and also can be self-hosted). Any can be
used, as long as there are APIs/SDKs or existing collections/lookup plugins to
fetch the secrets.

The lookup plugin for Infisical can be found in `lookup_plugins/get_secrets.py`.

Since we inject secrets during playbook execution using the template module,
secrets are not injected into LittleLab, but only in files sent to the managed
nodes.

## Docker secrets

There is minimal difference between using Docker secrets and writing it
directly into variables. If the attacker has access to the container, the secrets
is simply mounted to `/run/secrets` as a file, which can be displayed in plain
text. If the attacker has access to the host, they can do that and much more.
