# setup-sshd

## Usage

This role **configures sshd** to be more hardened through the following changes:

- Use the new protocol 2
- Ignore .rhosts and .shosts
- Disallow
  - Users to change environment variables
  - Root login
  - Port/agent/x11 forwarding
  - Accounts with empty passwords
  - Host-based authentication
- New limits
  - Max authentication attempts: 3
  - Max sessions: 6
  - Max login sessions: 4
  - Login timeout: 60s
- Added preferences for more secure ciphers, hash algorithms and MACs.
- Changed port to specified alternative port
- Changed logging to verbose, so key fingerprints of logins are recorded.
- Logging SFTP filesystem access
- Removed short ssh moduli.
- Added 2FA to non key-based authentication attempts (with
  libpam-google-authenticator).

## Variables

N/A

## Examples

```yml
- name: Configure and harden sshd
  hosts: all

  roles:
    - role: setup_sshd
```
