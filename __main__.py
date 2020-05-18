import argparse
import sys

from octosignblockchain.operations.meta import meta
from octosignblockchain.operations.sign import sign
from octosignblockchain.operations.verify import verify

class BlockchainBackend(object):
    def main(self):
        parser = argparse.ArgumentParser(description='Sign PDFs using blockchain.')
        subparsers = parser.add_subparsers(required=True)

        parser_meta = subparsers.add_parser('meta')
        parser_meta.set_defaults(func=self.meta)

        parser_sign = subparsers.add_parser('sign')
        parser_sign.add_argument('file', help='absolute path to the file')
        parser_sign.set_defaults(func=self.sign)

        parser_verify = subparsers.add_parser('verify')
        parser_verify.add_argument('file', help='absolute path to the file')
        parser_verify.set_defaults(func=self.verify)

        args = parser.parse_args()
        args.func(args)

    def meta(self, args):
        meta()

    def sign(self, args):
        sign(args.file)

    def verify(self, args):
        verify(args.file)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Missing required operation as first argument')
    BlockchainBackend().main()
