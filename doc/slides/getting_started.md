---
marp: true
theme: uncover
---
# Azure Purview CLI

`purviewcli`

---

<!-- _class: left -->
<!-- _footer: "Azure Purview High-Level Concepts" -->

![bg width:95%](https://raw.githubusercontent.com/tayganr/purviewcli/master/doc/image/purview_components.png)

<style>
section.left h4, section.left p {
  text-align: left;
}
</style>

---
<!-- paginate: true -->

## What is purviewcli?

`purviewcli` is a Python package that provides a cross-platform command line interface (CLI) to Azure Purview. Suitable for ad-hoc tasks and quick exploratory operations.

---

<!-- _class: left -->
<!-- _footer: "Python Package Index (PyPi) https://pypi.org/project/purviewcli/" -->

#### Installation

`pip install purviewcli`

<style>
section.left h4, section.left p {
  text-align: left;
}
</style>

---

<!-- _class: left -->
<!-- _footer: ":star: `PURVIEW_NAME` is mandatory, all other environment variables are optional." -->

#### Environment Variables

|Environment Variable|Description|
|:---|:---|
|`PURVIEW_NAME` (:star:)|Azure Purview account name.|
|`AZURE_CLIENT_ID`|The Azure AD tenant(directory) ID.|
|`AZURE_TENANT_ID`|Client(application) ID of an App Registration.|
|`AZURE_CLIENT_SECRET`|Client secret generated for the App Registration.|
|`AZURE_CLIENT_CERTIFICATE_PATH`|A path to certificate and private key pair.|
|`AZURE_USERNAME`|The username(upn) of an Azure AD user account.|
|`AZURE_PASSWORD`|The password of the Azure AD user account.|

<style>
table {
    font-size: 22px
}
</style>

---

<!-- _class: left -->
<!-- _footer: "azure-identity https://docs.microsoft.com/en-us/python/api/overview/azure/identity-readme" -->

#### Authentication

The `purviewcli` package leverages `DefaultAzureCredential` from [azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity#defaultazurecredential). `purviewcli` will attempt to authenticate via the following mechanisms in this order, stopping when one succeeds.
|Mechanism |Description|
|:---|:---|
|Environment|If account information has been specified via Environment Variables, purviewcli will use it to authenticate.|
|Managed Identity|If deployed to an Azure host with Managed Identity enabled, purviewcli will authenticate with it. |
|Visual Studio Code|If a user has signed in to the Visual Studio Code Azure Account extension, purviewcli will authenticate as that user.|
|Azure CLI|If a user has signed in via the Azure CLI `az login` command, purviewcli will authenticate as that user.|

<!-- Scoped style -->
<style scoped>
p {
  font-size: 22px;
}
ul {
    text-align: left;
}
table {
    font-size: 20px
}
</style>

---

<!-- _class: left -->
<!-- _footer: "Catalog Permissions https://docs.microsoft.com/en-us/azure/purview/catalog-permissions" -->

#### Authorization

The identity executing Azure Purview CLI commands will require the following role assignments:

|Role |Description|
|:---|:---|
|Purview Data Curator|Has access to the Purview portal and can read all content in Azure Purview except for scan bindings, can edit information about assets, can edit classification definitions and glossary terms, and can apply classifications and glossary terms to assets..|
|Purview Data Source Administrator|Does not have access to the Purview Portal (the user needs to also be in the Data Reader or Data Curator roles) and can manage all aspects of scanning data into Azure Purview but does not have read or write access to content in Azure Purview beyond those related to scanning.|

<!-- Scoped style -->
<style scoped>
p {
  font-size: 22px;
}
table {
    font-size: 20px
}
</style>

---

<!-- _class: left -->
<!-- _footer: "`pv --help`" -->

#### Commands

|Commands|Description|
|:---|:---|
|`pv entity`|Entities are a collection of attributes that model or represent an asset.|
|`pv glossary`|A glossary provides vocabulary for business users.|
|`pv lineage`|Understand the data's origin and where it moves over time.|
|`pv relationship`|Relationships describe connections between two entities.|
|`pv types`|A Type is a definition of how a particular object type is stored.|
|`pv scan`|Azure Purview scan.|
|`pv insight`|Azure Purview insights.|
|`pv search`|Azure Purview advanced search.|

<!-- Scoped style -->
<style scoped>
p {
  font-size: 22px;
}
ol {
  font-size: 22px;
}
</style>

---

<!-- _class: left -->
<!-- _footer: "GitHub https://aka.ms/purviewcli" -->

#### Usage

```python
pv command sub-command --parameter1='value' --parameter2='value'
```

- All parameters are required by default.
- Parameters enclosed with square brackets "**[ ]**" are optional.
- Mutually exclusive parameters are enclosed with parens "**( )**" and separated with a pipe "**|**".
- The "=&lt;val&gt;" indicates parameters which require an input (e.g. --parameter=&lt;val&gt;). Input can be specified after a space (e.g. --parameter 'value') or equal "=" sign (e.g. --parameter='value').
- Parameters that do not require an input are boolean operators and are **False** by default and **True** if present (e.g. --ignoreRelationships).
- The ellipsis "**...**" indicates parameters that are allowed to repeat (e.g. --guid='12345' --guid='23451' --guid='34512')

<!-- Scoped style -->
<style scoped>
ul {
  font-size: 22px;
}
</style>

---

<!-- _class: left -->
<!-- _footer: "Notebook Samples: https://github.com/tayganr/purviewcli/tree/master/samples" -->

#### Example

An example of how you can get started with `purviewcli` within a Jupyter Notebook.

 1. Install purviewcli
 2. Set Environment Variables
 3. Execute Command

![bg right fit](https://raw.githubusercontent.com/tayganr/purviewcli/master/doc/image/purviewcli_notebook.png)

<!-- Scoped style -->
<style scoped>
p {
  font-size: 22px;
}
ol {
  font-size: 22px;
}
</style>

---

<!-- _class: left -->
<!-- _footer: "https://aka.ms/purviewcli" -->

## Thank You :wave:
