import sys

def with_simple_result(func):
    """Simple result that uses returned value as-is"""
    def wrapper(*args, **kwargs):
        returned = func(*args, **kwargs)
        print('--RESULT--')
        print(returned)
        print('--RESULT--')
    return wrapper

def with_meta_result(func):
    """Meta result that expects dictionary with status and supports as return value"""
    def wrapper(*args, **kwargs):
        returned = func(*args, **kwargs)
        print('--RESULT--')

        if returned['status'] == True:
            print('OK')
        else:
            print(returned['status'])
        print(' '.join(returned['supports']))

        print('--RESULT--')
    return wrapper

def with_verify_result(func):
    """Verify result that expects None, False or str as return value"""
    def wrapper(*args, **kwargs):
        returned = func(*args, **kwargs)
        print('--RESULT--')

        if returned == None:
            print('UNSINGED')
        elif returned == False:
            print('INVALID')
        elif isinstance(returned, str):
            print('SIGNED')
            print(returned)
        else:
            print('UNKNOWN')

        print('--RESULT--')
    return wrapper
