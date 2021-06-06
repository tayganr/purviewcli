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
    --purviewName=<val>                 Azure Purview account name.
    --auditAction=<val>                 BUSINESS_ATTRIBUTE_UPDATE or CLASSIFICATION_ADD or CLASSIFICATION_DELETE or CLASSIFICATION_UPDATE or ENTITY_CREATE or ENTITY_DELETE or ENTITY_IMPORT_CREATE or ENTITY_IMPORT_DELETE or ENTITY_IMPORT_UPDATE or ENTITY_PURGE or ENTITY_UPDATE or LABEL_ADD or LABEL_DELETE or PROPAGATED_CLASSIFICATION_ADD or PROPAGATED_CLASSIFICATION_DELETE or PROPAGATED_CLASSIFICATION_UPDATE or TERM_ADD or TERM_DELETE.
    --count=<val>                       Number of events required	[default: 100].
    --startKey=<val>                    Used for pagination. Startkey is inclusive, the returned results contain the event with the given startkey.
    --tagUpdateStartTime=<val>          DataType long.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
