# pv scan readClassificationRule
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readClassificationRule

## Description
Get a classification rule

## Syntax
```
pv scan readClassificationRule --classificationRuleName=<val>
```

## Required Arguments
`--classificationRuleName` (string)  
The name of the classification rule.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Classification Rules > [Get](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/get)
```
GET https://{accountName}.purview.azure.com/scan/classificationrules/{classificationRuleName}
```

## Examples
Get a classification rule by name.
```powershell
pv scan readClassificationRule --classificationRuleName "twitter_handle"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "id": "classificationrules/twitter_handle",
    "kind": "Custom",
    "name": "twitter_handle",
    "properties": {
        "classificationAction": "Keep",
        "classificationName": "Twitter Handle",
        "classificationRuleBloomFilter": null,
        "collection": null,
        "columnPatterns": [],
        "createdAt": "2022-02-27T21:00:53.2883178Z",
        "dataPatterns": [
            {
                "kind": "Regex",
                "pattern": "^@[a-zA-Z0-9]+$"
            }
        ],
        "description": "This classification rule detects Twitter handles.",
        "lastModifiedAt": "2022-02-27T21:00:53.2883178Z",
        "minimumDistinctMatchCount": null,
        "minimumPercentageMatch": 60.0,
        "owner": "095354ff-cae8-44ff-8120-22ec5a941b40",
        "ruleStatus": "Enabled",
        "version": 1
    }
}
```
</p>
</details>