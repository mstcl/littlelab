# Using the main playbook

The `main.yml` playbook contains all of tasks needed to **reproduce** the entire
homelab. It shouldn't be run before all of the services you want to run have
been configured to your liking. It acts as instructions to recreate the desired
state of the lab. To be rerun if a part or all of the lab needs to be redone.

It starts out mostly all commented. As you work through it, uncomment each
playbook if you know it does what you want.

After adding your own `host_vars` and `group_vars`, go ahead and run
`main.yml`. This will only run two setup playbooks to setup the control node to
install several dependencies and make some symlinks, as well as to setup the
remote node(s), which will also install dependencies and prepare Docker, Cronie
and UFW.
