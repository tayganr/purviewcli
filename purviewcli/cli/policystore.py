"""
usage: 
    pv policystore readMetadataRoles
    pv policystore readMetadataPolicy (--collectionName=<val> | --policyId=<val>)
    pv policystore readMetadataPolicies
    pv policystore putMetadataPolicy --policyId=<val> --payload-file=<val>

options:
    --purviewName=<val>           [string]  Azure Purview account name.
    --collectionName=<val>        [string]  The technical name of the Collection (e.g. friendlyName: Sales; name: afwbxs).
    --policyId=<val>              [string]  The unique policy id.
    --payload-file=<val>          [string]  File path to a valid JSON document.

mapping:
https://{account_name}.purview.azure.com
+----------------------+--------+----------------------------------------------------------+
| Command              | Method | Path                                                     |
+----------------------+--------+----------------------------------------------------------+
| readMetadataroles    | GET    | /policystore/metadataroles                               |
| readMetadataPolicy   | GET    | /policystore/collections/{collectionName}/metadataPolicy |
| readMetadataPolicy   | GET    | /policystore/metadataPolicies/{policyId}                 |
| readMetadataPolicies | GET    | /policystore/metadataPolicies                            |
| putMetadataPolicy    | PUT    | /policystore/metadataPolicies/{policyId}                 |
+----------------------+--------+----------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
