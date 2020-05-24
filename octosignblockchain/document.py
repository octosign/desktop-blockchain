import hashlib
import tempfile
import random
import string
import binascii
from os import path, remove, rename
from PyPDF2 import PdfFileReader, PdfFileMerger
from web3 import Web3

from .config import NETWORK_URL, MAIN_ADDRESS
from .signature import Signature

class Document(object):
    """Abstraction around working with the document

    Provides adding signature and verifying of the current signature
    """

    def __init__(self, file: str):
        self.file = file
        # Open and save the PDF as temp file using PyPDF2 as it will influence the content
        self.output = self._set_pdf_signature(file)
        self.w3 = Web3(Web3.WebsocketProvider(NETWORK_URL))

    def add(self, name: str, address: str, key: str):
        """Add signature to the current document using the given name

        - Argument name: Name of the person signing the document.
        - Argument address: Address of the sender.
        - Argument key: Private key of the sender.
        """

        file_hash = self._get_hash(name)

        # Create transaction on the blockchain with sha3-256 hash as data
        signed_txn = self.w3.eth.account.signTransaction({
                'nonce': self.w3.eth.getTransactionCount(address),
                'gasPrice': self.w3.eth.gasPrice,
                'gas': int(self.w3.eth.estimateGas({'to': MAIN_ADDRESS, 'from': address}) * 1.2),
                'to': MAIN_ADDRESS,
                'data': file_hash.encode('ascii'),
            },
            key,
        )
        transaction_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        self.w3.eth.waitForTransactionReceipt(transaction_hash)

        new_signature = Signature(name, file_hash, transaction_hash.hex())

        oldOutput = self.output
        self.output = self._set_pdf_signature(self.output, signature=new_signature)
        remove(oldOutput)

    def save(self, path: str):
        """Save current document with given path

        - Argument path: Absolute path that should be used.
        """
        rename(self.output, path)

    def verify(self):
        """Verify signature of the current document

        Returns None if there is no signature, False if it is invalid and True if it is valid.
        """

        file_in = open(self.file, 'rb')
        pdf_reader = PdfFileReader(file_in)
        metadata = pdf_reader.getDocumentInfo().copy()
        if '/Signature' not in metadata:
            return None

        serialized_signature = metadata['/Signature']

        stored_signature = Signature.from_serialized(serialized_signature, self.w3)
        if stored_signature == None:
            return False

        calculated_signature = Signature(
            stored_signature.name,
            self._get_hash(stored_signature.name),
            stored_signature.transaction,
        )

        if stored_signature == calculated_signature:
            return f'''Signed by **{stored_signature.name}**

            **Date and time**: {stored_signature.date}

            **From address**: {stored_signature.address}

            **Transaction hash**: {stored_signature.transaction}
            '''
        else:
            return False

    def _get_hash(self, name: str):
        """Get hash of the current file

        - Argument name: Name of the person signing the document.
        """

        file_hash = hashlib.sha3_256()
        with open(self.output, 'rb') as f:
            while True:
                data = f.read(64 * 1024)
                if not data:
                    break
                file_hash.update(data)
        file_hash.update(name.encode('UTF-8'))

        return file_hash.hexdigest()

    def _set_pdf_signature(self, input: str, output: str = None, signature: Signature = None) -> str:
        """Sets signature metadata using the given input file to new output file

        Private method that should not be used directly, use add instead.

        - Argument input: absolute path to input PDF that will be untouched
        - Argument output: optional absolute path to the output file, creates new temp file if not set that should be cleaned
        - Argument signature: optional signature to set, if empty, existing is removed

        Returns absolute path to the output file.
        """

        if output == None:
            random_file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            random_temp_path = path.join(tempfile.gettempdir(), random_file_name)
            output = random_temp_path

        file_in = open(input, 'rb')
        pdf_reader = PdfFileReader(file_in)
        metadata = pdf_reader.getDocumentInfo().copy()

        if signature == None:
            if '/Signature' in metadata:
                del metadata['/Signature']
        else:
            metadata['/Signature'] = signature.serialize()

        pdf_merger = PdfFileMerger()
        pdf_merger.append(file_in)
        pdf_merger.addMetadata(metadata)
        file_out = open(output, 'wb')
        pdf_merger.write(file_out)

        file_in.close()
        file_out.close()

        return output
