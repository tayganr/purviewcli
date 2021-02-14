"""
usage: 
    pv scan read --datasource=<val> --scanName=<val>
    pv scan run --datasource=<val> --scanName=<val> [--scanLevel=<val>]
    pv scan createSource --datasource=<val> --kind=<val> [--accountUri=<val> --subscriptionId=<val> --resourceGroup=<val> --location=<val> --resourceName=<val> --endpoint=<val> --serverEndpoint=<val> --tenant=<val> --parentCollection=<val> --host=<val> --applicationServer=<val> --systemNumber=<val> --clusterUrl=<val> --roleARN=<val> --serviceUrl=<val>]
    pv scan readSource --datasource=<val>
    pv scan deleteSource --datasource=<val>
    pv scan readSources
    pv scan readScans --datasource=<val>
    pv scan readHistory --datasource=<val> --scanName=<val>
    pv scan readFilters --datasource=<val> --scanName=<val>
    pv scan readScanRulesets
    pv scan readSystemScanRulesets
    pv scan readSystemScanRulesetsSettings
    pv scan readClassificationRules
    pv scan readClassificationRule --classificationName=<val>
    pv scan createCollection --collection=<val> [--parentCollection=<val>]
    pv scan deleteCollection --collection=<val>

options:
    --scanLevel=<val>                   Incremental or Full.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
