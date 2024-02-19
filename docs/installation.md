# Installation

## Ansible

You're going to need Ansible on your own machine. Don't install it on the
server.

See [the official
docs](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#control-node-requirements)
on how to install it.

On Arch, this is:

```sh
$ pacman -S ansible
```

## LittleLab

Clone the repository:

```sh
$ git clone https://github.com/mstcl/littlelab
```

### Ignore tracked files that will be modified

Variable files in `vars/`, the `main.yml` playbook, and some roles' default
variable files are used to customize configuration. They are tracked by
default, but we can ignore it locally to prevent it from showing up in git
status.

For this, we can use `.git/info/exclude`, which can contain something like:

```
vars/*.yml
roles/cron/defaults/main.yml
main.yml
```

To apply the changes:

```sh
$ git update-index --assume-unchanged vars/*.yml main.yml roles/cron/defaults/main.yml
```

This also applies to Jinja templates (under the scope `**templates/*.j2`), as
they might not be flexible enough for all use cases.
