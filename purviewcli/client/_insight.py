from .client import get_data

# ---------------------------
# INSIGHT (GUARDIAN)
# ---------------------------
def insightAssetDistributionByDataSource(args):
    endpoint = '/mapanddiscover/reports/asset2/assetDistributionByDataSource'
    payload = {
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "classificationCategory": args['--classificationCategory'] or '',
        "classificationName": args['--classificationName'] or ''
    }
    http_dict = {'app': 'guardian', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def insightAssetDistributionByTopPaths(args):
    endpoint = '/mapanddiscover/reports/asset2/assetDistributionByTopPaths'
    payload = {
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "classificationCategory": args['--classificationCategory'] or '',
        "classificationName": args['--classificationName'] or '',
        "dataSource": args['--datasource'] or ''
    }
    http_dict = {'app': 'guardian', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def insightFileTypeSizeTimeSeries(args):
    endpoint = '/mapanddiscover/reports/asset2/fileTypeSizeTimeSeries'
    payload = {
        "dataSource": args['--datasource'] or '',
        "fileType": args['--fileType'] or '',
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "window": args['--window'] or ''
    }
    http_dict = {'app': 'guardian', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def insightFileTypeSizeTrendByDataSource(args):
    endpoint = '/mapanddiscover/reports/asset2/fileTypeSizeTrendByDataSource'
    payload = {
        "dataSource": args['--datasource'] or '',
        "fileType": args['--fileType'] or '',
        "registeredSourceGroup": args['--registeredSourceGroup'] or '',
        "window": args['--window'] or ''
    }
    http_dict = {'app': 'guardian', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def insightTopFileTypesBySize(args):
    endpoint = '/mapanddiscover/reports/asset2/topFileTypesBySize'
    payload = {
        "dataSource": args['--datasource'] or '',
        "registeredSourceGroup": args['--registeredSourceGroup'] or ''
    }
    http_dict = {'app': 'guardian', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def insightTopLevelSummary(args):
    endpoint = '/mapanddiscover/reports/asset2/topLevelSummary'
    payload = {
        "registeredSourceGroup": args['--registeredSourceGroup'] or ''
    }
    http_dict = {'app': 'guardian', 'method': 'POST', 'endpoint': endpoint, 'params': None, 'payload': payload}
    data = get_data(http_dict)
    return data

def insightRegisteredSourceGroupsWithAssets(args):
    endpoint = '/mapanddiscover/reports/asset2/registeredSourceGroupsWithAssets'
    http_dict = {'app': 'guardian', 'method': 'GET', 'endpoint': endpoint, 'params': None, 'payload': None}
    data = get_data(http_dict)
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
