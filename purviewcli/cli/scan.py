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
    pv scan deleteClassificationRule --classificationRuleName=<val>
    pv scan deleteDataSource --dataSourceName=<val>
    pv scan deleteKeyVault --keyVaultName=<val>
    pv scan deleteScanRuleset --scanRulesetName=<val>
    pv scan deleteScan --dataSourceName=<val> --scanName=<val>
    pv scan deleteTrigger --dataSourceName=<val> --scanName=<val>
    pv scan putDataSource --dataSourceName=<val> --payload-file=<val>
    pv scan putScan --dataSourceName=<val> --scanName=<val> --payload-file=<val>
    pv scan putFilter --dataSourceName=<val> --scanName=<val> --payload-file=<val>
    pv scan putTrigger --dataSourceName=<val> --scanName=<val> --payload-file=<val>
    pv scan runScan --dataSourceName=<val> --scanName=<val>
    pv scan cancelScan --dataSourceName=<val> --scanName=<val> --runId=<val>
    pv scan putClassificationRule --classificationRuleName=<val> --payload-file=<val>
    pv scan putKeyVault --keyVaultName=<val> --payload-file=<val>
    pv scan putScanRuleset --scanRulesetName=<val> --payload-file=<val>

options:
    --purviewName=<val>                 [string]  Azure Purview account name.
    --classificationRuleName=<val>      [string]  Name of the classification rule.
    --dataSourceName=<val>              [string]  Name of the data source.
    --scanName=<val>                    [string]  Name of the scan.
    --scanRulesetName=<val>             [string]  Name of the scan ruleset.
    --keyVaultName=<val>                [string]  Name of the key vault.
    --runId=<val>                       [string]  The unique identifier of the run.
    --dataSourceType=<val>              [string]  Type of data source.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
