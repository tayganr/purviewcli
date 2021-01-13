def getDatasources(self, args):
    endpoint = '/datasources'
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getDatasource(self, args):
    endpoint = '/datasources/%s' % args['--datasource']
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getScans(self, args):
    endpoint = '/datasources/%s/scans' % args['--datasource']
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getScan(self, args):
    endpoint = '/datasources/%s/scans/%s' % (args['--datasource'], args['--scanName'])
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getScanHistory(self, args):
    endpoint = '/datasources/%s/scans/%s/listHistory' % (args['--datasource'], args['--scanName'])
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getScanFilters(self, args):
    endpoint = '/datasources/%s/scans/%s/filters' % (args['--datasource'], args['--scanName'])
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def runScan(self, args):
    endpoint = '/datasources/%s/scans/%s/run' % (args['--datasource'], args['--scanName'])

    if args['--scanLevel']:
        payload = {'scanLevel': args['--scanLevel']}
    else:
        payload = None
    
    data = self.http_get(app='scan', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getScanRulesets(self, args):
    endpoint = '/scanrulesets'
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getSystemScanRulesets(self, args):
    endpoint = '/systemScanRulesets'
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getSystemScanRulesetsSettings(self, args):
    endpoint = '/systemScanRulesets/settings'
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getClassificationRules(self, args):
    endpoint = '/classificationrules'
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

def getClassificationRule(self, args):
    endpoint = '/classificationrules/%s' % args['--classificationName']
    data = self.http_get(app='scan', method='GET', endpoint=endpoint, params=None, payload=None)
    return data
