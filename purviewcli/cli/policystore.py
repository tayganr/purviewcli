"""
usage: 
    pv policystore readMetadataRoles
    pv policystore readMetadataPolicy (--collectionName=<val> | --policyId=<val>)
    pv policystore readMetadataPolicies
    pv policystore putMetadataPolicy --policyId=<val> --payloadFile=<val>
    pv policystore deleteDataPolicy --policyName=<val>
    pv policystore deleteDataPolicyScope --policyName=<val> --datasource=<val>
    pv policystore putDataPolicy --policyName=<val> --payloadFile=<val>
    pv policystore putDataPolicyScope --policyName=<val> --payloadFile=<val>
    pv policystore readDataPolicies [--policyName=<val>]
    pv policystore readDataPolicyScopes --policyName=<val>

options:
    --purviewName=<val>           [string]  Azure Purview account name.
    --collectionName=<val>        [string]  The technical name of the Collection (e.g. friendlyName: Sales; name: afwbxs).
    --policyId=<val>              [string]  The unique policy id.
    --payloadFile=<val>           [string]  File path to a valid JSON document.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
