# pv scan readClassificationRuleVersions
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > readClassificationRuleVersions

## Description
Lists the rule versions of a classification rule

## Syntax
```
pv scan readClassificationRuleVersions --classificationRuleName=<val>
```

## Required Arguments
`--classificationRuleName` (string)  
The name of the classification rule.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Classification Rules > [List Versions By Classification Rule Name](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/list-versions-by-classification-rule-name)
```
GET https://{accountName}.purview.azure.com/scan/classificationrules/{classificationRuleName}/versions
```

## Examples
Get classification rule versions by name.
```powershell
pv scan readClassificationRuleVersions --classificationRuleName "twitter_handle"
```
<details><summary>Sample response.</summary>
<p>

```json
{
    "count": 2,
    "value": [
        {
            "id": "classificationrules/twitter_handle/versions/1",
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
        },
        {
            "id": "classificationrules/twitter_handle/versions/2",
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
                        "pattern": "^@[a-zA-Z0-9]{5,15}$"
                    }
                ],
                "description": "This classification rule detects Twitter handles - v2.",
                "lastModifiedAt": "2022-02-27T21:02:53.9819342Z",
                "minimumDistinctMatchCount": null,
                "minimumPercentageMatch": 60.0,
                "owner": "095354ff-cae8-44ff-8120-22ec5a941b40",
                "ruleStatus": "Enabled",
                "version": 2
            }
        }
    ]
}
```
</p>
</details>