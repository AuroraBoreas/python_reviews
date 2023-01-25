import sys
sys.setrecursionlimit = 500
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

import time
from typing import Callable, Any
def timer(func: Callable) -> Callable:
    def timed(*args: Any, **kwargs: Any) -> Any:
        b: float = time.perf_counter()
        r: Any   = func(*args, **kwargs)
        e: float = time.perf_counter()
        logging.info('time elapsed(s): {0:.5f}'.format(e - b))
        return r
    return timed

class MyMath:
    def __fib(self, n: int) -> int:
        return 1 if n < 2 else self.__fib(n - 1) + self.__fib(n - 2)
    def __fact(self, n: int, tail: int = 1) -> int:
        return tail if n < 2 else self.__fact(n - 1, n * tail)
    @timer
    def fib(self, n: int) -> int:
        return self.__fib(n)

    @timer
    def fact(self, n: int) -> int:
        return self.__fact(n)

def main() -> None:
    m1: MyMath = MyMath()
    print(m1.fib(10))
    print(m1.fact(20))

if __name__ == '__main__':
    main()
