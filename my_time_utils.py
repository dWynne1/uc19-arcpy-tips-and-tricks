"""
Decorator to time functions

Adapted from jonaprieto's answer on
https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
"""

from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func: %r\nargs: [%r, %r]\ntime: %2.4f sec\n' %
              (f.__name__, args, kw, te-ts))
        return result
    return wrap


def timing_no_args(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func: %r\ntime: %2.4f sec\n' %
              (f.__name__, te-ts))
        return result
    return wrap
