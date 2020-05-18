import sys
from os import path

from ..prompt import prompt
from ..document import document
from ..results import with_simple_result

@with_simple_result
def sign(file: str):
    """Sign the given PDF document

    - Argument file: absolute path to the document
    """

    # Ask for the details: address, key, name
    details_prompt = prompt()
    details_prompt.show()
    details = details_prompt.get_data()

    if details == None:
        print('Signing process was canceled', file=sys.stderr)
        sys.exit(1)

    doc = document(file)
    doc.add(details['name'], details['address'], details['key'])

    absolute_path, ext = path.splitext(file)
    signed_path = absolute_path + '-signed' + ext

    doc.save(signed_path)

    return signed_path
