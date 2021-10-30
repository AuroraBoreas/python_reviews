# fence or barrier

class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int, rv:int=1)->int:
        return rv if n < 2 else self.fact(n-1, rv*n)

import time
from typing import Any, Callable
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def memoir(func:Callable)->Callable:
    _cache = {}
    @functools.wraps(func)
    def memorized(*args:Any,**kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if key in _cache:
            return _cache[key]
        _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return memorized

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Any)->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args, **kwargs)
        end = time.perf_counter_ns()
        logging.info(f'time lapsed(ns) : {end - beg}')
        return rv
    return inner

class ProxyCalculator:
    def __init__(self, target:RawCalculator, attr:str)->None:
        self.target = target
        func = getattr(self.target, attr)
        setattr(self.target, attr, memoir(func))

    def __getattr__(self, attr)->Any:
        return getattr(self.target, attr)

@timer
def client_code(attr:str, n:int=10):
    p = ProxyCalculator(RawCalculator(), 'fib')
    f = getattr(p, attr)
    rv = [f(x) for x in range(n)]
    print(f'{attr} sequence, length={n} :')
    print(rv)

if __name__ == '__main__':
    n:int = 80
    for attr in ['fib', 'fact']:
        client_code(attr, n)