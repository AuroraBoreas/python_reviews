#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented; 

def fibonacci(n:int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n:int)->int:
    return 1 if n < 2 else n * factorial(n-1)

def _sum(n:int)->float:
    return n * (n + 1) / 2

import time
import logging
import functools
from typing import Any, Callable, Dict
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable[...,Any])->Callable[...,Any]:
    @functools.wraps(func)
    def inner(*args:Any, **kwargs:Dict[Any,Any])->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args, **kwargs)
        end = time.perf_counter_ns()
        logging.info(f'{func.__name__} time lapsed: {end - beg}')
        return rv
    return inner

@timer
def myfib(n:int)->int:
    """[summary]

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return fibonacci(n)

@timer
def myfact(n:int)->int:
    """[summary]

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    return factorial(n)

@timer
def mysum(n:int)->float:
    """[summary]

    Args:
        n (int): [description]

    Returns:
        float: [description]
    """
    return _sum(n)


if __name__ == '__main__':
    rv1 = myfib(10)
    rv2 = myfact(10)
    rv3 = mysum(10)