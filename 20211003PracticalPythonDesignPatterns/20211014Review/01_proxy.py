
class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2) 

    def fact(self, n:int)->int:
        return 1 if n < 2 else self.fact(n-1) * n

import time
import logging
import functools
from typing import Callable, Any, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Dict[Any,Any])->Any:
        beg = time.time_ns()
        rv  = func(*args,**kwargs)
        end = time.time_ns()
        logging.info('time lapsed(ns) : {0:.4f}'.format(end - beg))
        return rv
    return inner

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

class ProxyCalculator:
    def __init__(self, target:RawCalculator, attr:str)->None:
        self.target = target
        func = getattr(self.target, attr)
        setattr(self.target, attr, memoir(func))

    def __getattr__(self, attr):
        return getattr(self.target, attr)

@timer
def test_fib(n:int)->None:
    p = ProxyCalculator(RawCalculator(), 'fib')
    seq = [p.fib(x) for x in range(n)]
    logging.info('{} fibonacci numbers'.format(len(seq)))
    print(seq)

@timer
def test_fact(n:int)->None:
    p = ProxyCalculator(RawCalculator(), 'fact')
    seq = [p.fact(x) for x in range(n)]
    logging.info('{} factorial numbers'.format(len(seq)))
    print(seq)

if __name__ == '__main__':
    n: int = 80
    rv1 = test_fib(n)
    rv2 = test_fact(n)