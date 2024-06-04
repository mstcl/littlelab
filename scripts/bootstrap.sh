#!/usr/bin/env sh
#
# Get uv and install a prefix with ansible on it
# This is for setting up a remote controller

yay -S --needed --noconfirm uv rbw expect
git clone /repos/littlelab.git && cd littlelab
uv venv .ansible_venv && source .ansible_venv/bin/activate
uv pip install -r requirements.txt
