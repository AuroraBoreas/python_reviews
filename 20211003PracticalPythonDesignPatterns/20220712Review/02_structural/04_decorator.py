"#" 

import functools, time, logging
from typing import Any, Callable

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable) -> Callable:
    @functools.wraps(func)
    def inner(*args:Any, **kwargs:Any) -> Any:
        b = time.perf_counter()
        r = func(*args, **kwargs)
        e = time.perf_counter()
        logging.info(f'time lapsed(ns) : {e - b}')
        return r
    return inner

class Math:
    def __fib(self, n:int) -> int:
        return 1 if n < 2 else self.__fib(n - 1) + self.__fib(n - 2)

    def __fact(self, n:int, tail:int=1) -> int:
        return tail if n < 2 else self.__fact(n - 1, n * tail)

    @timer
    def fib(self, n:int) -> int:
        return self.__fib(n)

    @timer
    def fact(self, n:int) -> int:
        return self.__fact(n)