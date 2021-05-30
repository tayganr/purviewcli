"""
usage: 
    pv insight assetDistributionByDataSource [--registeredSourceGroup=<val> --classificationCategory=<val> --classificationName=<val>]
    pv insight assetDistributionByTopPaths --datasource=<val> [--registeredSourceGroup=<val> --classificationCategory=<val> --classificationName=<val>]
    pv insight fileTypeSizeTimeSeries --fileType=<val> --window=<val> [--registeredSourceGroup=<val> --datasource=<val>]
    pv insight fileTypeSizeTrendByDataSource --fileType=<val> --window=<val> [--registeredSourceGroup=<val> --datasource=<val>]
    pv insight topFileTypesBySize [--registeredSourceGroup=<val> --datasource=<val>]
    pv insight topLevelSummary [--registeredSourceGroup=<val>]
    pv insight registeredSourceGroupsWithAssets

options:
    --purviewName=<val>               Azure Purview account name.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
