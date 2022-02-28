# pv entity readHeader
[Command Reference](../../../README.md#command-reference) > [entity](./main.md) > readHeader

## Description
Get entity header given its GUID.

## Syntax
```
pv entity readHeader --guid=<val>
```

## Required Arguments
`--guid` (string)  
The globally unique identifier of the entity.

## Optional Arguments
*None*

## API Mapping
Catalog Data Plane > Entity > [Get Header](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/entity/get-header)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity/guid/{guid}/header
```

## Examples
Get the header information for an existing entity via the entities GUID.
```powershell
pv entity readHeader --guid "c6a7811a-0699-44d0-b0be-68babe560ab2"
```

<details><summary>Sample response.</summary>
<p>

```json
{                           
    "attributes": {
        "description": "Portfolio company data collection template - Company ABC.",
        "name": "abc_company.csv",
        "owner": "60117586-ca87-4eac-a217-9d130ded9af0",
        "qualifiedName": "https://esg26fa7f24adls.dfs.core.windows.net/01-bronze/esg/abc_company.csv"
    },
    "classificationNames": [
        "Microsoft.Label.9FBDE396_1A24_4C79_8EDF_9254A0F35055",
        "MICROSOFT.GOVERNMENT.AUSTRIA.TAX.IDENTIFICATION.NUMBER",
        "MICROSOFT.GOVERNMENT.AUSTRALIA.COMPANY.NUMBER",
        "MICROSOFT.POWERBI.ENDORSEMENT",
        "MICROSOFT.FINANCIAL.US.ABA_ROUTING_NUMBER"
    ],
    "collectionId": "esg-26fa7f24-pv",
    "displayText": "abc_company.csv",
    "guid": "c6a7811a-0699-44d0-b0be-68babe560ab2",
    "lastModifiedTS": "9",
    "meaningNames": [
        "Work related injuries",
        "Employee feedback / survey",
        "Diversity of board members"
    ],
    "meanings": [
        {
            "confidence": 0,
            "displayText": "Work related injuries",
            "relationGuid": "d3f6fc76-c40b-4740-9cfa-c0eab6c277ae",
            "termGuid": "74a7901e-7049-4858-a103-4ffb889b5fc9"
        },
        {
            "confidence": 0,
            "displayText": "Employee feedback / survey",
            "relationGuid": "777f339a-1122-41eb-84be-ab03eefc4d2f",
            "termGuid": "5e492945-85a5-42c4-bbcd-dbfdb2dd8713"
        },
        {
            "confidence": 0,
            "displayText": "Diversity of board members",
            "relationGuid": "28013ca5-56b0-45a6-94da-7ffab0e173d6",
            "termGuid": "f1496766-3af2-461a-8d59-6eca8a716887"
        }
    ],
    "status": "ACTIVE",
    "typeName": "azure_datalake_gen2_path"
}
```
</p>
</details>