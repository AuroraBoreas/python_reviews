"#" 
from __future__ import annotations

import time
import functools
import sys
sys.setrecursionlimit(500)

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

from typing import ParamSpec, Callable, TypeVar
P = ParamSpec('P')
T = TypeVar('T')

def timer(func: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        b: float = time.perf_counter()
        r: T     = func(*args, **kwargs)
        e: float = time.perf_counter()
        logging.info(f'time lapsed(s): {e - b:.3f}')
        return r
    return wrapper

class Math:
    def __fib(self, n: int) -> int:
        return 1 if n < 2 else self.__fib(n - 1) + self.__fib(n - 2)
    
    def __fact(self, n: int, tail: int=1) -> int:
        return tail if n < 2 else self.__fact(n - 1, n * tail)
    
    @timer
    def fib(self, n: int) -> int:
        return self.__fib(n)

    @timer
    def fact(self, n: int) -> int:
        return self.__fact(n)

def client_code(m: Math) -> None:
    n: int = 30
    logging.info(f"{m.fact(n)=}")
    logging.info(f"{m.fib(n)=}")

def main() -> None:
    m: Math = Math()
    client_code(m)

if __name__ == '__main__':
    main()
