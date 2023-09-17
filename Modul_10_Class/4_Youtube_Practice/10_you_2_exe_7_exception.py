
class OutOfBoundError(Exception):
    pass


try:
    raise OutOfBoundError('you are out of bound')
except OutOfBoundError:
    print('Error')