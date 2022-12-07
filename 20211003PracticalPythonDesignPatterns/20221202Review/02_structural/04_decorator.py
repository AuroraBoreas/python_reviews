"#" 

import functools
from typing import Any, Callable
import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable) -> Callable:
    @functools.wraps(func)
    def timed(*args:Any, **kwargs:Any) -> Any:
        b = time.perf_counter_ns()
        r = func(*args, **kwargs)
        e = time.perf_counter_ns()
        logging.info(f'time lapsed(ns) : {e - b:.5f}')
        return r
    return timed

class MyMath:
    def __fact(self, n:int, tail:int=1) -> int:
        return tail if n < 2 else self.__fact(n - 1, n * tail)
    def __fib(self, n:int) -> int:
        return 1 if n < 2 else self.__fib(n - 1) + self.__fib(n - 2)

    @timer
    def fib(self, n:int) -> int:
        return self.__fib(n)

    @timer
    def fact(self, n:int) -> int:
        return self.__fact(n)

def client_code() -> None:
    mm:MyMath = MyMath()
    print(mm.fib(10))
    print(mm.fact(10))

if __name__ == '__main__':
    client_code()