from resources.faucet_aptos import *
from resources.generate import *
from resources.send_aptos import *

# Блок переменных
NODE_URL = os.getenv("APTOS_NODE_URL", "https://fullnode.testnet.aptoslabs.com/v1")
FAUCET_URL = os.getenv("APTOS_FAUCET_URL", "https://faucet.testnet.aptoslabs.com")
wallet1 = Account.load_key('0x10d41069ea727c93cd2475379ccd3063073337b282cc17be12f734fe07d1b61a')# sender
wallet2 = Account.load_key('0x10d41069ea727c93cd2475379ccd3063073337b282cc17be12f734fe07d1b61a')# recipient
rest_client = RestClient(NODE_URL)
# Либо читаем из файла
with open("private_key.txt", "r") as f:
    private_key = f.read().split('\n')
with open("recipient_key.txt", "r") as f:
    recipient_key = f.read().split('\n')



# функция клейма токенов из крана
#aptos_faucet(wallet1, NODE_URL, FAUCET_URL)

# функция отправки транзакций между кошельками
#send(rest_client, wallet1,wallet2)

# Функция генерации
#generate(rest_client)