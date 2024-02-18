# Creating new users

Some services use an API/CLI to create users. This can be used to further
automate user creation without the hassle of admin panels or docker `exec`.

The playbook `create_user.yml` can help with this.

To make an user:

```sh
$ ansible-playbook create_user.yml --tags='<service-name>' -e variable1='<variable1>' -e variable2='<variable2>' # etc.
```

The variables are specific for each service. Use single quotes on the
variables, especially on the password.

## Authelia

- `username`: the username to login (string).
- `display_name`: the display name that is shown on the login page (string).
- `password`: the password (string).
- `email`: the email that Authelia will use for confirmation of certain things (string).
- `admin`: whether or not the user is in the admin group, true/false/yes/no accepted (boolean).

## Headscale

- `username`: the username to login (string).

## Filebrowser

- `username`: the username to login (string).
- `password`: the password (string).
