# wearing

import time
import logging
import functools
from typing import Any, Callable, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Dict[Any,Any])->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args,**kwargs)
        end = time.perf_counter_ns()
        logging.info('time lapsed(ns) : {}'.format(end - beg))
        return rv
    return inner

class MyMath:
    def __fib(self, n:int)->int:
        return 1 if n < 2 else self.__fib(n-1) + self.__fib(n-2)

    def __fact(self, n:int)->int:
        return 1 if n < 2 else self.__fact(n-1) * n

    @timer
    def fib(self, n:int)->int:
        return self.__fib(n)

    @timer
    def fact(self, n:int)->int:
        return self.__fact(n)

if __name__ == '__main__':
    mm = MyMath()
    mm.fib(10)
    mm.fact(10)