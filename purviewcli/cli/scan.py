"""
usage: 
    pv scan cancelScan --dataSourceName=<val> --scanName=<val> --runId=<val>
    pv scan deleteClassificationRule --classificationRuleName=<val>
    pv scan deleteDataSource --dataSourceName=<val>
    pv scan deleteKeyVault --keyVaultName=<val>
    pv scan deleteScan --dataSourceName=<val> --scanName=<val>
    pv scan deleteScanRuleset --scanRulesetName=<val>
    pv scan deleteTrigger --dataSourceName=<val> --scanName=<val>
    pv scan putClassificationRule --classificationRuleName=<val> --payloadFile=<val>
    pv scan putDataSource --dataSourceName=<val> --payloadFile=<val>
    pv scan putFilter --dataSourceName=<val> --scanName=<val> --payloadFile=<val>
    pv scan putKeyVault --keyVaultName=<val> --payloadFile=<val>
    pv scan putScan --dataSourceName=<val> --scanName=<val> --payloadFile=<val>
    pv scan putScanRuleset --scanRulesetName=<val> --payloadFile=<val>
    pv scan putTrigger --dataSourceName=<val> --scanName=<val> --payloadFile=<val>
    pv scan readClassificationRule --classificationRuleName=<val>
    pv scan readClassificationRuleVersions --classificationRuleName=<val>
    pv scan readClassificationRules
    pv scan readDataSource --dataSourceName=<val>
    pv scan readDataSources [--collectionName=<val>]
    pv scan readFilters --dataSourceName=<val> --scanName=<val>
    pv scan readKeyVault --keyVaultName=<val>
    pv scan readKeyVaults
    pv scan readScan --dataSourceName=<val> --scanName=<val>
    pv scan readScanHistory --dataSourceName=<val> --scanName=<val>
    pv scan readScanRuleset --scanRulesetName=<val>
    pv scan readScanRulesets
    pv scan readScans --dataSourceName=<val>
    pv scan readSystemScanRuleset --dataSourceType=<val>
    pv scan readSystemScanRulesetLatest --dataSourceType=<val>
    pv scan readSystemScanRulesetVersion --version=<val> --dataSourceType=<val>
    pv scan readSystemScanRulesetVersions --dataSourceType=<val>
    pv scan readSystemScanRulesets
    pv scan readTrigger --dataSourceName=<val> --scanName=<val>
    pv scan runScan --dataSourceName=<val> --scanName=<val> [--scanLevel=<val>]
    pv scan tagClassificationVersion --classificationRuleName=<val> --classificationRuleVersion=<val> --action=<val>
    pv scan deleteCredential --credentialName=<val>
    pv scan putCredential --credentialName=<val> --payloadFile=<val>
    pv scan readCredential [--credentialName=<val>]

options:
    --purviewName=<val>                 [string]  Azure Purview account name.
    --action=<val>                      [string] Allowed values: Delete or Keep.
    --classificationRuleName=<val>      [string]  Name of the classification rule.
    --classificationRuleVersion=<val>   [integer] Version of the classification rule.    
    --dataSourceName=<val>              [string]  Name of the data source.
    --scanName=<val>                    [string]  Name of the scan.
    --scanRulesetName=<val>             [string]  Name of the scan ruleset.
    --keyVaultName=<val>                [string]  Name of the key vault.
    --runId=<val>                       [string]  The unique identifier of the run.
    --dataSourceType=<val>              [string]  Type of data source.
    --scanLevel=<val>                   [string]  Allowed values: Full or Incremental [default: Full].
    --collectionName=<val>              [string]  The unique collection name.
    --credentialName=<val>              [string]  The name of the credential.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
