import sys
import os
import logging
import requests
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ClientAuthenticationError

logging.getLogger("azure.identity").setLevel(logging.ERROR)

class PurviewClient():
    def __init__(self):
        self.access_token = None
        self.account_name = os.environ.get("PURVIEW_NAME")
        if self.account_name is None:
            print("[ERROR] Environment variable PURVIEW_NAME is missing. To set the environment variable, execute the following command: \033[94mexport PURVIEW_NAME=value\033[0m")
            sys.exit()

    def set_token(self):
        credential = DefaultAzureCredential()
        try:
            token = credential.get_token('https://purview.azure.net/.default')
        except ClientAuthenticationError as e:
            print(e)
            print("For more information, check out: https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python")
            sys.exit()
        self.access_token = token.token

    def get_token(self):
        return self.access_token

    def http_get(self, app, method, endpoint, params, payload):
        uri = 'https://%s.%s.purview.azure.com%s' % (self.account_name, app, endpoint)
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

def get_data(http_dict):
    client = PurviewClient()
    client.set_token()
    data = client.http_get(http_dict['app'], http_dict['method'], http_dict['endpoint'], http_dict['params'], http_dict['payload'])
    return data
