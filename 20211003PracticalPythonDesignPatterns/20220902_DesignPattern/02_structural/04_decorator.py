"#" 

import logging
from typing import Any, Callable
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable) -> Callable:
    def inner(*args:Any, **kwargs:Any) -> Any:
        beg = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        logging.info(f'time lapsed(s) : {end - beg}')
        return res
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

def client_code() -> int:
    m:Math = Math()
    fib = m.fib(10)
    fac = m.fact(10)
    print(fib)
    print(fac)

if __name__ == '__main__':
    client_code()