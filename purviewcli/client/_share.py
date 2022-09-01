from .endpoint import Endpoint, decorator, get_json

class Share(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'share'

    # Accepted Sent Shares
    @decorator
    def shareListAcceptedShares(self, args):
        sentShareName = args['--sentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/sentShares/{sentShareName}/acceptedSentShares"

    @decorator
    def shareGetAcceptedShare(self, args):
        sentShareName = args['--sentShareName']
        acceptedSentShareName = args['--acceptedSentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}"

    @decorator
    def shareReinstateAcceptedShare(self, args):
        sentShareName = args['--sentShareName']
        acceptedSentShareName = args['--acceptedSentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "POST"
        self.endpoint = f"/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}:reinstate"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareRevokeAcceptedShare(self, args):
        sentShareName = args['--sentShareName']
        acceptedSentShareName = args['--acceptedSentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "POST"
        self.endpoint = f"/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}:revoke"

    @decorator
    def shareUpdateExpirationAcceptedShare(self, args):
        sentShareName = args['--sentShareName']
        acceptedSentShareName = args['--acceptedSentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "POST"
        self.endpoint = f"/sentShares/{sentShareName}/acceptedSentShares/{acceptedSentShareName}:update-expiration"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareListAssetMappings(self, args):
        receivedShareName = args['--receivedShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/receivedShares/{receivedShareName}/assetMappings"

    @decorator
    def shareCreateAssetMapping(self, args):
        receivedShareName = args['--receivedShareName']
        assetMappingName = args['--assetMappingName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "PUT"
        self.endpoint = f"/receivedShares/{receivedShareName}/assetMappings/{assetMappingName}"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareDeleteAssetMapping(self, args):
        receivedShareName = args['--receivedShareName']
        assetMappingName = args['--assetMappingName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "DELETE"
        self.endpoint = f"/receivedShares/{receivedShareName}/assetMappings/{assetMappingName}"

    @decorator
    def shareGetAssetMapping(self, args):
        receivedShareName = args['--receivedShareName']
        assetMappingName = args['--assetMappingName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/receivedShares/{receivedShareName}/assetMappings/{assetMappingName}"

    @decorator
    def shareListAssets(self, args):
        sentShareName = args['--sentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/sentShares/{sentShareName}/assets"

    @decorator
    def shareCreateAsset(self, args):
        sentShareName = args['--sentShareName']
        assetName = args['--assetName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "PUT"
        self.endpoint = f"/sentShares/{sentShareName}/assets/{assetName}"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareDeleteAsset(self, args):
        sentShareName = args['--sentShareName']
        assetName = args['--assetName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "DELETE"
        self.endpoint = f"/sentShares/{sentShareName}/assets/{assetName}"

    @decorator
    def shareGetAsset(self, args):
        sentShareName = args['--sentShareName']
        assetName = args['--assetName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/sentShares/{sentShareName}/assets/{assetName}"

    @decorator
    def shareActivateEmail(self, args):
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "POST"
        self.endpoint = "/activateEmail"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareRegisterEmail(self, args):
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "POST"
        self.endpoint = "/registerEmail"

    @decorator
    def shareListReceivedAssets(self, args):
        receivedShareName = args['--receivedShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/receivedShares/{receivedShareName}/receivedAssets"

    @decorator
    def shareListReceivedInvitations(self, args):
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = "/receivedInvitations"

    @decorator
    def shareGetReceivedInvitation(self, args):
        receivedInvitationName = args['--invitationName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/receivedInvitations/{receivedInvitationName}"

    @decorator
    def shareRejectReceivedInvitation(self, args):
        receivedInvitationName = args['--invitationName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "POST"
        self.endpoint = f"/receivedInvitations/{receivedInvitationName}:reject"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareListReceivedShares(self, args):
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = "/receivedShares"

    @decorator
    def shareCreateReceivedShare(self, args):
        receivedShareName = args['--receivedShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "PUT"
        self.endpoint = f"/receivedShares/{receivedShareName}"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareDeleteReceivedShare(self, args):
        receivedShareName = args['--receivedShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "DELETE"
        self.endpoint = f"/receivedShares/{receivedShareName}"

    @decorator
    def shareGetReceivedShare(self, args):
        receivedShareName = args['--receivedShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/receivedShares/{receivedShareName}"

    @decorator
    def shareListSentInvitations(self, args):
        sentShareName = args['--sentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/sentShares/{sentShareName}/sentShareInvitations"

    @decorator
    def shareCreateSentInvitation(self, args):
        sentShareName = args['--sentShareName']
        sentShareInvitationName = args['--invitationName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "PUT"
        self.endpoint = f"/sentShares/{sentShareName}/sentShareInvitations/{sentShareInvitationName}"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareDeleteSentInvitation(self, args):
        sentShareName = args['--sentShareName']
        sentShareInvitationName = args['--invitationName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "DELETE"
        self.endpoint = f"/sentShares/{sentShareName}/sentShareInvitations/{sentShareInvitationName}"

    @decorator
    def shareGetSentInvitation(self, args):
        sentShareName = args['--sentShareName']
        sentShareInvitationName = args['--invitationName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/sentShares/{sentShareName}/sentShareInvitations/{sentShareInvitationName}"

    @decorator
    def shareListSentShares(self, args):
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = "/sentShares"

    @decorator
    def shareCreateSentShare(self, args):
        sentShareName = args['--sentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "PUT"
        self.endpoint = f"/sentShares/{sentShareName}"
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def shareDeleteSentShare(self, args):
        sentShareName = args['--sentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "DELETE"
        self.endpoint = f"/sentShares/{sentShareName}"

    @decorator
    def shareGetSentShare(self, args):
        sentShareName = args['--sentShareName']
        self.params = {"api-version": "2021-09-01-preview"}
        self.method = "GET"
        self.endpoint = f"/sentShares/{sentShareName}"
