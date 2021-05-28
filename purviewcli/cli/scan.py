"""
usage: 
    pv scan readClassificationRules
    pv scan readClassificationRule --classificationRuleName=<val>
    pv scan readClassificationRuleVersions --classificationRuleName=<val>
    pv scan readDatasources
    pv scan readDatasource --dataSourceName=<val>
    pv scan readScans --dataSourceName=<val>
    pv scan readScan --dataSourceName=<val> --scanName=<val>
    pv scan readScanHistory --dataSourceName=<val> --scanName=<val>
    pv scan readFilters --dataSourceName=<val> --scanName=<val>
    pv scan readTrigger --dataSourceName=<val> --scanName=<val>
    pv scan readScanRulesets
    pv scan readScanRuleset --scanRulesetName=<val>
    pv scan readSystemScanRulesets
    pv scan readSystemScanRuleset --dataSourceType=<val>
    pv scan readSystemScanRulesetVersion --version=<val> --dataSourceType=<val>
    pv scan readSystemScanRulesetLatest --dataSourceType=<val>
    pv scan readSystemScanRulesetVersions --dataSourceType=<val>
    pv scan readKeyVaults
    pv scan readKeyVault --keyVaultName=<val>

options:
    --purviewName=<val>                   Azure Purview account name.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
