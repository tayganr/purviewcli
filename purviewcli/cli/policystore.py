"""
usage: 
    pv policystore readMetadataroles
    pv policystore readMetadataPolicy (--collectionName=<val> | --metadataPolicyId=<val>)
    pv policystore readMetadataPolicies
    pv policystore putMetadataPolicy --metadataPolicyId=<val> --payload-file=<val>

options:
    --purviewName=<val>           [string]  Azure Purview account name.
    --payload-file=<val>          [string]  File path to a valid JSON document.

mapping:
https://{account_name}.purview.azure.com
+----------------------+--------+----------------------------------------------------------+
| Command              | Method | Path                                                     |
+----------------------+--------+----------------------------------------------------------+
| readMetadataroles    | GET    | /policystore/metadataroles                               |
| readMetadataPolicy   | GET    | /policystore/collections/{collectionName}/metadataPolicy |
| readMetadataPolicy   | GET    | /policystore/metadataPolicies/{metadataPolicyId}         |
| readMetadataPolicies | GET    | /policystore/metadataPolicies                            |
| putMetadataPolicy    | PUT    | /policystore/metadataPolicies/{metadataPolicyId}         |
+----------------------+--------+----------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
