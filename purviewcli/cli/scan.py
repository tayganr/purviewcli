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
    pv scan runScan --dataSourceName=<val> --scanName=<val> --runId=<val>
    pv scan putClassificationRule --classificationRuleName=<val> --payload-file=<val>
    pv scan putKeyVault --keyVaultName=<val> --payload-file=<val>
    pv scan putScanRuleset --scanRulesetName=<val> --payload-file=<val>

options:
    --purviewName=<val>        Azure Purview account name.
    --dataSourceType=<val>     AdlsGen1 | AdlsGen2 | AmazonAccount | AmazonPostgreSql | AmazonS3 | AmazonSql | AzureCosmosDb | AzureDataExplorer | AzureFileService | AzureMySql | AzurePostgreSql | AzureResourceGroup | AzureSqlDataWarehouse | AzureSqlDatabase | AzureSqlDatabaseManagedInstance | AzureStorage | AzureSubscription | AzureSynapse | AzureSynapseWorkspace | Oracle | PowerBI | SapEcc | SapS4Hana | SqlServerDatabase | Teradata.


"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
