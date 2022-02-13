# pv glossary readCategoryTerms
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readCategoryTerms

## Description
Get all terms associated with the specific category.

## Syntax
```
pv glossary readCategoryTerms --categoryGuid=<val> [--limit=<val> --offset=<val> --sort=<val>]
```

## Required Arguments
`--categoryGuid` (string)  
The globally unique identifier of the category.

## Optional Arguments
`--limit` (integer)  
The page size [default: 1000].

`--offset` (integer)  
Offset for pagination purpose [default: 0].

`--sort` (string)  
The sort order - ASC or DESC [default: ASC].

## API Mapping
Catalog Data Plane > Glossary > [List Category Terms](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/list-category-terms)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/category/{categoryGuid}/terms
```

## Examples
Get all terms associated with a category.
```powershell
pv glossary readCategoryTerms --categoryGuid "c856ecef-21e6-4e92-8607-9493d8432e78"
```
<details><summary>Sample response.</summary>
<p>

```json
[
    {
        "displayText": "Workplace Analytics_Organization",
        "relationGuid": "80384c75-8c29-45bc-9f7c-9bb3b1218320",
        "termGuid": "d99523b1-9b89-4748-8455-c00d76fd823a"
    },
    {
        "displayText": "Workplace Analytics_Pseudonymized",
        "relationGuid": "6a33dccf-4af8-4889-bd7d-a1c2034c5297",
        "termGuid": "06276c6f-aab7-46f3-980c-e92ad541f333"
    },
    {
        "displayText": "Workplace Analytics_Working hours",
        "relationGuid": "f68e9257-d2b5-4742-b40f-4d35ba86d6d8",
        "termGuid": "2796d276-75a0-46c0-9920-1d9e75c25842"
    }
]
```
</p>
</details>