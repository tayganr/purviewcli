# Entity
[Command Reference](../../../README.md#command-reference) > entity

## Entity
| Command | Description |
| --- | --- |
| [pv entity create](./create.md) | Create or update an entity in Atlas. |
| [pv entity createBulk](./createBulk.md) | Create or update entities in Atlas in bulk. |
| [pv entity delete](./delete.md) | Delete an entity identified by its GUID. |
| [pv entity deleteBulk](./deleteBulk.md) | Delete a list of entities in bulk identified by their GUIDs or unique attributes. |
| [pv entity deleteUniqueAttribute](./deleteUniqueAttribute.md) | Delete an entity identified by its type and unique attributes. |
| [pv entity put](./put.md) | Update entity partially - create or update entity attribute identified by its GUID. |
| [pv entity putUniqueAttribute](./putUniqueAttribute.md) | Update entity partially. |
| [pv entity read](./read.md) | Get complete definition of an entity given its GUID. |
| [pv entity readBulk](./readBulk.md) | List entities in bulk identified by its GUIDs. |
| [pv entity readBulkUniqueAttribute](./readBulkUniqueAttribute.md) | Bulk API to retrieve list of entities identified by its unique attributes. |
| [pv entity readHeader](./readHeader.md) | Get entity header given its GUID. |
| [pv entity readUniqueAttribute](./readUniqueAttribute.md) | Get complete definition of an entity given its type and unique attribute. |
| [pv entity createOrUpdateCollection](./createOrUpdateCollection.md) | Creates or updates an entity to a collection. |
| [pv entity createOrUpdateCollectionBulk](./createOrUpdateCollectionBulk.md) | Creates or updates entities in bulk to a collection. |
| [pv entity changeCollection](./changeCollection.md) | Move existing entities to the target collection. |

## Classification
| Command | Description |
| --- | --- |
| [pv entity createBulkClassification](./createBulkClassification.md) | Associate a classification to multiple entities in bulk. |
| [pv entity createBulkSetClassifications](./createBulkSetClassifications.md) | Set classifications on entities in bulk. |
| [pv entity createClassifications](./createClassifications.md) | Add classifications to an existing entity represented by a GUID. |
| [pv entity createUniqueAttributeClassifications](./createUniqueAttributeClassifications.md) | Add classification to the entity identified by its type and unique attributes. |
| [pv entity deleteClassification](./deleteClassification.md) | Delete a given classification from an existing entity represented by a GUID. |
| [pv entity deleteUniqueAttributeClassification](./deleteUniqueAttributeClassification.md) | Delete a given classification from an entity identified by its type and unique attributes. |
| [pv entity putClassifications](./putClassifications.md) | Update classifications to an existing entity represented by a guid. |
| [pv entity putUniqueAttributeClassifications](./putUniqueAttributeClassifications.md) | Update classification on an entity identified by its type and unique attributes. |
| [pv entity readClassification](./readClassification.md) | List classifications for a given entity represented by a GUID. |
| [pv entity readClassifications](./readClassifications.md) | List classifications for a given entity represented by a GUID. |

## Label
| Command | Description |
| --- | --- |
| [pv entity addLabels](./addLabels.md) | Append labels to an entity. |
| [pv entity deleteLabels](./deleteLabels.md) | Delete label(s) from an entity. |
| [pv entity setLabels](./setLabels.md) | Overwrite labels for an entity. |
| [pv entity addLabelsByUniqueAttribute](./addLabelsByUniqueAttribute.md) | Append labels to an entity identified by its type and unique attributes. |
| [pv entity deleteLabelsByUniqueAttribute](./deleteLabelsByUniqueAttribute.md) | Delete label(s) from an entity identified by its type and unique attributes. |
| [pv entity setLabelsByUniqueAttribute](./setLabelsByUniqueAttribute.md) | Overwrite labels for an entity identified by its type and unique attributes. |

## Business Metadata
| Command | Description |
| --- | --- |
| [pv entity addOrUpdateBusinessMetadata](./addOrUpdateBusinessMetadata.md) | Add or update business metadata to an entity. |
| [pv entity deleteBusinessMetadata](./deleteBusinessMetadata.md) | Delete business metadata from an entity. |
| [pv entity getBusinessMetadataTemplate](./getBusinessMetadataTemplate.md) | Get a sample template for uploading/creating business metadata in bulk. |
| [pv entity importBusinessMetadata](./importBusinessMetadata.md) | Import business metadata in bulk. |

## Business Attribute
| Command | Description |
| --- | --- |
| [pv entity addOrUpdateBusinessAttribute](./addOrUpdateBusinessAttribute.md) | Add or update business attributes to an entity. |
| [pv entity deleteBusinessAttribute](./deleteBusinessAttribute.md) | Delete business attributes from an entity. |