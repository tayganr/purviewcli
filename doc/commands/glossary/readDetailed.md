# pv glossary readDetailed
[Command Reference](../../../README.md#command-reference) > [glossary](./main.md) > readDetailed

## Description
Get a specific glossary with detailed information.

## Syntax
```
pv glossary readDetailed --glossaryGuid=<val> [--includeTermHierarchy]
```

## Required Arguments
`--glossaryGuid` (string)  
The globally unique identifier for glossary.

## Optional Arguments
`--includeTermHierarchy` (boolean)  
Whether to include the term hierarchy.

## API Mapping
Catalog Data Plane > Glossary > [Get Detailed Glossary](https://docs.microsoft.com/en-us/rest/api/purview/catalogdataplane/glossary/get-detailed-glossary)
```
GET https://{accountName}.purview.azure.com/catalog/api/atlas/v2/glossary/{glossaryGuid}/detailed
```

## Examples
Get a specific glossary with detailed information.
```powershell
pv glossary readDetailed --glossaryGuid "f2307f48-5834-4709-be85-02f3aea5d149"
```

<details><summary>Sample response.</summary>
<p>

```json
{
    "guid": "f2307f48-5834-4709-be85-02f3aea5d149",
    "name": "Glossary",
    "qualifiedName": "Glossary",
    "termInfo": {
        "079658e3-d0ca-41f2-a716-f277873c2c29": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "89973b52-33a6-4c6b-939d-b6b4f1a50d8b"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "079658e3-d0ca-41f2-a716-f277873c2c29",
            "lastModifiedTS": "1",
            "longDescription": "Pseudonymized data is personal data that has undergone processing so that it can no longer be attributed to a specific\u00a0data subject\u00a0without the use of additional information, provided that such additional information is kept separately and is subject to technical and organizational measures to ensure that the personal data is not attributed to an identified or identifiable natural person. Pseudonymization is one means of achieving de-identification.",
            "name": "Workplace Analytics_Pseudonymized",
            "qualifiedName": "Workplace Analytics_Pseudonymized@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "09a7f806-8612-4de4-b87a-5481f6e2878c": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "42435356-b3eb-49ee-b3ae-23676f43b4ba"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "09a7f806-8612-4de4-b87a-5481f6e2878c",
            "lastModifiedTS": "1",
            "longDescription": "A person who was invited and\u00a0attended\u00a0the meeting.",
            "name": "Workplace Analytics_Attendee",
            "qualifiedName": "Workplace Analytics_Attendee@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "0d8c0610-4c8b-4f90-b18b-e85d688eb2e6": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "f870d163-c9de-4cbd-8b29-41bd33c9612a"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "0d8c0610-4c8b-4f90-b18b-e85d688eb2e6",
            "lastModifiedTS": "1",
            "longDescription": "An audio or video communication or in-person meeting that has been scheduled -- that is, it appears on a person's Outlook calendar. A meeting must involve two or more people. Outlook calendar events determine the durations of meetings.",
            "name": "Workplace Analytics_Meeting",
            "qualifiedName": "Workplace Analytics_Meeting@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "102f72ff-b231-4df0-9b91-2583f430e5f1": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "a9fd4002-a837-45e0-bd2b-100890a46d56"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "102f72ff-b231-4df0-9b91-2583f430e5f1",
            "lastModifiedTS": "1",
            "longDescription": "A scheduled or unscheduled audio or video communication between two or more people over Microsoft Teams. If the call is scheduled, it appears on a person's Outlook calendar as a meeting appointment. A user's call duration is based on their join time and their leave time for the call.",
            "name": "Workplace Analytics_Call",
            "qualifiedName": "Workplace Analytics_Call@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "12e206ee-5b98-475d-ab7e-e827d38367bf": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "b751001e-a6c5-413c-8d23-2c9a707c5b9b"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "12e206ee-5b98-475d-ab7e-e827d38367bf",
            "lastModifiedTS": "1",
            "longDescription": "The number of\u00a0levels\u00a0of reporting in a company, starting from CEO and going down. For example, the CEO equals level 0.",
            "name": "Workplace Analytics_Layer",
            "qualifiedName": "Workplace Analytics_Layer@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "158674b1-129b-4e8b-b165-5b7eeae37e90": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "af986a4f-a56f-462c-a3d2-b0f5bcca4147"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "158674b1-129b-4e8b-b165-5b7eeae37e90",
            "lastModifiedTS": "1",
            "longDescription": "A\u00a0required attribute\u00a0that is a company-specific way of organizing employees by job experience or seniority.\u00a0",
            "name": "Workplace Analytics_Level",
            "qualifiedName": "Workplace Analytics_Level@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "17f6bb31-3787-4001-b172-1fe425359f49": {
            "abbreviation": "CM",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "b290ffa4-400f-4b1c-adde-41a315e7dcc4"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "17f6bb31-3787-4001-b172-1fe425359f49",
            "lastModifiedTS": "1",
            "longDescription": "A meeting on a person's calendar that overlaps with another meeting on that person's calendar.",
            "name": "Workplace Analytics_Conflicting meeting",
            "qualifiedName": "Workplace Analytics_Conflicting meeting@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "1a391268-9058-46ec-b924-14c1b5eac572": {
            "abbreviation": "CP",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "8b359c38-b353-4f7a-b03c-8272d8f307ab"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "1a391268-9058-46ec-b924-14c1b5eac572",
            "lastModifiedTS": "1",
            "longDescription": "Those who have had more than five connections with external people within the same month.",
            "name": "Workplace Analytics_Connected people",
            "qualifiedName": "Workplace Analytics_Connected people@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "1b402853-8a6c-4a1a-9064-290d26b7e736": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "6b338bdd-62d7-4701-9a23-c79d90be5320"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "1b402853-8a6c-4a1a-9064-290d26b7e736",
            "lastModifiedTS": "1",
            "longDescription": "The person who organizes a meeting. This person is also counted as an\u00a0attendee.",
            "name": "Workplace Analytics_Organizer",
            "qualifiedName": "Workplace Analytics_Organizer@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "21b5e0b7-1b24-4804-ac73-089004d46e95": {
            "abbreviation": "AMH",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "5a1caddc-5401-4b9f-96b1-6f87b9e8583e"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "21b5e0b7-1b24-4804-ac73-089004d46e95",
            "lastModifiedTS": "1",
            "longDescription": "An adjustment is applied so that overlapping time is not double-counted when a person has overlapping meeting hours. For example, a person with non-declined meeting requests from 2:00 to 3:00 PM and 2:30 to 3:30 PM would yield 1.5 adjusted meeting hours.",
            "name": "Workplace Analytics_Adjusted meeting hours",
            "qualifiedName": "Workplace Analytics_Adjusted meeting hours@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "2584bf5a-7df4-402f-b427-92c0f85be892": {
            "abbreviation": "CF",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "b00497da-83ce-49d5-acf6-d6371e9c6a4d"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "2584bf5a-7df4-402f-b427-92c0f85be892",
            "lastModifiedTS": "1",
            "longDescription": "When a person does not have blocks of time sufficient to focus on completing complex tasks. This is typical of those with only small blocks of time (15, 30, or 60 minutes) between meetings. Anything that is not\u00a0focus time\u00a0(uninterrupted time blocks of two hours or more with no meetings) is considered calendar fragmentation.",
            "name": "Workplace Analytics_Calendar fragmentation",
            "qualifiedName": "Workplace Analytics_Calendar fragmentation@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "26ec957d-834b-491b-a5c5-71cb78369dda": {
            "abbreviation": "DMM",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "4a5da1da-c187-4508-ab9e-6fcd88ee17aa"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "26ec957d-834b-491b-a5c5-71cb78369dda",
            "lastModifiedTS": "1",
            "longDescription": "A meeting that has between two and eight attendees and lasts less than one hour.",
            "name": "Workplace Analytics_Decision-making meeting",
            "qualifiedName": "Workplace Analytics_Decision-making meeting@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "2bbd7ff5-0142-4fad-aa2e-5fdf492f8a58": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "bb9943a0-5153-4b4e-9179-c5359433c191"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "2bbd7ff5-0142-4fad-aa2e-5fdf492f8a58",
            "lastModifiedTS": "1",
            "longDescription": "A process that is used to prevent the connection of personal identifiers with information.",
            "name": "Workplace Analytics_De-identification",
            "qualifiedName": "Workplace Analytics_De-identification@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "2dea0df8-959d-455d-8283-1582c770e80e": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "a7a378ef-a2a5-4b56-bd19-4f84f4b32446"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "2dea0df8-959d-455d-8283-1582c770e80e",
            "lastModifiedTS": "1",
            "longDescription": "Aggregation means compiling data from multiple individuals or sources. The more individuals or sources whose data is used, the more difficult it is to identify personal data. Aggregation is one means of achieving de-identification.",
            "name": "Workplace Analytics_Aggregation",
            "qualifiedName": "Workplace Analytics_Aggregation@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "4b1ac875-260e-4dcd-96f8-e843bd437587": {
            "abbreviation": "CA",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "d75df161-19b0-41a2-8b60-36332b0ecc7e"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "4b1ac875-260e-4dcd-96f8-e843bd437587",
            "lastModifiedTS": "1",
            "longDescription": "Organizational data\u00a0attributes that describe the people being analyzed. If supplied by the company, these attributes can be used in grouping of data, and to filter reports and customize metrics. However, they are not reserved for metrics calculations.",
            "name": "Workplace Analytics_Custom attribute",
            "qualifiedName": "Workplace Analytics_Custom attribute@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "4f2fa1a2-e7d3-4ac1-ad5d-e178f23973f4": {
            "abbreviation": "CN",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "b77ebec8-61b4-44c6-94f5-f404955d9497"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "4f2fa1a2-e7d3-4ac1-ad5d-e178f23973f4",
            "lastModifiedTS": "1",
            "longDescription": "A relationship that is based on an overlap between the collaboration networks of two or more people. For example, Megan and Vinod each has their own set of people with whom they work and meet. These sets of people overlap, which creates an indirect bonding or relationship \u2014 a\u00a0common network\u00a0\u2014 between Megan and Vinod.",
            "name": "Workplace Analytics_Common network",
            "qualifiedName": "Workplace Analytics_Common network@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "5a3358e6-ebf9-4d26-965f-87e1e6ecf52e": {
            "abbreviation": "CG",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "f33b9a2b-373c-44b4-a94b-7b9a8104ccf6"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "5a3358e6-ebf9-4d26-965f-87e1e6ecf52e",
            "lastModifiedTS": "1",
            "longDescription": "Those who spend a large proportion of their overall collaboration with people outside the company.",
            "name": "Workplace Analytics_Connected groups",
            "qualifiedName": "Workplace Analytics_Connected groups@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "5da6c9a6-7567-45fe-aa05-5cccfdbc23d2": {
            "abbreviation": "FH",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "1e4719bd-d6cb-4664-a471-e12966ffe4d6"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "5da6c9a6-7567-45fe-aa05-5cccfdbc23d2",
            "lastModifiedTS": "1",
            "longDescription": "A person's time after you subtract their meeting hours and their focus hours.",
            "name": "Workplace Analytics_Fragmented hours",
            "qualifiedName": "Workplace Analytics_Fragmented hours@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "60fb2c1c-005c-462b-b5e1-e6421328565e": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "d78b3534-9d41-4eee-920f-9e9c3273eaa2"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "60fb2c1c-005c-462b-b5e1-e6421328565e",
            "lastModifiedTS": "1",
            "longDescription": "The concept of not staying focused on the task at hand. Defined in Workplace Analytics as a person sending two emails or more per meeting hour, and in meetings shorter than an hour, two emails or more per meeting.",
            "name": "Workplace Analytics_Multitasking",
            "qualifiedName": "Workplace Analytics_Multitasking@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "61d1aa8f-7aed-4866-b563-5108ba5c67e7": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "64c795e0-1d8c-4436-ae91-7f1f171e0e4f"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "61d1aa8f-7aed-4866-b563-5108ba5c67e7",
            "lastModifiedTS": "1",
            "longDescription": "The number of direct reports per manager.",
            "name": "Workplace Analytics_Span",
            "qualifiedName": "Workplace Analytics_Span@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "67703464-7e08-4db4-ad1c-59d03f4a5d49": {
            "abbreviation": "PD",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "a7c58708-35ed-4718-919a-fe33bdc8f67d"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "67703464-7e08-4db4-ad1c-59d03f4a5d49",
            "lastModifiedTS": "1",
            "longDescription": "Personal data is any data that relates to an identified or identifiable natural person. An identifiable person is one who can be identified (directly or indirectly), in particular through an identifier such as a name, an identification number, location data, online identifier, or through one or more factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that person.",
            "name": "Workplace Analytics_Personal data",
            "qualifiedName": "Workplace Analytics_Personal data@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "6c4a2a0a-6cf3-4d01-b70c-a9461dfe971b": {
            "abbreviation": "PMH",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "c4c949ca-3049-4662-9b27-6cff3b2ed404"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "6c4a2a0a-6cf3-4d01-b70c-a9461dfe971b",
            "lastModifiedTS": "1",
            "longDescription": "The sum of adjusted meeting hours for each person in the meeting. For example, if a meeting lasts at least one hour with three attendees (and no attendees have overlapping meetings), the people meeting hours for that meeting is three.",
            "name": "Workplace Analytics_People meeting hours",
            "qualifiedName": "Workplace Analytics_People meeting hours@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "7770ef0f-74e0-43a1-bb6a-8eab9d5dce13": {
            "abbreviation": "CG",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "b13bd0f2-5729-4999-a31c-08c71c59312e"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "7770ef0f-74e0-43a1-bb6a-8eab9d5dce13",
            "lastModifiedTS": "1",
            "longDescription": "A group of collaborators that are identified as internal (within the company) or external (outside of the company) that interacts by email, in meetings, in calls, or with instant messages with a specified\u00a0time investor.",
            "name": "Workplace Analytics_Collaborator group",
            "qualifiedName": "Workplace Analytics_Collaborator group@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "7804d73c-d047-45ab-9728-87f53a842613": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "1a121daa-d4eb-4340-9175-5f72e372b065"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "7804d73c-d047-45ab-9728-87f53a842613",
            "lastModifiedTS": "1",
            "longDescription": "Hashing is a cryptographic process that converts a piece of data into another in a way that is easy to compute, extremely difficult to reverse, and highly unlikely that two different pieces of data have the same hash. For example, meeting\u00a0subject lines\u00a0that are hashed would appear not in their original, readable, form but as a meaningless number.",
            "name": "Workplace Analytics_Hashing",
            "qualifiedName": "Workplace Analytics_Hashing@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "78b536fb-813b-4e66-9c65-0422d5daa4d2": {
            "abbreviation": "OD",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "eb3eb201-57c5-4a33-bec7-b3095c1a2c1c"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "78b536fb-813b-4e66-9c65-0422d5daa4d2",
            "lastModifiedTS": "1",
            "longDescription": "Attributes about people in the organization or people who collaborate with the organization that Workplace Analytics can analyze. Most organizational data is obtained from a company\u2019s human resources information system. For example, job family, job role, organization, line of business, cost center, location, region, layer, level, number of direct reports, manager, and so on.\u00a0",
            "name": "Workplace Analytics_Organizational data",
            "qualifiedName": "Workplace Analytics_Organizational data@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "802fd63f-d3ba-40cf-a619-444ef9a34afc": {
            "abbreviation": "RO",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "91237131-3b1f-43ea-9698-c6a32d665c47"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "802fd63f-d3ba-40cf-a619-444ef9a34afc",
            "lastModifiedTS": "1",
            "longDescription": "Organizational redundancy is present if at least three attendees are from different levels within the same organization. For example, a meeting whose attendees included a General Manager, a Director, and an Independent Contributor from the same organization would be a redundant meeting.",
            "name": "Workplace Analytics_Redundancy (organizational)",
            "qualifiedName": "Workplace Analytics_Redundancy (organizational)@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "81ef18f0-7a49-4fc8-a24a-283d26a8a127": {
            "abbreviation": "LM",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "618093ba-f2c1-47bc-b684-0d2e80c5c6d2"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "81ef18f0-7a49-4fc8-a24a-283d26a8a127",
            "lastModifiedTS": "1",
            "longDescription": "A long meeting is scheduled for more than one hour and has more than one but fewer than nine attendees. Also see\u00a0Long and large meeting.",
            "name": "Workplace Analytics_Long meeting",
            "qualifiedName": "Workplace Analytics_Long meeting@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "8a2f1d84-b953-43de-bcf0-42a0f92faa5c": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "4a3bc643-42e8-42b7-91f9-24b97be5a795"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "8a2f1d84-b953-43de-bcf0-42a0f92faa5c",
            "lastModifiedTS": "1",
            "longDescription": "Anyone that\u00a0measured employees\u00a0or\u00a0time investors\u00a0interact with by email or instant message, in meetings, in unscheduled calls, or with instant messages. Collaborators are identified as internal (within the company) or external (outside of the company) and discovered through the data extracted for measured employees. Internal collaborators have domains internal to your organization, while external collaborators have domains external to your organization.",
            "name": "Workplace Analytics_Collaborators",
            "qualifiedName": "Workplace Analytics_Collaborators@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "8aae8706-1d0f-4ee9-8d5a-27a9d824f3df": {
            "abbreviation": "LM",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "666e19fe-6def-448d-a629-e754ea81c31f"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "8aae8706-1d0f-4ee9-8d5a-27a9d824f3df",
            "lastModifiedTS": "1",
            "longDescription": "A large meeting involves more than eight people\u00a0and lasts less than one hour. Also see\u00a0Long and large meeting.",
            "name": "Workplace Analytics_Large meeting",
            "qualifiedName": "Workplace Analytics_Large meeting@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "8bf2fbd9-a0a7-444b-8900-d62c2c3059de": {
            "abbreviation": "RLL",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "ca98292e-64c9-4c00-be42-64142905eb5a"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "8bf2fbd9-a0a7-444b-8900-d62c2c3059de",
            "lastModifiedTS": "1",
            "longDescription": "An attendee is considered redundant at the lower level if both the attendee's manager and skip-level manager are present in the meeting.",
            "name": "Workplace Analytics_Redundancy (lower level)",
            "qualifiedName": "Workplace Analytics_Redundancy (lower level)@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "943fcd23-c119-44f9-b63a-cfdf67bb104b": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "e2115e07-9121-42db-8744-ba06d1e86ce5"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "943fcd23-c119-44f9-b63a-cfdf67bb104b",
            "lastModifiedTS": "1",
            "longDescription": "The percentage of measured employees who have a non-blank value for the specified attribute as shown in\u00a0Data sources. If coverage levels are low, it'll be difficult to determine how people collaborate across different characteristics. Additionally, low coverage on required attributes may give skewed (under reported) metric calculations for metrics that rely on those attributes.",
            "name": "Workplace Analytics_Coverage",
            "qualifiedName": "Workplace Analytics_Coverage@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "95f7ebda-8a67-4b59-9978-3e5b10f3f465": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "7f0a7c53-9497-4986-9008-07b9280e355e"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "95f7ebda-8a67-4b59-9978-3e5b10f3f465",
            "lastModifiedTS": "1",
            "longDescription": "The\u00a0measured employee\u00a0for whom the metric is calculated.",
            "name": "Workplace Analytics_Person",
            "qualifiedName": "Workplace Analytics_Person@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "96e939cf-9aaf-46b9-bacb-fbfd98861c50": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "2c217691-6bc4-453e-b904-d2ad7b304233"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "96e939cf-9aaf-46b9-bacb-fbfd98861c50",
            "lastModifiedTS": "1",
            "longDescription": "A person who is invited to a meeting with a meeting request.",
            "name": "Workplace Analytics_Invitee",
            "qualifiedName": "Workplace Analytics_Invitee@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "982f2110-f53d-4c62-96aa-ab8f1754f1b8": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "77849f80-ceba-4ca0-bf89-f7410833adeb"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "982f2110-f53d-4c62-96aa-ab8f1754f1b8",
            "lastModifiedTS": "1",
            "longDescription": "When collaboration happens only with people from within a person\u2019s team, function, department, and so on.",
            "name": "Workplace Analytics_Insularity",
            "qualifiedName": "Workplace Analytics_Insularity@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "9f50e78b-d944-4572-b95e-23ea0dc5391f": {
            "abbreviation": "RA",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "4b8fbf84-f394-4d75-b500-925f6ff2578f"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "9f50e78b-d944-4572-b95e-23ea0dc5391f",
            "lastModifiedTS": "1",
            "longDescription": "Mandatory organizational data attributes that describe the people being analyzed. Required attributes are used in Workplace Analytics to explore, calculate, and customize metrics and filter query results. Required attributes include PersonId, EffectiveDate, ManagerId, LevelDesignation (also referred to as level), and Organization.",
            "name": "Workplace Analytics_Required attribute",
            "qualifiedName": "Workplace Analytics_Required attribute@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "a7327e7b-1164-4f28-a765-150cee46614c": {
            "abbreviation": "LLM",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "7e963cc2-4f42-4342-b5be-337d9eefe55f"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "a7327e7b-1164-4f28-a765-150cee46614c",
            "lastModifiedTS": "1",
            "longDescription": "A long and large meeting has more than eight attendees and is scheduled for longer than one hour.",
            "name": "Workplace Analytics_Long and large meeting",
            "qualifiedName": "Workplace Analytics_Long and large meeting@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "a91e0d7c-9504-44b8-87df-45b953e2b058": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "8de510cd-7455-4b8d-9356-c5e39eb1c3be"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "a91e0d7c-9504-44b8-87df-45b953e2b058",
            "lastModifiedTS": "1",
            "name": "Workplace Analytics",
            "qualifiedName": "Workplace Analytics@Glossary",
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "aa2d5bdd-98d6-499c-a82e-c91594d7e145": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "861f0d52-071a-4493-ab8e-d5de66bc89c0"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "aa2d5bdd-98d6-499c-a82e-c91594d7e145",
            "lastModifiedTS": "1",
            "longDescription": "A defined characteristic about the person, such as team, department, or function.\u00a0Required attributes\u00a0are the subset of attributes that are required in order to calculate metrics.",
            "name": "Workplace Analytics_Attributes",
            "qualifiedName": "Workplace Analytics_Attributes@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "ab66b6dd-3bf3-44e0-a8a4-323e421681cb": {
            "abbreviation": "WH",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "cbcb0fcf-4941-4721-964d-f4d579f0acc3"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "ab66b6dd-3bf3-44e0-a8a4-323e421681cb",
            "lastModifiedTS": "1",
            "longDescription": "Hours that represent the typical workweek for the company. The Workplace Analytics default setting is Monday through Friday from 8:00 AM to 5:00 PM for calculations of working hours. This default is only used for users who have not already set up their working days and hours in Outlook. Your admin can change the default working days and hours in\u00a0Admin settings\u00a0>\u00a0System defaults.",
            "name": "Workplace Analytics_Working hours",
            "qualifiedName": "Workplace Analytics_Working hours@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "ae2e1acb-3b40-406c-9090-350bd6cd36ee": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "9b140cdf-3d82-45f3-909d-c1a08e2b71e9"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "ae2e1acb-3b40-406c-9090-350bd6cd36ee",
            "lastModifiedTS": "1",
            "longDescription": "Two or more\u00a0meaningful interactions.",
            "name": "Workplace Analytics_Connection",
            "qualifiedName": "Workplace Analytics_Connection@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "b14e4e9f-1261-471a-b03a-889cc6bf6da3": {
            "abbreviation": "TI",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "7dcf7f48-c836-4009-8a23-629cd83375c3"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "b14e4e9f-1261-471a-b03a-889cc6bf6da3",
            "lastModifiedTS": "1",
            "longDescription": "A\u00a0measured employee\u00a0who interacts with other collaborators in meetings and with email or instant messages. Time investors allocate their time with the other participants or\u00a0collaborators\u00a0in the interaction in proportion to how many people are in the collaborator group for that interaction. People who do not have a license for Workplace Analytics can appear as collaborators, but never as time investors.",
            "name": "Workplace Analytics_Time investor",
            "qualifiedName": "Workplace Analytics_Time investor@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Alert",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "bff6735b-2c4a-4cb9-97b3-63cf96922fc5": {
            "abbreviation": "FT",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "743fdb23-9091-448c-b42a-c216423fc182"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "bff6735b-2c4a-4cb9-97b3-63cf96922fc5",
            "lastModifiedTS": "1",
            "longDescription": "Uninterrupted time blocks of two hours or more with no meetings.",
            "name": "Workplace Analytics_Focus time",
            "qualifiedName": "Workplace Analytics_Focus time@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "c059801e-5202-4b2c-8c41-6fc82f8404a0": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "6f95e12c-7dc2-4320-beb6-497d34f4a34d"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "c059801e-5202-4b2c-8c41-6fc82f8404a0",
            "lastModifiedTS": "1",
            "longDescription": "A person attended a meeting if they did not decline the meeting request. This means that they either accepted the meeting request, accepted it as\u00a0tentative, or did not respond to it. (This meeting request itself is subsequently referred to as a\u00a0non-declined meeting request.)",
            "name": "Workplace Analytics_Attended",
            "qualifiedName": "Workplace Analytics_Attended@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "c543cc1b-15b1-4741-bcf7-f7f71c1c4b19": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "d8ec18f4-60d2-4bfe-9cb3-449b87cfb974"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "c543cc1b-15b1-4741-bcf7-f7f71c1c4b19",
            "lastModifiedTS": "1",
            "longDescription": "A\u00a0required attribute\u00a0that describes the organizational unit in which the employee resides. The exact value will be determined by the company\u2019s structure, as well as how that structure is captured in within the company\u2019s human resources information system. For example, the organization might also be known as department, function, or defined by a specific manager name in the management hierarchy.\u00a0",
            "name": "Workplace Analytics_Organization",
            "qualifiedName": "Workplace Analytics_Organization@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Expired",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "c7e42d3e-aca4-4f90-9619-e98c921c1dd6": {
            "abbreviation": "NDMR",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "ac8f589b-e2d5-4b30-8dc7-8e05ef8f206f"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "c7e42d3e-aca4-4f90-9619-e98c921c1dd6",
            "lastModifiedTS": "1",
            "longDescription": "In Workplace Analytics, this is synonymous with\u00a0attended.",
            "name": "Workplace Analytics_Non-declined meeting request",
            "qualifiedName": "Workplace Analytics_Non-declined meeting request@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "d389568b-6958-4c6d-a5a7-4345f99d98dc": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "44643ab7-cf32-448d-9bd8-aaad5eb4ff11"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "d389568b-6958-4c6d-a5a7-4345f99d98dc",
            "lastModifiedTS": "1",
            "longDescription": "A person receiving an email (includes people in the to, cc, and bcc lines).",
            "name": "Workplace Analytics_Recipient",
            "qualifiedName": "Workplace Analytics_Recipient@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "e38c8012-1d3f-4891-b542-cad59f29b329": {
            "abbreviation": "MI",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "55d40650-1713-47f0-b1d3-5d91f62b3eba"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "e38c8012-1d3f-4891-b542-cad59f29b329",
            "lastModifiedTS": "1",
            "longDescription": "A meaningful interaction is defined as one of the following types of collaboration: an email, a meeting, a call, three instant messages. These messages could be sent by any of the collaborators in the chat. For example, they could be: (a) three messages sent by one individual to others in Teams, or (b) three distinct messages from distinct senders within the same Teams chat.",
            "name": "Workplace Analytics_Meaningful interaction",
            "qualifiedName": "Workplace Analytics_Meaningful interaction@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "e71b6629-da94-47ee-b307-69c020f15d9e": {
            "abbreviation": "TZ",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "ada17e8a-5f52-43fc-8c54-e2b9cd5199fb"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "e71b6629-da94-47ee-b307-69c020f15d9e",
            "lastModifiedTS": "1",
            "longDescription": "Workplace Analytics uses these\u00a0time zones. Personal metrics (person query results) are calculated by using the person\u2019s time zone. Meeting metrics (meeting query results) are calculated by using the organizer\u2019s time zone.",
            "name": "Workplace Analytics_Time zones",
            "qualifiedName": "Workplace Analytics_Time zones@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Draft",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "e9434e1f-b8df-4f6e-a8a8-38df63b84a26": {
            "abbreviation": "OA",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "21d1cfd0-2666-4728-9455-947e858dffd3"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "e9434e1f-b8df-4f6e-a8a8-38df63b84a26",
            "lastModifiedTS": "1",
            "longDescription": "Optional\u00a0organizational data\u00a0attributes that describe the people being analyzed. If supplied by the company, you can use these attributes to explore metrics, filter queries, and customize metrics.\u00a0These can be reserved for future metric calculations. Optional attributes include FunctionType, HireDate, HourlyRate, Layer, and TimeZone.",
            "name": "Workplace Analytics_Optional attribute",
            "qualifiedName": "Workplace Analytics_Optional attribute@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "ed696cbc-e425-403b-a0ea-74f124cb5ff2": {
            "abbreviation": "ME",
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "c5c207e8-c571-4da7-b74c-76b59c09d0f9"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "ed696cbc-e425-403b-a0ea-74f124cb5ff2",
            "lastModifiedTS": "1",
            "longDescription": "The employees to whom your Workplace Analytics administrator assigned licenses during setup. After license assignment, Workplace Analytics extracts Microsoft 365 data about meetings, email, unscheduled calls, and instant messages for these people. If you are an analyst or limited analyst, this is the population that you can analyze within Workplace Analytics. The number of measured employees can help determine whether you have good data coverage for analysis.",
            "name": "Workplace Analytics_Measured employees",
            "qualifiedName": "Workplace Analytics_Measured employees@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        },
        "fc32444a-86d9-481d-a9a9-23ca3d196500": {
            "anchor": {
                "glossaryGuid": "f2307f48-5834-4709-be85-02f3aea5d149",
                "relationGuid": "d211efe0-bb2d-4c79-8377-698e117151a7"
            },
            "createTime": 1642161716110,
            "createdBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd",
            "guid": "fc32444a-86d9-481d-a9a9-23ca3d196500",
            "lastModifiedTS": "1",
            "longDescription": "The person who sends an email.",
            "name": "Workplace Analytics_Sender",
            "qualifiedName": "Workplace Analytics_Sender@Glossary",
            "resources": [
                {
                    "displayName": "Workspace Analytics",
                    "url": "https://docs.microsoft.com/en-us/workplace-analytics/use/glossary"
                }
            ],
            "status": "Approved",
            "updateTime": 1642161716110,
            "updatedBy": "d8a669d2-5a08-4fb6-b169-0ba162ae7fbd"
        }
    },
    "terms": [
        {
            "displayText": "Workplace Analytics_Insularity",
            "relationGuid": "77849f80-ceba-4ca0-bf89-f7410833adeb",
            "termGuid": "982f2110-f53d-4c62-96aa-ab8f1754f1b8"
        },
        {
            "displayText": "Workplace Analytics_Collaborator group",
            "relationGuid": "b13bd0f2-5729-4999-a31c-08c71c59312e",
            "termGuid": "7770ef0f-74e0-43a1-bb6a-8eab9d5dce13"
        },
        {
            "displayText": "Workplace Analytics_Adjusted meeting hours",
            "relationGuid": "5a1caddc-5401-4b9f-96b1-6f87b9e8583e",
            "termGuid": "21b5e0b7-1b24-4804-ac73-089004d46e95"
        },
        {
            "displayText": "Workplace Analytics_Collaborators",
            "relationGuid": "4a3bc643-42e8-42b7-91f9-24b97be5a795",
            "termGuid": "8a2f1d84-b953-43de-bcf0-42a0f92faa5c"
        },
        {
            "displayText": "Workplace Analytics_Multitasking",
            "relationGuid": "d78b3534-9d41-4eee-920f-9e9c3273eaa2",
            "termGuid": "60fb2c1c-005c-462b-b5e1-e6421328565e"
        },
        {
            "displayText": "Workplace Analytics_Connection",
            "relationGuid": "9b140cdf-3d82-45f3-909d-c1a08e2b71e9",
            "termGuid": "ae2e1acb-3b40-406c-9090-350bd6cd36ee"
        },
        {
            "displayText": "Workplace Analytics_Measured employees",
            "relationGuid": "c5c207e8-c571-4da7-b74c-76b59c09d0f9",
            "termGuid": "ed696cbc-e425-403b-a0ea-74f124cb5ff2"
        },
        {
            "displayText": "Workplace Analytics_Attendee",
            "relationGuid": "42435356-b3eb-49ee-b3ae-23676f43b4ba",
            "termGuid": "09a7f806-8612-4de4-b87a-5481f6e2878c"
        },
        {
            "displayText": "Workplace Analytics_Required attribute",
            "relationGuid": "4b8fbf84-f394-4d75-b500-925f6ff2578f",
            "termGuid": "9f50e78b-d944-4572-b95e-23ea0dc5391f"
        },
        {
            "displayText": "Workplace Analytics_Call",
            "relationGuid": "a9fd4002-a837-45e0-bd2b-100890a46d56",
            "termGuid": "102f72ff-b231-4df0-9b91-2583f430e5f1"
        },
        {
            "displayText": "Workplace Analytics_Conflicting meeting",
            "relationGuid": "b290ffa4-400f-4b1c-adde-41a315e7dcc4",
            "termGuid": "17f6bb31-3787-4001-b172-1fe425359f49"
        },
        {
            "displayText": "Workplace Analytics_Connected groups",
            "relationGuid": "f33b9a2b-373c-44b4-a94b-7b9a8104ccf6",
            "termGuid": "5a3358e6-ebf9-4d26-965f-87e1e6ecf52e"
        },
        {
            "displayText": "Workplace Analytics_Redundancy (organizational)",
            "relationGuid": "91237131-3b1f-43ea-9698-c6a32d665c47",
            "termGuid": "802fd63f-d3ba-40cf-a619-444ef9a34afc"
        },
        {
            "displayText": "Workplace Analytics_Organizational data",
            "relationGuid": "eb3eb201-57c5-4a33-bec7-b3095c1a2c1c",
            "termGuid": "78b536fb-813b-4e66-9c65-0422d5daa4d2"
        },
        {
            "displayText": "Workplace Analytics_People meeting hours",
            "relationGuid": "c4c949ca-3049-4662-9b27-6cff3b2ed404",
            "termGuid": "6c4a2a0a-6cf3-4d01-b70c-a9461dfe971b"
        },
        {
            "displayText": "Workplace Analytics_Invitee",
            "relationGuid": "2c217691-6bc4-453e-b904-d2ad7b304233",
            "termGuid": "96e939cf-9aaf-46b9-bacb-fbfd98861c50"
        },
        {
            "displayText": "Workplace Analytics_Fragmented hours",
            "relationGuid": "1e4719bd-d6cb-4664-a471-e12966ffe4d6",
            "termGuid": "5da6c9a6-7567-45fe-aa05-5cccfdbc23d2"
        },
        {
            "displayText": "Workplace Analytics_Common network",
            "relationGuid": "b77ebec8-61b4-44c6-94f5-f404955d9497",
            "termGuid": "4f2fa1a2-e7d3-4ac1-ad5d-e178f23973f4"
        },
        {
            "displayText": "Workplace Analytics_Working hours",
            "relationGuid": "cbcb0fcf-4941-4721-964d-f4d579f0acc3",
            "termGuid": "ab66b6dd-3bf3-44e0-a8a4-323e421681cb"
        },
        {
            "displayText": "Workplace Analytics_Time investor",
            "relationGuid": "7dcf7f48-c836-4009-8a23-629cd83375c3",
            "termGuid": "b14e4e9f-1261-471a-b03a-889cc6bf6da3"
        },
        {
            "displayText": "Workplace Analytics_Layer",
            "relationGuid": "b751001e-a6c5-413c-8d23-2c9a707c5b9b",
            "termGuid": "12e206ee-5b98-475d-ab7e-e827d38367bf"
        },
        {
            "displayText": "Workplace Analytics_Recipient",
            "relationGuid": "44643ab7-cf32-448d-9bd8-aaad5eb4ff11",
            "termGuid": "d389568b-6958-4c6d-a5a7-4345f99d98dc"
        },
        {
            "displayText": "Workplace Analytics_Level",
            "relationGuid": "af986a4f-a56f-462c-a3d2-b0f5bcca4147",
            "termGuid": "158674b1-129b-4e8b-b165-5b7eeae37e90"
        },
        {
            "displayText": "Workplace Analytics",
            "relationGuid": "8de510cd-7455-4b8d-9356-c5e39eb1c3be",
            "termGuid": "a91e0d7c-9504-44b8-87df-45b953e2b058"
        },
        {
            "displayText": "Workplace Analytics_Non-declined meeting request",
            "relationGuid": "ac8f589b-e2d5-4b30-8dc7-8e05ef8f206f",
            "termGuid": "c7e42d3e-aca4-4f90-9619-e98c921c1dd6"
        },
        {
            "displayText": "Workplace Analytics_Large meeting",
            "relationGuid": "666e19fe-6def-448d-a629-e754ea81c31f",
            "termGuid": "8aae8706-1d0f-4ee9-8d5a-27a9d824f3df"
        },
        {
            "displayText": "Workplace Analytics_Decision-making meeting",
            "relationGuid": "4a5da1da-c187-4508-ab9e-6fcd88ee17aa",
            "termGuid": "26ec957d-834b-491b-a5c5-71cb78369dda"
        },
        {
            "displayText": "Workplace Analytics_Focus time",
            "relationGuid": "743fdb23-9091-448c-b42a-c216423fc182",
            "termGuid": "bff6735b-2c4a-4cb9-97b3-63cf96922fc5"
        },
        {
            "displayText": "Workplace Analytics_Person",
            "relationGuid": "7f0a7c53-9497-4986-9008-07b9280e355e",
            "termGuid": "95f7ebda-8a67-4b59-9978-3e5b10f3f465"
        },
        {
            "displayText": "Workplace Analytics_Long meeting",
            "relationGuid": "618093ba-f2c1-47bc-b684-0d2e80c5c6d2",
            "termGuid": "81ef18f0-7a49-4fc8-a24a-283d26a8a127"
        },
        {
            "displayText": "Workplace Analytics_Custom attribute",
            "relationGuid": "d75df161-19b0-41a2-8b60-36332b0ecc7e",
            "termGuid": "4b1ac875-260e-4dcd-96f8-e843bd437587"
        },
        {
            "displayText": "Workplace Analytics_Calendar fragmentation",
            "relationGuid": "b00497da-83ce-49d5-acf6-d6371e9c6a4d",
            "termGuid": "2584bf5a-7df4-402f-b427-92c0f85be892"
        },
        {
            "displayText": "Workplace Analytics_Personal data",
            "relationGuid": "a7c58708-35ed-4718-919a-fe33bdc8f67d",
            "termGuid": "67703464-7e08-4db4-ad1c-59d03f4a5d49"
        },
        {
            "displayText": "Workplace Analytics_De-identification",
            "relationGuid": "bb9943a0-5153-4b4e-9179-c5359433c191",
            "termGuid": "2bbd7ff5-0142-4fad-aa2e-5fdf492f8a58"
        },
        {
            "displayText": "Workplace Analytics_Meaningful interaction",
            "relationGuid": "55d40650-1713-47f0-b1d3-5d91f62b3eba",
            "termGuid": "e38c8012-1d3f-4891-b542-cad59f29b329"
        },
        {
            "displayText": "Workplace Analytics_Connected people",
            "relationGuid": "8b359c38-b353-4f7a-b03c-8272d8f307ab",
            "termGuid": "1a391268-9058-46ec-b924-14c1b5eac572"
        },
        {
            "displayText": "Workplace Analytics_Attended",
            "relationGuid": "6f95e12c-7dc2-4320-beb6-497d34f4a34d",
            "termGuid": "c059801e-5202-4b2c-8c41-6fc82f8404a0"
        },
        {
            "displayText": "Workplace Analytics_Redundancy (lower level)",
            "relationGuid": "ca98292e-64c9-4c00-be42-64142905eb5a",
            "termGuid": "8bf2fbd9-a0a7-444b-8900-d62c2c3059de"
        },
        {
            "displayText": "Workplace Analytics_Organizer",
            "relationGuid": "6b338bdd-62d7-4701-9a23-c79d90be5320",
            "termGuid": "1b402853-8a6c-4a1a-9064-290d26b7e736"
        },
        {
            "displayText": "Workplace Analytics_Attributes",
            "relationGuid": "861f0d52-071a-4493-ab8e-d5de66bc89c0",
            "termGuid": "aa2d5bdd-98d6-499c-a82e-c91594d7e145"
        },
        {
            "displayText": "Workplace Analytics_Aggregation",
            "relationGuid": "a7a378ef-a2a5-4b56-bd19-4f84f4b32446",
            "termGuid": "2dea0df8-959d-455d-8283-1582c770e80e"
        },
        {
            "displayText": "Workplace Analytics_Span",
            "relationGuid": "64c795e0-1d8c-4436-ae91-7f1f171e0e4f",
            "termGuid": "61d1aa8f-7aed-4866-b563-5108ba5c67e7"
        },
        {
            "displayText": "Workplace Analytics_Optional attribute",
            "relationGuid": "21d1cfd0-2666-4728-9455-947e858dffd3",
            "termGuid": "e9434e1f-b8df-4f6e-a8a8-38df63b84a26"
        },
        {
            "displayText": "Workplace Analytics_Organization",
            "relationGuid": "d8ec18f4-60d2-4bfe-9cb3-449b87cfb974",
            "termGuid": "c543cc1b-15b1-4741-bcf7-f7f71c1c4b19"
        },
        {
            "displayText": "Workplace Analytics_Meeting",
            "relationGuid": "f870d163-c9de-4cbd-8b29-41bd33c9612a",
            "termGuid": "0d8c0610-4c8b-4f90-b18b-e85d688eb2e6"
        },
        {
            "displayText": "Workplace Analytics_Hashing",
            "relationGuid": "1a121daa-d4eb-4340-9175-5f72e372b065",
            "termGuid": "7804d73c-d047-45ab-9728-87f53a842613"
        },
        {
            "displayText": "Workplace Analytics_Sender",
            "relationGuid": "d211efe0-bb2d-4c79-8377-698e117151a7",
            "termGuid": "fc32444a-86d9-481d-a9a9-23ca3d196500"
        },
        {
            "displayText": "Workplace Analytics_Time zones",
            "relationGuid": "ada17e8a-5f52-43fc-8c54-e2b9cd5199fb",
            "termGuid": "e71b6629-da94-47ee-b307-69c020f15d9e"
        },
        {
            "displayText": "Workplace Analytics_Pseudonymized",
            "relationGuid": "89973b52-33a6-4c6b-939d-b6b4f1a50d8b",
            "termGuid": "079658e3-d0ca-41f2-a716-f277873c2c29"
        },
        {
            "displayText": "Workplace Analytics_Coverage",
            "relationGuid": "e2115e07-9121-42db-8744-ba06d1e86ce5",
            "termGuid": "943fcd23-c119-44f9-b63a-cfdf67bb104b"
        },
        {
            "displayText": "Workplace Analytics_Long and large meeting",
            "relationGuid": "7e963cc2-4f42-4342-b5be-337d9eefe55f",
            "termGuid": "a7327e7b-1164-4f28-a765-150cee46614c"
        }
    ]
}
```
</p>
</details>