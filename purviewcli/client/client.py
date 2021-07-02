import jwt
import sys
import os
import logging
import requests
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ClientAuthenticationError
from . import settings

logging.getLogger("azure.identity").setLevel(logging.ERROR)

class PurviewClient():
    def __init__(self):
        self.access_token = None
        self.account_name = None

    def set_account(self, app):
        if app == "management" or app == 'graph':
            self.account_name = None
        else:
            self.account_name = settings.PURVIEW_NAME if settings.PURVIEW_NAME != None else os.environ.get("PURVIEW_NAME")
            if self.account_name is None:
                print("""[ERROR] Environment variable PURVIEW_NAME is missing.

Please configure the PURVIEW_NAME environment variable. Setting environment variables can vary by environment, see examples below.
\tWindows (Command Prompt):\tset PURVIEW_NAME=value
\tmacOS (Terminal):\t\texport PURVIEW_NAME=value
\tPython:\t\t\t\tos.environ["PURVIEW_NAME"] = "value"
\tPowerShell:\t\t\t$env:PURVIEW_NAME = "value"
\tJupyter Notebook:\t\t%env PURVIEW_NAME=value
""")
                sys.exit()

    def set_token(self, app):
        credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)

        if app == "management":
            resource = "https://management.azure.com/.default"
        elif app == 'graph':
            resource = "https://graph.microsoft.com/.default"
        else:
            resource = "https://purview.azure.net/.default"

        try:
            token = credential.get_token(f'{resource}')
        except ClientAuthenticationError as e:
            print(e)
            print("For more information, check out: https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python")
            sys.exit()
        self.access_token = token.token

    def get_token(self):
        return self.access_token

    def http_get(self, app, method, endpoint, params, payload):
        if app == "management":
            uri = f"https://{app}.azure.com{endpoint}"
        elif app == 'graph':
            uri = f"https://{app}.microsoft.com{endpoint}"
        else:
            uri = f"https://{self.account_name}.{app}.purview.azure.com{endpoint}"

        headers = {"Authorization": "Bearer {0}".format(self.access_token)}

        try:
            response = requests.request(method, uri, params=params, json=payload, headers=headers)
        except requests.exceptions.HTTPError as errh:
            print ("[HTTP ERROR]",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("[CONNECTION ERROR]",errc)
            sys.exit()
        except requests.exceptions.Timeout as errt:
            print ("[TIMEOUT ERROR]",errt)
        except requests.exceptions.RequestException as err:
            print ("[REQUEST EXCEPTION]",err)

        status_code = response.status_code
        if status_code == 204:
            data = {
                'operation': '[%s] %s' % (method, response.url),
                'status': 'The server successfully processed the request'
            }
        else:
            try:
                data = response.json()
            except ValueError:
                data = {
                    'url': response.url,
                    'status_code': response.status_code,
                    'reason': response.reason
                }
        return data
