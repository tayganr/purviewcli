"""
usage: 
    pv entity create --payload-file=<val>
    pv entity deleteBulk --guid=<val>...
    pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
    pv entity createBulk --payload-file=<val>
    pv entity createBulkClassification --payload-file=<val>
    pv entity createBulkClassifications --payload-file=<val>
    pv entity readUniqueAttribute --typeName=<val> [--ignoreRelationships --minExtInfo]
    pv entity createBusinessMetadataTemplate --payload-file=<val>
    pv entity readBusinessMetadataTemplate
    pv entity delete --guid=<val>
    pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
    pv entity put --guid=<val> --name=<val> --payload-file=<val>
    pv entity deleteBusinessMetadata --guid=<val> --payload-file=<val>
    pv entity createBusinessMetadata --guid=<val> --payload-file=<val> [--isOverwrite]
    pv entity deleteBusinessMetadataName --guid=<val> --payload-file=<val>
    pv entity createBusinessMetadataName --guid=<val> --payload-file=<val>
    pv entity deleteClassification --guid=<val> --classificationName=<val>
    pv entity readClassification --guid=<val> --classificationName=<val>
    pv entity readClassifications --guid=<val>
    pv entity createClassifications --guid=<val> --payload-file=<val>
    pv entity putClassifications --guid=<val> --payload-file=<val>
    pv entity readHeader --guid=<val>
    pv entity deleteLabels --guid=<val> --payload-file=<val>
    pv entity createLabels --guid=<val> --payload-file=<val>
    pv entity putLabels --guid=<val> --payload-file=<val>
    pv entity deleteType --typeName=<val>
    pv entity readType --typeName=<val> --qualifiedName=<val> [--ignoreRelationships --minExtInfo]
    pv entity putType --typeName=<val> --payload-file=<val>
    pv entity deleteTypeClassification --typeName=<val> --classificationName=<val>
    pv entity createTypeClassifications --typeName=<val> --payload-file=<val>
    pv entity putTypeClassifications --typeName=<val> --payload-file=<val>
    pv entity deleteTypeLabels --typeName=<val> --payload-file=<val>
    pv entity createTypeLabels --typeName=<val> --payload-file=<val>
    pv entity putTypeLabels --typeName=<val> --payload-file=<val>
    pv entity readAudit --guid=<val> --auditAction=<val> --startKey=<val> [--count=<val>]
    
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
