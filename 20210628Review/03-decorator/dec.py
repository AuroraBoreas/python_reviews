"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

def fibonacci(n:int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n:int)->int:
    return 1 if n < 2 else n * factorial(n-1)

import time
import functools
import logging
from typing import (Any, Callable, Dict)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

def timer(func:Callable[..., Any])->Callable[..., Any]:
    @functools.wraps(func)
    def inner(*args: Any, **kwargs: Dict[Any, Any])->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args, **kwargs)
        end = time.perf_counter_ns()
        logging.info("time lapsed(ns): {0}".format(end - beg))
        return rv
    return inner

@timer
def myfib(n:int)->int:
    return fibonacci(n)

@timer
def myfact(n:int)->int:
    return factorial(n)

if __name__ == "__main__":
    rv1 = myfib(10)
    rv2 = myfact(10)