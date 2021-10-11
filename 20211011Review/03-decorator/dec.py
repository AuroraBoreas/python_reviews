#Python is a protocol orientated lang; every top-level function has a correspoding dunder method implemented; 

import time
import logging
import functools
from typing import Any, Callable, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    _cache = {}
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Dict[Any,Any])->Any:
        beg = time.perf_counter_ns()
        key = (func.__name__, args, kwargs.__hash__)
        if key in _cache:
            return _cache[key]
        _cache[key] = func(*args,**kwargs)
        end = time.perf_counter_ns()
        logging.info('time lapsed(ns) : {0:.4f}'.format(end - beg))
        return _cache[key]
    return inner

class CMath:
    def _fibonacci(self, n:int)->int:
        return 1 if n < 2 else self._fibonacci(n-1) + self._fibonacci(n-2)

    def _factorial(self, n:int, rv=1)->int:
        return rv if n < 2 else self._factorial(n-1, rv*n)

    def _sum(self, n:int)->float:
        return n * (n+1) / 2

    @timer
    def fib(self, n:int)->int:
        return self._fibonacci(n)
    
    @timer
    def fact(self, n:int)->int:
        return self._factorial(n)

    @timer
    def sum(self, n:int)->float:
        return self._sum(n)

if __name__ == '__main__':
    m = CMath()
    rv1 = m.fib(10)
    rv2 = m.fact(10)
    rv3 = m.sum(10)