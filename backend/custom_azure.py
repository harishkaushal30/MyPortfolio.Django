from storages.backends.azure_storage import AzureStorage
from my_portfolio.azvault import AzVault
import os

vault = AzVault()
blobSecret = vault.getSecret(os.environ["STORAGE_ACCOUNT"])

class AzureMediaStorage(AzureStorage):
    account_name = blobSecret.name
    account_key = blobSecret.value
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = blobSecret.name
    account_key = blobSecret.value
    azure_container = 'static'
    expiration_secs = None