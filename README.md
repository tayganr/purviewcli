# Azure Purview CLI

This package provides a command line interface to Azure Purview's REST API.  
![purviewcli](./doc/image/purviewcli_example.png)

## Getting Started

[Getting Started](./doc/md/guide.md) for guidance on how to install, setup, and use purviewcli.

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

* pv entity
* pv glossary
* pv lineage
* pv relationship
* pv types
* pv account
* pv credential
* pv insight
* pv management
* pv policystore
* pv scan
* [pv search](./doc/commands/search/main.md)