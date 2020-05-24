from web3.datastructures import AttributeDict
from hexbytes import HexBytes

class Account:
    def signTransaction(self, transaction, key):
        return AttributeDict({
            'rawTransaction': '0xabc123',
            'key': key,
        })

class Eth:
    def __init__(self):
        self.account = Account()
        self.gasPrice = 10

    def getTransaction(self, tx):
        return AttributeDict({
            'hash': tx,
            # Hex encoded ascii string "mocked"
            'input': '0x6d6f636b6564',
            'blockHash': '0x123',
            'from': '0x777'
        })

    def getTransactionCount(self, addr):
        return 1

    def getBlock(self, blockHash):
        return AttributeDict({
            'hash': blockHash,
            'timestamp': 1590335395
        })

    def estimateGas(self, params):
        return 100

    def sendRawTransaction(self, tx):
        return HexBytes('123')

    def waitForTransactionReceipt(self, tx):
        return None

class Web3:
    def __init__(self, provider = None):
        self.provider = provider

        self.eth = Eth()
