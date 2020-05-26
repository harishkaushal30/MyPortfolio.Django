from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'myportfoliodjangosa'
    account_key = '5o7KibM9r0Iw/VInk7Xhiz4UGuOlBpLCBL5IYDSC91YDlH55pe88+bMgkdj67qiptj+1FLEtUHM5Z1ImwfIFug=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'myportfoliodjangosa'
    account_key = '5o7KibM9r0Iw/VInk7Xhiz4UGuOlBpLCBL5IYDSC91YDlH55pe88+bMgkdj67qiptj+1FLEtUHM5Z1ImwfIFug=='
    azure_container = 'static'
    expiration_secs = None