import os
import configparser
import json
import requests
from datetime import datetime
from pandas import json_normalize

def update_config(args):
    config = configparser.ConfigParser()
    config_filepath = os.path.dirname(os.path.abspath(__file__)) + '/../config.ini'
    
    if os.path.exists(config_filepath):
        config.read(config_filepath)

    if args['--clientId']:
        if 'service_principal' in config:
            config.set('service_principal','client_id',args['--clientId'])
        else:
            config.add_section('service_principal')
            config.set('service_principal','client_id',args['--clientId'])

    if args['--clientName']:
        if 'service_principal' in config:
            config.set('service_principal','client_name',args['--clientName'])
        else:
            config.add_section('service_principal')
            config.set('service_principal','client_name',args['--clientName'])

    if args['--clientSecret']:
        if 'service_principal' in config:
            config.set('service_principal','client_secret',args['--clientSecret'])
        else:
            config.add_section('service_principal')
            config.set('service_principal','client_secret',args['--clientSecret'])

    if args['--tenantId']:
        if 'service_principal' in config:
            config.set('service_principal','tenant_id',args['--tenantId'])
        else:
            config.add_section('service_principal')
            config.set('service_principal','tenant_id',args['--tenantId'])

    if args['--accountName']:
        if 'purview_account' in config:
            config.set('purview_account','account_name',args['--accountName'])
        else:
            config.add_section('purview_account')
            config.set('purview_account','account_name',args['--accountName'])


    with open(config_filepath, 'w') as configfile:
        config.write(configfile)

def http_get_catalog(endpoint, params, config):
    base_uri = 'https://%s.catalog.purview.azure.com' % config['purview_account']['account_name']
    headers = {"Authorization": "Bearer {0}".format(config['service_principal']['access_token'])}
    response = requests.get(base_uri + endpoint, params=params, headers=headers)
    print(response.url)
    data = response.content
    return data

def export_data(data, interface, fileformat):
    output_path = os.path.dirname(os.path.abspath(__file__)) + '/../output'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    timestamp = datetime.today().strftime('%Y%m%d%H%M%S')
    filename = '{0}_{1}.{2}'.format(interface,timestamp,fileformat)
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/../output/{0}'.format(filename)
    
    data_object = json.loads(data)
    if fileformat == 'json':
        with open(file_path, 'w') as outfile:
            json.dump(data_object, outfile, indent=4)
    elif fileformat == 'csv':
        df = json_normalize(data_object)
        df.to_csv(file_path, sep=',', encoding='utf-8', index=False)
    else:
        print(data_object) if len(data_object) > 0 else print('No data found for %s.' % (interface))

def selected_arg(args, arg_list):
    selection = None
    for item in  arg_list:
        if args[item]:
            selection = item
    return selection
