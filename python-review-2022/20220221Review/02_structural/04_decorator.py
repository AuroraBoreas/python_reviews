# 

from typing import Any, Callable
import functools
import logging
import time

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s %(message)s')


def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def timed(*args:Any, **kwargs:Any)->Any:
        b = time.perf_counter_ns()
        r = func(*args, **kwargs)
        e = time.perf_counter_ns()
        logging.info(f'time lapsed (ns) : {e-b:,.2f}')
        return r
    return timed


class RawMath:
    def __fib(self, n:int)->int:
        return n if n < 2 else self.__fib(n-1) + self.__fib(n-2)

    def __fact(self, n:int)->int:
        return 1 if n < 2 else n * self.__fact(n-1)

    @timer
    def fib(self, n:int)->int:
        return self.__fib(n)

    @timer
    def fact(self, n:int)->int:
        return self.__fact(n)