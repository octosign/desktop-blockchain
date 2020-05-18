import ast
import base64
from datetime import datetime
import web3

class signature(object):
    """Custom data structure of signature that is placed in the PDF document.

    It is represented by name of the signee, file digest, and transaction hash.
    It supports serialization using .serialize and .from_serialized.
    It can be compared with other signatures.
    """

    def __init__(self, name: str, digest: str, transaction: str):
        self.name = name
        self.hash = digest
        self.transaction = transaction
        self.date = None
        self.address = None

    def __eq__(self, other):
        if not(isinstance(other, signature)):
            return False
        return self.hash == other.hash

    def serialize(self):
        """Serializes properties name and transaction

        Timestamp, from address and hash is is not serialized as it is saved on the blockchain.
        """
        return base64.b64encode(repr([self.name, self.transaction]).encode('UTF-8'))

    @staticmethod
    def from_serialized(serialized: str, w3: web3):
        """Create new signature from the serialized signature

        Uses base64-encoded representation of the signature created using method .serialize.
        Requires instance of web3 client to gather information.
        Sets, in addition to name, hash, and transaction also date and address of the sender.
        """

        name, transaction = ast.literal_eval(base64.b64decode(serialized).decode('UTF-8'))

        tx = w3.eth.getTransaction(transaction)

        if tx == None:
            return None

        stored_hash = bytes.fromhex(tx.input[2:]).decode('ascii')

        block = w3.eth.getBlock(tx.blockHash)

        new_signature = signature(name, stored_hash, transaction)
        new_signature.date = datetime.fromtimestamp(block.timestamp)
        new_signature.address = tx['from']

        return new_signature
