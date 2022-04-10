"#" 

import functools
import time
from typing import Any, Callable


def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def timed(*args:Any, **kwargs:Any)->Any:
        b = time.perf_counter()
        r = func(*args, **kwargs)
        e = time.perf_counter()
        print(f'time elapsed(s) : {e-b}')
        return r
    return timed

class MyMath:
    def __fib(self, n:int)->int:
        return 1 if n < 2 else self.__fib(n - 1) + self.__fib(n - 2)

    def __fact(self, n:int, res:int=1)->int:
        return res if n < 2 else self.__fact(n - 1, n * res)

    @timer
    def fib(self, n:int)->int:
        return self.__fib(n)

    @timer
    def fact(self, n:int)->int:
        return self.__fact(n)