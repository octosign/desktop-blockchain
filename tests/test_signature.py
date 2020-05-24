import unittest

from octosignblockchain.signature import Signature
from .web3_mock import Web3

class TestSignature(unittest.TestCase):
    def test_instance(self):
        signature = Signature('Janko', 'ax3', '0x123')

        self.assertEqual(signature.name, 'Janko')
        self.assertEqual(signature.hash, 'ax3')
        self.assertEqual(signature.transaction, '0x123')
        self.assertEqual(signature.date, None)
        self.assertEqual(signature.address, None)

    def test_equality(self):
        signature = Signature('Janko', 'ax3', '0x123')

        self.assertEqual(signature, Signature('Jnko', 'ax3', '0123'))
        self.assertNotEqual(signature, Signature('Janko', 'a3', '0x123'))

    def test_serialization(self):
        signature = Signature('Janko', 'mocked', '0x123')

        w3 = Web3()

        serialized_signature = Signature.from_serialized('WydKYW5rbycsICcweDEyMydd', w3)

        self.assertEqual(signature, serialized_signature)
        self.assertEqual(
            serialized_signature.serialize().decode('UTF-8'),
            'WydKYW5rbycsICcweDEyMydd'
        )
