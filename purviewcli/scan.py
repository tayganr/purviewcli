from purviewcli.common import http_get

def getDatasources(config, args):
    endpoint = '/datasources'
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def getDatasource(config, args):
    endpoint = '/datasources/%s' % args['--datasource']
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def getScans(config, args):
    endpoint = '/datasources/%s/scans' % args['--datasource']
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def getScan(config, args):
    endpoint = '/datasources/%s/scans/%s' % (args['--datasource'], args['--scanName'])
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def getScanHistory(config, args):
    endpoint = '/datasources/%s/scans/%s/listHistory' % (args['--datasource'], args['--scanName'])
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def getScanFilters(config, args):
    endpoint = '/datasources/%s/scans/%s/filters' % (args['--datasource'], args['--scanName'])
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def runScan(config, args):
    endpoint = '/datasources/%s/scans/%s/run' % (args['--datasource'], args['--scanName'])

    if args['--scanLevel']:
        payload = {'scanLevel': args['--scanLevel']}
    else:
        payload = None
    
    data = http_get('scan', 'POST', endpoint, None, payload, config)
    return data

def getScanRulesets(config, args):
    endpoint = '/scanrulesets'
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def getSystemScanRulesets(config, args):
    endpoint = '/systemScanRulesets'
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data

def getSystemScanRulesetsSettings(config, args):
    endpoint = '/systemScanRulesets/settings'
    data = http_get('scan', 'GET', endpoint, None, None, config)
    return data
