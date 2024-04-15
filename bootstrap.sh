#!/usr/bin/env sh
#
# Get uv and install a prefix with ansible on it

yay -S --needed --noconfirm uv rbw expect
git clone /repos/littlelab.git && cd littlelab
uv venv .ansible_venv && source .ansible_venv/bin/activate
uv pip install requirements.txt
