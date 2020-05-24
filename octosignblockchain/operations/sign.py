import sys
from os import path
import threading
import time

from ..prompt import Prompt
from ..document import Document
from ..results import with_simple_result

def sign(file: str):
    """Sign the given PDF document

    - Argument file: absolute path to the document
    """

    # Ask for the details: address, key, name
    details_prompt = Prompt()
    details_prompt.show()
    details = details_prompt.get_data()

    if details == None:
        print('Signing process was canceled', file=sys.stderr)
        sys.exit(1)

    name, address, key = details['name'], details['address'], details['key']

    @with_simple_result
    def callback(signed_path):
        return signed_path

    thread = threading.Thread(target=add_signature, args=(file, name, address, key, callback,))
    thread.start()

def add_signature(file, name, address, key, callback):
    """Add a signature to the specified file and call callback on end"""

    doc = Document(file)
    doc.add(name, address, key)

    absolute_path, ext = path.splitext(file)
    signed_path = absolute_path + '-signed' + ext

    doc.save(signed_path)

    callback(signed_path)
