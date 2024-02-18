# Updating container images

LittleLab is designed to work with [Renovate](https://docs.renovatebot.com/).
This means container repository written inside Ansible files in the format
`image: repo/name:tag` will be picked up by Renovate.

One can set up Renovate with MEND and point it to LittleLab. It will make pull
requests when it detects an update. This is another reason why it is good to
pin container versions, if possible.

## Manual updates

If needed, the playbook `update_container.yml`  can help with this. It will
prompt for an image repo name.

Rerun the playbooks for this particular image with the tag `docker` to put the
containers back up again.

Example:

```sh
$ ansible-playbook update_container.yml
#STDOUT: Enter the repository name
#STDIN: authelia/authelia:latest
# [...]

$ ansible-playbook playbooks/authelia.yml --tags=docker
```
