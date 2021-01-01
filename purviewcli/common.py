import sys
import os
import configparser
import json
import requests
from datetime import datetime
from pandas import json_normalize

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
        sys.exit("[ERROR] Configuration file needs to be initialised. Run 'purviewcli config'.")
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
    output_path = input('Enter your Output Path: ')
    config.add_section('purview_account')
    config.set('purview_account', 'account_name', account_name)
    config.add_section('output')
    config.set('output', 'output_path', output_path)

    # Write config
    with open(CONFIG_FILEPATH, 'w') as configfile:
        config.write(configfile)

def http_get_catalog(endpoint, params, config):
    base_uri = 'https://%s.catalog.purview.azure.com' % config['purview_account']['account_name']
    headers = {"Authorization": "Bearer {0}".format(config['service_principal']['access_token'])}
    response = requests.get(base_uri + endpoint, params=params, headers=headers)
    
    # Refresh access token and retry if HTTP status is unauthorised
    if response.status_code == 401:
        tenant_id = config['service_principal']['tenant_id']
        client_id = config['service_principal']['client_id']
        client_secret = config['service_principal']['client_secret']
        token = get_token(tenant_id, client_id, client_secret)
        headers = {"Authorization": "Bearer %s" % token}
        response = requests.get(base_uri + endpoint, params=params, headers=headers)

    data = response.content
    return data

def export_data(data, interface, fileformat, config):
    output_path = config['output']['output_path']
    if not os.path.exists(output_path):
        sys.exit("[ERROR] Output path: '%s' does not exist." % output_path)
    timestamp = datetime.today().strftime('%Y%m%d%H%M%S')
    filename = '{0}_{1}.{2}'.format(interface,timestamp,fileformat)
    file_path = '%s/%s' % (output_path, filename)
    
    data_object = json.loads(data)
    if fileformat == 'json':
        with open(file_path, 'w') as outfile:
            json.dump(data_object, outfile, indent=4)
        print('[INFO] Successfully exported to: %s' % file_path)
    elif fileformat == 'csv':
        df = json_normalize(data_object)
        df.to_csv(file_path, sep=',', encoding='utf-8', index=False)
        print('[INFO] Successfully exported to: %s' % file_path)
    else:
        print(data_object) if len(data_object) > 0 else print('No data found for %s.' % (interface))

def selected_arg(args, arg_list):
    selection = None
    for item in  arg_list:
        if args[item]:
            selection = item
    return selection
