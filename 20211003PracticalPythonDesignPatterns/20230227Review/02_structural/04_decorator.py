# 

import functools
import logging
import time
from typing import Callable, ParamSpec, TypeVar

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

P = ParamSpec('P')
T = TypeVar('T')

def timer(func: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        b: float = time.perf_counter()
        r: T     = func(*args, **kwargs)
        e: float = time.perf_counter()
        logging.info(f'time lapsed(ns): {e - b:.5f}')
        return r
    return wrapper

class Math:
    def __fib(self, n: int) -> int:
        return 1 if n < 2 else self.__fib(n - 1) + self.__fib(n - 2)
    
    def __fact(self, n: int, tail: int = 1) -> int:
        return tail if n < 2 else self.__fact(n - 1, n * tail)
    
    def fib(self, n: int) -> int:
        return self.__fib(n)

    def fact(self, n: int) -> int:
        return self.__fact(n)
@timer
def client_code() -> None:
    m: Math = Math()
    print(m.fib(10))
    print(m.fact(10))
    
def main() -> None:
    client_code()

if __name__ == '__main__':
    main()