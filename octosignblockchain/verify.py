import hashlib
from web3 import Web3

def verify(file):
    # TODO: Open the PDF using PyPDF4, look at the metadata - serialized name and transaction hash

    # TODO: Remove metadata of the signature we are verifying

    # TODO: For each signature: Do a sha3-256 hash of the provided file
    m = hashlib.sha3_256()
    m.update(file.encode('utf-8'))
    print('Verify: I am trying to pretend I have compared PDF hash in the file with the blockchain transaction: ' + m.hexdigest())

    # TODO: For each signature: Get the transaction using hash stored in the metadata
    w3 = Web3(Web3.WebsocketProvider('wss://kovan.infura.io/ws/v3/358b9a4a54ea4fc8b0e53a741edfd5cc'))
    tx = w3.eth.getTransaction('0x35b4866b1ea53f2a475cd9bede92f8a197dad6e193cb5456ed17db7062cc6f1d')
    print('Verify: I am trying to pretend I am working with the blockchain and transaction:')
    print(tx)

    # TODO: For each signature: Compare hash in the transaction with the one we calculated locally

    # TODO: For each signature: Add name and validity of the signature to the buffered details

    # TODO: Respond ok if all signatures valid + add buffered details, with error of the failed signature(s) otherwise
