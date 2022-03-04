"""
usage: 
    pv account deleteCollection --collectionName=<val>
    pv account deleteResourceSetRule
    pv account getAccessKeys
    pv account getAccount
    pv account getChildCollectionNames --collectionName=<val>
    pv account getCollection --collectionName=<val>
    pv account getCollectionPath --collectionName=<val>
    pv account getCollections
    pv account getResourceSetRule
    pv account getResourceSetRules
    pv account putCollection --friendlyName=<val> --parentCollection=<val>
    pv account putResourceSetRule --payloadFile=<val>
    pv account regenerateAccessKeys --keyType=<val>
    pv account updateAccount --friendlyName=<val>


options:
    --purviewName=<val>           [string] Azure Purview account name.
    --collectionName=<val>        [string] The technical name of the collection.
    --keyType=<val>               [string] The access key type.
    --friendlyName=<val>          [string] The friendly name for the azure resource.
    --parentCollection=<val>      [string] Gets or sets the parent collection reference.
    --payloadFile=<val>           [string] File path to a valid JSON document.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
