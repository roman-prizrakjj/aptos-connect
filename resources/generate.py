from aptos_sdk.account import Account

def generate(rest_client):
    alice = Account.generate()
    return alice
