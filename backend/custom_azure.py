from storages.backends.azure_storage import AzureStorage
from my_portfolio.azvault import AzVault

vault = AzVault("https://my-test-py.vault.azure.net/")
blobSecret = vault.getSecret('myportfoliodjangosa')

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