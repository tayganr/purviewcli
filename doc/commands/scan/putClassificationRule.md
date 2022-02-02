# pv scan putClassificationRule
[Command Reference](../../../README.md#command-reference) > [scan](./main.md) > putClassificationRule

## Description
Creates or Updates a classification rule

## Syntax
```
pv scan putClassificationRule --classificationRuleName=<val> --payloadFile=<val>
```

## Required Arguments
`--classificationRuleName` (string)  
The name of the classification rule.

`--payloadFile` (string)  
File path to a valid JSON document.

## Optional Arguments
*None*

## API Mapping
Scanning Data Plane > Classification Rules > [Create Or Update](https://docs.microsoft.com/en-us/rest/api/purview/scanningdataplane/classification-rules/create-or-update)
```
PUT https://{accountName}.purview.azure.com/scan/classificationrules/{classificationRuleName}
```

## Examples
Create or update a classification rule.
```powershell
pv scan putClassificationRule --classificationRuleName "my_rule" --payloadFile "/path/to/file.json"
```

Regular Expression based Classification Rule.
```json
{
    "kind": "Custom",
    "name": "my_rule",
    "properties": {
        "classificationAction": "Keep",
        "classificationName": "Twitter Handle",
        "columnPatterns": [],
        "dataPatterns": [
            {
                "kind": "Regex",
                "pattern": "^@[a-zA-Z0-9]{5,15}$"
            }
        ],
        "description": "",
        "minimumDistinctMatchCount": null,
        "minimumPercentageMatch": 60.0
    }
}
```

Dictionary based Classification Rule.
```json
{
    "name":"my_rule",
    "kind":"Custom",
    "properties": {
        "description":"",
        "classificationName":"Twitter_Handle",
        "columnPatterns":[],
        "dataPatterns":[],
        "minimumPercentageMatch":60,
        "classificationRuleBloomFilter": {
            "sourceFileName":"dictionary.csv",
            "cookedBloomFilter":"sQPxegwAAAABBwgAAAAAAAYAAAAOAAAAFQAAAAAAAACN3Af9UPI7AkpL4RHZO4cIMGVXnTVGQSV07TARgE35QWHFVBaaYZwDr9WZlVdGKmc=",
            "bloomFilterName":null
        }
    }
}
```