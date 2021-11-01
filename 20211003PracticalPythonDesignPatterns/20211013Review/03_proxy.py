
from typing import Callable, Any, Dict
import functools
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class RawCalculator:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int, rv=1)->int:
        return rv if n < 2 else self.fact(n-1, n*rv)

def memoir(func:Callable)->Callable:
    _cache = {}
    @functools.wraps(func)
    def memorized(*args:Any,**kwargs:Dict[Any,Any])->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if key in _cache:
            return _cache[key]
        _cache[key] = func(*args,**kwargs)
        return _cache[key]
    return memorized

class ProxyCalculator:
    def __init__(self, target:RawCalculator, attr:str)->None:
        self.target = target
        f = getattr(self.target, attr)
        setattr(self.target, attr, memoir(f))

    def __getattr__(self, attr:str)->object:
        return getattr(self.target, attr)

def timer(func:Callable)->Callable:
    def inner(*args:Any, **kwargs:Any)->Any:
        beg = time.time()
        rv  = func(*args, **kwargs)
        end = time.time()
        logging.info('{0}, time lapsed(ss) : {1:.4f}'.format(func.__name__, end - beg))
        return rv
    return inner

@timer
def test_fib():
    p = ProxyCalculator(RawCalculator(), 'fib')
    fib_seq = [p.fib(x) for x in range(80)]
    print(fib_seq)

@timer
def test_fact():
    p = ProxyCalculator(RawCalculator(), 'fact')
    fact_seq = [p.fact(x) for x in range(80)]
    print(fact_seq)

if __name__ == '__main__':
    test_fib()
    test_fact()