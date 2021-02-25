"""
usage: 
    pv entity create --name=<val> --qualifiedName=<val> --typeName=<val> [--description=<val>]
    pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
    pv entity update --guid=<val> --attrKey=<val> --attrVal=<val>
    pv entity delete --guid=<val>
    pv entity createBulk --name=<val>... --qualifiedName=<val>... --typeName=<val>...
    pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
    pv entity readHeader --guid=<val>
    pv entity createClassifications --guid=<val> --classificationName=<val>...
    pv entity readClassifications --guid=<val>
    pv entity readClassification --guid=<val> --classificationName=<val>
    pv entity deleteClassification --guid=<val> --classificationName=<val>
    pv entity createBulkClassification --classificationName=<val> --guid=<val>...
    pv entity readUniqueAttributeType --typeName=<val> --attrKey=<val> --attrVal=<val> [--ignoreRelationships --minExtInfo]
    pv entity deleteUniqueAttributeType --typeName=<val> --attrKey=<val> --attrVal=<val>
    pv entity updateUniqueAttributeType --typeName=<val> --attrKey=<val> --attrVal=<val> [--description=<val>]
    pv entity readBulkUniqueAttributeType --typeName=<val> --attrKey=<val>... --attrVal=<val>... [--ignoreRelationships --minExtInfo]
    pv entity createUniqueAttributeTypeClassifications --typeName=<val> --attrKey=<val> --attrVal=<val> --classificationName=<val>...
    pv entity updateUniqueAttributeTypeClassifications --typeName=<val> --attrKey=<val> --attrVal=<val> --classificationName=<val>...
    pv entity deleteUniqueAttributeTypeClassification --typeName=<val> --attrKey=<val> --attrVal=<val> --classificationName=<val>
    
options:
    --auditAction=<val>                         BUSINESS_ATTRIBUTE_UPDATE or CLASSIFICATION_ADD or CLASSIFICATION_DELETE or CLASSIFICATION_UPDATE or ENTITY_CREATE or ENTITY_DELETE or ENTITY_IMPORT_CREATE or ENTITY_IMPORT_DELETE or ENTITY_IMPORT_UPDATE or ENTITY_PURGE or ENTITY_UPDATE or LABEL_ADD or LABEL_DELETE or PROPAGATED_CLASSIFICATION_ADD or PROPAGATED_CLASSIFICATION_DELETE or PROPAGATED_CLASSIFICATION_UPDATE or TERM_ADD or TERM_DELETE.
    --count=<val>                               Number of events required	[default: 100].
    --startKey=<val>                            Used for pagination. Startkey is inclusive, the returned results contain the event with the given startkey.
    --tagUpdateStartTime=<val>                  DataType long.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
