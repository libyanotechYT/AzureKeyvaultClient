###############################################################
#########           Azure Key Vault Client            #########
#########     Wanis Elabbar libyanotech@gmail.com     #########
###############################################################


from adal import AuthenticationContext
from msrestazure.azure_active_directory import AADTokenCredentials
from azure.keyvault import KeyVaultClient, KeyVaultId


clientid = 'id'  # This SPN must have secret read permissions on the keyvault not the IAM
clientsecret = 'secret'


def credsdk(resource):
    """
    get_credentials prepares credentials to connect to Azure Cloud/Stack API
    """

    auth_context = AuthenticationContext(
        "https://login.microsoftonline.com/tenantid")
    authjson = auth_context.acquire_token_with_client_credentials(
        resource, clientid, clientsecret)
    credentials = AADTokenCredentials(authjson, clientid)

    return credentials


def secclient(secname):

    # Define our keyvault
    # instead of azure you can use the azure stack hub name just make sure to get the resource name right or else you will get a wrong audience error
    kv_svc = "https://kevaultname.vault.azure.com/"
    # Define vault resource
    kv_res = "https://vault.tenantname.onmicrosoft.com/keyvaultresourceid"
    # Get credentials for Key Vault using SPN
    kvcred = credsdk(kv_res)

    # Initiate the KeyVault Secrets Client
    secclient = KeyVaultClient(kvcred)

    try:
        secret = secclient.get_secret(
            kv_svc, secname, secret_version=KeyVaultId.version_none)
        secval = secret.value  # actual secret

    except:
        secval = 'Unknown'

    return secval


# Grab secret from keyvault dynamically

apikey = secclient('nameofsecretinvault')
