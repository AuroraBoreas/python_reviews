"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

def fibonacci(n:int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n:int)->int:
    return 1 if n < 2 else n * factorial(n-1)

import time
import functools
from typing import (Callable, Tuple, TypeVar, Any, Dict)
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
T = TypeVar('T', int, float, Any)

def timer(func: Callable[..., Any])->Callable[..., Any]:
    @functools.wraps(func)
    def inner(*args: Tuple[T], **kwargs:Dict[Any, Any])->Any:
        beg = time.perf_counter_ns()
        end = time.perf_counter_ns()
        logging.info('time lapsed(ns): '.format(end - beg))
        return rv
    return inner

@timer
def myfib(n:int)->int:
    """my fibonacci

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return fibonacci(n)

@timer
def myfact(n:int)->int:
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