from __future__ import annotations
import time
import functools
import logging
from typing import Callable, Any, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Dict[Any, Any])->Any:
        beg = time.time_ns()
        rv  = func(*args, **kwargs)
        end = time.time_ns()
        logging.info('time lapsed(ns) : {}'.format(
            end - beg
        ))
        return rv
    return inner

class MyMath:
    @timer
    def fib(self, n:int)->int:
        return 1 if n < 2 else self.fib(n-1) + self.fib(n-2)

    def fact(self, n:int, rv:int=1)->int:
        return rv if n < 2 else self.fact(n-1, n*rv)

if __name__ == '__main__':
    mm = MyMath()
    rv1 = mm.fib(10)
    rv2 = mm.fact(10)

