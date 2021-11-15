"""
usage: 
    pv account deleteCollection --collectionName=<val>
    pv account getChildCollectionNames --collectionName=<val>
    pv account getCollection --collectionName=<val>
    pv account getCollectionPath --collectionName=<val>
    pv account getCollections
    pv account putCollection --friendlyName=<val> --parentCollection=<val>


options:
    --purviewName=<val>           [string]  Azure Purview account name.
    --collectionName=<val>        [string] The technical name of the collection.
    --friendlyName=<val>     
    --parentCollection=<val>

mapping:
https://{account_name}.purview.azure.com/account
+-------------------------+-------+--------------------------------------------------------+
| Command                 | Method | Path                                                  |
+-------------------------+--------+-------------------------------------------------------+
| getCollection           | GET    | /collections/{collectionName}                         |
| getCollectionPath       | GET    | /collections/{collectionName}/getCollectionPath       |
| getChildCollectionNames | GET    | /collections/{collectionName}/getChildCollectionNames |
| getCollections          | GET    | /collections                                          |
| deleteCollection        | DELETE | /collections/{collectionName}                         |
| putCollection           | PUT    | /collections/{collectionName}                         |
+-------------------------+-------+--------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
