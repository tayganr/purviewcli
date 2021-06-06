"""
usage: 
    pv entity create --payload-file=<val>
    pv entity deleteBulk --guid=<val>...
    pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
    pv entity createBulk --payload-file=<val>
    pv entity createBulkClassification --payload-file=<val>
    pv entity createBulkSetClassifications --payload-file=<val>
    pv entity delete --guid=<val>
    pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
    pv entity put --guid=<val> --name=<val> --payload-file=<val>
    pv entity deleteClassification --guid=<val> --classificationName=<val>
    pv entity readClassification --guid=<val> --classificationName=<val>
    pv entity readClassifications --guid=<val>
    pv entity createClassifications --guid=<val> --payload-file=<val>
    pv entity putClassifications --guid=<val> --payload-file=<val>
    pv entity readHeader --guid=<val>
    pv entity deleteUniqueAttribute --typeName=<val>
    pv entity readUniqueAttribute --typeName=<val> --qualifiedName=<val> [--ignoreRelationships --minExtInfo]
    pv entity putUniqueAttribute --typeName=<val> --payload-file=<val>
    pv entity deleteUniqueAttributeClassification --typeName=<val> --classificationName=<val>
    pv entity createUniqueAttributeClassifications --typeName=<val> --payload-file=<val>
    pv entity putUniqueAttributeClassifications --typeName=<val> --payload-file=<val>
    pv entity readBulkUniqueAttribute --typeName=<val> [--ignoreRelationships --minExtInfo]
    
options:
    --purviewName=<val>                 [string]  Azure Purview account name.
    --guid=<val>                        [string]  The globally unique identifier of the entity.
    --ignoreRelationships               [boolean] Whether to ignore relationship attributes.
    --minExtInfo                        [boolean] Whether to return minimal information for referred entities.
    --name=<val>                        [string]  The name of the attribute.
    --classificationName=<val>          [string]  The name of the classification.
    --typeName=<val>                    [string]  The name of the type.
    --qualifiedName=<val>               [string]  The qualified name of the entity.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
