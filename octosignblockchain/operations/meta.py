from web3 import Web3
import sys

from ..config import NETWORK_URL
from ..results import with_meta_result

@with_meta_result
def meta():
    """Checks whether we have correctly working web3 client"""
    try:
        w3 = Web3(Web3.WebsocketProvider(NETWORK_URL))
        gasPrice = w3.eth.gasPrice
    except Exception as err:
        return {
            'status': err,
            'supports': ['application/pdf'],
        }

    return {
        'status': True,
        'supports': ['application/pdf'],
    }
