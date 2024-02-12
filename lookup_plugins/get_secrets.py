from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

HAS_INFISICAL = False
try:
    from infisical_client import InfisicalClient, ClientSettings, GetSecretOptions

    HAS_INFISICAL = True
except ImportError:
    HAS_INFISICAL = False

DOCUMENTATION = r"""
name: get_secrets
author:
  - lckdscl
  - Infisical Inc.

short_description: Look up secrets stored in Infisical
description:
  - Retrieve secrets from Infisical, granted the caller has the right
    permissions to access the secret.

options:
  client_id:
    description: The Infisical client ID
    env:
      - name: INFISICAL_CLIENT_ID
    required: True
    type: string
    version_added: 1.0.0
  client_secret:
    description: The Infisical client secret
    env:
      - name: INFISICAL_CLIENT_SECRET
    required: True
    type: string
    version_added: 1.0.0
  url:
    description: Point to your self hosted instance of Infisical
    default: "https://app.infisical.com"
    env:
      - name: INFISICAL_URL
    required: False
    type: string
    version_added: 1.0.0
  project_id:
    description: The project ID of the secret you want to access
    required: True
    env:
      - name: INFISICAL_PROJECT_ID
    type: string
    version_added: 1.0.0
  path:
    description: "The folder path where the requested secret resides. For example: /services/backend"
    required: True
    type: string
    version_added: 1.0.0
  env_slug:
    description: "Used to select from which environment (environment slug) secrets should be fetched from. Environment slug is the short name of a given environment"
    required: False
    default: "prod"
    type: string
    version_added: 1.0.0
  secret_name:
    description: "The name of the secret(s) that should be fetched. The name
    should be exactly as it appears in Infisical"
    required: False
    type: string
    version_added: 1.0.0
  secret_type:
    description: "The type of secret (personal or shared). Defaults to shared."
    default: "shared"
    required: False
    type: string
    version_added: 1.0.0
"""

EXAMPLES = r"""
vars:
  read_secret_by_name_within_scope: "{{ lookup('infisical_vault', token='<>', path='/', env_slug='dev', secret_name='HOST', url='https://spotify.infisical.com') }}"
  # [{ "key": "HOST", "value": "google.com" }]
"""


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        self.set_options(var_options=variables, direct=kwargs)

        if not HAS_INFISICAL:
            raise AnsibleError(
                "Please pip install infisical to use the infisical_vault lookup module."
            )

        client_id = self.get_option("client_id")
        client_secret = self.get_option("client_secret")
        project_id = self.get_option("project_id")
        url = self.get_option("url")
        env_slug = self.get_option("env_slug")
        secret_type = self.get_option("secret_type")
        secret_name = self.get_option("secret_name")
        path = self.get_option("path")

        # Initialize the Infisical client
        client_settings = ClientSettings(
            client_id=client_id, client_secret=client_secret, site_url=url
        )
        client = InfisicalClient(client_settings)

        return self.get_single_secret(
            client, secret_name, project_id, env_slug, path, secret_type
        )

    def get_single_secret(
        self, client, secret_name, project_id, environment, path, secret_type
    ):
        try:
            secret = client.getSecret(
                options=GetSecretOptions(
                    environment=environment,
                    project_id=project_id,
                    secret_name=secret_name,
                    path=path,
                    type=secret_type,
                )
            )
            return [secret.secret_value]
        except Exception as e:
            print(e)
            raise AnsibleError(f"Error fetching single secret {e}")
