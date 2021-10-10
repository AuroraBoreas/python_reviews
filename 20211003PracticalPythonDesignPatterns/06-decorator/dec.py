
import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

from typing import Any, Callable, Dict

def timer(func:Callable[...,Any])->Callable[...,Any]:
    @functools.wraps(func)
    def inner(*args:Any,**kwargs:Dict[Any,Any])->Any:
        beg = time.perf_counter()
        rv  = func(*args, **kwargs)
        end = time.perf_counter()
        logging.info('time lapsed(ns) : {}'.format(end - beg))
        return rv
    return inner

class MyMath:
    def __fibonacci(self, n:int)->int:
        return 1 if n < 2 else self.__fibonacci(n-1) + self.__fibonacci(n-2)

    def __factorial(self, n:int, rv=1)->int:
        return rv if n < 2 else self.__factorial(n-1, n*rv)

    @timer
    def myfib(self, n)->int:
        return self.__fibonacci(n)

    @timer
    def myfact(self, n)->int:
        return self.__factorial(n, 1)

if __name__ == '__main__':
    mm = MyMath()
    rv1 = mm.myfib(5); print(rv1)
    rv2 = mm.myfact(5); print(rv2)
