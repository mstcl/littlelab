# Introduction

LittleLab aims to automate deploying self-hosted services, powered by Ansible
and Docker.

**Why not just Docker compose?**

Because it is not enough. It has a very basic secrets functionality, you can't
do things like add users on the host with it, it's not going to automate your
backups, and it can't help if your file structure is really poorly organized.

Ansible will force a more organized structure, but doesn't lock you into it.
This is exactly why it's so useful; you can use variables to easily replace
where you want stuff to be. Of course, it also automates, so saving you a
a lot of time as well.
