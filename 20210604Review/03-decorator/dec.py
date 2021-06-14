"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

def fibonacci(n: int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n: int)->int:
    return 1 if n < 2 else n * factorial(n-1)

import functools
import time
import logging
from typing import (Callable, Tuple, Dict, Any)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func: Callable)->Callable:
    @functools.wraps(func)
    def wrapper(*args: Tuple, **kwargs: Dict)->Any:
        start = time.perf_counter_ns()
        rv    = func(*args, **kwargs)
        end   = time.perf_counter_ns()
        logging.info('time lasped(ns) : {0}'.format(end - start))
        return rv
    return wrapper

@timer
def myfib(n: int)->int:
    """my fibonnaci

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return fibonacci(n)

@timer
def myfact(n: int)->int:
    """my factorial

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return factorial(n)

if __name__ == "__main__":
    rv1 = myfib(10)
    rv2 = myfact(10)