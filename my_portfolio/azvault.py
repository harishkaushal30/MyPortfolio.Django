from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

class AzVault:
    _credential = None
    _client = None
    def __init__(self, ):
        if self._credential == None or self._client == None:
            self._credential = DefaultAzureCredential()
            self._client = SecretClient(vault_url=os.environ["KEY_VAULT_URI"], credential=self._credential)
    
    def getCredential(self):
        return self._credential
    
    def  getClient(self):
        return self._client

    def getSecret(self, name):
        return self._client.get_secret(name)
