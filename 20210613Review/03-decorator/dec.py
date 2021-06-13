"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

def fibonacci(n: int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n: int)->int:
    return 1 if n < 2 else n * factorial(n-1)

import time
import functools
import logging
logging.basicConfig(level=logging.DEBUG, format="%(processName)s %(asctime)s %(message)s")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs)->int:
        begin = time.perf_counter_ns()
        rv    = func(*args, **kwargs)
        end   = time.perf_counter_ns()
        logging.debug('time lapsed(ns): {0:.4f}'.format(end - begin))
        return rv
    return wrapper

@timer
def myfib(n: int)->int:
    """my fibonacci

    Args:
        n (int): integer n must be > 1

    Returns:
        int: integer
    """
    return fibonacci(n)


@timer
def myfact(n: int)->int:
    """my factorial

    Args:
        n (int): integer n must be > 1

    Returns:
        int: integer
    """
    return factorial(n)

if __name__ == "__main__":
    rv1:int = myfib(10)
    rv2:int = myfact(10)
