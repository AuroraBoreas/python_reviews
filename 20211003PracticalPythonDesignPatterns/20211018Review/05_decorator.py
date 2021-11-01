# wearing

import time
import logging
import functools
from typing import Any, Callable

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Any)->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args,**kwargs)
        end = time.perf_counter_ns()
        logging.info(f'time lapsed(ns) :{end - beg}')
        return rv
    return inner

class MyMath:
    def __fib(self, n:int)->int:
        return 1 if n < 2 else self.__fib(n-1) + self.__fib(n-2) 

    def __fact(self, n:int, rv:int=1)->int:
        return rv if n < 2 else self.__fact(n-1, n*rv)

    @timer
    def fib(self, n:int)->int:
        return self.__fib(n)

    @timer
    def fact(self, n:int)->int:
        return self.__fact(n, 1)

if __name__ == '__main__':
    mm = MyMath()
    rv1 = mm.fib(10)
    rv2 = mm.fact(10)
    print(rv1, rv2)
