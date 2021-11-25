# 

from typing import Any, Callable
import functools
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime) %(message)s')

def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def timed(*args:Any, **kwargs:Any)->Any:
        b = time.perf_counter_ns()
        r = func(*args, **kwargs)
        e = time.perf_counter_ns()
        logging.info(f'time lasped(ns) : {e-b:,.2f}')
        return r
    return timed

class MyMath:
    def __fib(self, n:int)->int:
        pass

    def __fact(self, n:int, rv:int=1)->int:
        pass

    @timer
    def fib(self, n:int)->int:
        return self.__fib(n)

    @timer
    def fact(self, n:int)->int:
        return self.__fact(n)