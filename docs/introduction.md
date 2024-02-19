# Introduction

LittleLab is a pipeline that can automate the deployment of self-hosted
services. It is powered by Ansible and Docker, you just need to have Ansible
and Python installed on your local machine.

**Why not just Docker compose?**

Because it is not enough. It has a very basic secrets functionality, you can't
do things like add users on the host with it, it's not going to automate your
backups, and it can't help if your file structure is really poorly organized.

Ansible will force a more organized structure, but doesn't lock you into it.
This is exactly why it's so useful; you can use variables to easily replace
where you want stuff to be. Of course, it also automates, so saving you a lot
of time as well.

## Core components

These components are relatively static for now, as they are decently popular
choices:

- **Docker** and **Docker Compose**: Both are appropriate for our use case.
- **Traefik v2** (soon migrating to v3): A flexible reverse-proxy that works well with Docker.
- **NGINX**: for web-hosting and anything that Traefik can't do.
- **Headscale** and **Tailscale**: Both are well-maintained and have good clients.
- **Authelia**: probably the most lightweight and flexible option out there.

That being said, fork it and do whatever you want, Ansible is quite an
opinionated tool and there is no one true way for doing things.

## Roadmap

- Deploy from fresh installation
- Apply hardening practices
- Services
  - Immich
  - Dendrite
  - Netdata
  - Crowdsec
  - OliveTin
  - Gluetun
  - LDAP
- Better docs (one for each service)
  - Add some tips for running each one
- Potentially look at Kubernetes
