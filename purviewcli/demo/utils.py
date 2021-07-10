import sys, requests
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import ClientAuthenticationError

class Utils():
    def get_token(app):
        credential = DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True,
            exclude_shared_token_cache_credential=True
        )

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
        return token.token

    def http_get(method, endpoint, params, payload, access_token):
        headers = {"Authorization": "Bearer {0}".format(access_token)}

        try:
            response = requests.request(method, endpoint, params=params, json=payload, headers=headers)
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