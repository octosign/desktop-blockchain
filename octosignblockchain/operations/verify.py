import hashlib
from web3 import Web3

from ..config import NETWORK_URL
from ..document import document
from ..results import with_verify_result

@with_verify_result
def verify(file: str):
    """Verifies document signature

    - Argument file: Absolute path to the document
    """

    doc = document(file)
    return doc.verify()
