import unittest
from unittest.mock import patch, mock_open, MagicMock, ANY, call
import sys

PyPDF2Mock = MagicMock()
sys.modules['PyPDF2'] = PyPDF2Mock

from .web3_mock import Web3
from octosignblockchain.document import Document

class TestDocument(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data='data'.encode('UTF-8')))
    @patch('octosignblockchain.document.remove')
    def test_add(self, mock_remove):
        document = Document('./test.pdf')
        document.w3 = Web3()

        PyPDF2Mock.PdfFileReader.return_value.getDocumentInfo.return_value.copy.return_value = {}

        document.add('Jakub', '0x123', 'key')

        # Test that set PDF metadata property matches (serialized signature)
        PyPDF2Mock.PdfFileMerger.return_value.addMetadata.assert_called_with(
            {'/Signature': b'WydKYWt1YicsICcweDAxMjMnXQ=='}
        )

        # Test that temporary file was removed
        mock_remove.assert_called()

    @patch('octosignblockchain.document.rename')
    def test_save(self, mock_rename):
        document = Document('./test.pdf')
        document.w3 = Web3()
        document.save('./output.pdf')

        mock_rename.assert_called_with(ANY, './output.pdf')

    @patch('builtins.open', mock_open(read_data='data'.encode('UTF-8')))
    def test_verify(self):
        document = Document('./test.pdf')
        document.w3 = Web3()
        withoutSignature = document.verify()

        self.assertIsNone(withoutSignature)

        # TODO: Add mocking return value on metadata
