import sys
import requests
import os
from azure.identity import DefaultAzureCredential, AzureCliCredential
from azure.core.exceptions import ClientAuthenticationError

mapAppToResource = {
    'management': 'https://management.azure.com/.default',
    'graph': 'https://graph.microsoft.com/.default',
    'purview': 'https://purview.azure.net/.default'
}


def get_token(app):
    # credential = DefaultAzureCredential(
    #     exclude_environment_credential=True,
    #     exclude_managed_identity_credential=True,
    #     exclude_shared_token_cache_credential=True
    # )
    credential = AzureCliCredential()
    token = None
    resource = mapAppToResource[app]

    try:
        token = credential.get_token(f'{resource}').token
    except ClientAuthenticationError as e:
        print(e)

    return token


def http_get(method, endpoint, params, payload, access_token):
    headers = {"Authorization": "Bearer {0}".format(access_token)}

    try:
        response = requests.request(
            method, endpoint, params=params, json=payload, headers=headers)
    except requests.exceptions.HTTPError as errh:
        print("[HTTP ERROR]", errh)
    except requests.exceptions.ConnectionError as errc:
        print("[CONNECTION ERROR]", errc)
        sys.exit()
    except requests.exceptions.Timeout as errt:
        print("[TIMEOUT ERROR]", errt)
    except requests.exceptions.RequestException as err:
        print("[REQUEST EXCEPTION]", err)

    status_code = response.status_code
    if status_code == 204:
        data = {
            'operation': '[%s] %s' % (method, response.url),
            'status': 'The server successfully processed the request',
            'status_code': status_code
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
