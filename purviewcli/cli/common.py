import sys
import os
import configparser
import json
import requests

CONFIG_FILEPATH = os.path.dirname(os.path.abspath(__file__)) + '/../config.ini'

def get_token(tenant_id, client_id, client_secret):
    endpoint = 'https://login.microsoftonline.com/{0}/oauth2/token'.format(tenant_id)
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': '73c2949e-da2d-457a-9607-fcc665198967'
    }
    response = requests.post(endpoint, data=payload)
    if response.status_code != 200:
        sys.exit("[ERROR] Status Code: %s. Reason: %s." % (response.status_code, response.reason))
    data = json.loads(response.content)
    token = data['access_token']
    return token

def read_config():
    if not os.path.exists(CONFIG_FILEPATH):
        sys.exit("[ERROR] Configuration file needs to be initialised. Run 'pv config'.")
    config = configparser.ConfigParser()
    config.read(CONFIG_FILEPATH)
    return config

def init_config():
    # Configure (service_principal)
    client_id = input('Enter your Client ID: ')
    client_secret = input('Enter your Client Secret: ')
    tenant_id = input('Enter your Tenant ID: ')
    config = configparser.ConfigParser()
    config.add_section('service_principal')
    config.set('service_principal', 'client_id', client_id)
    config.set('service_principal', 'client_secret', client_secret)
    config.set('service_principal', 'tenant_id', tenant_id)
    config.set('service_principal', 'access_token', get_token(tenant_id, client_id, client_secret))

    # Configure (other)
    account_name = input('Enter your Account Name: ')
    config.add_section('purview_account')
    config.set('purview_account', 'account_name', account_name)

    # Write config
    with open(CONFIG_FILEPATH, 'w') as configfile:
        config.write(configfile)
    
    print('[INFO] You have successfully configured purviewcli.')

def http_get(app, method, endpoint, params, payload, config):
    # Endpoint
    base_uri = 'https://%s.%s.purview.azure.com' % (config['purview_account']['account_name'], app)
    uri = base_uri + endpoint

    # HTTP Header (with existing token)
    headers = {"Authorization": "Bearer {0}".format(config['service_principal']['access_token'])}

    # HTTP Attempt #1
    if method == 'GET':
        response = requests.get(uri, params=params, headers=headers)
    elif method == 'POST':
        response = requests.post(uri, params=params, json=payload, headers=headers)
    else:
        pass
    
    # HTTP Attempt #2
    if response.status_code == 401:
        tenant_id = config['service_principal']['tenant_id']
        client_id = config['service_principal']['client_id']
        client_secret = config['service_principal']['client_secret']
        token = get_token(tenant_id, client_id, client_secret)
        headers = {"Authorization": "Bearer %s" % token}
        if method == 'GET':
            response = requests.get(uri, params=params, headers=headers)
        elif method == 'POST':
            response = requests.post(uri, params=params, json=payload, headers=headers)
        else:
            pass

    data = json.loads(response.content)
    return data

def selected_arg(args, arg_list):
    selection = None
    for item in  arg_list:
        if args[item]:
            selection = item
    return selection
