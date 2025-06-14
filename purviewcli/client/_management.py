import uuid
from .endpoint import Endpoint, decorator, get_json
from .endpoints import PurviewEndpoints

class Management(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'management'

    @decorator
    def managementListOperations(self, args):
        self.method = 'GET'
        self.endpoint = PurviewEndpoints.MANAGEMENT['operations']
        self.params = PurviewEndpoints.get_api_version_params('management')
   
    @decorator
    def managementCheckNameAvailability(self, args):
        self.method = 'POST'
        self.endpoint = PurviewEndpoints.format_endpoint(PurviewEndpoints.MANAGEMENT['check_name_availability'], subscriptionId=args["--subscriptionId"])
        self.params = PurviewEndpoints.get_api_version_params('management')
        self.payload = {'name': args['--accountName'], 'type': 'Microsoft.Purview/accounts'}
    
    @decorator
    def managementReadAccounts(self, args):
        self.method = 'GET'
        if args["--resourceGroupName"] is None:
            self.endpoint = PurviewEndpoints.format_endpoint(PurviewEndpoints.MANAGEMENT['accounts'], subscriptionId=args["--subscriptionId"])
        else:
            self.endpoint = PurviewEndpoints.format_endpoint(PurviewEndpoints.MANAGEMENT['accounts_by_rg'], 
                                                           subscriptionId=args["--subscriptionId"], 
                                                           resourceGroupName=args["--resourceGroupName"])
        self.params = PurviewEndpoints.get_api_version_params('management')

    @decorator
    def managementReadAccount(self, args):
        self.method = 'GET'
        self.endpoint = PurviewEndpoints.format_endpoint(PurviewEndpoints.MANAGEMENT['account'], 
                                                       subscriptionId=args["--subscriptionId"],
                                                       resourceGroupName=args["--resourceGroupName"],
                                                       accountName=args["--accountName"])
        self.params = PurviewEndpoints.get_api_version_params('management')
    
    @decorator
    def managementCreateAccount(self, args):
        self.method = 'PUT'
        self.endpoint = PurviewEndpoints.format_endpoint(PurviewEndpoints.MANAGEMENT['account'], 
                                                       subscriptionId=args["--subscriptionId"],
                                                       resourceGroupName=args["--resourceGroupName"],
                                                       accountName=args["--accountName"])
        self.params = PurviewEndpoints.get_api_version_params('management')
        self.payload = get_json(args, '--payloadFile')
    
    @decorator
    def managementDeleteAccount(self, args):
        self.method = 'DELETE'
        self.endpoint = PurviewEndpoints.format_endpoint(PurviewEndpoints.MANAGEMENT['account'], 
                                                       subscriptionId=args["--subscriptionId"],
                                                       resourceGroupName=args["--resourceGroupName"],
                                                       accountName=args["--accountName"])
        self.params = PurviewEndpoints.get_api_version_params('management')
    
    @decorator
    def managementListKeys(self, args):
        self.method = 'POST'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/listkeys'
        self.params = {'api-version': '2020-12-01-preview'}
    
    @decorator
    def managementUpdateAccount(self, args):
        self.method = 'PATCH'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = get_json(args, '--payloadFile')

    @decorator
    def managementDefaultAccount(self, args):
        self.method = 'GET'
        self.endpoint = f'/providers/Microsoft.Purview/getDefaultAccount'
        self.params = {'scopeTenantId': args["--scopeTenantId"], 'scopeType': args["--scopeType"], 'scope': args["--scope"], 'api-version': '2020-12-01-preview'}

    @decorator
    def managementSetDefaultAccount(self, args):
        self.method = 'POST'
        self.endpoint = '/providers/Microsoft.Purview/setDefaultAccount'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = {
            "scopeTenantId": args["--scopeTenantId"],
            "scopeType": args["--scopeType"],
            "scope": args["--scope"],
            "accountName": args["--accountName"],
            "resourceGroupName": args["--resourceGroupName"],
            "subscriptionId": args["--subscriptionId"]
        }
    
    @decorator
    def managementRemoveDefaultAccount(self, args):
        self.method = 'POST'
        self.endpoint = '/providers/Microsoft.Purview/removeDefaultAccount'
        self.params = {'scopeTenantId': args["--scopeTenantId"], 'scopeType': args["--scopeType"], 'scope': args["--scope"], 'api-version': '2020-12-01-preview'}

    @decorator
    def managementListPrivateLinkResources(self, args):
        self.method = 'GET'
        if args["--groupId"] is None:
            self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateLinkResources'
        else:
            self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateLinkResources/{args["--groupId"]}'
        self.params = {'api-version': '2020-12-01-preview'}

    @decorator
    def managementPutPrivateEndpoint(self, args):
        self.method = 'PUT'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections/{args["--privateEndpointConnectionName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
        self.payload = get_json(args, '--payloadFile')
    
    @decorator
    def managementDeletePrivateEndpoint(self, args):
        self.method = 'DELETE'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections/{args["--privateEndpointConnectionName"]}'
        self.params = {'api-version': '2020-12-01-preview'}
    
    @decorator
    def managementReadPrivateEndpoint(self, args):
        self.method = 'GET'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections/{args["--privateEndpointConnectionName"]}'
        self.params = {'api-version': '2020-12-01-preview'}

    @decorator
    def managementReadPrivateEndpoints(self, args):
        self.method = 'GET'
        self.endpoint = f'/subscriptions/{args["--subscriptionId"]}/resourceGroups/{args["--resourceGroupName"]}/providers/Microsoft.Purview/accounts/{args["--accountName"]}/privateEndpointConnections'
        self.params = {'api-version': '2020-12-01-preview'}
    
    @decorator
    def managementAddRootCollectionAdmin(self, args):
        self.method = 'POST'
        self.endpoint = f"/subscriptions/{args['--subscriptionId']}/resourceGroups/{args['--resourceGroupName']}/providers/Microsoft.Purview/accounts/{args['--accountName']}/addRootCollectionAdmin"
        self.payload = { "objectId": f"{args['--objectId']}" }
        self.params = {'api-version': '2021-07-01'}