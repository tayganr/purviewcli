import os
import json
import requests
from datetime import datetime
from pandas import json_normalize

def http_get(endpoint, params, config):
    base_uri = config['purview_account']['atlas_endpoint']
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
