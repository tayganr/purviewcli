# Share
[Command Reference](../../../README.md#command-reference) > share

## Sent Shares
| Command | Description |
| --- | --- |
| [pv share listSentShares](./listSentShares.md) | Get list of sent shares in the given Purview account. |
| [pv share createSentShare](./createSentShare.md) | Create a sent share in the given Purview account. |
| [pv share deleteSentShare](./deleteSentShare.md) | Deletes a sent share. |
| [pv share getSentShare](./getSentShare.md) | Get a sent share in the given Purview account. |

## Accepted Sent Shares
| Command | Description |
| --- | --- |
| [pv share listAcceptedShares](./listAcceptedShares.md) | List of accepted shares for the current sent share. |
| [pv share getAcceptedShare](./getAcceptedShare.md) | Get an accepted share with acceptedSentShareName to a particular sent share. |
| [pv share reinstateAcceptedShare](./reinstateAcceptedShare.md) | Reinstate a revoked accepted sent share. |
| [pv share revokeAcceptedShare](./revokeAcceptedShare.md) | Revoke an accepted sent share's access. |
| [pv share updateExpirationAcceptedShare](./updateExpirationAcceptedShare.md) | Update the expiration date of an active accepted sent share. |

## Sent Invitations
| Command | Description |
| --- | --- |
| [pv share listSentInvitations](./listSentInvitations.md) | List all Invitations in a share. |
| [pv share createSentInvitation](./createSentInvitation.md) | Create/Update a sent share invitation in the given account. |
| [pv share deleteSentInvitation](./deleteSentInvitation.md) | Delete Invitation in a share. |
| [pv share getSentInvitation](./getSentInvitation.md) | Get Invitation for a given share. |

## Received Shares
| Command | Description |
| --- | --- |
| [pv share listReceivedShares](./listReceivedShares.md) | Get a list of received shares. |
| [pv share createReceivedShare](./createReceivedShare.md) | Create a received share in the given account. |
| [pv share deleteReceivedShare](./deleteReceivedShare.md) | Deletes a received share. |
| [pv share getReceivedShare](./getReceivedShare.md) | Get a received share by name. |

## Received Invitations
| Command | Description |
| --- | --- |
| [pv share listReceivedInvitations](./listReceivedInvitations.md) | Lists the received invitations. |
| [pv share getReceivedInvitation](./getReceivedInvitation.md) | Gets the received invitation identified by name. |
| [pv share rejectReceivedInvitation](./rejectReceivedInvitation.md) | Rejects the received invitation identified by name. |

## Asset Mappings
| Command | Description |
| --- | --- |
| [pv share listAssetMappings](./listAssetMappings.md) | List AssetMappings in a received share. |
| [pv share createAssetMapping](./createAssetMapping.md) | Maps a source asset in the sent share to a destination asset in the received share. |
| [pv share deleteAssetMapping](./deleteAssetMapping.md) | Delete AssetMapping in a receivedShare. |
| [pv share getAssetMapping](./getAssetMapping.md) | Get AssetMapping in a receivedShare. |

## Assets
| Command | Description |
| --- | --- |
| [pv share listAssets](./listAssets.md) | List Assets in a share. |
| [pv share createAsset](./createAsset.md) | Adds a new asset to an existing share. |
| [pv share deleteAsset](./deleteAsset.md) | Delete asset in a sentShare. |
| [pv share getAsset](./getAsset.md) | Get asset in a sentShare. |
| [pv share listReceivedAssets](./listReceivedAssets.md) | List source asset of a received share. |

## Email Registration
| Command | Description |
| --- | --- |
| [pv share activateEmail](./activateEmail.md) | Activates the tenant and email combination using the activation code received. |
| [pv share registerEmail](./registerEmail.md) | Registers the tenant and email combination for activation. |

## ER Diagram #1

```mermaid
erDiagram
    purviewAccount ||--o{ collections : has
    purviewAccount ||--o{ receivedInvitations : has
    collections ||--o{ sentShares : has
    collections ||--o{ receivedShares : has
    receivedShares ||--o{ assetMappings : has
    receivedShares ||--o{ receivedAssets : has
    sentShares || --o{ assets : has
    sentShares || --o{ sentShareInvitations : has
    sentShares ||--o{ acceptedSentShares : has
```

## ER Diagram #2

*Includes properties, data types, and example values.*

```mermaid
erDiagram
    purviewAccount ||--o{ collections : has
    purviewAccount ||--o{ receivedInvitations : has
    collections ||--o{ sentShares : has
    collections ||--o{ receivedShares : has
    receivedShares ||--o{ assetMappings : has
    receivedShares ||--o{ receivedAssets : has
    sentShares || --o{ assets : has
    sentShares || --o{ sentShareInvitations : has
    sentShares ||--o{ acceptedSentShares : has
    receivedInvitations {
        string id "/receivedInvitations/0acdde01-bdbd-49e1-b3d8-275d62b9b9bc"
        string invitationKind "User"
        string name "0acdde01-bdbd-49e1-b3d8-275d62b9b9bc"
        string description "This is a description."
        string invitationStatus "Pending"
        string location "northeurope"
        string receiverEmail "tarifat@microsoft.com"
        string receiverName
        string receiverTenantName
        string senderEmail "tarifat@microsoft.com"
        string senderName "Taygan Rifat"
        string senderTenantName "Microsoft"
        date sentAt "2022-09-02T13:38:29.3185176Z"
        string sentShareName "NewShare"
        string shareKind "InPlace"
        string targetEmail "tarifat@microsoft.com"
        string type "receivedInvitations"
    }
    sentShares {
        string id "/sentShares/NewShare"
        string name "NewShare"
        string collection_referenceName "qrzdyx"
        string collection_type "CollectionReference"
        date createdAt "2022-09-01T16:48:25.0489591Z"
        string description "This is a description."
        string provisioningState "Succeeded"
        string senderEmail "tarifat@microsoft.com"
        string senderName "Taygan Rifat"
        string senderTenantName "Microsoft"
        string shareKind "InPlace"
        string type "sentShares"
    }
    acceptedSentShares {
        string id "/sentShares/NewShare/acceptedSentShares/be2c3f1d-ac06-4aca-a5f8-28b44cad17ef"
        string name "be2c3f1d-ac06-4aca-a5f8-28b44cad17ef"
        string createdAt "2022-09-02T13:28:13.1922869Z"
        string expirationDate "null"
        string receivedShareStatus "Active"
        string receiverEmail "tarifat@microsoft.com"
        string receiverName "Taygan Rifat"
        string receiverTargetObjectId "095354ff-cae8-44ff-8120-22ec5a941b40"
        string receiverTenantName "Microsoft"
        string senderEmail "tarifat@microsoft.com"
        string senderName "Taygan Rifat"
        string senderTenantName "Microsoft"
        string sharedAt "2022-09-01T16:48:25.7585096Z"
        string shareKind "InPlace"
        string type "sentShares/acceptedSentShares"
    }
    receivedShares {
        string id "/receivedShares/NewShare"
        string name "NewShare"
        string collection_referenceName "pvdemo52dg4-pv"
        string collection_type "CollectionReference"
        string createdAt "2022-09-02T13:28:13.1922869Z"
        string invitationId "037ac95e-98a4-4b6a-aba7-7f915ab72497"
        string provisioningState "Succeeded"
        string receivedShareStatus "Active"
        string receiverEmail "tarifat@microsoft.com"
        string receiverName "Taygan Rifat"
        string receiverTenantName "Microsoft"
        string senderEmail "tarifat@microsoft.com"
        string senderName "Taygan Rifat"
        string senderTenantName "Microsoft"
        string sentShareDescription "This is a description."
        string sentShareLocation "northeurope"
        string shareName "NewShare"
        string sharedAt "2022-09-01T16:48:25.7585096Z"
        string shareKind "InPlace"
        string type "receivedShares"
    }
    assetMappings {
        string id "/receivedShares/MyShare/assetMappings/storagedatashare01"
        string kind "BlobAccount"
        string name "storagedatashare01"
        string assetId "f4a4d0f9-d3db-4c80-944e-fe692705f27f"
        string assetMappingStatus "Broken"
        string containerName "customer"
        string folder "helloWorld"
        string location "uksouth"
        string mountPath ""
        string provisioningState "Succeeded"
        string storageAccountResourceId "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pv-7643-rg/providers/Microsoft.Storage/storageAccounts/storagedatashare01"
        string type "receivedShares/assetMappings"
    }
    receivedAssets {
        string id "/receivedShares/NewShare/receivedAssets/6408e9cb-273a-49c7-8e2d-c89e928fd197"
        string kind "BlobAccount"
        string name "6408e9cb-273a-49c7-8e2d-c89e928fd197"
        string location "uksouth"
        string receiverAssetName "assetName"
        string receiverPaths "['products.csv']"
        string type "receivedShares/receivedAssets"
    }
    sentShareInvitations {
        string id "/sentShares/NewShare/sentShareInvitations/607c8df07dc82107ccab50bd1b8c792279b1d9fc"
        string invitationKind "User"
        string name "607c8df07dc82107ccab50bd1b8c792279b1d9fc"
        string invitationId "47d63726-9373-417e-94a2-85afad2edd3e"
        string invitationStatus "Pending"
        string provisioningState "Succeeded"
        string senderEmail "tarifat@microsoft.com"
        string senderName "Taygan Rifat"
        string senderTenantName "Microsoft"
        string sentAt "2022-09-02T13:31:32.6057188Z"
        string shareKind "InPlace"
        string targetEmail "taygan.rifat@microsoft.com"
        string type "sentShares/sentShareInvitations"
    }
    assets {
        string id "/sentShares/NewShare/assets/assetName"
        string kind "BlobAccount"
        string name "assetName"
        string location "uksouth"
        string paths "[{'containerName':'products','receiverPath':'products.csv','senderPath':'products.csv'}]"
        string provisioningState "Succeeded"
        string receiverAssetName "assetName"
        string storageAccountResourceId "/subscriptions/2c334b6c-e556-40ac-a4c0-c0d1d2e08ca0/resourceGroups/pv-7643-rg/providers/Microsoft.Storage/storageAccounts/storagedatashare01"
        string type "sentShares/assets"
    }
```