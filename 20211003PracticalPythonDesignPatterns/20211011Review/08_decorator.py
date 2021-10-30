from __future__ import annotations
import time
import functools
from typing import Callable, Any, Dict
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Any)->Any:
        beg = time.time_ns()
        rv  = func(*args,**kwargs)
        end = time.time_ns()
        logging.info('time lapsed(ns) : {0}'.format(end - beg))
        return rv
    return inner

def memoir(func:Callable)->callable:
    _cache = {}
    @functools.wraps(func)
    def memorized(*args:Any,**kwargs:Any)->Any:
        key = (func.__name__, args, kwargs.__hash__)
        if key in _cache:
            return _cache[key]
        _cache[key] = func(*args,**kwargs)
        return _cache[key]
    return memorized

class MyMath:
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int, rv:int=1)->int:
        return rv if n < 2 else self.fact(n-1, rv*n)

    # @timer
    # def fib(self, n:int)->int:
    #     return self.__fib(n)

    # @timer
    # def fact(self, n:int)->int:
    #     return self.__fact(n)

class ProxyMath:
    def __init__(self, target:MyMath, attr:str)->None:
        self.target = target
        f = getattr(self.target, attr)
        setattr(self.target, attr, memoir(f))

    def __getattr__(self, attr:str)->Any:
        return getattr(self.target, attr)

if __name__ == '__main__':
    p = ProxyMath(MyMath(), 'fib')
    fib_seq = [p.fib(x) for x in range(80)]
    print(fib_seq)

    p = ProxyMath(MyMath(), 'fact')
    fact_seq = [p.fact(x) for x in range(80)]
    print(fact_seq)

