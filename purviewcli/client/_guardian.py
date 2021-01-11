def getAssetDistributionByDataSource(self, args):
    endpoint = '/mapanddiscover/reports/asset2/assetDistributionByDataSource'
    payload = {
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "classificationCategory": args['--classificationCategory'] or '',
        "classificationName": args['--classificationName'] or ''
    }
    data = self.http_get(app='guardian', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getAssetDistributionByTopPaths(self, args):
    endpoint = '/mapanddiscover/reports/asset2/assetDistributionByTopPaths'
    payload = {
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "classificationCategory": args['--classificationCategory'] or '',
        "classificationName": args['--classificationName'] or '',
        "dataSource": args['--datasource'] or ''
    }
    data = self.http_get(app='guardian', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getFileTypeSizeTimeSeries(self, args):
    endpoint = '/mapanddiscover/reports/asset2/fileTypeSizeTimeSeries'
    payload = {
        "dataSource": args['--datasource'] or '',
        "fileType": args['--fileType'] or '',
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "window": args['--window'] or ''
    }
    data = self.http_get(app='guardian', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getFileTypeSizeTrendByDataSource(self, args):
    endpoint = '/mapanddiscover/reports/asset2/fileTypeSizeTrendByDataSource'
    payload = {
        "dataSource": args['--datasource'] or '',
        "fileType": args['--fileType'] or '',
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "window": args['--window'] or ''
    }
    data = self.http_get(app='guardian', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getTopFileTypesBySize(self, args):
    endpoint = '/mapanddiscover/reports/asset2/topFileTypesBySize'
    payload = {
        "dataSource": args['--datasource'] or '',
        "registeredSourceGroup": args['--registeredSourceGroup'] or ''
    }
    data = self.http_get(app='guardian', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getTopLevelSummary(self, args):
    endpoint = '/mapanddiscover/reports/asset2/topLevelSummary'
    payload = {
        "registeredSourceGroup": args['--registeredSourceGroup'] or ''
    }
    data = self.http_get(app='guardian', method='POST', endpoint=endpoint, params=None, payload=payload)
    return data

def getRegisteredSourceGroupsWithAssets(self, args):
    endpoint = '/mapanddiscover/reports/asset2/registeredSourceGroupsWithAssets'
    data = self.http_get(app='guardian', method='GET', endpoint=endpoint, params=None, payload=None)
    return data

# Map & Discover > Reports > Asset2
# [POST] /mapanddiscover/reports/asset2/assetDistributionByDataSource
# [POST] /mapanddiscover/reports/asset2/assetDistributionByTopPaths
# [GET]  /mapanddiscover/reports/asset2/registeredSourceGroupsWithAssets
# [POST] /mapanddiscover/reports/asset2/fileTypeSizeTimeSeries
# [POST] /mapanddiscover/reports/asset2/fileTypeSizeTrendByDataSource
# [POST] /mapanddiscover/reports/asset2/filesWithoutResourceSetByDataSource
# [POST] /mapanddiscover/reports/asset2/topFileTypesBySize
# [POST] /mapanddiscover/reports/asset2/topLevelSummary

# Map & Discover > Reports > Scan Status
# [POST] /mapanddiscover/reports/scanstatus/summary
# [POST] /mapanddiscover/reports/scanstatus/summarybytimeseries

# Map & Discover > Reports > Glossary
# [POST] /mapanddiscover/reports/user/latesttopnroles
# [POST] /mapanddiscover/reports/glossary/latesttopnterms
# [POST] /mapanddiscover/reports/glossary/latestsummarybystatus

# Reports > Classification
# [POST] /reports/classification/calculateFileTotalsOverTime
# [POST] /reports/classification/calculateTableTotalsOverTime

# Reports > (Sensitivity) Labels
# [POST] /reports/label/calculateList
# [POST] /reports/label/calculatePaginatedList

# Reports > File Extensions
# [POST] /reports/fileExtensions

# Classification & Sensitivity Labels
# [POST] /graphql
