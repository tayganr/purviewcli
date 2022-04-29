"""
usage: 
    pv entity addLabels --guid=<val> --payloadFile=<val>
    pv entity addLabelsByUniqueAttribute --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
    pv entity addOrUpdateBusinessAttribute --guid=<val> --bmName=<val> --payloadFile=<val>
    pv entity addOrUpdateBusinessMetadata --guid=<val> --payloadFile=<val> [--isOverwrite]
    pv entity changeCollection --collection=<val> --payloadFile=<val>
    pv entity create --payloadFile=<val>
    pv entity createBulk --payloadFile=<val>
    pv entity createBulkClassification --payloadFile=<val>
    pv entity createBulkSetClassifications --payloadFile=<val>
    pv entity createClassifications --guid=<val> --payloadFile=<val>
    pv entity createOrUpdateCollection --collection=<val> --payloadFile=<val>
    pv entity createOrUpdateCollectionBulk --collection=<val> --payloadFile=<val>
    pv entity createUniqueAttributeClassifications --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
    pv entity delete --guid=<val>
    pv entity deleteBulk --guid=<val>...
    pv entity deleteBusinessAttribute --guid=<val> --bmName=<val> --payloadFile=<val>
    pv entity deleteBusinessMetadata --guid=<val> --payloadFile=<val>
    pv entity deleteClassification --guid=<val> --classificationName=<val>
    pv entity deleteLabels --guid=<val> --payloadFile=<val>
    pv entity deleteLabelsByUniqueAttribute --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
    pv entity deleteUniqueAttribute --typeName=<val> --qualifiedName=<val>
    pv entity deleteUniqueAttributeClassification --typeName=<val> --qualifiedName=<val> --classificationName=<val>
    pv entity getBusinessMetadataTemplate
    pv entity importBusinessMetadata --bmFile=<val>
    pv entity put --guid=<val> --attrName=<val> --attrValue=<val>
    pv entity putClassifications --guid=<val> --payloadFile=<val>
    pv entity putUniqueAttribute --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
    pv entity putUniqueAttributeClassifications --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
    pv entity read --guid=<val> [--ignoreRelationships --minExtInfo]
    pv entity readBulk --guid=<val>... [--ignoreRelationships --minExtInfo]
    pv entity readBulkUniqueAttribute --typeName=<val> --qualifiedName=<val>... [--ignoreRelationships --minExtInfo]
    pv entity readClassification --guid=<val> --classificationName=<val>
    pv entity readClassifications --guid=<val>
    pv entity readHeader --guid=<val>
    pv entity readUniqueAttribute --typeName=<val> --qualifiedName=<val> [--ignoreRelationships --minExtInfo]
    pv entity setLabels --guid=<val> --payloadFile=<val>
    pv entity setLabelsByUniqueAttribute --typeName=<val> --qualifiedName=<val> --payloadFile=<val>
    
options:
    --purviewName=<val>                 [string]  Azure Purview account name.
    --bmFile=<val>                      [string]  File path to a valid business metadata template CSV file.
    --bmName=<val>                      [string]  BusinessMetadata name.
    --classificationName=<val>          [string]  The name of the classification.
    --collection=<val>                  [string]  The collection unique name.
    --guid=<val>                        [string]  The globally unique identifier of the entity.
    --ignoreRelationships               [boolean] Whether to ignore relationship attributes [default: false].
    --isOverwrite                       [boolean] Whether to overwrite the existing business metadata on the entity or not [default: false].
    --minExtInfo                        [boolean] Whether to return minimal information for referred entities [default: false].
    --name=<val>                        [string]  The name of the attribute.
    --payloadFile=<val>                 [string]  File path to a valid JSON document.
    --qualifiedName=<val>               [string]  The qualified name of the entity.
    --typeName=<val>                    [string]  The name of the type.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
