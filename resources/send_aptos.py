from aptos_sdk.client import FaucetClient, RestClient
import os
from aptos_sdk.account import Account
from aptos_sdk.client import RestClient


def send(rest_client, sender, recipient):
    txn_hash = rest_client.transfer(sender, recipient.address(), 1_000)  # создаем транзакцию
    rest_client.wait_for_transaction(txn_hash)# ждем ответа
    print(f"Баланс получатяля: {rest_client.account_balance(recipient.address())}")


