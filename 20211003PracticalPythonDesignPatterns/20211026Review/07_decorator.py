# decorator

import time
from typing import Any, Callable
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable)->Callable:
    def inner(*args:Any,**kwargs:Any)->Any:
        beg = time.perf_counter_ns()
        rv  = func(*args,**kwargs)
        end = time.perf_counter_ns()
        logging.info('time lapsed(ns) : {0:>,}'.format(end - beg))
        return rv
    return inner

class MyMath:
    def __fib(self,n:int)->int:
        return 1 if n < 2 else self.__fib(n-1) + self.__fib(n-2)

    def __fact(self,n:int, rv:int=1)->int:
        return rv if n < 2 else self.__fact(n-1, n * rv)

    @timer
    def fib(self,n:int)->int:
        return self.__fib(n)

    @timer
    def fact(self,n:int)->int:
        return self.__fact(n)

if __name__ == '__main__':
    mm = MyMath()
    mm.fib(40)
    mm.fact(20)