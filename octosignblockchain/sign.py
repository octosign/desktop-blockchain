import hashlib
from web3 import Web3
from tkinter import *

from .prompt import prompt

def sign(file):
    # TODO: Do a sha3-256 hash of the provided file
    m = hashlib.sha3_256()
    m.update(file.encode('utf-8'))
    print('Sign: I am trying to pretend I have saved PDF hash in the file and created blockchain transaction: ' + m.hexdigest())

    # TODO: Ask for the details: address, key, name
    details_prompt = prompt()
    details_prompt.show()

    # TODO: Create transaction on the blockchain with sha3-256 hash as data
    w3 = Web3(Web3.WebsocketProvider('wss://kovan.infura.io/ws/v3/358b9a4a54ea4fc8b0e53a741edfd5cc'))
    tx = w3.eth.getTransaction('0x35b4866b1ea53f2a475cd9bede92f8a197dad6e193cb5456ed17db7062cc6f1d')
    print('Sign: I am trying to pretend I am working with the blockchain and transaction:')
    print(tx)

    # TODO: Open the PDF using PyPDF4, edit metadata - add serialized name and transaction hash
