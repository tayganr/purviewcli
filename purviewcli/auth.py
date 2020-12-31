import os
import configparser
import json
import requests

API_VERSION = '2019-11-01-preview'

def get_token(config):
    endpoint = 'https://login.microsoftonline.com/{0}/oauth2/token'.format(config['service_principal']['tenant_id'])
    payload = {
        'grant_type': 'client_credentials',
        'client_id': config['service_principal']['client_id'],
        'client_secret': config['service_principal']['client_secret'],
        'resource': '73c2949e-da2d-457a-9607-fcc665198967'
    }
    response = requests.post(endpoint, data=payload)
    data = json.loads(response.content)
    token = data['access_token']
    return token

def is_token_valid(config):
    endpoint = 'https://purview-sandbox.purview.azure.com?api-version={0}'.format(API_VERSION)
    headers = {"Authorization": "Bearer {0}".format(config['service_principal']['access_token'])}
    response = requests.get(endpoint, headers=headers)
    return True if response.status_code == 200 else False

def set_token():
    # Read config.ini
    config = configparser.ConfigParser()
    config_filepath = os.path.dirname(os.path.abspath(__file__)) + '/../config.ini'
    config.read(config_filepath)

    # Refresh access token
    if not config.has_option('service_principal', 'access_token'):
        token = get_token(config)
        config.set('service_principal', 'access_token', token)
        with open(config_filepath, 'w') as configfile:
            config.write(configfile)
    else:
        if is_token_valid(config) == False:
            config['service_principal']['access_token'] = get_token(config)
            with open(config_filepath, 'w') as configfile:    # save
                config.write(configfile)

