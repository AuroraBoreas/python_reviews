#

from typing import Any, Callable
import logging, functools, time
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def timer(func:Callable) -> Callable:
    @functools.wraps(func)
    def inner(*args:Any, **kwargs:Any) -> Any:
        b = time.perf_counter()
        r = func(*args,**kwargs)
        e = time.perf_counter()
        logging.info(f'time lapsed(ns): {e-b}')
        return r
    return inner

class Math:
    @functools.lru_cache(128)
    def __fib(self, n:int) -> int:
        return 1 if n < 2 else self.__fib(n - 1) + self.__fib(n - 2)

    def __fact(self, n:int, tail:int = 1) -> int:
        return tail if n < 2 else n * self.__fact(n - 1)

    def __gcd(self, a:int, b:int) -> int:
        return a if b == 0 else self.__gcd(b, a%b)

    @timer
    def fib(self, n:int) -> int:
        return self.__fib(n)

    @timer
    def fact(self, n:int) -> int:
        return self.__fact(n)

    @timer
    def gcd(self, a:int, b:int) -> int:
        return self.__gcd(a, b)

def client_code() -> None:
    math = Math()
    print(math.fib(50))
    print(math.fact(50))
    print(math.gcd(1_000_000, 11))

if __name__ == '__main__':
    client_code()