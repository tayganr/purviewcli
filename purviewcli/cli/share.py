"""
usage: 
    pv share listAcceptedShares --sentShareName=<val> [--skipToken=<val>]
    pv share getAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val>
    pv share reinstateAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val> --payloadFile=<val>
    pv share revokeAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val>
    pv share updateExpirationAcceptedShare --sentShareName=<val> --acceptedSentShareName=<val> --payloadFile=<val>
    pv share listAssetMappings --receivedShareName=<val> [--skipToken=<val> --filter=<val> --orderBy=<val>]
    pv share createAssetMapping --receivedShareName=<val> --assetMappingName=<val> --payloadFile=<val>
    pv share deleteAssetMapping --receivedShareName=<val> --assetMappingName=<val>
    pv share getAssetMapping --receivedShareName=<val> --assetMappingName=<val>
    pv share listAssets --sentShareName=<val> [--skipToken=<val> --filter=<val> --orderBy=<val>]
    pv share createAsset --sentShareName=<val> --assetName=<val> --payloadFile=<val>
    pv share deleteAsset --sentShareName=<val> --assetName=<val>
    pv share getAsset --sentShareName=<val> --assetName=<val>
    pv share activateEmail --payloadFile=<val>
    pv share registerEmail
    pv share listReceivedAssets --receivedShareName=<val> [--skipToken=<val>]
    pv share listReceivedInvitations [--skipToken=<val> --filter=<val> --orderBy=<val>]
    pv share getReceivedInvitation --invitationName=<val>
    pv share rejectReceivedInvitation --invitationName=<val> --payloadFile=<val>
    pv share listReceivedShares [--skipToken=<val> --filter=<val> --orderBy=<val>]
    pv share createReceivedShare --receivedShareName=<val> --payloadFile=<val>
    pv share deleteReceivedShare --receivedShareName=<val>
    pv share getReceivedShare --receivedShareName=<val>
    pv share listSentInvitations --sentShareName=<val> [--skipToken=<val> --filter=<val> --orderBy=<val>]
    pv share createSentInvitation --sentShareName=<val> --invitationName=<val> --payloadFile=<val>
    pv share deleteSentInvitation --sentShareName=<val> --invitationName=<val>
    pv share getSentInvitation --sentShareName=<val> --invitationName=<val>
    pv share listSentShares [--skipToken=<val> --filter=<val> --orderBy=<val>]
    pv share createSentShare --sentShareName=<val> --payloadFile=<val>
    pv share deleteSentShare --sentShareName=<val>
    pv share getSentShare --sentShareName=<val>


options:
    --purviewName=<val>           [string]  The name of the Microsoft Purview account.
    --receivedShareName=<val>     [string]  The name of the received share.
    --sentShareName=<val>         [string]  The name of the sent share.
    --acceptedSentShareName=<val> [string]  The name of the accepted sent share.
    --assetMappingName=<val>      [string]  The name of the asset mapping.
    --assetName=<val>             [string]  The name of the asset.
    --invitationName=<val>        [string]  The name of the invitation.
    --skipToken=<val>             [string]  The continuation token to list the next page.
    --filter=<val>                [string]  Filters the results using OData syntax.
    --orderBy=<val>               [string]  Sorts the results using OData syntax.
    --payloadFile=<val>           [string]  File path to a valid JSON document.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
