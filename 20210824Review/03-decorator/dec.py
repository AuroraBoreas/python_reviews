"Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

def fibonacci(n:int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n:int)->int:
    return 1 if n < 2 else n * factorial(n-1)

import time
import logging
import functools
from typing import Any, Callable
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args, **kwargs:Any)->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args, **kwargs)
        end = time.perf_counter_ns()
        logging.info(f'time lapsed(s) : {end-beg}')
        return rv
    return inner

@timer
def myfib(n:int)->int:
    return fibonacci(n)

@timer
def myfact(n:int)->int:
    return factorial(n)

if __name__ == '__main__':
    rv1 = myfib(10)
    rv2 = myfact(10)