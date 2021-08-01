"""
usage: 
    pv entity create --payload-file=<val>
    pv entity createBulk --payload-file=<val>
    pv entity createBulkClassification --payload-file=<val>
    pv entity createBulkSetClassifications --payload-file=<val>
    pv entity createClassifications --guid=<val> --payload-file=<val>
    pv entity createUniqueAttributeClassifications --typeName=<val> --payload-file=<val>
    pv entity delete --guid=<val>
    pv entity deleteBulk --guid=<val>...
    pv entity deleteClassification --guid=<val> --classificationName=<val>
    pv entity deleteUniqueAttribute --typeName=<val>
    pv entity deleteUniqueAttributeClassification --typeName=<val> --classificationName=<val>
    pv entity put --guid=<val> --name=<val> --payload-file=<val>
    pv entity putClassifications --guid=<val> --payload-file=<val>
    pv entity putUniqueAttribute --typeName=<val> --payload-file=<val>
    pv entity putUniqueAttributeClassifications --typeName=<val> --payload-file=<val>
    pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
    pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
    pv entity readBulkUniqueAttribute --typeName=<val> [--ignoreRelationships --minExtInfo]
    pv entity readClassification --guid=<val> --classificationName=<val>
    pv entity readClassifications --guid=<val>
    pv entity readHeader --guid=<val>
    pv entity readUniqueAttribute --typeName=<val> --qualifiedName=<val> [--ignoreRelationships --minExtInfo]
    
options:
    --purviewName=<val>                 [string]  Azure Purview account name.
    --classificationName=<val>          [string]  The name of the classification.
    --guid=<val>                        [string]  The globally unique identifier of the entity.
    --ignoreRelationships               [boolean] Whether to ignore relationship attributes [default: false].
    --minExtInfo                        [boolean] Whether to return minimal information for referred entities [default: false].
    --name=<val>                        [string]  The name of the attribute.
    --payload-file=<val>                [string]  File path to a valid JSON document.
    --qualifiedName=<val>               [string]  The qualified name of the entity.
    --typeName=<val>                    [string]  The name of the type.

mapping:
https://{account_name}.catalog.purview.azure.com
+--------------------------------------+--------+-------------------------------------------------------------------------------------------+
| Command                              | Method | Path                                                                                      |
+--------------------------------------+--------+-------------------------------------------------------------------------------------------+
| create                               | POST   | /api/atlas/v2/entity                                                                      |
| createBulk                           | POST   | /api/atlas/v2/entity/bulk                                                                 |
| createBulkClassification             | POST   | /api/atlas/v2/entity/bulk/classification                                                  |
| createBulkSetClassifications         | POST   | /api/atlas/v2/entity/bulk/setClassifications                                              |
| createClassifications                | POST   | /api/atlas/v2/entity/guid/{guid}/classifications                                          |
| createUniqueAttributeClassifications | POST   | /api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classifications                      |
| delete                               | DELETE | /api/atlas/v2/entity/guid/{guid}                                                          |
| deleteBulk                           | DELETE | /api/atlas/v2/entity/bulk                                                                 |
| deleteClassification                 | DELETE | /api/atlas/v2/entity/guid/{guid}/classification/{classificationName}                      |
| deleteUniqueAttribute                | DELETE | /api/atlas/v2/entity/uniqueAttribute/type/{typeName}                                      |
| deleteUniqueAttributeClassification  | DELETE | /api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classification/{classificationName}  |
| put                                  | PUT    | /api/atlas/v2/entity/guid/{guid}                                                          |
| putClassifications                   | PUT    | /api/atlas/v2/entity/guid/{guid}/classifications                                          |
| putUniqueAttribute                   | PUT    | /api/atlas/v2/entity/uniqueAttribute/type/{typeName}                                      |
| putUniqueAttributeClassifications    | PUT    | /api/atlas/v2/entity/uniqueAttribute/type/{typeName}/classifications                      |
| read                                 | GET    | /api/atlas/v2/entity/guid/{guid}                                                          |
| readBulk                             | GET    | /api/atlas/v2/entity/bulk                                                                 |
| readBulkUniqueAttribute              | GET    | /api/atlas/v2/entity/bulk/uniqueAttribute/type/{typeName}                                 |
| readClassification                   | GET    | /api/atlas/v2/entity/guid/{guid}/classification/{classificationName}                      |
| readClassifications                  | GET    | /api/atlas/v2/entity/guid/{guid}/classifications                                          |
| readHeader                           | GET    | /api/atlas/v2/entity/guid/{guid}/header                                                   |
| readUniqueAttribute                  | GET    | /api/atlas/v2/entity/uniqueAttribute/type/{typeName}                                      |
+---------------------------------------+---------+-----------------------------------------------------------------------------------------+

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
