# proxy

import time, logging, functools
from typing import Any, Callable

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Any)->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args,**kwargs)
        end = time.perf_counter_ns()
        logging.info('time lapsed(ns) : {0:,}'.format(end - beg))
        return rv
    return inner
def memoir(func:Callable)->Callable:
    _cache = {}
    def memorized(*args:Any,**kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if not key in _cache:
            _cache[key] = func(*args,**kwargs)
        return _cache[key]
    return memorized

class MyMath:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int)->int:
        return 1 if n < 2 else self.fact(n-1) * n

class ProxyMath:
    def __init__(self, target:MyMath, attr:str)->None:
        self.target = target
        func = getattr(target, attr)
        setattr(self.target, attr, memoir(func))
    
    def __getattr__(self, attr:str)->Any:
        return getattr(self.target, attr)

@timer
def client_code(attr:str, n=30)->None:
    p = ProxyMath(MyMath(), attr)
    f = getattr(p, attr)
    seq = [f(x) for x in range(n)]
    print(seq)

if __name__ == '__main__':
    n:int = 40
    for attr in ['fib', 'fact']:
        client_code(attr, n)
    