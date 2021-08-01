"""
usage: 
    pv scan cancelScan --dataSourceName=<val> --scanName=<val> --runId=<val>
    pv scan deleteClassificationRule --classificationRuleName=<val>
    pv scan deleteDataSource --dataSourceName=<val>
    pv scan deleteKeyVault --keyVaultName=<val>
    pv scan deleteScan --dataSourceName=<val> --scanName=<val>
    pv scan deleteScanRuleset --scanRulesetName=<val>
    pv scan deleteTrigger --dataSourceName=<val> --scanName=<val>
    pv scan putClassificationRule --classificationRuleName=<val> --payload-file=<val>
    pv scan putDataSource --dataSourceName=<val> --payload-file=<val>
    pv scan putFilter --dataSourceName=<val> --scanName=<val> --payload-file=<val>
    pv scan putKeyVault --keyVaultName=<val> --payload-file=<val>
    pv scan putScan --dataSourceName=<val> --scanName=<val> --payload-file=<val>
    pv scan putScanRuleset --scanRulesetName=<val> --payload-file=<val>
    pv scan putTrigger --dataSourceName=<val> --scanName=<val> --payload-file=<val>
    pv scan readClassificationRule --classificationRuleName=<val>
    pv scan readClassificationRuleVersions --classificationRuleName=<val>
    pv scan readClassificationRules
    pv scan readDatasource --dataSourceName=<val>
    pv scan readDatasources
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
    pv scan runScan --dataSourceName=<val> --scanName=<val>

options:
    --purviewName=<val>                 [string]  Azure Purview account name.
    --classificationRuleName=<val>      [string]  Name of the classification rule.
    --dataSourceName=<val>              [string]  Name of the data source.
    --scanName=<val>                    [string]  Name of the scan.
    --scanRulesetName=<val>             [string]  Name of the scan ruleset.
    --keyVaultName=<val>                [string]  Name of the key vault.
    --runId=<val>                       [string]  The unique identifier of the run.
    --dataSourceType=<val>              [string]  Type of data source.

mapping:
https://{account_name}.scan.purview.azure.com
+--------------------------------+--------+------------------------------------------------------------------------+
| Command                        | Method | Path                                                                   |
+--------------------------------+--------+------------------------------------------------------------------------+
| cancelScan                     | POST   | /datasources/{dataSourceName}/scans/{scanName}/runs/{runId}/:cancel    |
| deleteClassificationRule       | DELETE | /classificationrules/{classificationRuleName}                          |
| deleteDataSource               | DELETE | /datasources/{dataSourceName}                                          |
| deleteKeyVault                 | DELETE | /azureKeyVaults/{keyVaultName}                                         |
| deleteScan                     | DELETE | /datasources/{dataSourceName}/scans/{scanName}                         |
| deleteScanRuleset              | DELETE | /scanrulesets/{scanRulesetName}                                        |
| deleteTrigger                  | DELETE | /datasources/{dataSourceName}/scans/{scanName}/triggers/default        |
| putClassificationRule          | PUT    | /classificationrules/{classificationRuleName}                          |
| putDataSource                  | PUT    | /datasources/{dataSourceName}                                          |
| putFilter                      | PUT    | /datasources/{dataSourceName}/scans/{scanName}/filters/custom          |
| putKeyVault                    | PUT    | /azureKeyVaults/{keyVaultName}                                         |
| putScan                        | PUT    | /datasources/{dataSourceName}/scans/{scanName}                         |
| putScanRuleset                 | PUT    | /scanrulesets/{scanRulesetName}                                        |
| putTrigger                     | PUT    | /datasources/{dataSourceName}/scans/{scanName}/triggers/default        |
| readClassificationRule         | GET    | /classificationrules/{classificationRuleName}                          |
| readClassificationRuleVersions | GET    | /classificationrules/{classificationRuleName}/versions                 |
| readClassificationRules        | GET    | /classificationrules                                                   |
| readDatasource                 | GET    | /datasources/{dataSourceName}                                          |
| readDatasources                | GET    | /datasources                                                           |
| readFilters                    | GET    | /datasources/{dataSourceName}/scans/{scanName}/filters/custom          |
| readKeyVault                   | GET    | /azureKeyVaults/{keyVaultName}                                         |
| readKeyVaults                  | GET    | /azureKeyVaults                                                        |
| readScan                       | GET    | /datasources/{dataSourceName}/scans/{scanName}                         |
| readScanHistory                | GET    | /datasources/{dataSourceName}/scans/{scanName}/runs                    |
| readScanRuleset                | GET    | /scanrulesets/{scanRulesetName}                                        |
| readScanRulesets               | GET    | /scanrulesets                                                          |
| readScans                      | GET    | /datasources/{dataSourceName}/scans                                    |
| readSystemScanRuleset          | GET    | /systemScanRulesets/datasources/{dataSourceType}                       |
| readSystemScanRulesetLatest    | GET    | /systemScanRulesets/versions/latest?dataSourceType={dataSourceType}    |
| readSystemScanRulesetVersion   | GET    | /systemScanRulesets/versions/{version}?dataSourceType={dataSourceType} |
| readSystemScanRulesetVersions  | GET    | /systemScanRulesets/versions?dataSourceType={dataSourceType}           |
| readSystemScanRulesets         | GET    | /systemScanRulesets                                                    |
| readTrigger                    | GET    | /datasources/{dataSourceName}/scans/{scanName}/triggers/default        |
| runScan                        | PUT    | /datasources/{dataSourceName}/scans/{scanName}/runs/{uuid}             |
+--------------------------------+--------+------------------------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
