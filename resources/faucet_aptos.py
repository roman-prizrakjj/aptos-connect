from aptos_sdk.client import FaucetClient, RestClient
import os
from aptos_sdk.account import Account
from aptos_sdk.client import RestClient


def aptos_faucet(wallet1, NODE_URL, FAUCET_URL):

    #Создаем экземпляр класса
    rest_client = RestClient(NODE_URL) #экземпляр клиента
    faucet_client = FaucetClient(FAUCET_URL, rest_client)# экземпляр крана
    # вход на кошельки
    wallet1 = wallet1

    #инициализация кошелька в блокчейне путем взаимодействия с краном
    faucet_client.fund_account(wallet1.address(), 0)
    print("======Балланс========")
    print(f"Баланс: {rest_client.account_balance(wallet1.address())}")
    return rest_client

