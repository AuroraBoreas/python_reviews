# wrapping
from __future__ import annotations
import time
import logging
from typing import Callable, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    def inner(*args:Any,**kwargs:Any)->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args,**kwargs)
        end = time.perf_counter_ns()
        logging.info(f'time lapsed(ns) : {end-beg:,.2f}')
        return rv
    return inner

class MyMath:
    def __fib(self, n:int)->int:
        return 1 if n < 2 else self.__fib(n-1) + self.__fib(n-2)

    def __fact(self, n:int, rv:int=1)->int:
        return rv if n < 2 else self.__fact(n-1, rv * n)

    @timer
    def fib(self, n:int)->None:
        return self.__fib(n)

    @timer
    def fact(self, n:int)->None:
        return self.__fact(n)

def client_code()->None:
    mm = MyMath()
    mm.fact(10)
    mm.fib(10)

if __name__ == '__main__':
    client_code()