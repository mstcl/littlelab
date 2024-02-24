# Initial setup

## Setup control node

After this, go ahead and run:

```sh
$ ansible-playbook -e "ansible_user=$(whoami)" playbooks/setup_control.yml
```

This is get all the necessary collections, tools and libraries **locally**.

## Setup the managed node

### SSH access for root

On some distribution, the default sshd configuration prohibit password root
login. We have to append our public key ahead in this case.

After setting up root and a strong root password, append your public key to the
`authorized_keys` file:

```sh
$ echo "<public-key>" >> ~/.ssh/authorized_keys
```

Then make sure sshd is running

```sh
$ systemctl enable --now sshd
```

### Running the playbook

After this, go ahead and run:

```sh
$ ansible-playbook -e "ansible_user=root" playbooks/setup_remote.yml
```

This will:

- Prompt for the password of our base user we declared previously in the
  variable file `host_vars/<host_name>.yml`.
- Create all the directories for services later on.
- Create our base user.
- Setup sshd. Refer to the role documentation of [setup_sshd](./setup_sshd) for
  a full description of what it does.
- Setup the firewall with ufw.
- Setup docker
- Setup cronie.

> [!WARNING]
> This playbook expects `ansible_user` to be root. After setting up sshd, root
> access will be prohibited. To run it again, instead of setting
> `ansible_user`, run it with the flag `--become` instead.
