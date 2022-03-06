# Azure Purview CLI

This package provides a command line interface to Azure Purview's REST API.  
![purviewcli](./doc/image/purviewcli_example.png)

## Getting Started

[Getting Started](./doc/md/guide.md) - how to install, setup, and use purviewcli.

## Installation

```
pip install purviewcli
```

## Usage

```
pv command sub-command --parameter1='value' --parameter2='value'
```

## Parameter Types

* All parameters are required by default.
* Parameters enclosed with square brackets "**[ ]**" are optional.
* Mutually exclusive parameters are enclosed with parens "**( )**" and separated with a pipe "**|**".
* The "=&lt;val&gt;" indicates parameters which require an input (e.g. --parameter=&lt;val&gt;). Input can be specified after a space (e.g. --parameter 'value') or equal "**=**" sign (e.g. --parameter='value').
* Parameters that do not require an input are **False** by default and **True** if present (e.g. --ignoreRelationships).
* The ellipsis "**...**" indicates parameters that are allowed to repeat (e.g. --guid='12345' --guid='23451' --guid='34512')

## Command Reference

Control Plane (Azure Resource Manager)

| Command | Surface Area |
| --- | --- |
| [pv management](./doc/commands/management/main.md) | `Account`, `Private Endpoint`, `Other` |

Data Plane (Apache Atlas)
| Command | Surface Area |
| --- | --- |
| [pv entity](./doc/commands/entity/main.md) | `Classification`, `Entity` |
| [pv glossary](./doc/commands/glossary/main.md) | `Glossary`, `Terms`, `Categories` |
| [pv lineage](./doc/commands/lineage/main.md) | `Lineage` |
| [pv relationship](./doc/commands/relationship/main.md) | `Relationship` |
| [pv types](./doc/commands/types/main.md) | `Type Definitions` (Classification, Entity, Enum, Relationship, Struct, and Term Template) |

Data Plane (Other)
| Command | Surface Area |
| --- | --- |
| [pv account](./doc/commands/account/main.md) | `Account`, `Collection`, `Resource Set Rule` |
| [pv insight](./doc/commands/insight/main.md) | `Asset`, `Scan` |
| [pv policystore](./doc/commands/policystore/main.md) | `Metadata Policies`, `Data Policies` |
| [pv scan](./doc/commands/scan/main.md) | `Classification Rule`, `Credential`, `Data Source`, `Scan`, `Scan Filter`, `Scan Ruleset`, `Scan Trigger` |
| [pv search](./doc/commands/search/main.md) | `Search` |